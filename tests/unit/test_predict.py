import string
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


def test_load_and_prep_image():
    """
    GIVEN a path to an image
    WHEN trying to predict the imnage
    THEN check the returned image tensor is in correct shape
    """
    img = helpers.load_and_prep_image(image_path, scale=False)
    assert img.shape == (224, 224, 3)


def test_get_price():
    """
    GIVEN a name of a vehicle
    WHEN trying to find the current market price
    THEN check the returned value is a string (cannot check for an exact value since market value is not constant, therefore checking the return type is the only option)
    """
    price = helpers.get_price("Toyota Aqua 2014")
    assert type(price) == str