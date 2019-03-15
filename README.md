# Nutrisnap

Using Tensorflow and Anaconda, utilize Transfer Learning and build upon Google Inception V3 model to better classify a database of 101 food classes.

## Languages Used

* Python

## Project Highlights

To see the a project overview and to dive into the math, check out [Nutrisnap](http://joshpatel.ca/nutrisnap) at my portfolio [JoshPatel.ca](http://joshpatel.ca/).

## Contributors
* Joshil Patel
* Sid Agrawal
* Sonal Unadkat

## Environment Setup

Ensure to use a GPU, then do install the following:

* Install Anaconda
* Install tensorflow-gpu
* Install CUDA Toolkit
* Set Enviroment Variables

## Project Components

`Retrain_with_Device.py`
* Modified Tensorflow's Retrain Script that uses a GPU to retrain Google' Inception V3 final layers with a GPU-enabled
* Original Source: https://github.com/tensorflow/hub/blob/master/examples/image_retraining/retrain.py

* Retrain Scripts will contain all the different models we modified for this project.

`NutriSnapTest.py`
* Python Script that will feed a Model with a picture and output the model's top 5 predictions as well as feed Nutritionix Client to obtain nutritional information.

* Logic Imported from: https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/label_image/label_image.py

## Usage 

```
python3 NutriSnapTest.py (image_file.jpg) (output_graph.pb)
```
* Sample Images can be found in `test_pictures`
* Sample Output Graphs can be found in `old_models`

## Debugging
* Depending on the model you are testing, you may have to modify input_height /input_weight in NutriSnapTest.py 
* Mobile Net requires both to be 224/224 respectively, while Google Inception V3 requres both to be 299/299.
