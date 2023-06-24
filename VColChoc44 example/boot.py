# VColMX44 designed by jpconstantineau
# https://github.com/jpconstantineau/VColChoc44


import board
import digitalio


'''---------------------------------------------------------------------+
|                                                                       |
|   Check if Key Esc pressed, then show USB. If not, hide USB           |
|                                                                       |
+---------------------------------------------------------------------'''

row = digitalio.DigitalInOut(board.ROW1)
col = digitalio.DigitalInOut(board.COL1)
col.switch_to_output(value=1)
row.switch_to_input(pull=digitalio.Pull.DOWN)


if not row.value:
    
    import storage
    import usb_cdc
    import usb_midi
    storage.disable_usb_drive()  # disable CIRCUITPY
    usb_cdc.disable()            # disable REPL
    usb_midi.disable()           # disable MIDI


row.deinit()
col.deinit()# Write your code here :-)

