import numpy as np
import time
import cv2
import math

labelsPath = "./coco.names"
LABELS = open(labelsPath).read().strip().split("\n")

np.random.seed(42)
COLORS = np.random.randint(0, 255, size=(len(LABELS), 3),dtype="uint8")

configPath = "./yolov3.cfg"
weightsPath = "./yolov3.weights"

net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)

image =cv2.imread('./images/test_image.jpg')

