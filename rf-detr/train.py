from rfdetr import RFDETRLarge
from roboflow import download_dataset
import os
from roboflow import Roboflow
rf = Roboflow(api_key="4DAjUvJqgEBbY7vw9wTk")

model = RFDETRLarge()
project = rf.workspace("projectulartangga").project("harmonic_drive")
version = project.version(7)
dataset = version.download("coco")
model.train(dataset_dir=dataset.location, epochs=300, batch_size=8, grad_accum_steps=2)
#model.train(dataset_dir="Harmonic_Drive-3", epochs=1, batch_size=8, grad_accum_steps=2)

