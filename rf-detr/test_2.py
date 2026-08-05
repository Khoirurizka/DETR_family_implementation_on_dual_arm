import requests
import supervision as sv
from PIL import Image
from rfdetr import RFDETRLarge
from tqdm import tqdm
from supervision.metrics import MeanAveragePrecision
import random


model = RFDETRLarge(pretrain_weights="output/checkpoint_best_total.pth")
model.optimize_for_inference()

import supervision as sv

Classes = ["","circular_spline", "wave_generator"] 

file_name ="eye2_env_11"
image = Image.open(f"{file_name}.jpg")

detections = model.predict(image, threshold=0.5)

text_scale = sv.calculate_optimal_text_scale(resolution_wh=image.size)
thickness = sv.calculate_optimal_line_thickness(resolution_wh=image.size)
color = sv.ColorPalette.from_hex([
    "#ffff00", "#ff9b00", "#ff66ff", "#3399ff", "#ff66b2", "#ff8080",
    "#b266ff", "#9999ff", "#66ffff", "#33ff99", "#66ff66", "#99ff00"
])

bbox_annotator = sv.BoxAnnotator(color=color,thickness=thickness)
label_annotator = sv.LabelAnnotator(
    color=color,
    text_color=sv.Color.BLACK,
    text_scale=text_scale)

detections_labels = [
    f"{Classes[class_id]} {confidence:.2f}"
    for class_id, confidence
    in zip(detections.class_id, detections.confidence)
]

detections_image = image.copy()
detections_image = bbox_annotator.annotate(detections_image, detections)
detections_image = label_annotator.annotate(detections_image, detections, detections_labels)

detections_image.save(f"{file_name}_result_3.jpg")

