# VColMX44 designed by jpconstantineau
# https://github.com/jpconstantineau/VColChoc44


'''---------------------------------------------------------------------+
|                                                                       |
|   Blink to show it's alive                                            |
|                                                                       |
+---------------------------------------------------------------------'''
import board
from digitalio import DigitalInOut, Direction
import pwmio
import time

red_led = DigitalInOut(board.LED)
red_led.direction = Direction.OUTPUT

for i in range(3):
        red_led.value = True
        time.sleep(0.3)
        red_led.value = False
        time.sleep(0.2)

red_led.deinit()


'''---------------------------------------------------------------------+
|                                                                       |
|   Begin KmK configuration                                             |
|                                                                       |
+---------------------------------------------------------------------'''



from kb import KMKKeyboard
from kmk.keys import KC

keyboard = KMKKeyboard()

from kmk.modules.layers import Layers
from kmk.handlers.sequences import simple_key_sequence
from kmk.extensions.media_keys import MediaKeys
from kmk.handlers.sequences import send_string

from kmk.modules.tapdance import TapDance
tapdance = TapDance()

from kmk.modules.holdtap import HoldTap
holdtap = HoldTap()
# optional: set a custom tap timeout in ms
# holdtap.tap_time = 300

from kmk.modules.combos import Combos, Chord
combos = Combos()

# Put a LED on Caps Lock (not really, but on the upper layer that simulates CapsLock)
from kmk.extensions.LED import LED
from kb import betterLED
caps_led = betterLED(led_pin=board.LED)
caps_led._enabled = False  # LED is on by default on import, make it off
keyboard.extensions.append(caps_led)


keyboard.modules.append(Layers())
keyboard.modules.append(holdtap)
keyboard.modules.append(combos)
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(tapdance)

# Swap keys with iso azerty
# import kmk.extensions.keymap_extras.keymap_fr_mac
import keymap_fr_mac

EURO = KC.LALT(KC.DLR)



# Accuentuated caps
UPAGRV = simple_key_sequence((KC.GRV, KC.LSFT(KC.A), ))
UPEACT = simple_key_sequence((KC.LALT(KC.LSFT(KC.N1)), KC.LSFT(KC.E), ))
UPEGRV = simple_key_sequence((KC.GRV, KC.LSFT(KC.E), ))
UPUGRV = simple_key_sequence((KC.GRV, KC.LSFT(KC.U), )) 


# White space if tapped, GUI if hold
CMDSP = KC.HT(KC.SPC, KC.LCMD)

# SHIFT on Q
Q_SFT = KC.HT(KC.Q, KC.LSFT) 
# put CTRL on W
W_CTR = KC.HT(KC.W, KC.LCTL) 
# Place ç on the NUM / Symbols layer
C_CTRL = KC.HT(KC.CCEDIL, KC.LCTL)

F_ALT = KC.HT(KC.F, KC.LALT)


# NEXT & PREVIOUS TAB
NTAB = KC.LCTL(KC.TAB)
PTAB = KC.LSFT(KC.LCTL(KC.TAB))

 
# Browser Fav
FAVS = KC.LGUI(KC.LALT(KC.B))


# Print Screen & Area
PSCR  = KC.LGUI(KC.LSFT(KC.N3))
PAREA = KC.LGUI(KC.LSFT(KC.N4))


# Rectangle Shortcuts (Windows Mgt)
W_UP = KC.LCTL(KC.LGUI(KC.UP))
W_DWN = KC.LCTL(KC.LGUI(KC.DOWN))
W_RGHT = KC.LCTL(KC.LGUI(KC.RGHT))
W_LEFT = KC.LCTL(KC.LGUI(KC.LEFT))
W_FULL = KC.LCTL(KC.LGUI(KC.ENTER))




# LAYERS
UPPER = simple_key_sequence((KC.LED_TOG(), KC.TO(0), KC.TO(1)))
LOWER = simple_key_sequence((KC.LED_OFF(), KC.TO(0)))
CAPS_CMD = KC.HT(UPPER, KC.LCMD)
#CAPS_CMD = KC.HT(KC.TO(1), KC.LCMD)
#NUM = KC.HT(KC.TO(2), KC.MO(2))
NUM_TOG = simple_key_sequence((KC.LED_OFF(), KC.TO(2)))  # TO SWITCH OFF CAPS LED
NUM = KC.HT(NUM_TOG, KC.MO(1))  # TO NUM - If hold - Caps (UPPER) layer

#SYS_NAV = KC.HT(KC.TO(3), KC.MO(3)) # SYS - NAV 
SYS_TOG = simple_key_sequence((KC.LED_OFF(), KC.TO(3))) 
SYS_NAV = KC.HT(SYS_TOG, KC.MO(1))  # SYS - NAV - If hold - Caps (UPPER) layer

____ = KC.TRNS
XXXX = KC.NO

# COMBOS (touches simultanées)
combos.combos = [
    # Q - S for TAB
    Chord((KC.Z, KC.K), KC.TAB),
    Chord((KC.TAB, KC.BSLS), KC.TAB),     # To keep consistency with main layer : TAB on two left keys on NUM
    Chord((KC.K, KC.L, KC.M), SYS_NAV)
]



# ESC as Function keys layer on Hold 
#ESC_Fn = KC.HT(KC.ESC, KC.MO(4))
ESC_Fn = KC.TD(
        LOWER,                    # Tap once => return to base
        KC.HT(KC.ESC, KC.MO(4)),  # Tap twice send Esc - Hold for Function keys
        )



