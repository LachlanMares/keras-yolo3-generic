# YOLO3 (Convert to Keras, Training, and Evaluation)

## Model

Grab the pretrained weights of yolo3 from https://pjreddie.com/media/files/yolov3.weights.

Create additional folders in keras-yolo3-generic for:
train images            "train_image_folder"
train annotations       "train_annot_folder"
validation images       "valid_image_folder"
validation annotations  "valid_annot_folder"
evaluation images       "eval_image_folder"
evaluation annotations  "eval_annots_folder"
test images
output

Add downloaded yolov3 weights into keras-yolov3-generic folder. Edit the line below in RunMeToDoSTuff.py. Set path to folder, specify a name for your model, then run it

#os.system("python create.py -w Path_to_current_folder -m NewModelName.h5")

## Training

Add your images into the train_images and valid_images folder. If you put all images in train_images and don't specify a vaid_images path in config.json the data is split 80/20 automatically during training
Add your annotations files to the train_annotations folder, and vaild_annotations if used. Use PascalVOC annotations

edit the config.json to alter training settings, add paths, labels and names

    "model" : {
        "min_input_size":       132,
        "max_input_size":       448,
        "anchors":              [10,13,  16,30,  33,23,  30,61,  62,45,  59,119,  116,90,  156,198,  373,326],
        "labels":               [""]
    },

    "train": {
        "train_image_folder":   "Path to train_images folder",
        "train_annot_folder":   "Path to train_annotations folder",
        "cache_name":           "Add a name.pkl",

        "train_times":          20,                 # the number of time to cycle through the training set, useful for small datasets
        "pretrained_weights":   "model.h5",         # specify the path of the pretrained weights, but it's fine to start from scratch
        "batch_size":           8,                  # the number of images to read in each batch
        "learning_rate":        1e-4,               # the base learning rate of the default Adam rate scheduler
        "nb_epochs":            100,                # number of epoches
        "warmup_epochs":        3,
        "ignore_thresh":        0.5,
        "gpus":                 "0,1",

        "grid_scales":          [1,1,1],
        "obj_scale":            5,
        "noobj_scale":          1,
        "xywh_scale":           1,
        "class_scale":          1,

        "tensorboard_dir":      "logs",
        "saved_weights_name":   "Add a name",
        "debug":                true
    },

    "valid": {
        "valid_image_folder":   "Path to valid_images folder or leave blank to use a 80/20 train valid split",
        "valid_annot_folder":   "Path to valid_annotations folder or leave blank to use a 80/20 train valid split",
        "cache_name":           "",

        "valid_times":          1
    }

Run this line in RunMeToDoStuff.py

#os.system("python train.py -c config.json")

## Re-Training

Use this if you have made additions to your image/annotations or want to retain a extra few epochs, edit config.json retrain section, 

    "retrain": {
        "train_times":          10,
        "learning_rate":        5e-5,
        "nb_epochs":            25,
        "warmup_epochs":        3,
        "ignore_thresh":        0.5
    },

Run this line in RunMeToDoStuff.py

#os.system("python train.py -c config.json -r retrain")

## Evaluation

#Evaluate, edit config.json, put some images in eval_images and eval images annotations into eval_annotations

    "evaluate": {
        "eval_image_folder":   ".../eval_images/",
        "eval_annot_folder":   ".../eval_annotations/"
    }
}

Run this line in RunMeToDoStuff.py

#os.system("python evaluate.py -c config.json")

## Predict

Put images into test_images folder

Run this line in RunMeToDoStuff.py

#os.system("python predict.py -c config.json -i Path to test_images folder -o Path to output folder")
