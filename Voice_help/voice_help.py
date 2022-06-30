import os
from io import BytesIO
from PIL import Image
from PIL import Image, ImageDraw, ImageFont
from flaskT import Flask, render_template, request, jsonify
import imageio as iio
from keras.preprocessing.image import img_to_array
import cv2
#https://imageio.readthedocs.io/en/stable/examples.html
# from scipy.misc import imresize
#from matplotlib.pyplot import imread
import numpy as np
import keras.models
import tensorflow as tf
from tensorflow.keras.models import model_from_json
# from skimage import transform, io
import re
import base64

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
graph = tf.compat.v1.get_default_graph()
json_file = r'C:\Users\ysatr\OneDrive\Рабочий стол\MMNIST\model_numMy.json'
with open(json_file) as json_file:
    model_json = json_file.read()

def convertImage(imgdata1):
    imgstr = re.search(r'base64,(.*)', str(imgdata1)).group(1)
    with open('output.png', 'wb') as output:
        output.write(base64.b64decode(imgstr))
def predict():
    global graph, model
    with graph.as_default():

        json_file.close()
        model = model_from_json(model_json)
        weights_file = r'C:\Users\ysatr\OneDrive\Рабочий стол\MMNIST\modelMy.h5'
        model.load_weights(weights_file)
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        model.call = tf.function(model.call)
        # test = cv2.imread('output.png',)


        #print(imgdata)

        #x = imread('output.png', mode='L')
        #x.shape
        #(280, 280)
        # x = iio.imread('output.png', pilmode='L')
        # test = iio.imread('output.png', pilmode='L')
        # draw = Image.open('output.png', 'r')
        # background = Image.new('RGBA', (100,100), (255,255,255))
        # text_img = Image.new('RGBA', (100,100), (255,255,255))
        # text_img.paste(background, (0,0))
        # text_img.paste(draw, (0,0), mask=draw)
        # text_img.save('output1.png', format='png')

        test = cv2.imread('output1.png', cv2.IMREAD_ANYDEPTH)
        cv2.imshow('Display Window', test)
        # test = convertImage(test)
        # test = np.invert(test)
        test = test/28
        # test = (test.as_type(np.float32)-127.5) / 127.5
        # test = imresize(test, (28, 28))
        test = cv2.resize(test, (28,28), interpolation = cv2.INTER_AREA)
        print(test)
        # test = test.resize(test, (28, 28))
        # test = transform.resize(test, (28, 28), mode='symmetric', preserve_range=True)
        #(28, 28)
        #type(x)
        #<class 'numpy.ndarray'>
        test = np.asarray(test, dtype="uint8")
        test = test.reshape(-1, 28, 28, 1)
        #(1, 28, 28, 1)
        # test = tf.cast(test, tf.float32)


        # perform the prediction
        # out = model.predict(x)
        #print(np.argmax(out, axis=1))
        # convert the response to a string
        # response = np.argmax(out, axis=1)
        # return str(response[0])

        # with graph.as_default():
        #     out = model.predict(test)
        #     response = np.argmax(out, axis=1)
        #     return str(response[0])

        # json_file = r'C:\Users\ysatr\OneDrive\Рабочий стол\MMNIST\model_numMy.json'
        # with open(json_file) as json_file:
        #     model_json = json_file.read()
        # json_file.close()
        # model = model_from_json(model_json)
        # weights_file = r'C:\Users\ysatr\OneDrive\Рабочий стол\MMNIST\weightsMy.h5'
        # model.load_weights(weights_file)
        # model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        # out = model.predict(x)
        # response = np.argmax(out, axis=1)
        # return str(response[0])

        out = model.predict(test)
        print(out)
        response = np.argmax(out, axis=1)
        print(response)
        return {"output": response}
def main():
    predict()

if __name__ == '__main__':
    main()