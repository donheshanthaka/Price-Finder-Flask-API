from app import utils


def test_predict(image_path):
    """
    GIVEN a path to an image of a vehicle (Toyota Aqua)
    WHEN trying to identify the vehicle
    THEN check the identified vehicle is correct according to the given image
    """
    vehicle = utils.predict(image_path)
    assert vehicle == "Toyota Aqua 2014"
