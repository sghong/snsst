## test3
import smbus
import sys, getopt 
from time import sleep

bus=smbus.SMBus(1)

BMI160_DEVICE_ADDRESS = 0x69

BMI160_REGA_USR_CHIP_ID      = 0x00
BMI160_REGA_USR_ACC_CONF_ADDR     = 0x40 
BMI160_REGA_USR_ACC_RANGE_ADDR    = 0x41
BMI160_REGA_USR_GYR_CONF_ADDR     = 0x42
BMI160_REGA_USR_GYR_RANGE_ADDR    = 0x43

BMI160_REGA_CMD_CMD_ADDR          =   0x7e
BMI160_REGA_CMD_EXT_MODE_ADDR     =   0x7f

CMD_SOFT_RESET_REG      = 0xb6

CMD_PMU_ACC_SUSPEND     = 0x10
CMD_PMU_ACC_NORMAL      = 0x11
CMD_PMU_ACC_LP1         = 0x12
CMD_PMU_ACC_LP2         = 0x13
CMD_PMU_GYRO_SUSPEND    = 0x14
CMD_PMU_GYRO_NORMAL     = 0x15
CMD_PMU_GYRO_FASTSTART  = 0x17

BMI160_USER_DATA_14_ADDR = 0X12 # accel x 
BMI160_USER_DATA_15_ADDR = 0X13 # accel x 
BMI160_USER_DATA_16_ADDR = 0X14 # accel y 
BMI160_USER_DATA_17_ADDR = 0X15 # accel y 
BMI160_USER_DATA_18_ADDR = 0X16 # accel z 
BMI160_USER_DATA_19_ADDR = 0X17 # accel z 

BMI160_USER_DATA_8_ADDR  = 0X0C 
BMI160_USER_DATA_9_ADDR  = 0X0D
BMI160_USER_DATA_10_ADDR = 0X0E
BMI160_USER_DATA_11_ADDR = 0X0F
BMI160_USER_DATA_12_ADDR = 0X10
BMI160_USER_DATA_13_ADDR = 0X11

if len(sys.argv) == 1 :
  print "Usage : bmi160.py [ A | G ] "
  sys.exit()

chipid = bus.read_byte_data(BMI160_DEVICE_ADDRESS, BMI160_REGA_USR_CHIP_ID )

print "---------"
if chipid == 0xD1 :
  print "chip id is 0x%X, BMI160" % chipid
else :
  print "Exit"
  sys.exit()
print "---------" 

#bus.write_byte_data(BMI160_DEVICE_ADDRESS, 0x03, 0x19 )
#tmp = bus.read_byte_data(BMI160_DEVICE_ADDRESS, 0x03)
#print "tmp 0x%X, BMI160" % tmp 

#chip init
bus.write_byte_data(BMI160_DEVICE_ADDRESS, BMI160_REGA_USR_ACC_CONF_ADDR, 0x25)
bus.write_byte_data(BMI160_DEVICE_ADDRESS, BMI160_REGA_USR_ACC_RANGE_ADDR, 0x5)
bus.write_byte_data(BMI160_DEVICE_ADDRESS, BMI160_REGA_USR_GYR_CONF_ADDR, 0x26)
bus.write_byte_data(BMI160_DEVICE_ADDRESS, BMI160_REGA_USR_GYR_RANGE_ADDR, 0x1)

#command register
bus.write_byte_data(BMI160_DEVICE_ADDRESS, BMI160_REGA_CMD_CMD_ADDR, CMD_SOFT_RESET_REG)

def enable_accel( ) :
  acc_value = [ 0, 0, 0, 0, 0, 0]
  #op_mode set to 0 and go to normal mode
  sleep(0.1)
  bus.write_byte_data(BMI160_DEVICE_ADDRESS, BMI160_REGA_CMD_CMD_ADDR, CMD_PMU_ACC_NORMAL)
  sleep(0.1)

  #read acc xyz
  acc_value = bus.read_i2c_block_data(BMI160_DEVICE_ADDRESS, BMI160_USER_DATA_14_ADDR, 6)

  #print "0x%X, 0x%X 0x%X" % ( acc_value[0], acc_value[1], acc_value[2])  
  #print "0x%X, 0x%X 0x%X" % ( acc_value[3], acc_value[4], acc_value[5])  
  acc_x =  (acc_value[1] << 8) | acc_value[0]
  acc_y =  (acc_value[3] << 8) | acc_value[2]
  acc_z =  (acc_value[5] << 8) | acc_value[4]

  #Need to be remap according to 1 pin postion
  print "accel x = %d, y = %d z = %d" % (acc_x, acc_y, acc_z)
  return;

def enable_gyro( ) :
  gyro_value = [ 0, 0, 0, 0, 0, 0]
  #op_mode set to 0 and go to normal mode
  sleep(0.1)
  bus.write_byte_data(BMI160_DEVICE_ADDRESS, BMI160_REGA_CMD_CMD_ADDR, CMD_PMU_GYRO_NORMAL)
  sleep(0.1)

  #read gyro xyz
  gyro_value = bus.read_i2c_block_data(BMI160_DEVICE_ADDRESS, BMI160_USER_DATA_8_ADDR, 6)

  gyro_x =  (gyro_value[1] << 8) | gyro_value[0]
  gyro_y =  (gyro_value[3] << 8) | gyro_value[2]
  gyro_z =  (gyro_value[5] << 8) | gyro_value[4]

  #Need to be remap according to 1 pin postion
  print "gyro x = %d, y = %d z = %d" % (gyro_x, gyro_y, gyro_z)

  return;

if sys.argv[1] == "A" :
  enable_accel( )
elif sys.argv[1] == "G" :
  enable_gyro( )

sys.exit()




