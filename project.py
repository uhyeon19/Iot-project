import RPi.GPIO as GPIO
import time
import I2C_LCD_driver

class gpioset:
    def __init__(self):
        self.led = 4
        self.button = 15
        self.mylcd = I2C_LCD_driver.lcd()        
    
    def gpioinit(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.led, GPIO.OUT)

    def lcdplay(self, first, second):
        self.mylcd.lcd_display_string(first, 1)
        self.mylcd.lcd_display_string(second, 2)
    
    def lcd_clear(self):
        self.mylcd.lcd_clear()
    
    def lcd_off(self):
        self.mylcd.backlight(0)

    def run(self):
        self.gpioinit()
        def button_callback(channel):
            GPIO.output(self.led, 0)
        while 1:
            GPIO.output(self.led, 1)
            time.sleep(0.5)
            GPIO.output(self.led, 0)
            time.sleep(0.5)
            if GPIO.input(self.button) == 1:
                GPIO.output(self.led, 0)
                break

if __name__ == "__main__":
    gpio = gpioset()
    gpio.lcdplay("hello", "world")
    time.sleep(1.0)
    gpio.lcd_clear()
    time.sleep(1.0)
    gpio.lcd_off()
    gpio.run()

