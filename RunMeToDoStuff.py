import os

#Create - converts darknet weights to keras weights for full model
#os.system("python create.py -w Path to yolov3.weights -c config.json")

#Train - edit config.json to alter training settings, currently using auto train/valid split
#os.system("python train.py -c config.json")

#Evaluate, put some images in eval_images and images annotations into eval_annotations
#os.system("python evaluate.py -c config.json")

#Predict, put images into test_images folder
#os.system("python predict.py -c config.json")