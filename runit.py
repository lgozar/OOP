from lcd_class import LCD
from board import Board
from time import sleep

board = Board()
lcd = LCD(board)

lcd.lcd_string("Testing ....",lcd.LCD_LINE_1)
lcd.lcd_string("And it works!",lcd.LCD_LINE_2)

sleep(3)

lcd.cleanup()
