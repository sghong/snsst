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

BMM050_POWER_CNTL             =     0x4B 

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

sys.exit()




