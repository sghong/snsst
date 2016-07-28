#!/bin/sh


# make ARCH=arm CROSS_COMPILE=bcm2708- bcmrpi_defconfig menuconfig
# make ARCH=arm CROSS_COMPILE=bcm2708- -k -j5
# make ARCH=arm CROSS_COMPILE=bcm2708- modules -k -j5
# make modules_install ARCH=arm CROSS_COMPILE=bcm2708- INSTALL_MOD_PATH=../modules/

export PATH=/home/p12791/rbp/kernel/tools/arm-bcm2708/arm-bcm2708-linux-gnueabi/bin:$PATH
