#Function for determining compute capability 
def get_compute_capability(string):
    return string.split(',')[3].split(':')[1].strip()

from tensorflow.python.client import device_lib
gpu = device_lib.list_local_devices()
compute = get_compute_capability(gpu[1].physical_device_desc)

print(gpu[1].physical_device_desc)
print(compute)


#Install precompiled wheel
if(compute == "8.6"):
    !pip install https://github.com/daswer123/stable-diffusion-colab/raw/main/xformers%20prebuild/sm_86/xformers-0.0.14.dev0-cp39-cp39-linux_x86_64.whl
if(compute == "7.5"):
    !pip install https://github.com/daswer123/stable-diffusion-colab/raw/main/xformers%20prebuild/sm_75/xformers-0.0.14.dev0-cp39-cp39-linux_x86_64.whl
if(compute == "6.1"):
    !pip install https://github.com/daswer123/stable-diffusion-colab/raw/main/xformers%20prebuild/sm_61/xformers-0.0.14.dev0-cp39-cp39-linux_x86_64.whl
if(compute == "5.2"):
    !pip install https://github.com/daswer123/stable-diffusion-colab/raw/main/xformers%20prebuild/sm_52/xformers-0.0.14.dev0-cp310-cp310-win_amd64.whl
