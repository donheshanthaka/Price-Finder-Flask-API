import tensorflow as tf
import requests
from bs4 import BeautifulSoup
from app import error_handlers

loaded_model_1 = tf.keras.models.load_model(
    'model/feature_extraction_efficientnetB1')
class_names = ['Alto 2015', 'Hero Dash 2016',
               'Toyota Aqua 2014', 'Wagon R Stingray 2018']


def predict(image_path):
    """
    Takes the image path and pass it to be reshaped using the reshape_image function and
    make a prediction of the reshaped image using the AI model

    Args:
        image_path (str): path to the vehicle image

    Returns:
        String value of the predicted model
    """
    img = reshape_image(image_path, scale=False)
    # make prediction on image with shape [1, 224, 224, 3] (same shape as model was trained on)
    pred_prob = loaded_model_1.predict(tf.expand_dims(img, axis=0), verbose=0)
    # get the index with the highet prediction probability
    pred_class = class_names[pred_prob.argmax()]

    return pred_class


def reshape_image(filename, img_shape=224, scale=True):
    """
    Reads in an image from filename, turns it into a tensor and reshapes into
    specified shape (img_shape, img_shape, color_channels=3).

    Args:
      filename (str): path to target image
      image_shape (int): height/width dimension of target image size
      scale (bool): scale pixel values from 0-255 to 0-1 or not

    Returns:
      Image tensor of shape (img_shape, img_shape, 3)
    """
    img = tf.io.read_file(filename)
    img = tf.io.decode_image(img, channels=3)
    img = tf.image.resize(img, [img_shape, img_shape])
    if scale:
        # rescale the image (get all values between 0 and 1)
        return img/255.
    else:
        return img  # don't need to rescale images for EfficientNet models


def get_price(predicted_vehicle_model):
    """
    Takes a string value of the predicted vehicle model and extract the model
    and year, then the extracted values are passed through a web scraper
    to find the current market price of the vehicle

    Args:
        predicted_vehicle_model (str): model and year of the predicted vehicle

    Returns:
        Formatted string value of the market price
    """
    vehicle_model = predicted_vehicle_model

    cars_list = ['Alto 2015', 'Toyota Aqua 2014', 'Wagon R Stingray 2018']
    bikes_list = ['Hero Dash 2016']

    # Extract the model name from the prediction and
    # add '%20' for the white spaces to be used in the url
    model = '%20'.join([str(s) for s in vehicle_model.split() if s.isalpha()])
    # Extract the model year from the prediction
    year = str([int(s) for s in vehicle_model.split() if s.isdigit()][0])

    if (predicted_vehicle_model in cars_list):
        url = f"""https://ikman.lk/en/ads/sri-lanka/cars?sort=relevance&
            buy_now=0&urgent=0&query={model}&page=1&numeric.model_year.minimum={year}
            &numeric.model_year.maximum={year}"""

    elif (predicted_vehicle_model in bikes_list):
        print(model)
        print(year)
        url = f"""https://ikman.lk/en/ads/sri-lanka/motorbikes-scooters?sort=relevance&buy_now=0&urgent=0&query={model}&page=1&numeric.model_year.minimum={year}&numeric.model_year.maximum={year}"""

    try:
        # Making a http request to get the required webpage
        result = requests.get(url)

        doc = BeautifulSoup(result.text, "html.parser")

        # Extracting the tag that contains the price details
        # find_all returns a set of elements that contains all the prices from the page
        tag = doc.find_all(class_="price--3SnqI color--t0tGX")
        if (len(tag) < 1):
            return 'No active advertisements found to calculate the market price'

        # Iterates through the list of elements and extracting the price span tag
        total_price = 0
        for spans in tag:
            extracted_price = spans.find("span").string
            # Filtering the string to get the price in integer value
            total_price += int(''.join(filter(str.isdigit, extracted_price)))

        average_price = total_price // len(tag)
        average_price = "RS. " + "{:,}".format(average_price)
        return average_price

    # Return a 502 (Bad Gateway) http status code
    except requests.exceptions.ConnectionError:
        raise error_handlers.WebScraperUrlError

    # Return a 502 (Bad Gateway) http status code
    except requests.exceptions.InvalidURL:
        raise error_handlers.WebScraperUrlError
