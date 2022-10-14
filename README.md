# xformers_prebuild_wheels
xformers prebuild wheels for various video cards, suitable for both paperspace and google colab

All prebuilds were created on paperspace, tested on stable-diffusion neural network

You can try to install a prebuild wheel if your gpu meets the requirements of https://developer.nvidia.com/cuda-gpus under CUDA-Enabled 

All wheels are suitable for the paperspace platform

Below I will list exactly which wheels fit on your card and other cards might fit too

### Script for auto-installation, this script automatically detects the GPU in the system and installs the appropriate xformers wheels 

1) [paperspace_xformers_intall.py](https://github.com/daswer123/xformers_prebuild_wheels/raw/main/paperspace_xformers_intall.py) - This script automatically detects the GPU and installs the appropriate wheels, works on **paperspace** includes all free GPU level PRO

2) google_xformers_install.py - also detects GPU and install wheels

# Paperspace GPU's

### SM_86 - RTX A4000

`pip install https://github.com/daswer123/xformers_prebuild_wheels/raw/main/sm_86/xformers-0.0.14.dev0-cp39-cp39-linux_x86_64.whl`

### SM_75 - RTX 5000, RTX 4000

`pip install https://github.com/daswer123/xformers_prebuild_wheels/raw/main/sm_75/xformers-0.0.14.dev0-cp39-cp39-linux_x86_64.whl`

### SM_61 - P5000

`pip install https://github.com/daswer123/xformers_prebuild_wheels/raw/main/sm_61/xformers-0.0.14.dev0-cp39-cp39-linux_x86_64.whl`

### SM_52 - Free GPU, Quadro M4000

`pip install https://github.com/daswer123/xformers_prebuild_wheels/raw/main/sm_52/xformers-0.0.14.dev0-cp39-cp39-linux_x86_64.whl`


# Google Colab GPU's

### Tesla T4, python 3.7 ( default ) and python 3.9

**Python 3.7 ( default in colab )**

`pip install https://github.com/daswer123/xformers_prebuild_wheels/raw/main/Google%20Collab/T4/python37/xformers-0.0.14.dev0-cp37-cp37m-linux_x86_64.whl`

**Python 3.8**

`pip install https://github.com/daswer123/xformers_prebuild_wheels/raw/main/Google%20Collab/T4/python38/xformers-0.0.14.dev0-cp38-cp38-linux_x86_64.whl`

**Python 3.9**

`pip install https://github.com/daswer123/xformers_prebuild_wheels/raw/main/Google%20Collab/T4/python37/xformers-0.0.14.dev0-cp37-cp37m-linux_x86_64.whl`

### V100, P100, A100, I don't have a Google Colab subscription, so I can't guarantee that it works.
Thanks to https://github.com/TheLastBen/fast-stable-diffusion for posting the wheels for these GPU's

**V100**

`pip install https://github.com/daswer123/xformers_prebuild_wheels/raw/main/Google%20Collab/V100/xformers-0.0.13.dev0-py3-none-any.whl`

**P100**

`pip install https://github.com/daswer123/xformers_prebuild_wheels/raw/main/Google%20Collab/P100/xformers-0.0.13.dev0-py3-none-any.whl`

**A100**

`pip install https://github.com/daswer123/xformers_prebuild_wheels/raw/main/Google%20Collab/A100/xformers-0.0.13.dev0-py3-none-any.whl`
