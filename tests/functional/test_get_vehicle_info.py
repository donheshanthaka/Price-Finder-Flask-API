from app import create_app

image_path = "tests/images/1.jpeg"
invalid_image_path = "tests/images/dash.bmp"

img = open(image_path, 'rb')

def test_get_vehicle():
    """
    GIVEN a Flask application
    WHEN the '/get-vehicle-info' is requested (POST)
    THEN check that the response is valid
    """
    flask_app = create_app()

    # Create a test client using the FLask application
    with flask_app.test_client() as test_client:
        response = test_client.post('/get-vehicle-info', data = {'imageFile' : img})
        assert response.status_code == 200
        assert b'model' in response.data
        assert b'price' in response.data


def test_get_vehicle_without_image():
    """
    GIVEN a Flask application
    WHEN the '/get-vehicle-info' is requested (POST) without an image attached in the body
    THEN check that a '400' status code is returned
    """
    flask_app = create_app()

    # Create a test client using the FLask application
    with flask_app.test_client() as test_client:
        response = test_client.post('/get-vehicle-info')
        assert response.status_code == 400
