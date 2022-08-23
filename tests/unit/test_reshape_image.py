from app import utils


def test_reshape_image(image_path):
    """
    GIVEN a path to an image
    WHEN trying to predict the imnage
    THEN check the returned image tensor is in correct shape
    """
    img = utils.reshape_image(image_path, scale=False)
    assert img.shape == (224, 224, 3)