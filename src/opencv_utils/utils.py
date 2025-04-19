import cv2 as cv
import sys

def read_image(file_path, *args):
    
    img = cv.imread(cv.samples.findFile(file_path), *args)
    
    if img is None:
        sys.exit("Could not read the image.")

    return img