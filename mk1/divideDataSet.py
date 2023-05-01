import os
import random

pathToRepo = r'C:\Users\zoehe\Documents\2023VisionProject'
folderName = 'WorldsData/'
extension = ".jpg"
trainingLoc = pathToRepo + r'/mk1/train.txt'
validationLoc = pathToRepo + r'/mk1/validate.txt'
imageLocations = pathToRepo + r'/mk1/labeledData'
edge = .95

if(os.path.exists(trainingLoc)):
    os.remove(trainingLoc)
    
if(os.path.exists(validationLoc)):
    os.remove(validationLoc)

with open(trainingLoc, 'w', encoding='utf-8') as f:
    with open(validationLoc, 'w', encoding='utf-8') as f2:
        for root, dirs, files in os.walk(imageLocations):
            count = 0
            random.shuffle(files)
            for file in files:
                if file.endswith(extension) and count <= len(files) * edge:
                    f.write(folderName + file + "\n")
                elif file.endswith(extension):
                    f2.write(folderName + file + "\n")
                count = count + 1
