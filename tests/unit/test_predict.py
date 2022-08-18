from app import helpers

image_path = "tests/images/1.jpeg"

def test_predict():
    """
    GIVEN an image file path of a vehicle (Toyota Aqua)
    WHEN trying to identify the vehicle
    THEN check the identified vehicle is correct
    """
    vehicle = helpers.predict(image_path)
    assert vehicle == "Toyota Aqua 2014"


def test_load_and_prep_image():
    """
    GIVEN an image file path
    WHEN trying to predict the imnage
    THEN check the returned image tensor is in correct shape
    """
    img = helpers.load_and_prep_image(image_path, scale=False)
    assert img.shape == (224, 224, 3)