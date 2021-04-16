import time
import keyboard
import pynput
import ctypes

'Please enter your screen resolution below (only 16:9 screens work)'
resolution = [2560, 1440]

LICENSE = """
    F clicker
    Copyright (C) 2021

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, see <http://www.gnu.org/licenses/>.
"""

print(LICENSE)
if not ctypes.windll.shell32.IsUserAnAdmin():
    print("\n\nPlease run as admin.")
    exit()

print("\n\nThe program has started. Press backspace to begin, long press 1 to stop. Be sure to hover your mouse over "
      "the thing you want to click.\n")


def end():
    print("1 pressed. Program ended.")
    exit()


def on_press(key):
    kb = pynput.keyboard.Controller()
    mouse = pynput.mouse.Controller()
    stop = False
    if key == pynput.keyboard.Key.backspace:
        print("Backspace pressed. Begin loop")
        while not stop:
            if keyboard.is_pressed('1'):
                end()

            kb.press('f')
            kb.release('f')
            print("Pressed F")
            time.sleep(1)
            if keyboard.is_pressed('1'):
                end()

            kb.press(' ')
            kb.release(' ')
            print("Pressed Space")
            mouse.move(resolution[0]*0.1953, resolution[1]*0.26)
            time.sleep(1)
            if keyboard.is_pressed('1'):
                end()

            mouse.press(pynput.mouse.Button.left)
            mouse.release(pynput.mouse.Button.left)
            print("Left clicked")
            time.sleep(1)
            if keyboard.is_pressed('1'):
                end()

            kb.press(' ')
            kb.release(' ')
            print("Pressed Space")
            time.sleep(2)
            if keyboard.is_pressed('1'):
                end()

            print("One cycle ended.")


def on_release(key):
    pass


# Collect events until released
with pynput.keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
