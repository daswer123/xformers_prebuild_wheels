import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

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
    install("https://github.com/daswer123/xformers_prebuild_wheels/raw/main/sm_86/xformers-0.0.14.dev0-cp39-cp39-linux_x86_64.whl")
if(compute == "7.5"):
    install("https://github.com/daswer123/xformers_prebuild_wheels/raw/main/sm_75/xformers-0.0.14.dev0-cp39-cp39-linux_x86_64.whl")
if(compute == "6.1"):
   install("https://github.com/daswer123/xformers_prebuild_wheels/raw/main/sm_61/xformers-0.0.14.dev0-cp39-cp39-linux_x86_64.whl")
if(compute == "5.2"):
    install("https://github.com/daswer123/xformers_prebuild_wheels/raw/main/sm_52/xformers-0.0.14.dev0-cp39-cp39-linux_x86_64.whl")
