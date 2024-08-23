import requests

def create_tweet(keyboard_image):
    prompt = f"Generate a tweet about this beautiful {keyboard_image.get('alt')} keyboard"
    response = requests.post(
        "https://api-inference.huggingface.co/models/valhalla/chatgpt",
        headers={"Authorization": f"Bearer {CHATGPT_API_KEY}"},
        json=prompt,
    )
    
    # Get the generated tweet text
    tweet_text = response.json()["generated_text"]
    
    return tweet_text
