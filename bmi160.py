import smbus
import sys, getopt 

bus=smbus.SMBus(1)

BMI160_DEVICE_ADDRESS = 0x69

BMI160_REGA_USR_CHIP_ID      = 0x00
BMI160_REGA_USR_ERR_REG      = 0x02
BMI160_REGA_USR_PMU_STATUS   = 0x03
BMI160_REGA_USR_DATA_0       = 0x04
BMI160_REGA_USR_DATA_7       = 0x0b
BMI160_REGA_USR_DATA_8       = 0x0c
BMI160_REGA_USR_DATA_13      = 0x11
BMI160_REGA_USR_DATA_14      = 0x12
BMI160_REGA_USR_DATA_19      = 0x17
BMI160_REGA_USR_SENSORTIME_0 = 0x18
BMI160_REGA_USR_SENSORTIME_2 = 0x1a


if len(sys.argv) == 1 :
  print "Usage : bmi160.py [ A | G ] "
  sys.exit()

chipid = bus.read_byte_data(BMI160_DEVICE_ADDRESS, BMI160_REGA_USR_CHIP_ID )

print "---------"
if chipid == 0xD1 :
 print "chip id is 0x%X, BMI160" % chipid
print "---------" 

#bus.write_byte_data(BMI160_DEVICE_ADDRESS, 0x03, 0x19 )
#tmp = bus.read_byte_data(BMI160_DEVICE_ADDRESS, 0x03)
#print "tmp 0x%X, BMI160" % tmp 

#chip init

def enable_accel( ) :
  return;

def enable_gyro( ) :
  return;

if sys.argv[1] == "A" :
  enable_accel( )
elif sys.argv[1] == "G" :
  enable_gyro( )

sys.exit()




