from transformers import pipeline
from PIL import Image
import requests

def tag_image_from_url(img_url):
    classifier = pipeline("image-classification", model="google/vit-base-patch16-224")
    img = Image.open(requests.get(img_url, stream=True).raw)
    tags = classifier(img)
    return [t['label'] for t in tags[:3]]
