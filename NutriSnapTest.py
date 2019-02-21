#Imported Logic from TensorFlow's label_image.py
#https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/label_image/label_image.py
#Label_image.Py, is a tensorflow script that imports your output_graph.pb and and feeds an image to the 
# model and output the top 5 matches results.
# We have combined label_image.py, feed our Nutritionix Client our top results.


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from nutritionix.nutritionix import NutritionixClient 

import argparse

import numpy as np
import tensorflow as tf
import sys

def load_graph(model_file):
  graph = tf.Graph()
  graph_def = tf.GraphDef()

  with open(model_file, "rb") as f:
    graph_def.ParseFromString(f.read())
  with graph.as_default():
    tf.import_graph_def(graph_def)

  return graph

def read_tensor_from_image_file(file_name,
                                input_height=224,
                                input_width=224,
                                input_mean=0,
                                input_std=224):
  input_name = "file_reader"
  output_name = "normalized"
  file_reader = tf.read_file(file_name, input_name)
  
  image_reader = tf.image.decode_jpeg(
        file_reader, channels=3, name="jpeg_reader")
  float_caster = tf.cast(image_reader, tf.float32)
  dims_expander = tf.expand_dims(float_caster, 0)
  resized = tf.image.resize_bilinear(dims_expander, [input_height, input_width])
  normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
  sess = tf.Session()
  result = sess.run(normalized)

  return result


def load_labels(label_file):
  label = []
  proto_as_ascii_lines = tf.gfile.GFile(label_file).readlines()
  for l in proto_as_ascii_lines:
    label.append(l.rstrip())
  return label


nix = NutritionixClient(
    application_id='8efe0287',
    api_key='ec7815360d9e4277462ca7daf2f903b5',
    # debug=True, # defaults to False
)

if __name__ == "__main__":

  file_name = sys.argv[1]
  model_file = sys.argv[2]
  label_file = "output_labels.txt"
  input_height = 299
  input_width = 299
  input_mean = 0
  input_std = 255
  input_layer = "Placeholder"
  output_layer = "final_result"


  graph = load_graph(model_file)
  t = read_tensor_from_image_file(
      file_name,
      input_height=input_height,
      input_width=input_width,
      input_mean=input_mean,
      input_std=input_std)

  input_name = "import/" + input_layer
  output_name = "import/" + output_layer
  input_operation = graph.get_operation_by_name(input_name)
  output_operation = graph.get_operation_by_name(output_name)

  with tf.Session(graph=graph) as sess:
    results = sess.run(output_operation.outputs[0], {
        input_operation.outputs[0]: t
    })
  results = np.squeeze(results)
  top_k = results.argsort()[-5:][::-1]
  labels = load_labels(label_file)
  for i in top_k:
    print(labels[i], results[i])

  topFoodItem = labels[top_k[0]]
  nutritionInfo = nix.search(q=topFoodItem, limit=10, offset=0)
  print(nutritionInfo)

