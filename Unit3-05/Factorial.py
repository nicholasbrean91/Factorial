# Code Created on: October 2017
# Code Created by: Nicholas Brean
# This code is a longer way to show the factorial kf a number that is chosen

import ui



def Factorial_number_calculate_button(sender):
    input = int(view['factorial_textfield'].text)
    
    counter = 1
    answer = 1

    while(counter <= input):
        answer = answer * counter
        counter = counter + 1
        view['answer_label'].text = 'the factorial is: ' + str(answer)




view = ui.load_view()
view.present('sheet')
