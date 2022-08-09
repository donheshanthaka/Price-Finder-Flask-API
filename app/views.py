from flask import request, jsonify
from werkzeug.utils import secure_filename
from app import app

@app.route('/test', methods=['GET', 'POST'])
def test():
  print('Called')
  image_file = request.files['imageFile']
  image_type = secure_filename(image_file.filename).split('.')[1]
  if (image_type != 'jpeg' and image_type != 'png'):
    # Return a 415 (Unsupported Media Type) http status code
    raise InvalidImageType
      # return 'File type not supported!'
  data = {"model": "Wagon R", "price": "Rs. 6,500,000"}
  return jsonify(data)

@app.route('/', methods = ['GET'])
def hellow():
    return "Hellow"

class NoActiveListingsFound(Exception):
  pass

@app.errorhandler(NoActiveListingsFound)
def no_active_listing_found(e):
  """Return a 204 (No Content) http status code with the error message (No active advertisements found for the current vehicle model)"""
  return {'message': 'No active advertisements found for the current vehicle model'}, 204

class WebScraperUrlError(Exception):
  pass

@app.errorhandler(WebScraperUrlError)
def web_scraper_url_error(e):
    """Return a 502 (Bad Gateway) http status code with the error message (Unable to access price retrieval web server)"""
    return {'message': 'Unable to access price retrieval web server'}, 502

class InvalidImageType(Exception):
  pass

@app.errorhandler(InvalidImageType)
def invalid_image_type(e):
    """Return a 415 (Unsupported Media Type) http status code with the error message (Invalid Image Type)"""  
    return {'message': 'Invalid Image Type'}, 415
