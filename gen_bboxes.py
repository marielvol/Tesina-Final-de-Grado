import os
import numpy as np
import cv2
from glob import glob
from tqdm import tqdm
from skimage.measure import label, regionprops, find_contours

# Create a directory
def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Convert a mask to border image
def mask_to_border(mask):
    h, w = mask.shape
    border = np.zeros((h, w))
    contours = find_contours(mask, 128)
    for contour in contours:
        for c in contour:
            x = int(c[0])
            y = int(c[1])
            border[x][y] = 255

    return border

# Convert a mask to bounding boxes
def mask_to_bbox(mask):
    bboxes = []
    mask = mask_to_border(mask)
    lbl = label(mask)
    props = regionprops(lbl)
    for prop in props:
        x1 = prop.bbox[1]
        y1 = prop.bbox[0]
        x2 = prop.bbox[3]
        y2 = prop.bbox[2]
        bboxes.append([x1, y1, x2, y2])

    return bboxes

# Transform bounding box to YOLO format
def bbox_to_YOLO(bboxes):
    bboxes_YOLO = []
    for bbox in bboxes:
      w = bbox[2] - bbox[0]
      h = bbox[3] - bbox[1]
      x = bbox[0] + int(w/2)
      y = bbox[1] + int(h/2)
      bboxes_YOLO.append([x, y, w, h])

    return bboxes_YOLO

# Normalize bounding boxes
def normalize_bboxes(bboxes,mask):
    h, w = mask.shape
    for bbox in bboxes:
      bbox[0] = bbox[0] / w
      bbox[1] = bbox[1] / h
      bbox[2] = bbox[2] / w
      bbox[3] = bbox[3] / h
    
    return bboxes


if __name__ == "__main__":
    # Load the dataset
    folder_path = "CVC-ClinicDB" # Indicate dataset path
    images = sorted(glob(os.path.join(folder_path, "images", "*")))
    masks = sorted(glob(os.path.join(folder_path, "annotations", "*")))

    # Create a folder to save the labels
    create_dir(os.path.join(folder_path, "labels"))

    # Loop over the dataset
    for x, y in tqdm(zip(images, masks), total=len(images)):
        # Extract the image name
        name = x.split("\\")[-1].split(".")[0]
        #print(name)

        # Read image and mask
        x = cv2.imread(x, cv2.IMREAD_COLOR)
        y = cv2.imread(y, cv2.IMREAD_GRAYSCALE)

        # Detect the bounding boxes
        bboxes = mask_to_bbox(y)

        # Convert the bounding boxes to YOLO format
        bboxes_YOLO = bbox_to_YOLO(bboxes)

        # Normalize the bounding boxes
        bboxes_YOLO_norm = normalize_bboxes(bboxes_YOLO,y)
        
        # Create a .txt file with the labels
        file = open(f"labels\\{name}.txt", "w")
        for bbox in bboxes_YOLO_norm:
          line = str('0')+' '+str(bbox[0])+' '+str(bbox[1])+' '+str(bbox[2])+' '+str(bbox[3])+'\n'
          file.write(line)
        file.close()
        