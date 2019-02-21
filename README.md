# CMPT 470 - Final Project

## Group Members
+ Joshil Patel
+ Sid Agrawal
+ Sonal Unadkat


## Project Description:
Using Tensorflow and Anaconda, utilize Transfer Learning and build upon Google Inception V3 model to better classify our database of 101 food classes.  This model was eventually used in a an Android Application and NutriSnapTest.py to not only classify images but also produce the corresponding nutritional Information. 

## Environment Setup
	 - Anaconda
	 - Install tensorflow-gpu
	 - CUDA Toolkit Installed
	 - Enviroment Variables Set


## Project Components:

1. Retrain_with_Device.py 
	- Modified Tensorflow's Retrain Script that uses a GPU to retrain Google' Inception V3 final layers with a GPU-enabled
	- Original Source : https://github.com/tensorflow/hub/blob/master/examples/image_retraining/retrain.py

	Retrain Scripts will contain all the different models we modified for our project.

2. NutriSnapTest.py
	- Python Script that will feed a Model with a picture and output the model's top 5 predictions as well as feed Nutritionix Client to obtain nutritional information.

	Logic Imported from : https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/label_image/label_image.py

	Usage :python3 NutriSnapTest.py (image_file.jpg) (output_graph.pb)
	Sample Images can be found in : test_pictures 
	Sample Output Graphs can be found in : old_models

	Debugging: Depending on the model you are testing, you may have to modify input_height /input_weight in NutriSnapTest.py Mobile Net requires both to be 224/224 respectively, while Google Inception V3 requres both to be 299/299.

**SUBMISSION DETAILS:**

+ **Git Repo URL:** https://csil-git1.cs.surrey.sfu.ca/agrawal/NutriSnap
+ **Git Branch Name:** Master
+ **Git Tag Name:** nutriSnapSubmission

**DUE:** August 3rd, 2018
