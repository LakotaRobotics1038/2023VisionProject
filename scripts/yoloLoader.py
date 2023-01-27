import numpy as np
import argparse
import cv2

#when run run from the comand line!!

# yoloLoading is branch to pus this tonight make sure you are on teh branch\

#do not look at this code it is very messy

#creating the blob, remember this later
blob = cv2.dnn.blobFromImage(image, (416, 416), (0, 0, 0), True, crop = False);

#accesssing the network, this will be what is referenced later in get_output and draw_box. The network passes in the
#weights file and the yolo config file. 
net = cv2.dnn.readNetFromDarknet(args.weights, args.config);

#all files/text that will be passed in when we run the program in the terminal. this should hopefully work but ehh
argparse = argparse.ArgumentParser();

ap.add_argument('-w', '--weights', required = True);
ap.add_argument('-i', '--image', required = True, help = '/home/team1038/repos/2023VisionProject/mk1/labeledData');#should be the path to our input images
ap.add_argument('-c', '--config', required = True, help = '/home/team1038/repos/2023VisionProject/mk1/yoloCon-tiny-mk1.cfg');
ap.add_argument('-cl', '--classes', required = True);

#the image!!!!
image = cv2.imread(args.image);

#the output!!!!
net.setInput(blob);


#unfinished code. see 'output layer and bounding box' section of reference code. will *hopefully* access layers
#from the network.
def get_output (net) {

    #accessing layer names from network
    layer_names = net.getLayerNames();

    output_layers;

    return output_layers;
    }

#also very unfinished, relies almost entirely on line 16 correctly accessing the network and the network correctly
#having stored the layers and colours. ask connor, idk.

def draw_box (image, x, y, x_plus_w, y_plus_h) {

    #will draw a box around objects. [colors] represents the colors that each object the network is trained to
    #recognize should have. for example cones should be preassigned bright green (i think). 

    cv2.rectangle(image, (x,y), (x_plusw, y_plus_h), [COLORS], 1);

    #puts text/labels next to the box. for example a cone should say "cone".

    cv2.putText(img, [LABEL], (x-10, y-10), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.5, [COLORS],2); 
    }
