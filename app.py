from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

def create_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='cdnapp'
    )

@app.route('/')
def index():
    return render_template('upload.html', title='Upload to CDN')

def get_file_type(filename):
    file_extension = filename.rsplit('.', 1)[-1].lower()
    
    if file_extension in ['jpg', 'jpeg', 'png', 'gif']:
        return 'image'
    elif file_extension in ['mp4', 'avi', 'mkv']:
        return 'video'
    else:
        return 'file'
    
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    caption = request.form['caption']
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        url = 'static/uploads/' + file.filename
        file_type = get_file_type(file.filename) 

        conn = create_connection()
        cursor = conn.cursor()
        insert_query = "INSERT INTO items (url, caption, type) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (url, caption, file_type))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    
@app.route('/media-hub')
def gallery():
    return render_template('media-hub.html', title='Media Hub')

@app.route('/items_data')
def items_data():
    conn = create_connection()
    cursor = conn.cursor()
    select_query = "SELECT * FROM items"
    cursor.execute(select_query)
    items = cursor.fetchall()
    cursor.close()
    conn.close()

    items_data = [{"id": item[0], "url": item[1], "caption": item[2], "type": item[3]} for item in items]
    return jsonify(items_data)

if __name__ == '__main__':
    app.run(debug=True)
