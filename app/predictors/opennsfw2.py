import opennsfw2 as n2
from PIL import Image

OPENNSFW2_THRESHOLD = 0.5125

def opennsfw2_predict_image(image: Image.Image):
    nsfw_probability = n2.predict_image(image, weights_path='./models/opennsfw2.h5')
    return {
        'isNsfw': nsfw_probability >= OPENNSFW2_THRESHOLD,
        'probability': nsfw_probability
    }
