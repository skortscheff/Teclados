import requests
from bs4 import BeautifulSoup

# Set up ChatGPT API key (free version)
CHATGPT_API_KEY = "YOUR_CHATGPT_API_KEY"

def scrape_keyboards():
    url = "https://example.com/aesthetic-keyboards"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    images = soup.find_all('img')
    keyboards = [image for image in images if "keyboard" in image.get("alt") or "/keyboards/" in image.get("src")]
    
    return keyboards

def create_tweet(keyboard_image):
    prompt = f"Generate a tweet about this beautiful {keyboard_image.get('alt')} keyboard"
    response = requests.post(
        "https://api-inference.huggingface.co/models/valhalla/chatgpt",
        headers={"Authorization": f"Bearer {CHATGPT_API_KEY}"},
        json=prompt,
    )
    
    tweet_text = response.json()["generated_text"]
    
    return tweet_text

from flask import Flask, request

app = Flask(__name__)

@app.route("/scrape", methods=["GET"])
def scrape():
    keyboards = scrape_keyboards()
    
    return {"keyboards": [keyboard.get("src") for keyboard in keyboards]}

@app.route("/tweet", methods=["POST"])
def tweet():
    keyboard_image = request.json["image"]
    
    tweet_text = create_tweet(keyboard_image)
    
    return {"tweet": tweet_text}

@app.route("/upload", methods=["POST"])
def upload_image():
    image_data = request.files["image"]
    
    # Save the image to a file or database
    image.save(image_data.filename)
    
    return "Image uploaded successfully!"

if __name__ == "__main__":
    app.run(debug=True)
