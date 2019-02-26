import signal
import time
import Adafruit_Trellis

controller = Adafruit_Trellis.Adafruit_TrellisSet( Adafruit_Trellis.Adafruit_Trellis() )
controller_address = 0x70
numKeys = 16
I2C_BUS = 1

def init_demo(ctlr):
    for i in range(numKeys):
        ctlr.setLED(i)
        ctlr.writeDisplay()
        time.sleep(0.05)
    for i in range(numKeys):
        ctlr.clrLED(i)
        ctlr.writeDisplay()
    time.sleep(0.05)

controller.begin((controller_address, I2C_BUS))

while True:
    init_demo( controller )
