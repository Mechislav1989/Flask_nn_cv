from keras.models import model_from_json
# from scipy.misc.pilutil import imread, imresize, imshow
import tensorflow as tf
import os
JSONpath = os.path.join(os.path.dirname(__file__), 'models', 'model_num2.json')
MODELpath = os.path.join(os.path.dirname(__file__), 'models', 'model_num2.h5')
def init():
    json_file = open(JSONpath, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights(MODELpath)
    print("Loaded Model from disk")
    loaded_model.compile(loss='categorical_crossentropy',
                         optimizer='adam', metrics=['accuracy'])
    graph = tf.get_default_graph()
    return loaded_model, graph