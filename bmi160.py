import smbus
import sys, getopt 

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
CMD_PMU_ACC_LP2               = 0x13


if len(sys.argv) == 1 :
  print "Usage : bmi160.py [ A | G ] "
  sys.exit()

chipid = bus.read_byte_data(BMI160_DEVICE_ADDRESS, BMI160_REGA_USR_CHIP_ID )

print "---------"
if chipid == 0xD1 :
 print "chip id is 0x%X, BMI160" % chipid
else :
 print "This is not a bmi160"
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

#op_mode set to 0 and go to normal mode


def enable_accel( ) :
  return;

def enable_gyro( ) :
  return;

if sys.argv[1] == "A" :
  enable_accel( )
elif sys.argv[1] == "G" :
  enable_gyro( )

sys.exit()




