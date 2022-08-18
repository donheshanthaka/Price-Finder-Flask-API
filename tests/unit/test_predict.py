from app import helpers

image_path = "tests/images/1.jpeg"

def test_predict():
    """
    GIVEN a path to an image of a vehicle (Toyota Aqua)
    WHEN trying to identify the vehicle
    THEN check the identified vehicle is correct according to the given image
    """
    vehicle = helpers.predict(image_path)
    assert vehicle == "Toyota Aqua 2014"





