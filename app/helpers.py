import tensorflow as tf

loaded_model_1 = tf.keras.models.load_model('model/feature_extraction_efficientnetB1')
class_names = ['Alto 2015', 'Hero Dash 2016', 'Toyota Aqua 2014', 'Wagon R Stingray 2018']


def predict(image_path):
    img = load_and_prep_image(image_path, scale=False)
    # make prediction on image with shape [1, 224, 224, 3] (same shape as model was trained on)
    pred_prob = loaded_model_1.predict(tf.expand_dims(img, axis=0), verbose=0)
    # get the index with the highet prediction probability
    pred_class = class_names[pred_prob.argmax()]
    # classification = (f"pred: {pred_class}, prob: {pred_prob.max():.2f}")

    return pred_class


def load_and_prep_image(filename, img_shape=224, scale=True):
  """
  Reads in an image from filename, turns it into a tensor and reshapes into
  specified shape (img_shape, img_shape, color_channels=3).

  Args:
    filename (str): path to target image
    image_shape (int): height/width dimension of target image size
    scale (bool): scale pixel values from 0-255 to 0-1 or not
  
  Returns:
    Image tensor of shape (img_shape, img_shape, 3)
  """
  # Read in the image
  img = tf.io.read_file(filename)

  # Decode image into tensor
  img = tf.io.decode_image(img, channels=3)

  # Resize the image
  img = tf.image.resize(img, [img_shape, img_shape])

  # Scale? Yes/no
  if scale:
    # rescale the image (get all values between 0 and 1)
    return img/255.
  else:
    return img # don't need to rescale images for EfficientNet models in TensorFlow