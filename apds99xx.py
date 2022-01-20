###



import smbus
import sys, getopt 

bus=smbus.SMBus(1)

DEVICE_ADDRESS = 0x39

APDS99XX_CMD_BYTE = 0x80
APDS99XX_CMD_WORD = 0xA0

APDS9930_CHIP_ID = 0x12 

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

if len(sys.argv) == 1 :
  print "Usage : apds99xx.py [ L | P ] "
  sys.exit()

chipid = bus.read_byte_data(DEVICE_ADDRESS, APDS99XX_CMD_BYTE | APDS9930_CHIP_ID)

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

def enable_proximity( ) :
  bus.write_byte_data(DEVICE_ADDRESS, APDS99XX_CMD_BYTE | APDS99XX_ENABLE_ADDR, 0x25 )

  while 1 :
    pdata = bus.read_word_data(DEVICE_ADDRESS, APDS99XX_CMD_WORD | APDS99XX_PDATAL_ADDR)
    pdata |= bus.read_word_data(DEVICE_ADDRESS, APDS99XX_CMD_WORD | APDS99XX_PDATAH_ADDR) << 8
    print "pdata is %d" % pdata
  return;

# lux value be more calibrated
def lux_calculation( ch0, ch1 ) :
  v_lux = 0
  als_B = 186 #223 
  als_C = 75 #70
  als_D = 129 #142
  als_GA = 256
  als_DF = 52

  IAC1 = ( ch0 - ( als_B * ch1) / 100)
  IAC2 = ( ( als_C * ch0 ) / 100  - ( als_D * ch1 ) / 100 )

  if IAC1 > IAC2 :
    IAC = IAC1
  elif IAC1 <= IAC2 :
    IAC = IAC2
  else :
    IAC = 0

  #v_lux = ((IAC * als_GA * als_DF ) / 100) * 65 / 10 / ((2720 / 100) * 1)
  v_lux = ((IAC * als_GA * als_DF ) / 100) / ((2720 / 100) * 1)

  return v_lux

def enable_light( ) :
  bus.write_byte_data(DEVICE_ADDRESS, APDS99XX_CMD_BYTE | APDS99XX_ENABLE_ADDR, 0x23 )

  while 1 :
    ch0data = bus.read_word_data(DEVICE_ADDRESS, APDS99XX_CMD_WORD | APDS99XX_CDATAL_ADDR)
    ch1data = bus.read_word_data(DEVICE_ADDRESS, APDS99XX_CMD_WORD | APDS99XX_CDATAH_ADDR)
    #print "0x%X, 0x%X" % ( ch0data, ch1data )
    print "lux is %d" % lux_calculation( ch0data, ch1data )
  return;

if sys.argv[1] == "P" :
  enable_proximity( )
elif sys.argv[1] == "L" :
  enable_light( )

sys.exit()




