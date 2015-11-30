Installation of NVIDIA GPU Driver and CUDA
========================================


Disable Nouveau (default graphic driver on Ubuntu)
--------------------------------------------------
1. Open `/etc/modprobe.d/blacklist-nouveau.conf` and add the following lines:
   ```bash
   blacklist nouveau
   options nouveau modeset=0
   ```
   Save it (`sudo` privilege may be required).

2. Execute `$sudo update-initramfs -u` and reboot system.


Install NVIDIA GPU Driver
-------------------------
(You can download the latest NVIDIA GPU driver (.run file) from <http://www.nvidia.com/Download/index.aspx>)

1. If graphical login-screen appears, press `[Alt] + [Ctrl] + [F1]` and login by virtual console (CUI environment).

2. Execute `$sudo service lightdm stop` to kill X server temporarily.

3. Execute `$sudo sh NVIDIA-***.run`  or `$sudo sh NVIDIA-***.run --no-opengl-files` (on laptops that have both integrated graphic card and NVIDIA-GPU).

    _NOTE:_
    **DO NOT run the NVIDIA configuration for X windowing system at the end of the installation of the GPU driver on laptop**,
    since your integrated graphic card will be used to display the desktop.
    The NVIDIA card will run whenever needed automatically.

4. Reboot system


Install CUDA
------------
(You can download the latest CUDA installer (.run file) from <https://developer.nvidia.com/cuda-downloads>)

1. Execute `$sudo sh cuda_***.run`
   You don't have to install GPU driver contained in CUDA installer as you have already installed the latest one in the previous section.

2. Once the installation completes, export PATH and LD_LIBRARY_PATH according to the installer message.
   EX.
   open `~/.bashrc` with your favorite text editor and add these two lines:
   ```bash
   export PATH=/usr/local/cuda/bin:$PATH
   export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
   ```

Some additional packages maybe required in order to fully compile CUDA samples:
`$sudo apt-get install freeglut3-dev build-essential libx11-dev libxmu-dev libxi-dev libgl1-mesa-glx libgl1-mesa-dev`

If you receive a compiler error such as `/usr/bin/ld: cannot find -lGL`, this command may resolve it:
```bash
$sudo ln -s /usr/lib/libGL.so.1 /usr/lib/libGL.so
```


If CUDA is not active, you can enable it manually running the following lines as root:
----------------------------------------------------------------
1. Create `/etc/init.d/cuda_setup_script` with the following content:

    ```bash
    #!/bin/bash

    /sbin/modprobe nvidia

    if [ "$?" -eq 0 ]; then
    # Count the number of NVIDIA controllers found.
    NVDEVS=`lspci | grep -i NVIDIA`
    N3D=`echo "$NVDEVS" | grep "3D controller" | wc -l`
    NVGA=`echo "$NVDEVS" | grep "VGA compatible controller" | wc -l`

    N=`expr $N3D + $NVGA - 1`
    for i in `seq 0 $N`; do
    mknod -m 666 /dev/nvidia$i c 195 $i
    done

    mknod -m 666 /dev/nvidiactl c 195 255

    else
    exit 1
    fi

    /sbin/modprobe nvidia-uvm

    if [ "$?" -eq 0 ]; then
    # Find out the major device number used by the nvidia-uvm driver
    D=`grep nvidia-uvm /proc/devices | awk '{print $1}'`

    mknod -m 666 /dev/nvidia-uvm c $D 0
    else
    exit 1
    fi
    ```
    (Reference: <http://docs.nvidia.com/cuda/cuda-getting-started-guide-for-linux/index.html#runfile-verifications>)

2. Execute: `$sudo chmod +x /etc/init.d/cuda_setup_script`

3. Finally run: `$sudo update-rc.d cuda_setup_script defaults`

   _NOTE:_
   **DO NOT** specify full path of cuda_setup_script as 2nd argument.
