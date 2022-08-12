from app import app

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