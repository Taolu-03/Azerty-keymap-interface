# What for ?

The purpose of this library is to provide a standard **KC** object to configure an **AZERTY keymap for your keyboard**, mapping the AZERTY keys to the standard Ansii / Qwerty keys that KMK will communicate to the computer.

# Preamble

For history reasons and now defacto standard, every existing keyboard sends key codes to the computer, based on the qwerty layout.

When you press a key (let's say the letter A), the keyboard sends a code corresponding to the physical position of the key pressed on a qwerty keyboard.
When the computer receives this code, it translates it to the chosen character based on its keyboard layout configuration.
Alongside the key code, the keyboard also sends informations about any modifier (like Shift, Alt,...)

So when you type SHFT + A to get a capital 'a', the computer displays an 'A'

## How does it translate to KMK (and Azerty) ?

When you define your keymap (in code.py or main.py), you will use KC.A for an 'a'. KMK then sends the code of the A position on a Qwerty keyboard. If your computer (or tablet, phone,...) is configured to listen to a qwerty keyboard (qwerty keyboard layout selected in your computer system configuration), you're done, it will display an 'a'

If your computer thinks that your keyboard is Azerty, then it will translate the received key code to the character at the same physical position on an Azerty keyboard, which is a 'q'.

You now have three options to get the correct character :

- [ ] Configure your computer to a qwerty keyboard layout (not always desired nor possible)
- [ ] place KC.Q in your keymap where you want an 'A'
- [ ] write an intermediate translation layer to do the permutations (KC.A becomes KC.Q and vice-versa for example) - this is the purpose of this library.

# Usage

- [ ] Leave your computer configured to the Azerty keyboard layout
- [ ] Add keymap\_fr\_mac.py at the root of your keyboard
- [ ] In your code.py import keymap\_fr\_mac
- [ ] Use KC as you would do for a qwerty keyboard : use KC.A for an A, etc...

For the time being (as of june 2023), you need to add the definition for EURO (can't define KC.EURO as it is)

`import keymap_fr_mac`

`EURO = KC.LALT(KC.DLR)`

## MAC, Windows, Unix,...

If most of the Azerty layout is identical, there might be small differences for different operating systems.
This library has been written for a french azerty mac but can easily be adapted. Just copy keymap\_fr\_mac.py to keymap\_fr\_yoursytem.py and make the appropriate modifications.

The same principle applies for **other languages.**

*If you write a new version for your language, please consider submitting it to the KMK community.*

## Example

A kb.py and code.py are provided as an example. They have been defined for a 44 keys keyboard (VColChoc44 from JP Constantineau) and the layout is a modified version of Colemak, with a touch of french (accentuated character : éèàù, ç, ...)
As such, it is a good example to configure your french layout, be it a pure standard Azerty layout.

Note : the shifted version of the alphas will work (SHFT + 'a' will give a capital 'A') but not for the other keys. So an UPPER layer has been defined which acts as a "faux" shift
