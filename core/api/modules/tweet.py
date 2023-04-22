import snscrape.modules.twitter as sntwitter
import tempfile
import cv2
import random
import string
import numpy as np
import re

class Tweet:
    """
    Parameters:
        id: (str)
        content: (str)
        medium: (sntwitter.Gif)
    """
    def __init__(self, id, content, medium):
        self.id = id
        self.content = content
        self.capture = self.gen_capture(medium.variants[0].url)

    def gen_capture(url):
        """
        This function captures the first frame of a GIF and 
        saves it as an image file.

        Parameters:
            url (str): The URL of the GIF media.
        
        Returns:
            If successful, the function returns the temporary 
            directory location where the captured image is 
            stored as "img.jpg".
            If there is an error, the function returns False.
        """
        cam = cv2.VideoCapture(url)
        temp_dir = tempfile.TemporaryDirectory()
        ret,frame = cam.read()
        if(ret):
            cv2.imwrite(f"{temp_dir}/img.jpg", frame)
            return temp_dir
        return False
    
    def get_type(self):
        """
        This function determines the type of an image by 
        comparing it with three default images.

        Returns:
            If the function cannot recognize the type of the 
            image, it returns False. Otherwise, it returns the 
            key of the default image that the captured image matches.
        """
        img = cv2.imread(f"{self.capture}/img.jpg")
        colors = {
            "P": cv2.imread("./images/yellow.jpg"),
            "O": cv2.imread("./images/green.jpg"),
            "M": cv2.imread("./images/red.jpg")
        }
        for key, value in list(colors.items()):
            if value.shape != img.shape: break
            err = np.sum(cv2.subtract(img, value) ** 2)
            h, w, _ = img.shape
            # Average error
            mse = err/float(h*w)
            # Return image match if there is not too much error between images
            if(mse < 0.05): return key
        return False
    
    def get_lines(self):
        lineas_referencia = re.findall(r'línea\s+(\d+|[A-Za-z])', self.content)
        return lineas_referencia

