import os

#Build new keras model by loading/converting pre-trained weights
#os.system("python create.py -w .../yolov3.weights -m .h5")

#Train - edit config.json to alter training settings, currently using auto train/valid split
#os.system("python train.py -c config.json")

#Re-train
#os.system("python train.py -c config.json -r retrain")

#Evaluate, put some images in eval_images and images annotations into eval_annotations
#os.system("python evaluate.py -c config.json")

#Predict, put images into test_images folder
#os.system("python predict.py -c config.json -i .../test_images/ -o .../output/")

