#import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
from shutil import move, copy
import pathlib
import shutil
#import skimage as skimg
from skimage import io
import os

#--------------------------

def sort(label, fname):
    file = fname.name

    if label == 'animals':
        if not os.path.exists('PHOTOS/animals'):
            os.mkdir('PHOTOS/animals')

            animals = 'PHOTOS/animals/' + file
            dst_animals = pathlib.Path(animals)
            
            print("moving ANIMAL to the folder")
            shutil.copy(fname, dst_animals)
            os.remove(fname)
            print("done\n")
            
        else:
            animals = 'PHOTOS/animals/' + file
            dst_animals = pathlib.Path(animals)
            
            print("moving ANIMAL to the folder")
            shutil.copy(fname, dst_animals)
            os.remove(fname)
            print("done\n")
            
    elif label == 'fruits':
        if not os.path.exists('PHOTOS/fruits'):
            os.mkdir('PHOTOS/fruits')
            
            fruits = 'PHOTOS/fruits/' + file
            dst_fruits = pathlib.Path(fruits)
            
            print("moving FRUIT to the folder")
            shutil.copy(fname, dst_fruits)
            os.remove(fname)
            print("done\n")
            
        else:
            fruits = 'PHOTOS/fruits/' + file
            dst_fruits = pathlib.Path(fruits)
            
            print("moving FRUIT to the folder")
            shutil.copy(fname, dst_fruits)
            os.remove(fname)
            print("done\n")
            
    elif label == 'car':
        if not os.path.exists('PHOTOS/cars'):
            os.mkdir('PHOTOS/cars')
            
            cars = 'PHOTOS/cars/' + file
            dst_cars = pathlib.Path(cars)
            
            print("moving CAR to the folder")
            shutil.copy(fname, dst_cars)
            os.remove(fname)
            print("done\n")
            
        else:
            cars = 'PHOTOS/cars/' + file
            dst_cars = pathlib.Path(cars)
            
            print("moving CAR to the folder")
            shutil.copy(fname, dst_cars)
            os.remove(fname)
            print("done\n")
    
    elif label == 'other':
        if not os.path.exists('PHOTOS/other'):
            os.mkdir('PHOTOS/other')
            
            other = 'PHOTOS/other/' + file
            dst_other = pathlib.Path(other)
            
            print("moving OTHER to the folder")
            shutil.copy(fname, dst_other)
            os.remove(fname)
            print("done\n")
            
        else:
            other = 'PHOTOS/other/' + file
            dst_other = pathlib.Path(other)
            
            print("moving OTHER to the folder")
            shutil.copy(fname, dst_other)
            os.remove(fname)
            print("done\n")
    
    elif label == 'people':
        if not os.path.exists('PHOTOS/people'):
            os.mkdir('PHOTOS/people')
            
            people = 'PHOTOS/people/' + file
            dst_people = pathlib.Path(people)
            
            print("moving PEOPLE to the folder")
            shutil.copy(fname, dst_people)
            os.remove(fname)
            print("done\n")
            
        else:
            people = 'PHOTOS/people/' + file
            dst_people = pathlib.Path(people)
            
            print("moving PEOPLE to the folder")
            shutil.copy(fname, dst_people)
            os.remove(fname)
            print("done\n")
            
    elif label == 'home_furniture':
        if not os.path.exists('PHOTOS/home_furniture'):
            os.mkdir('PHOTOS/home_furniture')
            
            fur = 'PHOTOS/home_furniture/' + file
            dst_fur = pathlib.Path(fur)
            
            print("moving FURNITURE to the folder")
            shutil.copy(fname, dst_fur)
            os.remove(fname)
            print("done\n")
            
        else:
            fur = 'PHOTOS/home_furniture/' + file
            dst_fur = pathlib.Path(fur)
            
            print("moving FURNITURE to the folder")
            shutil.copy(fname, dst_fur)
            os.remove(fname)
            print("done\n")
    
    elif label == 'items':
        if not os.path.exists('PHOTOS/items'):
            os.mkdir('PHOTOS/items')
        
            items = 'PHOTOS/items/' + file
            dst_items = pathlib.Path(items)
            
            print("moving ITEM to the folder")
            shutil.copy(fname, dst_items)
            os.remove(fname)
            print("done\n")
            
        else:
            items = 'PHOTOS/items/' + file
            dst_items = pathlib.Path(items)
            
            print("moving ITEM to the folder")
            shutil.copy(fname, dst_items)
            os.remove(fname)
            print("done\n")
    
    elif label == 'eat':
        if not os.path.exists('PHOTOS/food'):
            os.mkdir('PHOTOS/food')
        
            eat = 'PHOTOS/food/' + file
            dst_eat = pathlib.Path(eat)
            
            print("moving FOOD to the folder")
            shutil.copy(fname, dst_eat)
            os.remove(fname)
            print("done\n")
            
        else:
            eat = 'PHOTOS/food/' + file
            dst_eat = pathlib.Path(eat)
            
            print("moving FOOD to the folder")
            shutil.copy(fname, dst_eat)
            os.remove(fname)
            print("done\n")
     
#-------------------------------------------
def sharing_photo(label):
    if len(label)>=1: 
        txt = label[0]
    elif len(label)<1:
        txt = "other"

    if txt=='apple' or txt=='orange' or txt=='banana':
        txt = 'fruits'
    elif txt=='dog' or txt=='cat' or txt=='bird' or txt=='cow' or txt=='horse' or txt=='bear':
        txt = 'animals'
    elif txt=='car' or txt=='truck' or txt=='bus':
        txt = 'car'
    elif txt=='couch' or txt=='bed' or txt=='chair' or txt=='dining table':
        txt = 'home_furniture'
    elif txt=='book' or txt=='clock' or txt=='umbrella' or txt=='bottle' or txt=='keyboard' or txt=='knife' or txt=='cup':
        txt = 'items'
    elif txt=='pizza' or txt=='sandwich' or txt=='cake' or txt=='hot dog' or txt=='donut':
        txt = 'eat'
    elif txt=='person':
        txt = 'people'
    else:
        txt = 'other'
    
    return txt
    
#------------------------------

py = pathlib.Path('PHOTOS').glob("*.jpg")
result = []
i = 0

#--------------------------------------------------------------------------------

for file in py:
    img = io.imread(file)
    bbox, label, conf = cv.detect_common_objects(img)
#    output_image = draw_bbox(img, bbox, label, conf)
#    plt.imshow(output_image)
#    plt.show()
#    print(label)
    if(len(label)):
        txt = label[0]
    else: 
        txt = 'none'
    
    print("Found Object: ", txt)
    result.append(sharing_photo(label))
    
    sort(result[i], file)
    i+=1
    

#--------------------------------------------------------------

if(i==0):
    print("\nFolder is empty.")

