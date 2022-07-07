import tensorflow as tf
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

loaded_model_1 = tf.keras.models.load_model('model/feature_extraction_efficientnetB1')
class_names = ['Alto 2015', 'Hero Dash 2016', 'Toyota Aqua 2014', 'Wagon R Stingray 2018']

app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def hello_world():
#     return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    image_file = request.files['imageFile']
    image_type = secure_filename(image_file.filename).split('.')[1]
    print(image_type)
    if (image_type != 'jpeg' and image_type != 'png'):
      return 'File type not supported!'
    image_path = './images/' + secure_filename(image_file.filename)
    image_file.save(image_path)
    
    img = load_and_prep_image(image_path, scale=False)
    pred_prob = loaded_model_1.predict(tf.expand_dims(img, axis=0), verbose=0) # make prediction on image with shape [1, 224, 224, 3] (same shape as model was trained on)
    pred_class = class_names[pred_prob.argmax()] # get the index with the highet prediction probability
    classification = (f"pred: {pred_class}, prob: {pred_prob.max():.2f}")

    os.remove(image_path)
    #return render_template('index.html', prediction = classification) 
    return (classification) 

# Create a function to load and prepare images
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

if __name__ == '__main__':
    app.run(port=3000, debug=True)