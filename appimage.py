from flask import Flask, request, jsonify, send_from_directory
import os
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__)


UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.')[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_image():
   
    if 'image' not in request.files:
        return jsonify({"error": "No image part in the request"}), 400

    file = request.files['image']

 
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    
    if file and allowed_file(file.filename):
        try:
           
            filename = secure_filename(file.filename)

            
            image = Image.open(file)
            width, height = image.size
            
            m_width=1920
            m_height=1080
            
            if width >m_width or height>m_height:
                return jsonify({f"message":"The image has higher resolution with {width} width and {height} height.Not valid"})

           
            image = image.convert("RGB") 
            
            max_size = (800, 800)
            image.thumbnail(max_size)

            processed_filename = os.path.splitext(filename)[0] + '.png'
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], processed_filename)
            image.save(save_path, 'PNG')

            return jsonify({
                "message": "Image uploaded and processed successfully",
                "filename": processed_filename,
                "format": "PNG",
                "size": image.size
            }), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Invalid file type or size"}), 400


@app.route('/image/<filename>', methods=['GET'])
def get_image(filename):
    try:
    
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404

@app.errorhandler(413)
def request_entity_too_large(error):
    return jsonify({"error": "File size exceeds limit (5 MB max)"}), 413

if __name__ == "__main__":
    app.run(debug=True)
