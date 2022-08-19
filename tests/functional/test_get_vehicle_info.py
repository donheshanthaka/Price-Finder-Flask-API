
image_path = "tests/images/1.jpeg"
invalid_image_path = "tests/images/dash.bmp"

img = open(image_path, 'rb')
invalid_img = open(invalid_image_path, 'rb')


def test_get_vehicle(client):
    """
    GIVEN a Flask application
    WHEN the '/get-vehicle-info' is requested (POST)
    THEN check that the response is valid
    """
    response = client.post('/get-vehicle-info', data = {'imageFile' : img})
    assert response.status_code == 200
    assert b'model' in response.data
    assert b'price' in response.data


def test_get_vehicle_without_image(client):
    """
    GIVEN a Flask application
    WHEN the '/get-vehicle-info' is requested (POST) without an image attached in the body
    THEN check that a '400' status code is returned
    """
    response = client.post('/get-vehicle-info')
    assert response.status_code == 400


def test_get_vehicle_invalid_image_type(client):
    """
    GIVEN a Flask application
    WHEN the '/get-vehicle-info' is requested (POST) with an invalid image type
    THEN check that a '415' status code is returned
    """
    response = client.post('/get-vehicle-info', data = {'imageFile' : invalid_img})
    assert response.status_code == 415
