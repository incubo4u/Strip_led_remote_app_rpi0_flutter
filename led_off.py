from rpi_ws281x import *
import time, os

LED_COUNT = 13     #number of LEDs
LED_PIN = 18       #Led strip din pin
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 0
LED_INVERT = False
LED_CHANNEL = 0

print(os.getpid())
strip = Adafruit_NeoPixel(LED_COUNT,LED_PIN,LED_FREQ_HZ,LED_DMA,LED_INVERT,LED_BRIGHTNESS,LED_CHANNEL)
strip.begin()

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)
while True:

    rainbow(strip)
