import argparse
import json
import glob
from lxml import etree as ET

def _main_(args):
    config_path  = args.conf

    with open(config_path) as config_buffer:
        config = json.load(config_buffer)

    folder_name = config['path']['folder']
    annotations_path = config['path']['annotations_path']
    print_out = config['path']['print']

    annotations_paths = glob.glob(annotations_path + '*.xml')
    k=-1

    for k, path in enumerate(annotations_paths):
        tree = ET.parse(path)
        filename = ""

        for elem in tree.iter():
            if 'folder' in elem.tag:
                elem.text = folder_name
            if 'filename' in elem.tag:
                filename = elem.text
            if 'path' in elem.tag:
                elem.text = annotations_path + filename
        if print_out:
            print(filename)
        tree.write(path)

    if print_out:
        print("processed", k+1, "files")

if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='Update annotation xml file for a new folder')
    argparser.add_argument('-c', '--conf', help='path to configuration file')

    args = argparser.parse_args()
    _main_(args)