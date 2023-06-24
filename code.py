'''---------------------------------------------------------------------+
|                                                                       |
|   Board : VColChoc44 designed by jpconstantineau                      |
|                                                                       |
|   https://github.com/jpconstantineau/VColChoc44                       |
|                                                                       |
+---------------------------------------------------------------------'''
import board
from digitalio import DigitalInOut, Direction
import pwmio
import time


'''---------------------------------------------------------------------+
|                                                                       |
|   Begin KmK configuration                                             |
|                                                                       |
+---------------------------------------------------------------------'''

from kb import KMKKeyboard
from kmk.keys import KC

keyboard = KMKKeyboard()

# Swap keys with iso azerty
# import kmk.extensions.keymap_extras.keymap_fr_mac
import keymap_fr_mac
EURO = KC.LALT(KC.DLR)



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


keyboard.modules.append(Layers())
keyboard.modules.append(holdtap)
keyboard.modules.append(combos)
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(tapdance)



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

# Print Screen & Area
PSCR  = KC.LGUI(KC.LSFT(KC.N3))
PAREA = KC.LGUI(KC.LSFT(KC.N4))



# LAYERS
UPPER = KC.TO(1)
LOWER = KC.TO(0)
CAPS_CMD = KC.HT(UPPER, KC.LCMD)
NUM = KC.HT(KC.TO(2), KC.MO(1))  # TO NUM - If hold - Caps (UPPER) layer
SYS_NAV = KC.HT(KC.TO(3), KC.MO(1))  # SYS - NAV - If hold - Caps (UPPER) layer

____ = KC.TRNS
XXXX = KC.NO

# COMBOS (touches simultanées)
combos.combos = [
    # Q - S for TAB
    Chord((KC.Z, KC.K), KC.TAB),
    Chord((KC.TAB, KC.BSLS), KC.TAB),     # To keep consistency with main layer : TAB on two left keys on NUM
    Chord((KC.K, KC.L, KC.M), SYS_NAV)
]


# ESC / Back to lower alphas 
ESCP = KC.TD(
        LOWER,          # Tap once => return to base
        KC.ESC,         # Tap twice send Esc - Hold for Function keys
        )



keyboard.keymap = [

 # Colemak - DBE (modified Colemak with a touch of french)
 [
 ESCP,   KC.AMPR,               KC.DLR,  KC.QUOT,                KC.CIRC,               KC.B,             KC.AGR,  KC.EACUTE,             KC.EGR,  KC.UGR,   KC.BSPC,
 KC.Z,   KC.K,                  KC.L,    KC.M,                   KC.N,                  NUM,              KC.P,    KC.U,                  KC.Y,    KC.G,     KC.J,
 Q_SFT,  KC.HT(KC.S, KC.MO(3)), KC.R,    KC.HT(KC.T, KC.MO(2)),  KC.D,                  KC.H,             KC.A,    KC.HT(KC.E, KC.MO(2)), KC.I,    KC.O,     KC.HT(KC.ENTER, KC.RSFT),
 W_CTR,  KC.X,                  KC.C,    KC.HT(KC.V, KC.LALT),   CAPS_CMD,              SYS_NAV,          CMDSP,   F_ALT,                 KC.DOT,  KC.COMM,  KC.HT(KC.COLN, KC.RCTL)
 ], 

 # UPPER (Faux Caps) (1)
 [
 ESCP,           KC.AT,                          KC.HASH,        KC.DQT,                          KC.TREMA,                  KC.LSFT(KC.B),           UPAGRV,         UPEACT,                          UPEGRV,         UPUGRV,         KC.DEL,
 KC.LSFT(KC.Z),  KC.LSFT(KC.K),                  KC.LSFT(KC.L),  KC.LSFT(KC.M),                   KC.LSFT(KC.N),             NUM,                     KC.LSFT(KC.P),  KC.LSFT(KC.U),                   KC.LSFT(KC.Y),  KC.LSFT(KC.G),  KC.LSFT(KC.J),
 KC.LSFT(KC.Q),  KC.HT(KC.LSFT(KC.S), KC.MO(3)), KC.LSFT(KC.R),  KC.HT(KC.LSFT(KC.T), KC.MO(2)),  KC.LSFT(KC.D),             KC.LSFT(KC.H),           KC.LSFT(KC.A),  KC.HT(KC.LSFT(KC.E), KC.MO(2)),  KC.LSFT(KC.I),  KC.LSFT(KC.O),  KC.ENTER,
 KC.LSFT(KC.W),  KC.LSFT(KC.X),                  KC.LSFT(KC.C),  KC.LSFT(KC.V),                   LOWER,                     SYS_NAV,                 CMDSP,          KC.LSFT(KC.F),                   KC.EXLM,        KC.SCLN,        KC.SLSH,
 ], 

 # NUM  (2)
 [
 ESCP,     KC.PIPE,   KC.LBRC,  KC.RBRC,                  KC.BSPC,            KC.PERC,          KC.PPLS,  KC.N7,  KC.N8,   KC.N9,    KC.PSLS,  
 KC.TAB,   KC.BSLS,   KC.LCBR,  KC.RCBR,                  KC.DEL,             XXXX,             KC.MINS,  KC.N4,  KC.N5,   KC.N6,    KC.PAST,
 KC.LSFT,  EURO,      KC.LPRN,  KC.RPRN,                  KC.QUES,            KC.EQL,           KC.DEG,   KC.N1,  KC.N2,   KC.N3,    KC.HT(KC.ENTER, KC.RSFT), 
 C_CTRL,   KC.POUND,  KC.LABK,  KC.HT(KC.RABK, KC.LALT),  CMDSP,              SYS_NAV,          CMDSP,    KC.N0,  KC.DOT,  KC.LEFT,  KC.HT(KC.RGHT, KC.RCTL), 
 ],


 # SYS-NAV - (3)
 [
 ESCP,     KC.VOLD,  KC.MUTE,        KC.VOLU,               XXXX,               XXXX,               XXXX,   PSCR,                    PAREA,          XXXX,     KC.BSPC,
 KC.TAB,   PTAB,     KC.LGUI(KC.W),  NTAB,                  KC.N,               NUM,                XXXX,   PTAB,                    KC.LGUI(KC.W),  NTAB,     KC.DEL,
 KC.LSFT,  KC.S,     KC.R,           KC.T,                  KC.D,               XXXX,               XXXX,   XXXX,                    KC.UP,          KC.O,     KC.HT(KC.ENTER, KC.RSFT),
 W_CTR,    KC.X,     KC.C,           KC.HT(KC.V, KC.LALT),  CAPS_CMD,           XXXX,               CMDSP,  KC.HT(KC.LEFT, KC.ALT),  KC.DOWN,        KC.RGHT,  KC.RCTL,
 ],
]



if __name__ == '__main__':
 keyboard.go()



































