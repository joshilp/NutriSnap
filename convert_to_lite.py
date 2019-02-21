#https://stackoverflow.com/questions/50349473/tensorflow-lite-no-module-named-tf-contrib-lite
from  tensorflow.contrib.lite.python import convert_saved_model

convert_saved_model.tflite_from_saved_model(saved_model_dir="/output_graph.pb",output_file="/TF_Lite_Model")

'''

toco \
  --input_file=output_graph.pb \
  --output_file=optimized_graph.tflite \
  --input_format=TENSORFLOW_GRAPHDEF \
  --output_format=TFLITE \
  --input_shape=1,224,224,3 \
  --input_array=input \
  --output_array=final_result \
  --inference_type=FLOAT \
  --input_data_type=FLOAT
  '''

  '''
  toco \
  --input_file=output_graph.pb \
  --output_file=output_graph.tflite \
  --input_format=TENSORFLOW_GRAPHDEF \
  --output_format=TFLITE \
  --inference_type=QUANTIZED_UINT8 \
  --input_shape=1,224,224,3 \
  --input_array=Placeholder \
  --output_array=final_result \
  --mean_value=128 --std_value=128 --default_range_min=0 --default_range_max=1
  '''

  --input_format=TENSORFLOW_GRAPHDEF --output_format=TFLITE --inference_type=QUANTIZED_UINT8 --input_shape=1,224,224,3 --input_array=Placeholder --output_array=final_result --mean_value=128 --std_value=128 --default_ranges_min=0 --default_ranges_max=1