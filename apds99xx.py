import smbus
import sys 

bus=smbus.SMBus(1)

DEVICE_ADDRESS = 0x39

APDS99XX_CMD_BYTE = 0x80
APDS99XX_CMD_WORD = 0xA0

v_CHIP_ID = 0x12 
v_ATIME = 0xff # 2.7ms minimum ALS integration time
v_PTIME = 0xff # 2.7ms minimum Wait time 
v_WTIME = 0xff # 2.7 ms minimum Prox integration time 
#v_PPCOUNT = 1 # Minimum prox pulse count
v_PPCOUNT = 8 # Minimum prox pulse count

v_APDS993X_PDRVIE_100MA = 0x00 # PS 100mA LED driver
v_APDS993X_PRX_IR_DIOD = 0x20 # Proximity uses CH1 diode
#v_APDS993X_PGAIN = 0x0C # PS GAIN 8X
v_APDS993X_PGAIN = 0x08 # PS GAIN 4X
#v_APDS993X_AGAIN = 0x00 # ALS GAIN 1X
v_APDS993X_AGAIN = 0x01 # ALS GAIN 8X

#Register Addresses define
APDS99XX_ENABLE_ADDR = 0x00
APDS99XX_ATIME_ADDR = 0x01
APDS99XX_PTIME_ADDR = 0x02
APDS99XX_WTIME_ADDR = 0x03
APDS99XX_AILTL_ADDR = 0x04
APDS99XX_AILTH_ADDR = 0x05
APDS99XX_AIHTL_ADDR = 0x06
APDS99XX_AIHTH_ADDR = 0x07
APDS99XX_PILTL_ADDR = 0x08
APDS99XX_PILTH_ADDR = 0x09
APDS99XX_PIHTL_ADDR = 0x0A
APDS99XX_PIHTH_ADDR = 0x0B
APDS99XX_PERS_ADDR = 0x0C
APDS99XX_CONFIG_ADDR = 0x0D
APDS99XX_PPCOUNT_ADDR = 0x0E
APDS99XX_CONTROL_ADDR = 0x0F
APDS99XX_REV_ADDR = 0x11
APDS99XX_ID_ADDR = 0x12
APDS99XX_STATUS_ADDR = 0x13
APDS99XX_CDATAL_ADDR = 0x14
APDS99XX_CDATAH_ADDR = 0x15
APDS99XX_IRDATAL_ADDR = 0x16
APDS99XX_IRDATAH_ADDR = 0x17
APDS99XX_PDATAL_ADDR = 0x18
APDS99XX_PDATAH_ADDR = 0x19

chipid = bus.read_byte_data(DEVICE_ADDRESS, APDS99XX_CMD_BYTE | v_CHIP_ID)

print "---------"
if chipid == 0x39 :
  print "chip id is 0x%X, apds9930" % chipid
print "---------" 

bus.write_byte_data(DEVICE_ADDRESS, APDS99XX_CMD_BYTE | APDS99XX_ATIME_ADDR, v_ATIME )
bus.write_byte_data(DEVICE_ADDRESS, APDS99XX_CMD_BYTE | APDS99XX_PTIME_ADDR, v_PTIME )
bus.write_byte_data(DEVICE_ADDRESS, APDS99XX_CMD_BYTE | APDS99XX_WTIME_ADDR, v_WTIME )
bus.write_byte_data(DEVICE_ADDRESS, APDS99XX_CMD_BYTE | APDS99XX_PPCOUNT_ADDR, v_PPCOUNT )

bus.write_byte_data(DEVICE_ADDRESS, APDS99XX_CMD_BYTE | APDS99XX_CONFIG_ADDR, 0 )
bus.write_byte_data(DEVICE_ADDRESS, APDS99XX_CMD_BYTE | APDS99XX_CONTROL_ADDR, v_APDS993X_PDRVIE_100MA | v_APDS993X_PRX_IR_DIOD | v_APDS993X_PGAIN | v_APDS993X_AGAIN )

#print "=%x=" % (v_APDS993X_PDRVIE_100MA | v_APDS993X_PRX_IR_DIOD | v_APDS993X_PGAIN | v_APDS993X_AGAIN)

bus.write_byte_data(DEVICE_ADDRESS, APDS99XX_CMD_BYTE | APDS99XX_ENABLE_ADDR, 0x27 )

#sys.exit()

while 1 :
  pdata = bus.read_word_data(DEVICE_ADDRESS, APDS99XX_CMD_WORD | APDS99XX_PDATAL_ADDR)
  pdata |= bus.read_word_data(DEVICE_ADDRESS, APDS99XX_CMD_WORD | APDS99XX_PDATAH_ADDR) << 8
  print "pdata is %d" % pdata