keyboard.keymap = [

 # Colemak - DBE
 [
 ESC_Fn,  KC.AMPR,               KC.DLR,  KC.QUOT,                KC.CIRC,               KC.B,             KC.AGR,  KC.EACUTE,             KC.EGR,  KC.UGR,   KC.BSPC,
 KC.Z,    KC.K,                  KC.L,    KC.M,                   KC.N,                  NUM,              KC.P,    KC.U,                  KC.Y,    KC.G,     KC.J,
 Q_SFT,   KC.HT(KC.S, KC.MO(3)), KC.R,    KC.HT(KC.T, KC.MO(2)),  KC.D,                  KC.H,             KC.A,    KC.HT(KC.E, KC.MO(2)), KC.I,    KC.O,     KC.HT(KC.ENTER, KC.RSFT),
 W_CTR,   KC.X,                  KC.C,    KC.HT(KC.V, KC.LALT),   CAPS_CMD,              SYS_NAV,          CMDSP,   F_ALT,                 KC.DOT,  KC.COMM,  KC.HT(KC.COLN, KC.RCTL)
 ], 

 # UPPER (Faux Caps) (1)
 [
 ESC_Fn,         KC.AT,                          KC.HASH,        KC.DQT,                          KC.TREMA,                  KC.LSFT(KC.B),           UPAGRV,         UPEACT,                          UPEGRV,         UPUGRV,         KC.DEL,
 KC.LSFT(KC.Z),  KC.LSFT(KC.K),                  KC.LSFT(KC.L),  KC.LSFT(KC.M),                   KC.LSFT(KC.N),             NUM,                     KC.LSFT(KC.P),  KC.LSFT(KC.U),                   KC.LSFT(KC.Y),  KC.LSFT(KC.G),  KC.LSFT(KC.J),
 KC.LSFT(KC.Q),  KC.HT(KC.LSFT(KC.S), KC.MO(3)), KC.LSFT(KC.R),  KC.HT(KC.LSFT(KC.T), KC.MO(2)),  KC.LSFT(KC.D),             KC.LSFT(KC.H),           KC.LSFT(KC.A),  KC.HT(KC.LSFT(KC.E), KC.MO(2)),  KC.LSFT(KC.I),  KC.LSFT(KC.O),  KC.ENTER,
 KC.LSFT(KC.W),  KC.LSFT(KC.X),                  KC.LSFT(KC.C),  KC.LSFT(KC.V),                   LOWER,                     SYS_NAV,                 CMDSP,          KC.LSFT(KC.F),                   KC.EXLM,        KC.SCLN,        KC.SLSH,
 ], 

 # NUM  (2)
 [
 ESC_Fn,   KC.PIPE,   KC.LBRC,  KC.RBRC,                  KC.BSPC,            KC.PERC,          KC.PPLS,  KC.N7,  KC.N8,   KC.N9,    KC.PSLS,  
 KC.TAB,   KC.BSLS,   KC.LCBR,  KC.RCBR,                  KC.DEL,             XXXX,             KC.MINS,  KC.N4,  KC.N5,   KC.N6,    KC.PAST,
 KC.LSFT,  EURO,      KC.LPRN,  KC.RPRN,                  KC.QUES,            KC.EQL,           KC.DEG,   KC.N1,  KC.N2,   KC.N3,    KC.HT(KC.ENTER, KC.RSFT), 
 C_CTRL,   KC.POUND,  KC.LABK,  KC.HT(KC.RABK, KC.LALT),  CMDSP,              SYS_NAV,          CMDSP,    KC.N0,  KC.DOT,  KC.LEFT,  KC.HT(KC.RGHT, KC.RCTL), 
 ],


 # SYS - NAV  (FUL KBD) - (3)
 [
 ESC_Fn,   KC.VOLD,  KC.MUTE,        KC.VOLU,               FAVS,               W_FULL,             W_UP,    PSCR,                    PAREA,          XXXX,     KC.BSPC,
 KC.TAB,   PTAB,     KC.LGUI(KC.W),  NTAB,                  KC.N,               NUM,                W_DWN,   PTAB,                    KC.LGUI(KC.W),  NTAB,     KC.DEL,
 KC.LSFT,  KC.S,     KC.R,           KC.T,                  KC.D,               W_LEFT,             W_RGHT,  XXXX,                    KC.UP,          KC.O,     KC.HT(KC.ENTER, KC.RSFT),
 W_CTR,    KC.X,     KC.C,           KC.HT(KC.V, KC.LALT),  CAPS_CMD,           XXXX,               CMDSP,   KC.HT(KC.LEFT, KC.ALT),  KC.DOWN,        KC.RGHT,  KC.RCTL,
 ],

 # FN KEYS  (4)
 [
 ____,  XXXX,  XXXX,  KC.LSFT,   KC.LALT,        XXXX,           KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   
 XXXX,  XXXX,  XXXX,  XXXX,      XXXX,           XXXX,           KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,   
 XXXX,  XXXX,  XXXX,  XXXX,      XXXX,           XXXX,           KC.F11,  KC.F12,  KC.F13,  KC.F14,  KC.F15,   
 XXXX,  XXXX,  XXXX,  XXXX,      KC.CMD,         KC.LCTL,        XXXX,    XXXX,    XXXX,    XXXX,    XXXX,  
 ]
]



buzzer = pwmio.PWMOut(board.SPEAKER, variable_frequency=True)
OFF = 0
ON = 2**15
buzzer.frequency = 1660 #
buzzer.duty_cycle = ON
time.sleep(0.2)
buzzer.duty_cycle = OFF




if __name__ == '__main__':
 keyboard.go()



































