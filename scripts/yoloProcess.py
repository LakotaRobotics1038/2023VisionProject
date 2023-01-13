import numpy as np
import argparse
import cv2

conf_threshold = 0.3
nms_threshold = 0.2

net = cv2.dnn.readNetFromDarknet('/home/team1038/repos/2023VisionProject/mk1/yoloCon-tiny-mk1.cfg', '/home/team1038/repos/2023VisionProject/mk1/backup/yoloCon-tiny-mk1_last.weights')
scale = 1.0 / 255.0
classes = None

classes = None
with open('/home/team1038/repos/2023VisionProject/mk1/labels.txt', 'r') as f:
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

    
def process(image):
    
    Width = image.shape[1]
    Height = image.shape[0]
    blob = cv2.dnn.blobFromImage(image, scale, (416, 416), (0, 0, 0), True, crop = False)
    net.setInput(blob)
    outs = net.forward(get_output(net))

    class_ids = []

    confidences = []

    boxes = []


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
    

    for i in indices:

        box = boxes[i]

        x = box[0]

        y = box[1]

        w = box[2]

        h = box[3]

        
        draw_bounding_box(image, class_ids[i], confidences[i], round(x), round(y), round(x+w), round(y+h))

    return image

