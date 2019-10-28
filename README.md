# YOLO3 (Convert to Keras, Training, and Evaluation)

## Model

To greate a full version:

Grab the pretrained weights of yolo3 from https://pjreddie.com/media/files/yolov3.weights.

Create additional folders in keras-yolo3-generic for:
train images            "train_image_folder"
train annotations       "train_annot_folder"
validation images       "valid_image_folder"
validation annotations  "valid_annot_folder"
evaluation images       "eval_image_folder"
evaluation annotations  "eval_annots_folder"
test images             "test_images"
output                  "output"

Add downloaded yolov3 weights into keras-yolov3-generic folder. 

Edit config.json. set your label names, specify a name for your model, set tiny to false

Edit the line below in RunMeToDoSTuff.py. Set path to weights file, then run it

#os.system("python create.py -c config.json")

## Training

Add your images into the train_images and valid_images folder. If you put all images in train_images and don't specify a vaid_images path in config.json the data will be randomly split as per parameter "valid""train_validate_split"

Add your annotations files to the train_annotations folder, and vaild_annotations if used. Use PascalVOC annotations

edit the config.json to alter training settings, add paths, labels and names

    "model" : {
        "min_input_size":       132,
        "max_input_size":       448,
        "anchors":              [10,13,  16,30,  33,23,  30,61,  62,45,  59,119,  116,90,  156,198,  373,326],
        "labels":               ["obj 1","obj 2","obj 3","obj 4"],
        "name":                 "model_name",
        "tiny":                 true
    },

    "train": {
        "train_image_folder":   "Path to train_images",
        "train_annot_folder":   "Path to train annotations",
        "cache_name":           "model_name.pkl",

        "train_times":          10,
        "pretrained_weights":   "model_name.h5",
        "batch_size":           8,
        "learning_rate":        1.5e-4,
        "nb_epochs":            97,
        "warmup_epochs":        3,
        "ignore_thresh":        0.5,
        "gpus":                 "0",

        "grid_scales":          [1,1,1],
        "obj_scale":            5,
        "noobj_scale":          1,
        "xywh_scale":           1,
        "class_scale":          1,

        "tensorboard_dir":      "model_name_logs",
        "saved_weights_name":   "",
        "debug":                true
    },

    "retrain": {
        "train_times":          5,
        "learning_rate":        1e-4,
        "nb_epochs":            20,
        "warmup_epochs":        0,
        "ignore_thresh":        0.5,
        "enabled":              false
    },

    "valid": {
        "valid_image_folder":   "",
        "valid_annot_folder":   "",
        "cache_name":           "",
        "train_validate_split": 0.8,
        "valid_times":          1
    },

    "evaluate": {
        "eval_image_folder":    "Path to eval_images",
        "eval_annot_folder":    "Path to eval_annotations/"
    },

    "predict": {
        "test_images":          "Path to test_images",
        "output_folder":        "Path to output",
        "net_h":                416,
        "net_w":                416,
        "obj_thresh":           0.5,
        "nms_thresh":           0.5,
        "print":                false,
        "image":                true

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

#Evaluate, edit config.json retrain parameter "enabled" to true, put some images in eval_images and eval images annotations into eval_annotations

    "retrain": {
        "train_times":          5,
        "learning_rate":        1e-4,
        "nb_epochs":            20,
        "warmup_epochs":        0,
        "ignore_thresh":        0.5,
        "enabled":              false
    },

Run this line in RunMeToDoStuff.py

#os.system("python evaluate.py -c config.json")

## Predict

Put images into test_images folder

Run this line in RunMeToDoStuff.py

#os.system("python predict.py -c config.json)
