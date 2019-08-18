import os

#Build new keras model by loading/converting pre-trained yolov3 weights
#os.system("python create.py -w Path_to_current_folder -m NewModelName.h5")

#Train - edit config.json to alter training settings, add paths, labels and names
#os.system("python train.py -c config.json")

#Re-train - edit retrain_config.json to alter training settings, add paths, labels and names
#os.system("python train.py -c retrain_config.json")

#Evaluate, edit eval_config.json, put some images in eval_images and eval_images annotations into eval_annotations
#os.system("python evaluate.py -c eval_config.json")

#Predict, put images into test_images folder
#os.system("python predict.py -c config.json -i Path to test_images folder -o Path to output folder")

