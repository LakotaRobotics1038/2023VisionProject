import numpy as np
import argparse
import cv2
import time

conf_threshold = 0.9
nms_threshold = 0.8
inf_thresh = 50
pixToll = 25 

net = cv2.dnn.readNetFromDarknet('../mk1/yoloCon-tiny-mk1.cfg', '../mk1/backup/yoloCon-tiny-mk1_last.weights')
scale = 1.0 / 255.0
classes = None

classes = None
with open('../mk1/labels.txt', 'r') as f:
    classes = [line.strip() for line in f.readlines()]

COLORS = np.random.uniform(0, 255, size=(len(classes), 3))

def get_output (net):

    layer_names = net.getLayerNames()
    
    output_layers = [layer_names[i-1] for i in net.getUnconnectedOutLayers()]

    return output_layers
    


def draw_bounding_box (img, class_id, confidence, x, y, x_plus_w, y_plus_h):

    label = str(classes[class_id])

    color = COLORS[class_id]

    cv2.rectangle(img, (x,y), (x_plus_w, y_plus_h), color, 2)

    cv2.putText(img, label + f" {confidence}", (x-10, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

def getBetterObj(ID, xBox, yBox, conf, ids, boxes, confs):
    #print('Getting Better object')
    #print(ID, xBox, yBox, conf, ids, boxes, confs)

    ret = True

    for ido, boxo, confo in zip(ids, boxes, confs):
        if ID == ido:
            x = boxo[0]
            y = boxo[1]
            if abs(xBox-x) >= pixToll and abs(yBox-y) >= pixToll:
                ret = ret and True
            else:
                ret = False
    
    return ret
        
    # create if for if there is at least one thing in the index and if there is at least 2 

    #return true if you find abetter box or if the box is not near another box
    # if better box remove the inferior box 

def process(image):
    
    Width = image.shape[1]
    Height = image.shape[0]
    blob = cv2.dnn.blobFromImage(image, scale, (128, 128), (0, 0, 0), True, crop = False)
    net.setInput(blob)
    
    outs = net.forward(get_output(net))

    
    class_ids = []

    confidences = []

    boxes = []

    dataOut = []
    
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
                if len(boxes) == 0 or class_id not in class_ids or getBetterObj(class_id, x, y, confidence, class_ids, boxes, confidences):
                    
                    class_ids.append(class_id)
                    confidences.append(float(confidence))
                    boxes.append([x, y, w, h])
                    dataOut.append({
                        'id': str(class_id),
                        'x': str(center_x),
                        'y': str(center_y),
                        'conf': str(confidence),
                        'area' : str(w * h)
                    })



    indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)
    

    for i in indices:

        box = boxes[i]

        x = box[0]

        y = box[1]

        w = box[2]

        h = box[3]

        
        draw_bounding_box(image, class_ids[i], confidences[i], round(x), round(y), round(x+w), round(y+h))

    
          
    return image, dataOut

