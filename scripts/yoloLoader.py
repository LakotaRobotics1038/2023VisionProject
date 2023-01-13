
import numpy as np
import argparse
import cv2

#when run run from the comand line!!

# yoloLoading is branch to pus this tonight make sure you are on teh branch\

#do not look at this code it is very messy

#creating the blob, remember this later


#accesssing the network, this will be what is referenced later in get_output and draw_box. The network passes in the
#weights file and the yolo config file. 

#all files/text that will be passed in when we run the program in the terminal. this should hopefully work but ehh
ap = argparse.ArgumentParser()

ap.add_argument('-w', '--weights', required = True, help = '/home/team1038/repos/2023VisionProject/mk1/backup')
ap.add_argument('-i', '--image', required = True, help = '/home/team1038/repos/2023VisionProject/mk1/labeledData')#should be the path to our input images put it's the folder they're in
ap.add_argument('-c', '--config', required = True, help = '/home/team1038/repos/2023VisionProject/mk1/yoloCon-tiny-mk1.cfg')
ap.add_argument('-cl', '--classes', required = True, help = '/home/team1038/repos/2023VisionProject/mk1/labels.txt')

args = ap.parse_args()
#the image!!!!
image = cv2.imread(args.image)

Width = image.shape[1]
Height = image.shape[0]

scale = 1.0 / 255 # this is the default you don't need to pass this in

#read class names from text files

classes = None
with open(args.classes, 'r') as f:
    classes = [line.strip() for line in f.readlines()]

#not sure if this needs to be changed
COLORS = np.random.uniform(0, 255, size=(len(classes), 3))

net = cv2.dnn.readNetFromDarknet(args.config, args.weights)

blob = cv2.dnn.blobFromImage(image, scale, (416, 416), (0, 0, 0), True, crop = False)

#the output!!!!
net.setInput(blob)


#unfinished code. see 'output layer and bounding box' section of reference code. will *hopefully* access layers
#from the network.
def get_output (net):

    #accessing layer names from network
    layer_names = net.getLayerNames()
    print(net.getUnconnectedOutLayers())
    output_layers = [layer_names[i-1] for i in net.getUnconnectedOutLayers()]

    return output_layers
    

#also very unfinished, relies almost entirely on line 16 correctly accessing the network and the network correctly
#having stored the layers and colours. ask connor, idk.

def draw_bounding_box (img, class_id, confidence, x, y, x_plus_w, y_plus_h):

    label = str(classes[class_id])

    color = COLORS[class_id]

    cv2.rectangle(img, (x,y), (x_plus_w, y_plus_h), color, 2)

    cv2.putText(img, label, (x-10, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    
outs = net.forward(get_output(net))

class_ids = []

confidences = []

boxes = []

conf_threshold = 0.3
nms_threshold = 0.2

for out in outs:
    for detection in out:

        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        
        if confidence > conf_threshold:
            
            center_x = int(detection[0] * Width)
            center_y = int(detection[1] * Height)
            w = int(detection[2] * Width)
            h = int(detection[3] * Height)
            x = center_x - w/2
            y = center_y - h/2
            class_ids.append(class_id)
            confidences.append(float(confidence))
            boxes.append([x, y, w, h])
            


indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)
print(indices)

for i in indices:

    box = boxes[i]

    x = box[0]

    y = box[1]

    w = box[2]

    h = box[3]

    draw_bounding_box(image, class_ids[i], confidences[i], round(x), round(y), round(x+w), round(y+h))


image = cv2.resize(image, (900, 2000))

cv2.imshow('object detection', image)

cv2.waitKey()
