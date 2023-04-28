import cv2
import numpy as np
import re
import itertools
import os
from django.conf import settings
import random
import string



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

    def gen_capture(self, url):
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
        ret,frame = cam.read()
        if(ret):
            file_name = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
            cv2.imwrite(os.path.join(settings.PROJECT_ROOT, f"../api/modules/images/temp/{file_name}.jpg"), frame)
            return f"../api/modules/images/temp/{file_name}.jpg"
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
        img = cv2.imread(os.path.join(settings.PROJECT_ROOT, self.capture))
        os.remove(os.path.join(settings.PROJECT_ROOT, self.capture))
        colors = {
            "P": cv2.imread(os.path.join(settings.PROJECT_ROOT, "../api/modules/images/yellow.jpg")),
            "O": cv2.imread(os.path.join(settings.PROJECT_ROOT, "../api/modules/images/green.jpg")),
            "M": cv2.imread(os.path.join(settings.PROJECT_ROOT, "../api/modules/images/red.jpg"))
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
        """
        This function determines the referenced lines in a tweet.

        Returns:
            A list with the referenced lines.
        """
        caso1, caso2, caso3 = list(), list(), list()
        # Finding all matches for 'línea' followed by a digit or alphabet and adding it to 'caso1'
        match = re.findall(r'línea\s+(\d+|[A-Za-z])', self.content)
        if match:
            caso1 = match 

        # Finding all matches for 'líneas' followed by a digit or alphabet and adding it to 'caso2'
        # 'caso2' is flattened using itertools.chain()
        busqueda = re.findall(r'\b(líneas?)\s+([A-Za-z]|\d+)(?:\s+y\s+(\d+|[A-Za-z]|\d+))?', self.content)
        if busqueda:
            caso2 = list(itertools.chain(*busqueda))

        
        # Finding all matches for 'líneas 1🚌 y 2🚌' and adding '1' and '2' to 'pepe'
        patron = r"líneas\s+1🚌\s+y\s+2🚌"
        if re.search(patron, self.content):
            caso3 = ["1", "2"]
            
        # Combining all the cases and returning a list of unique elements
        return list(set(caso1 + caso2 + caso3))

