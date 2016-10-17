#!/bin/sh

#build env

# KERNEL=kernel
# KERNEL=kernel7
# make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- bcm2709_defconfig
# make ARCH=arm CROSS_COMPILE=bcm2708- bcmrpi_defconfig menuconfig
# make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- bcmrpi_defconfig
# make ARCH=arm CROSS_COMPILE=bcm2708- -k -j5
# make ARCH=arm CROSS_COMPILE=bcm2708- modules -k -j5
# make modules_install ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- INSTALL_MOD_PATH=../modules/
# make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- zImage modules dtbs

#export PATH=/home/p12791/rbp2/kernel/tools/arm-bcm2708/arm-bcm2708-linux-gnueabi/bin:$PATH
export PATH=/home/p12791/rbp2/tools/arm-bcm2708/gcc-linaro-arm-linux-gnueabihf-raspbian/bin:$PATH
