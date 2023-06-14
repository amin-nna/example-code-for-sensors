"""Simple test script for 2.9" 296x128 grayscale display.

Supported products:
  * Adafruit 2.9" Grayscale
    * https://www.adafruit.com/product/4777
  """

import time
import busio
import board
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_uc8151d

displayio.release_displays()

# This pinout works on the Raspberry Pi Pico and Pico W and may need to be altered if these pins are being used by other packs or bases.
spi = busio.SPI(board.GP18, MOSI=board.GP19, MISO=board.GP16)  # Uses SCK and MOSI
epd_cs = board.GP17
epd_dc = board.GP20
epd_reset = board.GP21
epd_busy = None

# Make a bus to communicate with the screen.
display_bus = displayio.FourWire(
    spi, command=epd_dc, chip_select=epd_cs, reset=epd_reset, baudrate=400000
)
time.sleep(1)

# Setting parameters for the display.
display = adafruit_uc8151d.UC8151D(
    display_bus,
    width=128,
    height=296,
    rotation=180,
    black_bits_inverted=False,
    color_bits_inverted=False,
    grayscale=True,
    refresh_time=1,
)

# Make a group to write to.
g = displayio.Group()

text = "Hello World"
text_area = label.Label(terminalio.FONT,text=text)
text_area.x = 10
text_area.y = 10
display.show(text_area)
 
display.refresh()
while True:
    pass