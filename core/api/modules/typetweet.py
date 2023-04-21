import snscrape.modules.twitter as sntwitter
import cv2
import random
import string
import numpy as np

def gen_capture(url):
    cam = cv2.VideoCapture(url)
    ret,frame = cam.read()
    if(ret):
        rand = f"./{''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))}.jpg"
        cv2.imwrite(rand, frame)
        return rand
    return False

def compare_img(img):
    img = cv2.imread(img)
    colors = {
        "yellow": cv2.imread("./yellow.jpg"),
        "green": cv2.imread("./green.jpg"),
        "red": cv2.imread("./red.jpg")
    }
    for key, value in list(colors.items()):
        if value.shape != img.shape: break
        err = np.sum(cv2.subtract(img, value) ** 2)
        h, w, _ = img.shape
        # promedio error
        mse = err/float(h*w)
        # si no hay mucho error entre las dos imagenes
        if(mse < 0.05): return key
    return False

# crear scraper
scraper = sntwitter.TwitterProfileScraper("metrodemedellin")

# recorrer todos los tweets del metro
for i, tweet in enumerate(scraper.get_items()):
    content = tweet.rawContent
    # verificar que no es una respueta
    if(content[0] != "@" and ''.join(content[0:2]) != "RT"):
        # verificar que tiene un GIF
        if(tweet.media):
            for medium in tweet.media:
                if type(medium) == sntwitter.Gif:
                    # generar captura del primer frame del gif
                    img = gen_capture(medium.variants[0].url)
                    # comparar imagenes
                    print(compare_img(img))
    if(i > 100):
        break