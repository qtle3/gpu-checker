# GPU and CUDA Check for PyTorch and TensorFlow

This script checks the availability of CUDA-enabled GPUs and prints detailed GPU information for both PyTorch and TensorFlow frameworks. It's a handy utility for ensuring that your deep learning environment is correctly configured to utilize GPU acceleration.

## Detailed Summary

The script begins by importing necessary libraries, PyTorch and TensorFlow, which are commonly used for deep learning tasks. It checks whether CUDA (the parallel computing platform by NVIDIA) is available, which is essential for running computations on GPUs. For both PyTorch and TensorFlow, the script retrieves and prints detailed information about the available GPUs, including device count, current device, and device name. This information is critical for verifying that your machine learning models will run with GPU acceleration, potentially speeding up training and inference processes significantly.

## Key Concepts Covered

- **CUDA Availability Check:** Verifies if CUDA, NVIDIA's parallel computing architecture, is available, enabling GPU support in PyTorch and TensorFlow.
- **PyTorch GPU Information:** Retrieves and prints the number of GPUs, the current device, and the device name if CUDA is available in the PyTorch environment.
- **TensorFlow GPU Information:** Checks if TensorFlow is configured to use a GPU, lists available GPU devices, and prints the device name.
- **Cross-Framework Compatibility:** Ensures that both PyTorch and TensorFlow environments are correctly set up to leverage GPU resources.

## How to Run

1. **Ensure you have the required dependencies:**
   ```bash
   pip install torch tensorflow
   
2. **Run the script**
   ```bash
   python check_cuda_gpu.py
