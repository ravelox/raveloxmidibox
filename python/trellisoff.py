import signal
import time
import Adafruit_Trellis

controller = Adafruit_Trellis.Adafruit_TrellisSet( Adafruit_Trellis.Adafruit_Trellis() )

controller_address = 0x70
numKeys = 16
I2C_BUS = 1

controller.begin((controller_address, I2C_BUS))

for i in range(numKeys):
    controller.clrLED(i)
    controller.writeDisplay()
    time.sleep(0.05)
