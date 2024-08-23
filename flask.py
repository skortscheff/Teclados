from flask import Flask, request

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload_image():
    # Get the uploaded image data
    image_data = request.files["image"]
    
    # Save the image to a file or database
    image.save(image_data.filename)
    
    return "Image uploaded successfully!"
