import signal
import time
import Adafruit_Trellis
from raveloxmidi import *
from config import *

c = config("config.json")
cb = c['buttons']
r = raveloxmidi( c['remote_host'], c['remote_port'])
r.connect()

controller = Adafruit_Trellis.Adafruit_TrellisSet( Adafruit_Trellis.Adafruit_Trellis() )
controller_address = 0x70
numKeys = 16
I2C_BUS = 1
global shutdown
shutdown = False

controller.begin((controller_address, I2C_BUS))

class App:

    def sigint_handler( self ):
        self.shutdown = True

    def __init__(self, controller, rmidi):
        signal.signal( signal.SIGINT, lambda signal, frame : self.sigint_handler() )
        self.shutdown = False
        self.controller = controller
        self.rmidi = rmidi
        
    def loop( self ):
        while not self.shutdown:
            time.sleep(0.02)
            if self.controller.readSwitches():
                for button in cb:
                    i = button['button_id']
                    if self.controller.justPressed(i):
                        self.controller.setLED(i)
                        self.rmidi.note_on( button['midi_channel'], button['midi_id'], button['midi_value'] );
                    if self.controller.justReleased(i):
                        self.controller.clrLED(i)
                        self.rmidi.note_off( button['midi_channel'], button['midi_id'] , button['midi_value']);
                self.controller.writeDisplay()

def init_demo(ctlr):
    for i in range(numKeys):
        ctlr.setLED(i)
        ctlr.writeDisplay()
        time.sleep(0.05)
    for i in range(numKeys):
        ctlr.clrLED(i)
        ctlr.writeDisplay()
        time.sleep(0.05)

init_demo( controller )
app = App( controller, r )
app.loop()
print 'Shutting down'
init_demo( controller )
r.close()
