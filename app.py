import requests
from bs4 import BeautifulSoup

def scrape_keyboards():
    url = "https://example.com/aesthetic-keyboards"  # Replace with a website of keyboards
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all image tags on the page
    images = soup.find_all('img')
    
    # Filter for keyboard images (e.g., based on alt text or src URL)
    keyboards = [image for image in images if "keyboard" in image.get("alt") or "/keyboards/" in image.get("src")]
    
    return keyboards
