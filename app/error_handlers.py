from flask import Blueprint

error_handlers = Blueprint('error_handlers', __name__)


class WebScraperUrlError(Exception):
    pass


@error_handlers.app_errorhandler(WebScraperUrlError)
def web_scraper_url_error(e):
    """Return a 502 (Bad Gateway)
    http status code with the error message
    (Unable to access price retrieval web server)
    """
    return {'message': 'Unable to access price retrieval web server'}, 502


class InvalidImageType(Exception):
    pass


@error_handlers.app_errorhandler(InvalidImageType)
def invalid_image_type(e):
    """Return a 415 (Unsupported Media Type)
    http status code with the error message
    (Invalid Image Type)
    """
    return {'message': 'Invalid Image Type'}, 415


class ImageFileNotFound(Exception):
    pass


@error_handlers.app_errorhandler(ImageFileNotFound)
def image_file_not_found(e):
    """Return a 400 (Bad Request)
    http status code with the error message
    (Image file not found in the request)
    """
    return {'message': 'Image file not found in the request'}, 400


class PageNotFound(Exception):
    pass


@error_handlers.app_errorhandler(404)
def page_not_found(e):
    """Return a 404 (Not Found)
    http status code with the error message
    (Server cannot find the requested resource)
    """
    return {'message': 'The requested resource was not found'}, 404


@error_handlers.app_errorhandler(405)
def method_not_allowed(e):
    """Return a 405 (Method Not Allowed)
    http status code with the error message
    (The requested method is not allowed)
    """
    return {'message': 'The requested method is not allowed'}, 405
