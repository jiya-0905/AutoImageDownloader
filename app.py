from flask import Flask, request, render_template
from mailsend import mail_bhejo
from zip import zip_file
from downloadi import imgsear
import os

app = Flask(__name__,
            static_folder=r"static/",
            template_folder=r"template/")

@app.route('/', methods=['GET','POST'])

def index():
    if request.method == 'POST':
        topic= request.form['search']
        n= int(request.form['How_many?'])
        email_id= request.form['email_id']  
        current_directory = os.path.dirname(os.path.abspath(__file__))
        images_folder = os.path.join(current_directory, 'images')  
        if not os.path.exists(images_folder):
            os.makedirs(images_folder) 
        imgsear(topic, n)
        output_rar = os.path.join(current_directory, "result.rar")
        zip_file(images_folder, output_rar)        
        subject = "IMAGES"
        body = f"Your order of {n} images has arrived."
        mail_bhejo(email_id, subject, body, output_rar)  
        return "Check your mail"
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)