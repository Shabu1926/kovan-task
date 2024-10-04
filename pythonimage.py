from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
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

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class ImageModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    format = db.Column(db.String(10), nullable=False)
    size = db.Column(db.String(20), nullable=False)

    def __init__(self, filename, format, size):
        self.filename = filename
        self.format = format
        self.size = size


with app.app_context():
    db.create_all()


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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
            image = image.convert("RGB")
            max_size = (800, 800)
            image.thumbnail(max_size)

            processed_filename = os.path.splitext(filename)[0] + '.png'
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], processed_filename)
            image.save(save_path, 'PNG')

          
            image_record = ImageModel(
                filename=processed_filename,
                format="PNG",
                size=str(image.size)
            )
            db.session.add(image_record)
            db.session.commit()

            return jsonify({
                "message": "Image uploaded and processed successfully",
                "id": image_record.id, 
                "filename": processed_filename,
                "format": "PNG",
                "size": image.size
            }), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Invalid file type or size"}), 400

#retrive all
@app.route('/image', methods=['GET'])
def get_images():
    images = ImageModel.query.all()  
    
    if images:
        image_list = []
        for image in images:
            image_list.append({
                "id": image.id,  
                "filename": image.filename,
                "format": image.format,
                "size": image.size,
                "url": f"/image/{image.id}"
                
            })
            
        return jsonify(image_list), 200  
    else:
        return jsonify({"message": "No images found"}), 404 
 
# GET single image
@app.route('/image/<int:id>', methods=['GET'])
def get_image_metadata(id):
    image_record = ImageModel.query.get(id)
    """if image_record:
        return jsonify({
            "id": image_record.id,
            "filename": image_record.filename,
            "format": image_record.format,
            "size": image_record.size
        }), 200
    else:
        return jsonify({"error": "Image not found"}), 404
"""
    if not image_record:
        return jsonify({"error": "Image not found"}), 404

    try:
       
        filename = image_record.filename

        
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    
    except FileNotFoundError:
        return jsonify({"error": "File not found in the server"}), 404
    
    
# PUT to update image
@app.route('/image/<int:id>', methods=['PUT'])
def update_image_metadata(id):
    image_record = ImageModel.query.get(id)
    if not image_record:
        return jsonify({"error": "Image not found"}), 404
    
    data = request.json
    
   
    existing_image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_record.filename)
    
    if 'size' in data:
        new_size = data['size']  
        
        try:
            image = Image.open(existing_image_path)
            image = image.convert("RGB") 

           
            image.thumbnail(new_size)

            
            processed_filename = os.path.splitext(image_record.filename)[0] + '_resized.png'
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], processed_filename)
            image.save(save_path, 'PNG')

           
            image_record.filename = processed_filename 
            image_record.size = str(new_size) 

            db.session.commit()
            

            return jsonify({
                "message": "Image metadata updated successfully",
                "id": image_record.id,
                "filename": processed_filename,
                "format": "PNG",
                "size": new_size
               
                }), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return jsonify({"error": "No size provided for update"}), 400

# DELETE method to remove an image
@app.route('/image/<int:id>', methods=['DELETE'])
def delete_image(id):
    image_record = ImageModel.query.get(id)
    if not image_record:
        return jsonify({"error": "Image not found"}), 404

    try:
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], image_record.filename))
    except FileNotFoundError:
        pass

    db.session.delete(image_record)
    db.session.commit()

    return jsonify({"message": "Image deleted successfully"}), 200

#delete all images
@app.route('/image', methods=['DELETE'])
def delete_all_images():
    images = ImageModel.query.all()  
    if images:
        for img in images:
            db.session.delete(img)  
        db.session.commit() 
        return jsonify({"message": "All images deleted successfully"}), 200
    else:
        return jsonify({"message": "No images found to delete"}), 404  # Handle no images case

    

# Error handling for file size limit exceeded
@app.errorhandler(413)
def request_entity_too_large(error):
    return jsonify({"error": "File size exceeds limit (5 MB max)"}), 413

if __name__ == "__main__":
    app.run(debug=True)
