# Created by Jenny Trac
# Created on Oct 30 2017
# Program calculates temp in F from temp in C
# uses procedures

import ui

def calculate_tempf(tempc_sent):
    # calculates celsius
    
    # process
    tempf = (tempc_sent * 9 / 5) + 32
    
    # output
    view['fahrenheit_label'].text = str(tempf) + "F"

def calculate_touch_up_inside(sender):
    # function for calculate button
    
    # input
    tempc = int(view['celsius_textfield'].text)
    
    # process
    calculate_tempf(tempc)

view = ui.load_view()
view.present('sheet')
