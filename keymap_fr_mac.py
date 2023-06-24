
'''---------------------------------------------------------------------+
|                                                                       |
|   Set an alternate keymap for french (azerty) mac keyboard            |
|                                                                       |
|   This keymap was defined with a mac iso french layout on the system  |
|   side                                                                |
|                                                                       |
+---------------------------------------------------------------------'''

# usage :
'''

import kmk.extensions.keymap_extras.keymap_fr_mac
EURO = KC.LALT(KC.DLR)

'''
# then use KC.XXX as usual : KC.A, KC.B, KC.LALT(KC.XXX), ...
# N.B. : EURO is added as the current version (june 2023) of kmk doesn't handle ALT to make a new key





from kmk.keys import KeyAttrDict, KC, make_key, make_shifted_key

# To make the permutations, we make a duplicate of KC to get the US Qwerty codes
# This is done to avoid overwriting codes before copying them (like KC.A = KC.Q then KC.Q = KC.A would be incorrect)
KQ = KeyAttrDict()

KC.A = KQ.Q
KC.Z = KQ.W
KC.Q = KQ.A
KC.M = KQ.SCLN
KC.W = KQ.Z

KC.N1 = KQ.LSFT(KQ.N1)
KC.N2 = KQ.LSFT(KQ.N2)
KC.N3 = KQ.LSFT(KQ.N3)
KC.N4 = KQ.LSFT(KQ.N4)
KC.N5 = KQ.LSFT(KQ.N5)
KC.N6 = KQ.LSFT(KQ.N6)
KC.N7 = KQ.LSFT(KQ.N7)
KC.N8 = KQ.LSFT(KQ.N8)
KC.N9 = KQ.LSFT(KQ.N9)
KC.N0 = KQ.LSFT(KQ.N0)

KC.PERC = KQ.LSFT(KQ.QUOT)
KC.EQL = KQ.SLSH
KC.MINS = KQ.EQL
KC.COLN = KQ.DOT
KC.COMM = KQ.M
KC.DOT = KQ.LSFT(KQ.COMM)
KC.AMPR = KQ.N1
KC.DLR = KQ.RBRC
KC.QUOT = KQ.N4
KC.GRV = KQ.BSLS
KC.AT = KQ.LALT(KQ.BSLS)
KC.HASH = KQ.LALT(KQ.LSFT(KQ.BSLS))
KC.DQT = KQ.N3
KC.EXLM = KQ.N8
KC.SCLN = KQ.COMM      
KC.SLSH = KQ.LSFT(KQ.DOT)
KC.PIPE = KQ.LALT(KQ.LSFT(KQ.L))
KC.BSLS = KQ.LALT(KQ.LSFT(KQ.DOT))
KC.QUES = KQ.LSFT(KQ.M)
# ()  {}  []  <>
KC.LPRN = KQ.N5
KC.RPRN = KQ.MINS 
KC.LCBR = KQ.LALT(KQ.N5)
KC.RCBR = KQ.LALT(KQ.MINS)
KC.LBRC = KQ.LALT(KQ.LSFT(KQ.N5))
KC.RBRC = KQ.LALT(KQ.LSFT(KQ.MINS))
KC.LABK = KQ.GRV
KC.RABK = KQ.TILD

KC.CIRC = KQ.LBRC

# Create missing keys
make_shifted_key(KQ.LBRC.code, ("TREMA", "TREM",))	# ¨
make_shifted_key(KQ.MINS.code, ("DEGREE", "DEG",))	# °
make_key(KQ.N9.code, ("CCEDIL",))					# ç
make_key(KQ.N0.code, ("AGRAVE", "AGR"))				# à
make_key(KQ.N2.code, ("EACUTE", "EAC"))				# é
make_key(KQ.N7.code, ("EGRAVE", "EGR"))				# è
make_key(KQ.QUOT.code, ("UGRAVE", "UGR"))			# ù
make_shifted_key(KQ.BSLS.code, ("POUND", "£"))		# £


# we don't need KQ anymore
KQ.deinit()








































