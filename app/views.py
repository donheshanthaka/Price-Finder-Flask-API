from fileinput import filename
from flask import jsonify, request
from werkzeug.utils import secure_filename
import os
import uuid
import requests
from bs4 import BeautifulSoup
from app import error_handlers
from app import app
from app.helpers import predict

@app.route('/test', methods=['GET', 'POST'])
def test():
  print('Called')
  image_file = request.files['imageFile']
  image_type = secure_filename(image_file.filename).split('.')[1]
  if (image_type != 'jpeg' and image_type != 'png'):
    # Return a 415 (Unsupported Media Type) http status code
    raise error_handlers.invalid_image_type
      # return 'File type not supported!'
  data = {"model": "Wagon R", "price": "Rs. 6,500,000"}
  return jsonify(data)



@app.route('/', methods=['POST'])
def get_vehicle():
    prediction = {}
    image_file = request.files['imageFile']
    image_type = secure_filename(image_file.filename).split('.')[1]
    if (image_type != 'jpeg' and image_type != 'png' and image_type != 'jpg'):
      # Return a 415 (Unsupported Media Type) http status code
      raise error_handlers.InvalidImageType
    # Create a unique id for the filename
    uid = str(uuid.uuid4())    
    filename = uid + secure_filename(image_file.filename)
    image_path = './images/' + filename
    image_file.save(image_path)

    vehicle = predict(image_path)

    prediction['model'] = vehicle

    os.remove(image_path)

    prediction['price'] = get_price(vehicle)

    return (prediction)



# @app.route('/price', methods=['GET'])
def get_price(pred):
  prediction = pred
  # Extract the model name from the prediction and add '%20' for the white spaces to be used in the url
  model = '%20'.join([str(s) for s in prediction.split() if s.isalpha()])
  # Extract the model year from the prediction
  year = str([int(s) for s in prediction.split() if s.isdigit()][0])

  url = f"https://ikman.lk/en/ads/sri-lanka/cars?sort=relevance&buy_now=0&urgent=0&query={model}&page=1&numeric.model_year.minimum={year}&numeric.model_year.maximum={year}"

  try:
    # Making a http request to get the required webpage
    result = requests.get(url)

    doc = BeautifulSoup(result.text, "html.parser")

    # Extracting the tag that contains the price details
    # find_all returns a set of elements that contains all the prices from the page
    tag = doc.find_all( class_ ="price--3SnqI color--t0tGX")
    #print(len(tag))

    if (len(tag) < 1):
      # Return a 204 (No Content) http status code
      raise error_handlers.NoActiveListingsFound

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
