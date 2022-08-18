from app import helpers

image_path = "tests/images/1.jpeg"

def test_reshape_image():
    """
    GIVEN a path to an image
    WHEN trying to predict the imnage
    THEN check the returned image tensor is in correct shape
    """
    img = helpers.reshape_image(image_path, scale=False)
    assert img.shape == (224, 224, 3)