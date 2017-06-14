import keras
import numpy as np
import cv2
import tensorflow as tf
generator = keras.models.load_model('sketches/generator.pkl')
generator._make_predict_function()
graph = tf.get_default_graph()
def img2img(img):
    
    im = img.reshape(-1, 128, 128, 1).astype(np.float32)
    print im.shape
    noise = np.random.normal(-1,0, size=[128, 128]).reshape(1,128,128,1)
    im = np.concatenate((im,noise),axis=3)
    print im.shape
    with graph.as_default():
        gen = generator.predict(im)*256
    # print gen
    _gen = gen[0].reshape(128,128)
    return _gen