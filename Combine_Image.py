from pdb import set_trace as st
import os
import numpy as np
import cv2

# base_root = '/home/nguyetgt/Projects/ChuyenDe1/DataFace_created'
fold_a = '/home/nguyetgt/Projects/ChuyenDe1/DataFace_created/GroundTruth'
fold_b = '/home/nguyetgt/Projects/ChuyenDe1/DataFace_created/Skecth'
def combine (src_path):
    if fold_b is None:
        raise Exception('missing fold_b')
    basename, _ = os.path.splitext(os.path.basename(src_path))
    for ext in [".png",".jpg"]:
        sibling_path = os.path.join (fold_b, basename + ext)
        if os.path.exists(sibling_path):
            sibling_path = cv2.imread(sibling_path)
            break
    else:
        raise Exception(" could not find sibling image for "+ fold_a)

    heigh, width, _ = shape
