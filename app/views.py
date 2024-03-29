from flask import jsonify, request, Blueprint
from werkzeug.utils import secure_filename
import os
import uuid
from app import error_handlers
from app.utils import predict, get_price

views = Blueprint('views', __name__)

# @views.route('/test', methods=['GET', 'POST'])
# def test():
#   print('Called')
#   try:
#     image_file = request.files['imageFile']
#   except KeyError:
#     raise error_handlers.ImageFileNotFound
#   image_type = secure_filename(image_file.filename).split('.')[1]
#   if (image_type != 'jpeg' and image_type != 'png'):
#     # Return a 415 (Unsupported Media Type) http status code
#     raise error_handlers.invalid_image_type
#       # return 'File type not supported!'
#   data = {"model": "Wagon R", "price": "Rs. 6,500,000"}
#   return jsonify(data)


@views.route('/get-vehicle-info', methods=['POST'])
def get_vehicle_info():
    """
    Reads and save the image recieved through the POST request and
    pass it to the predict function to identify the vehicle and then
    use utility function get_price to retrieve the market price.

    Returns:
      Json object of the vehicle model and price
    """
    vehicle_info = {}
    try:
        image_file = request.files['imageFile']
    except KeyError:
        raise error_handlers.ImageFileNotFound
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
    vehicle_info['model'] = vehicle
    os.remove(image_path)
    vehicle_info['price'] = get_price(vehicle)

    return (vehicle_info)
