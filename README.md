This project was done using YOLOv5 Algorithm
Refer to the official YOLOv5 GitHub Repository below for installation steps
GitHub Source: https://github.com/ultralytics/yolov5

This project prototype was done on a Raspberry Pi 4 with 4 GB RAM as the controller.

Project Summary:
Traffic congestion problems caused by traffic lights stopping the vehicles on pedestrian crossing roads even though there are no pedestrians have been a common problem on busy roads. The project aims to create a fully automated traffic light environment that prevents traffic congestion by detecting if there are pedestrians trying to cross the road using a deep learning based object detection system and a pressure sensor as a double verification system.


The project utilizes MySQL as the local database of the system. Set up the local database and make the necessary changes in detect.py and dasb.py before running the files

To run this project, run the run.py file

To visualize the dashboard graph, run dasb.py


Note:
1. Model used in this project is named as best.pt
   Should a new model be trained, replace the best.pt with the new model and change the model name according to the name of the new model

3. As the project was done on Raspberry Pi, pins on the detect.py file would vary depending on the placement of the wires on the raspberry pins.
   Make sure to modify the settings on the file according to the pin placement should there be any difference
