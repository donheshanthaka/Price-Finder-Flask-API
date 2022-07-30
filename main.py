import tensorflow as tf
from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
import os
import requests
from bs4 import BeautifulSoup

# loaded_model_1 = tf.keras.models.load_model('model/feature_extraction_efficientnetB1')
# class_names = ['Alto 2015', 'Hero Dash 2016', 'Toyota Aqua 2014', 'Wagon R Stingray 2018']

app = Flask(__name__)

# @app.route('/', methods=['POST'])
# def predict():
#     image_file = request.files['imageFile']
#     image_type = secure_filename(image_file.filename).split('.')[1]
#     # print(image_type)
#     if (image_type != 'jpeg' and image_type != 'png' and image_type != 'jpg'):
#       return 'File type not supported!'
#     image_path = './images/' + secure_filename(image_file.filename)
#     image_file.save(image_path)
    
#     img = load_and_prep_image(image_path, scale=False)
#     pred_prob = loaded_model_1.predict(tf.expand_dims(img, axis=0), verbose=0) # make prediction on image with shape [1, 224, 224, 3] (same shape as model was trained on)
#     pred_class = class_names[pred_prob.argmax()] # get the index with the highet prediction probability
#     # classification = (f"pred: {pred_class}, prob: {pred_prob.max():.2f}")

#     os.remove(image_path)
 
#     return (pred_class)

# Create a function to load and prepare images
def load_and_prep_image(filename, img_shape=224, scale=True):
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
  # Read in the image
  img = tf.io.read_file(filename)

  # Decode image into tensor
  img = tf.io.decode_image(img, channels=3)

  # Resize the image
  img = tf.image.resize(img, [img_shape, img_shape])

  # Scale? Yes/no
  if scale:
    # rescale the image (get all values between 0 and 1)
    return img/255.
  else:
    return img # don't need to rescale images for EfficientNet models in TensorFlow


@app.route('/price', methods=['GET'])
def get_price():
  prediction = request.args['vehicle']
  # Extract the model name from the prediction and add '%20' for the white spaces to be used in the url
  model = '%20'.join([str(s) for s in prediction.split() if s.isalpha()])
  # Extract the model year from the prediction
  year = str([int(s) for s in prediction.split() if s.isdigit()][0])

  url = f"https://ikman.lk/en/ads/sri-lanka/cars?sort=relevance&buy_now=0&urgent=0&query={model}&page=1&numeric.model_year.minimum={year}"

  # Making a http request to get the required webpage
  result = requests.get(url)

  doc = BeautifulSoup(result.text, "html.parser")

  # Extracting the tag that contains the price details
  # find_all returns a set of elements that contains all the prices from the page
  tag = doc.find_all( class_ ="price--3SnqI color--t0tGX")
  print(len(tag))

  # Iterates through the list of elements and extracting the price span tag
  total_price = 0
  for spans in tag:
      extracted_price = spans.find("span").string
      # Filtering the string to get the price in integer value
      total_price += int(''.join(filter(str.isdigit, extracted_price)))

  average_price = total_price // len(tag)
  average_price = "RS. " + "{:,}".format(average_price)
  return average_price


@app.route('/test', methods=['GET', 'POST'])
def test():
  image_file = request.files['imageFile']
  image_type = secure_filename(image_file.filename).split('.')[1]
  if (image_type != 'jpeg' and image_type != 'png'):
    #response = {"error": "Invalid Image Type"}
    # Return a 415 (Unsupported Media Type) http status code
    #return jsonify(response), 415
    raise InvalidImageType("Invalid Image Type", status_code=415)
      # return 'File type not supported!'
  data = {"model": "Wagon R", "price": "Rs. 6,500,000"}
  return jsonify(data)



class InvalidImageType(Exception):
  status_code = 400

  def __init__(self, message, status_code=None):
    super().__init__()
    self.message = message
    if status_code is not None:
      self.status_code = status_code

  def to_dict(self):
    rv = dict()
    rv['message'] = self.message
    return rv

@app.errorhandler(InvalidImageType)
def invalid_image_type(e):
  return jsonify(e.to_dict()), e.status_code


if __name__ == '__main__':
    # When using the android emulator
    app.run(host="0.0.0.0", port=8000, debug=True)
    #app.run() # For production
