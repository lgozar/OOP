from board import Board
from time import sleep
from temp_class import Temperature
from button_class import Button
from rgb_class import RGB

'''main code'''

board = Board()
temp = Temperature()
rgb = RGB(board, 16, 20, 21)
button1 = Button(board, 24)
button2 = Button(board, 12)
set_temp = 22

def up():
    global set_temp
    set_temp += 1
    
def down():
    global set_temp
    set_temp -= 1

try:
    while True:
        
        c = temp.read_temp()
        celsius = str(float(round(c, 2)))
        msg = celsius + ' degress C.'
        print(msg)
            
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
            print('Button 1 pressed. New Value ' + str(set_temp))
            button1.pressed = False
        if button2.pressed:
            down()
            print('Button 2 pressed. New value ' + str(set_temp))
            button2.pressed = False
        

except KeyboardInterrupt:
    rgb.turnRGB_off()
    sleep(1)

finally:
    board.clean_up()
