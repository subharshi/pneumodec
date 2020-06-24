# Importing the libraries
from flask import Flask,render_template,redirect,request,send_from_directory
from tensorflow.keras.models import load_model
import os
from PIL import Image
import numpy as np

# Loading the model before starting the app
model_file = "model.h5"
model = load_model(model_file)

# Initializing the flask app
# We start the web app and add path to "upload folder" for our uploaded images
app = Flask(__name__,template_folder='templates')
UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

# Creating the makePredictions() function
def makePredictions(path):
    
  '''
  Method to predict if the image uploaed is healthy or pneumonic
  '''
  
  # we open the image
  img = Image.open(path) 
  
  # we resize the image for the model
  img_d = img.resize((224,224))
  
  rgbimg=None
  #We check if image is RGB or not
  if len(np.array(img_d).shape)<3:
    rgbimg = Image.new("RGB", img_d.size)
    rgbimg.paste(img_d)
  else:
      rgbimg = img_d
      
      
      
  # we convert the image to NumPy array and reshape it to (1,224,224,3)   
  rgbimg = np.array(rgbimg,dtype=np.float64)
  rgbimg = rgbimg.reshape((1,224,224,3))
  
  
   # we make predictions from the model, convert them to our labels (healthy/pneumonic)
  predictions = model.predict(rgbimg)
  a = int(np.argmax(predictions))
  if a==1:
    a = "Result : Pneumonic"
  else:
    a = "Result : Healthy"
  return a


# Defining a route for the HOMEPAGE
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        if 'img' not in request.files:
            return render_template('home.html',filename="illuminators.png",message="Please upload an file")
        f = request.files['img']  
        if f.filename=='':
            return render_template('home.html',filename="illuminators.png",message="No file selected")
        if not ('jpeg' in f.filename or 'png' in f.filename or 'jpg' in f.filename):
            return render_template('home.html',filename="illuminators.png",message="Please upload an image with .png or .jpg/.jpeg extension")
        files = os.listdir(app.config['UPLOAD_FOLDER'])
        if len(files)==1:
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
        else:
            files.remove("illuminators.png")
            file_ = files[0]
            os.remove(app.config['UPLOAD_FOLDER']+'/'+file_)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
        
        # At the home method, we take this label and send this to our template
        predictions = makePredictions(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
        return render_template('home.html',filename=f.filename,message=predictions,show=True)
    return render_template('home.html',filename='illuminators.png')

if __name__=="__main__":
    app.run(debug=True)