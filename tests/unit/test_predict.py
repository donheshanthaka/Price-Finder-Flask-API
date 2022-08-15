from app import helpers

image_path = "tests/images/1.jpeg"

def test_predict():
    """
    GIVEN an image file path of a vehicle
    WHEN trying to identify the vehicle
    THEN check the identified vehicle is correct
    """
    vehicle = helpers.predict(image_path)
    assert vehicle == "Toyota Aqua 2014"


