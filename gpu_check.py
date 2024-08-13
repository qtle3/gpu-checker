# Description: Check if CUDA is available and print the GPU information

# import libraries
import torch
import tensorflow as tf

# check if CUDA is available
print("PyTorch CUDA available:", torch.cuda.is_available())
print("PyTorch CUDA device count:", torch.cuda.device_count())

# print the GPU information
if torch.cuda.is_available():
    print("PyTorch CUDA current device:", torch.cuda.current_device())
    print(
        "PyTorch CUDA device name:",
        torch.cuda.get_device_name(torch.cuda.current_device()),
    )
else:
    print("No PyTorch CUDA device found")

# Check if TensorFlow is using GPU
print("\nTensorFlow GPU available:", tf.config.list_physical_devices("GPU"))
print("TensorFlow GPU device count:", len(tf.config.list_physical_devices("GPU")))

# print the Tensorflow GPU information
if tf.config.list_physical_devices("GPU"):
    gpu_devices = tf.config.list_physical_devices("GPU")
    print("TensorFlow GPU device name:", gpu_devices[0].name)
else:
    print("No TensorFlow GPU device found")
