#! /usr/bin/env python
import os
import argparse
import json
import cv2
from utils.utils import get_yolo_boxes
from utils.colors import get_color
from keras.models import load_model
import numpy as np
import glob
from lxml import etree as ET

def _main_(args):
    config_path  = args.conf

    with open(config_path) as config_buffer:    
        config = json.load(config_buffer)

    print_out = config['predict']['print']
    image_out = config['predict']['image']
    tiny = config['model']['tiny']

    # load variables from config file
    net_h, net_w = config['predict']['net_h'], config['predict']['net_w'] # a multiple of 32, the smaller the faster
    obj_thresh, nms_thresh = config['predict']['obj_thresh'], config['predict']['nms_thresh']
    labels = config['model']['labels']
    anchors = config['model']['anchors']

    # check for CPU or GPU(s)
    os.environ['CUDA_VISIBLE_DEVICES'] = config['model']['gpus']

    # load model weights
    infer_model = load_model(config['train']['saved_weights_name'])

    # gather file paths
    output_path = config['predict']['output_folder']
    test_image_path = config['predict']['test_images']

    image_paths = glob.glob(test_image_path + '*.png')

    # loop through the images
    for k,image_path in enumerate(image_paths):

        # open first image in folder
        image = cv2.imread(image_path)
        image_name = image_path.split("\\")[-1]
        image_title = image_name.split('.')[0]

        boxes = get_yolo_boxes(infer_model, [image], net_h, net_w, anchors, obj_thresh, nms_thresh)[0]
        if print_out:
            print('\n',image_name," 40ft Model")

        # create an etree
        if tiny:
            dataset = ET.Element('dataset', name=config['model']['name'], comment="yolov3_tiny")
        else:
            dataset = ET.Element('dataset', name=config['model']['name'], comment="yolov3")

        image_container = ET.SubElement(dataset, 'image', Name=image_name)

        # loop through the predictions
        for box in boxes:
            label = -1
            score = ""

            # loop through the labels
            for i in range(len(labels)):
                if box.classes[i] > obj_thresh:
                    score = str(round(box.get_score() * 100, 2))+'%'
                    label = i

            if label >= 0:
                ymin_s, xmin_s, ymax_s, xmax_s = str(box.ymin), str(box.xmin), str(box.ymax), str(box.xmax)

                new_label = ET.SubElement(image_container,'bounding_box', object=labels[label], score=score, Ymin=ymin_s, Xmin=xmin_s, Ymax=ymax_s, Xmax=xmax_s)
                image_container.append(new_label)

                if print_out:
                    print(labels[label]+' '+score+' Ymin='+ymin_s+' Xmin='+xmin_s+' Ymax='+ymax_s+' Xmax='+xmax_s)
                if image_out:
                    cv2.rectangle(img=image, pt1=(box.xmin, box.ymin), pt2=(box.xmax, box.ymax), color=get_color(label), thickness=1)

        tree = ET.ElementTree(dataset)
        tree.write(output_path + image_title+'.xml', pretty_print=True, xml_declaration=True, encoding="ISO-8859-1")

        if image_out:
            cv2.imwrite(output_path + image_name, np.uint8(image))

if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='Predict with a trained yolo model')
    argparser.add_argument('-c', '--conf', help='path to configuration file')

    args = argparser.parse_args()
    _main_(args)
