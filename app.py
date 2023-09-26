from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb+srv://AmirulMushthofa:UZ3sAzCIWF8HGuLW@cluster0.tl9qxli.mongodb.net/')
db = client.AmirulMushthofa

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/diary', methods=['GET'])
def show_diary():
    articles_list = list(db.dairy.find({},{'_id':False}))
    return jsonify({'articles': articles_list})

@app.route('/diary', methods=['POST'])
def save_diary():

    title = request.form.get('title_give')
    content = request.form.get('content_give')

    today = datetime.now()

    file = request.files["file_give"]
    extension =  file.filename.split(".")[-1]
    mytime = today.strftime('%Y-%m-%d %H-%M-%S')
    filename = f'static/post-{mytime}.{extension}'
    file.save(filename)

    profile = request.files["profile_give"]
    extension = profile.filename.split('.')[-1]
    profilename = f'static/profile-{mytime}.{extension}'
    profile.save(profilename)

    time = today.strftime('%Y-%m-%d')

    doc = {
        'time' : time,
        'file' : filename,
        'profile' : profilename,
        'title' : title,
        'content' : content,
    }

    db.dairy.insert_one(doc)
    return jsonify({'msg': 'Data Posted'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)