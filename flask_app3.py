import os
from PIL import Image, ImageChops
from flask import Flask, render_template, request, flash, redirect, url_for
import cv2
import numpy as np
import tensorflow as tf
from keras.models import model_from_json
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import re
import base64
from datetime import datetime

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
tf.config.LogicalDeviceConfiguration(memory_limit=2024)
    

app = Flask(__name__)
db_name = 'users.db'
ENV = 'dev'
if ENV == 'loc':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:21071987@127.0.0.1:5432/estimate'
elif ENV == 'dev':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://qscsxfigbwhajk:66d4ca6be7f1060eeed7005770c7f7aaffcb7957c88a9eb8ddac3692f3d7b395@ec2-23-23-151-191.compute-1.amazonaws.com:5432/d1ds9hsal9udrg'   
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'super secret key'
db = SQLAlchemy(app)
db.init_app(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(100))
    lname = db.Column(db.String(100))
    estim = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, fname, lname, estim):
        self.fname = fname
        self.lname = lname
        self.estim = estim
    
    def __repr__(self):
        return f'<{self.fname} {self.lname} give me  {self.estim}>'

@app.route('/')
def index():
    return render_template("index.html")

def convertImage(imgdata1) -> None:
    try:
        imgstr = re.search(r'base64,(.*)', str(imgdata1)).group(1)
        with open('output.png', 'wb') as output:
            output.write(base64.b64decode(imgstr))
    except Exception:
        print('No image-data')        

@app.route('/predict/', methods = ['GET', 'POST'])
def predict() -> str:
    image_to_nn = _process_with_image() 
    model_json = _model_structure_from_json()
    loaded_model = _model_load(model_json)
    out = loaded_model.predict(image_to_nn)
    print(out)
    global response
    response = str(*(np.argmax(out, axis=1)))
    return response

def _model_structure_from_json() -> str:
    json_file = r'/app/model_numMy.json'
    with open(json_file) as json_file:
        model_json = json_file.read()
    
    return model_json 

def _model_load(model_json: str):
    loaded_model = tf.keras.models.model_from_json(model_json)
    weights_file = r'/app/modelMy.h5'
    loaded_model.load_weights(weights_file)
    return loaded_model

def _process_with_image():
    imgdata = request.get_data()
    convertImage(imgdata)
    draw = Image.open('output.png', 'r')
    image_with_background = _add_background(draw)
    transformed_image = _transf_image(_centering_image(image_with_background))
    return transformed_image 

def _add_background(draw):
    background = Image.new('RGBA', (100, 100), (255, 255, 255))
    text_img = Image.new('RGBA', (100, 100), (255, 255, 255))
    text_img.paste(background, (0, 0))
    text_img.paste(draw, (0, 0), mask=draw)
    return text_img.save('output1.png', format='png') 

def _centering_image(image_with_background):
    img = Image.open('output1.png', 'r').convert("L")
    w, h = img.size[:2]
    left, top, right, bottom = w, h, -1, -1
    pixels = img.getdata()

    for y in range(h):
        yoffset = y * w
        for x in range(w):
            if pixels[yoffset + x] > 0:
                left = min(left, x)
                top = min(top, y)
                right = max(right, x)
                bottom = max(bottom, y)

    shiftX = (left + (right - left) // 2) - w // 2
    shiftY = (top + (bottom - top) // 2) - h // 2
    return ImageChops.offset(img, -shiftX, -shiftY)

def _transf_image(_centering_image):
    centring_image = cv2.imread('output1.png', cv2.IMREAD_ANYDEPTH) / -1
    centring_image = cv2.resize(centring_image, (28,28), interpolation = cv2.INTER_AREA)
    centring_image = np.asarray(centring_image)
    centring_image = centring_image.reshape(1, 28, 28, 1)
    transformed_image = centring_image
    return transformed_image    

@app.route('/submit', methods = ['POST'])
def submit() -> str:
    
    fname = request.form['fname']
    lname = request.form['lname']
    estim = response
    print(fname, lname, estim)
    try:
        datas = User(fname, lname, estim)
        db.session.add(datas)
        db.session.commit()
    except:
        flash("Don't unique name") 
        return redirect(url_for('index'))   
    if fname == '' or lname == '' or estim == '':
        flash('Please enter both the first and last name and give estimate, please)')
        return redirect(url_for('index'))   
    return render_template('success.html', datas=datas)
        # return flash('nothing else metterrs')
    
    # return render_template('index2.html')
        
if __name__ == '__main__':
    db.create_all()
    app.run(host='127.0.0.2', port=80)
    app.run(debug=True)
