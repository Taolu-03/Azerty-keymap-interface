import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.extensions.led import LED
from kmk.keys import make_argumented_key, make_key

class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.COL1,
        board.COL2,
        board.COL3,
        board.COL4,
        board.COL5,
        board.COL6,
        board.COL7,
        board.COL8,
        board.COL9,
        board.COL10,
        board.COL11,
    )
    row_pins = (board.ROW1, board.ROW2, board.ROW3, board.ROW4)
    diode_orientation = DiodeOrientation.COL2ROW
    pixel_pin = board.NEOPIXEL
    num_pixels = 44



# Extend LED functions to switch the LED Off
class betterLED(LED):
    def __init__(self, led_pin):
        self.redled = led_pin
        LED.__init__(self, led_pin = self.redled)

        make_argumented_key(
            names=('LED_OFF',),
            validator=self._led_key_validator,
            on_press=self._key_led_off,
        )


    def _key_led_off(self, *args, **kwargs):
        self.off()
        self._enabled = False

