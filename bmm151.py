import smbus
import sys, getopt 
from time import sleep

bus=smbus.SMBus(1)

BMM151_DEVICE_ADDRESS = 0x10

BMI151_CHIP_ID = 0x32

#Mag bmm150 register adress
BMM050_CHIP_ID                =     0x40
        
BMM050_DATAX_LSB              =     0x42
BMM050_DATAX_MSB              =     0x43
BMM050_DATAY_LSB              =     0x44
BMM050_DATAY_MSB              =     0x45
BMM050_DATAZ_LSB              =     0x46
BMM050_DATAZ_MSB              =     0x47                                                                                
BMM050_R_LSB                  =     0x48
BMM050_R_MSB                  =     0x49

BMM050_INT_STAT               =     0x4A

BMM050_POWER_CNTL             =     0x4B 
BMM050_CONTROL                =     0x4C                                                                                
BMM050_INT_CNTL               =     0x4D
BMM050_SENS_CNTL              =     0x4E
BMM050_LOW_THRES              =     0x4F
BMM050_HIGH_THRES             =     0x50
BMM050_NO_REPETITIONS_XY      =     0x51
BMM050_NO_REPETITIONS_Z       =     0x52

BMM050_DR_10HZ                =     0
BMM050_DR_02HZ                =     1
BMM050_DR_06HZ                =     2
BMM050_DR_08HZ                =     3
BMM050_DR_15HZ                =     4
BMM050_DR_20HZ                =     5
BMM050_DR_25HZ                =     6
BMM050_DR_30HZ                =     7

BMM050_NORMAL_MODE            =          0x00 
BMM050_FORCED_MODE            =          0x01
BMM050_SUSPEND_MODE           =          0x02
BMM050_SLEEP_MODE             =          0x03

BMM050_DATAX_LSB              =     0x42
BMM050_DATAX_MSB              =     0x43
BMM050_DATAY_LSB              =     0x44
BMM050_DATAY_MSB              =     0x45
BMM050_DATAZ_LSB              =     0x46
BMM050_DATAZ_MSB              =     0x47

#wake up bmm151
bus.write_byte_data(BMM151_DEVICE_ADDRESS, BMM050_POWER_CNTL, 0x01 )
sleep(0.1)
#tmp = bus.read_byte_data(BMM151_DEVICE_ADDRESS, 0x4b)
#print "tmp 0x%X, BMI160" % tmp

#sleep(1)
chipid = bus.read_byte_data(BMM151_DEVICE_ADDRESS, BMM050_CHIP_ID)

print "---------"
if chipid == BMI151_CHIP_ID:
  print "chip id is 0x%X, bmm151" % chipid
print "---------" 

# data rate set to 10hz
v_data_rate_bit = bus.read_byte_data(BMM151_DEVICE_ADDRESS, BMM050_CONTROL)
print "0x%X, " % v_data_rate_bit
data_rate = BMM050_DR_10HZ 
v_data_rate_bit = (v_data_rate_bit & ~0x38) | ((data_rate << 3) & 0x38) 
bus.write_byte_data(BMM151_DEVICE_ADDRESS, BMM050_CONTROL, v_data_rate_bit)

#op_mode set to normal
v_op_mode_bit = bus.read_byte_data(BMM151_DEVICE_ADDRESS, BMM050_CONTROL)
#print "0x%X, " % v_data_rate_bit
op_mode = BMM050_NORMAL_MODE
v_op_mode_bit = (v_op_mode_bit & ~0x06) | ((op_mode << 2) & 0x06) 
bus.write_byte_data(BMM151_DEVICE_ADDRESS, BMM050_CONTROL, v_op_mode_bit)

while 1:
 #read XYZ mag value
 mag_value = [ 0, 0, 0, 0, 0, 0 ]
 mag_value = bus.read_i2c_block_data(BMM151_DEVICE_ADDRESS, BMM050_DATAX_LSB, 6)
 
 mag_value[0] = ((mag_value[0] &  0xF8) >> 3)
 mag_raw_x =  (mag_value[1] << 5) | mag_value[0]
 
 mag_value[2] = ((mag_value[2] &  0xF8) >> 3)
 mag_raw_y =  (mag_value[2] << 5) | mag_value[2]
 
 mag_value[4] = ((mag_value[4] &  0xFE) >> 1)
 mag_raw_z =  (mag_value[4] << 5) | mag_value[4]
 
 print "mag x=0x%X, y=0x%X, z=0x%X" % (mag_raw_x, mag_raw_y, mag_raw_z)

sys.exit()




