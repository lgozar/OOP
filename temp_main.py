from board import Board
from time import sleep
from lcd_class import LCD
from temp_class import Temperature
from button_class import Button
from rgb_class import RGB

'''main code'''

board = Board()
lcd = LCD(board)
temp = Temperature()
rgb = RGB(board, 16, 20, 21)
button1 = Button(board, 24)
button2 = Button(board, 12)
set_temp = 22

def up():
    global set_temp
    set_temp += 1
    lcd.lcd_string("Set temperature", lcd.LCD_LINE_1)
    lcd.lcd_string("to " + str(set_temp) + ' C', lcd.LCD_LINE_2)
    sleep(1)
    
def down():
    global set_temp
    set_temp -= 1
    lcd.lcd_string("Set temperature", lcd.LCD_LINE_1)
    lcd.lcd_string("to " + str(set_temp) + ' C', lcd.LCD_LINE_2)
    sleep(1)

try:
    while True:
        
        lcd.lcd_string("Temperature is",lcd.LCD_LINE_1)
        lcd.lcd_string(str(int(temp.c)) + ' degrees C',lcd.LCD_LINE_2)
            
        if temp.c < set_temp:
            rgb.turnRGB_off()
            rgb.turnRed_on()
        elif temp.c >= set_temp:
            rgb.turnRGB_off()
            rgb.turnGreen_on()
        else:
            print('Error')
        sleep(1)
        
        if button1.pressed:
            up()
            button1.pressed = False
        if button2.pressed:
            down()
            button2.pressed = False
        

except KeyboardInterrupt:
    rgb.turnRGB_off()
    sleep(1)

finally:
    board.clean_up()
