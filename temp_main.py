from board import Board #import the board class
from time import sleep 
from lcd_class import LCD #import the LCD class
from temp_class import Temperature #import the temperature class
from button_class import Button #import the button class
from rgb_class import RGB #import the rgb class

'''main code'''

board = Board() #implement Board class to variable board
lcd = LCD(board) #implement LCD class to variable lcd while implementing the Board class into the LCD class
temp = Temperature() #implement Temperature class to variable temp
rgb = RGB(board, 16, 20, 21) #implement RGB class to variable rgb with pins 16 20 21
button1 = Button(board, 24) #implement Button class to variable button1 with pin 24
button2 = Button(board, 12) #implement Button class to variable button2 with pin 12
set_temp = 22

def up(): #this adds +1 value to the variable set_temp
    global set_temp
    set_temp += 1 #adds +1 to set_temp
    lcd.lcd_string("Set temperature", lcd.LCD_LINE_1) #shows text to LCD
    lcd.lcd_string("to " + str(set_temp) + ' C', lcd.LCD_LINE_2)
    sleep(1)
    
def down(): #this subtracts -1 value to the variable set_temp
    global set_temp
    set_temp -= 1 #subtracts -1 to set_temp
    lcd.lcd_string("Set temperature", lcd.LCD_LINE_1) #shows text to LCD
    lcd.lcd_string("to " + str(set_temp) + ' C', lcd.LCD_LINE_2)
    sleep(1)

try:
    while True:
        
        lcd.lcd_string("Temperature is",lcd.LCD_LINE_1) #shows text to LCD
        lcd.lcd_string(str(int(temp.c)) + ' degrees C',lcd.LCD_LINE_2)
            
        if temp.c < set_temp: #if temp.c is less than set_temp - turns red light on
            rgb.turnRGB_off() #turns rgb off
            rgb.turnRed_on() #turns red light on
        elif temp.c >= set_temp: #if temp.c is greater than or equal to set_temp - turns green light on
            rgb.turnRGB_off() #turns rgb off
            rgb.turnGreen_on() #turns green light on
        else:
            print('Error') #prints error with none of the statements above are found
        sleep(1)
        
        if button1.pressed: #if button1 is pressed adds +1 to set_temp
            up() #runs the up property
            button1.pressed = False
        if button2.pressed: #if button2 is pressed substracts -1 to set_temp
            down() #runs the down property
            button2.pressed = False
        

except KeyboardInterrupt:
    rgb.turnRGB_off() #turns the RGB light off
    print('Exiting..')
    sleep(1)

finally:
    lcd.lcd_string("Cleaning up GPIO", lcd.LCD_LINE_1) #shows text to LCD
    lcd.lcd_string("", lcd.LCD_LINE_2)
    print('Cleaning up GPIO')
    sleep(2)
    lcd.lcd_clear() #clears the LCD 
    board.clean_up() #clean up pins
    sleep(1)
