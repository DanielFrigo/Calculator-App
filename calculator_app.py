"""
Instructions
- If you want to input an expression manually after calculating a result you MUST press "Clear"
- using +/- will make a number negative for the purposes of order of operation ex. -1^2 = 1 not -1
- appling an operation to a single number like +/- or sqrt will fix the formatting

Consider case where I press for example + multiple times
Maybe disable the buttons?

Program is getting a bit tricky now. Stuff I need to implement
- abs. there's a way to do it with the | lines instead of writing abs but it's a bit complicated
  I have to keep track of where I'm using | as an opener and | as a closer and replace the symbols appropiatley
  Gets especially tricky if you have nested absolute operators
- delete button can maybe be smart about deleting entire log or sin or whatever
- write 2 more stores and display their values? may not be worth it
- Put buttons on their own frame?
- the arctan functions do not know which quadrant you are in. Maybe you an figure out a way to implement this
- Implement a button (buttons?) to convert from degrees to radians and vice versa
- I do believe there is a major security flaw in using the eval function to evaluate the expression in the entry field.
  A quick solution would be to disable the entry field all together and force the user to use the buttons
  As it stands the user can input whatever code he wants in the entry field and it will get executed if it's valid (not good)
- Put buttons in different frames to organize it better
"""


import tkinter as tk
import re
import math

BUTTON_PADDING_X = 5
BUTTON_PADDING_Y = 1
BUTTON_BORDER = 3
BUTTON_WIDTH = 5
BUTTON_HEIGHT = 1
NUM_COLUMNS = 6
MAX_DECIMAL_PLACES = 5
EXPRESSION_HISTORY_SIZE = 5

calc_string = ''

result = 0
result_just_calculated = False

stored_value = 0


#Number Buttons
def zero():
    global calc_string
    
    if result_just_calculated:
        clear()

    entry_pos = results_entry.index('insert')  
    calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)
    calc_string = calc_string[:entry_pos] + '0' + calc_string[entry_pos:]
    results_entry.insert(entry_pos, '0')
def one():
    global calc_string

    if result_just_calculated:
        clear()

    entry_pos = results_entry.index('insert')  
    calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)
    calc_string = calc_string[:entry_pos] + '1' + calc_string[entry_pos:]
    results_entry.insert(entry_pos, '1')
def two():
    global calc_string

    if result_just_calculated:
        clear()

    entry_pos = results_entry.index('insert')  
    calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)
    calc_string = calc_string[:entry_pos] + '2' + calc_string[entry_pos:]
    results_entry.insert(entry_pos, '2')
def three():
    global calc_string

    if result_just_calculated:
        clear()

    entry_pos = results_entry.index('insert')  
    calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)
    calc_string = calc_string[:entry_pos] + '3' + calc_string[entry_pos:]
    results_entry.insert(entry_pos, '3')
def four():
    global calc_string

    if result_just_calculated:
        clear()

    entry_pos = results_entry.index('insert')  
    calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)
    calc_string = calc_string[:entry_pos] + '4' + calc_string[entry_pos:]
    results_entry.insert(entry_pos, '4')
def five():
    global calc_string

    if result_just_calculated:
        clear()

    entry_pos = results_entry.index('insert')  
    calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)
    calc_string = calc_string[:entry_pos] + '5' + calc_string[entry_pos:]
    results_entry.insert(entry_pos, '5')
def six():
    global calc_string

    if result_just_calculated:
        clear()

    entry_pos = results_entry.index('insert')  
    calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input) 
    calc_string = calc_string[:entry_pos] + '6' + calc_string[entry_pos:]
    results_entry.insert(entry_pos, '6')
def seven():
    global calc_string

    if result_just_calculated:
        clear()

    entry_pos = results_entry.index('insert')  
    calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)
    calc_string = calc_string[:entry_pos] + '7' + calc_string[entry_pos:]
    results_entry.insert(entry_pos, '7')
def eight():
    global calc_string

    if result_just_calculated:
        clear()

    entry_pos = results_entry.index('insert')  
    calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)
    calc_string = calc_string[:entry_pos] + '8' + calc_string[entry_pos:]
    results_entry.insert(entry_pos, '8')
def nine():
    global calc_string

    if result_just_calculated:
        clear()

    entry_pos = results_entry.index('insert')  
    calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)
    calc_string = calc_string[:entry_pos] + '9' + calc_string[entry_pos:]
    results_entry.insert(entry_pos, '9')
def dot():
    global calc_string

    if result_just_calculated:
        clear()

    entry_pos = results_entry.index('insert')  
    calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)
    calc_string = calc_string[:entry_pos] + '.' + calc_string[entry_pos:]
    results_entry.insert(entry_pos, '.')
def open_bracket():
    global calc_string
    global result
    global result_just_calculated

    if result_just_calculated:
        clear(keep_result=True)
        calc_string = '(' + str(result)
        results_entry.insert(0, calc_string)
        entry_pos = results_entry.index('insert')  
        result_just_calculated = False     
        
    else:
        entry_pos = results_entry.index('insert')
        calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)
        calc_string = calc_string[:entry_pos] + '(' + calc_string[entry_pos:]
        results_entry.insert(entry_pos, '(')

    results_entry.delete(0, 'end')
    results_entry.insert(0, calc_string)
def close_bracket():
    global calc_string
    global result
    global result_just_calculated

    entry_pos = results_entry.index('insert')
    calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)
    calc_string = calc_string[:entry_pos] + ')' + calc_string[entry_pos:]
    results_entry.insert(entry_pos, ')')
def insert_pi():
    
    global MAX_DECIMAL_PLACES
    global calc_string

    if result_just_calculated:
        clear()

    entry_pos = results_entry.index('insert')  
    calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)
    calc_string = calc_string[:entry_pos] + str(math.pi) + calc_string[entry_pos:]
    results_entry.insert(entry_pos, f'{math.pi:.{MAX_DECIMAL_PLACES}f}')
def insert_e():
    
    global MAX_DECIMAL_PLACES
    global calc_string

    if result_just_calculated:
        clear()

    entry_pos = results_entry.index('insert')  
    calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)
    calc_string = calc_string[:entry_pos] + str(math.e) + calc_string[entry_pos:]
    results_entry.insert(entry_pos, f'{math.e:.{MAX_DECIMAL_PLACES}f}')

#Operators

def neg():
    global calc_string
    global result
    global result_just_calculated

    if result_just_calculated:
        clear(keep_result=True)
        result = -result
        calc_string = str(result)
        results_entry.delete(0, 'end')
        results_entry.insert(0, calc_string)
    else:
        entry_pos = results_entry.index('insert') #get cursor position        
        calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)
        number, index = is_number(calc_string) #check if the last thing in the entry is a number
        if number is not None and entry_pos >= len(calc_string): #cursor is at the end of the entry:
            number = convert_number(number)
            number = -number
            number = str(number)
            calc_string = calc_string[:index] + number
            
            results_entry.delete(0, 'end')
            results_entry.insert(0, calc_string)

        else:
            calc_string = calc_string[:entry_pos] + '-' + calc_string[entry_pos:]
            results_entry.insert(entry_pos, '-')

def plus():
    global calc_string
    global result
    global result_just_calculated

    if result_just_calculated:
        clear(keep_result=True)
        calc_string = str(result)
        results_entry.insert(0, calc_string)
        entry_pos = results_entry.index('insert')  
        result_just_calculated = False      
    else:
        entry_pos = results_entry.index('insert') #get cursosr position
        calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)

    calc_string = calc_string[:entry_pos] + '+' + calc_string[entry_pos:]
    results_entry.insert(entry_pos, '+')

def minus():
    global calc_string
    global result
    global result_just_calculated

    if result_just_calculated:
        clear(keep_result=True)
        calc_string = str(result)
        results_entry.insert(0, calc_string)
        entry_pos = results_entry.index('insert')  
        result_just_calculated = False    
    else:
        entry_pos = results_entry.index('insert')  
        calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)
  
    #NOT THE NORMAL "-". THIS IS A SPECIAL MINUS SIGN TO DIFFERENTIATE WITH NEGATIVE NUMBERS
    calc_string = calc_string[:entry_pos] + '−' + calc_string[entry_pos:]
    results_entry.insert(entry_pos, '−')

def mult():
    global calc_string
    global result
    global result_just_calculated

    if result_just_calculated:
        clear(keep_result=True)
        calc_string = str(result)
        results_entry.insert(0, calc_string)
        entry_pos = results_entry.index('insert')  
        result_just_calculated = False     
    else:
        entry_pos = results_entry.index('insert')  
        calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)

    calc_string = calc_string[:entry_pos] + 'x' + calc_string[entry_pos:]
    results_entry.insert(entry_pos, 'x')

def div():
    global calc_string
    global result
    global result_just_calculated

    if result_just_calculated:
        clear(keep_result=True)
        calc_string = str(result)
        results_entry.insert(0, calc_string)
        entry_pos = results_entry.index('insert')  
        result_just_calculated = False    
    else:
        entry_pos = results_entry.index('insert')  
        calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)

    calc_string = calc_string[:entry_pos] + '÷' + calc_string[entry_pos:]
    results_entry.insert(entry_pos, '÷')

def mod():
    global calc_string
    global result
    global result_just_calculated

    if result_just_calculated:
        clear(keep_result=True)
        calc_string = str(result)
        results_entry.insert(0, calc_string)
        entry_pos = results_entry.index('insert')  
        result_just_calculated = False      
    else:
        entry_pos = results_entry.index('insert')  
        calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)
    
    calc_string = calc_string[:entry_pos] + '%' + calc_string[entry_pos:]
    results_entry.insert(entry_pos, '%')

def power():
    global calc_string
    global result
    global result_just_calculated

    if result_just_calculated:
        clear(keep_result=True)
        calc_string = str(result)
        results_entry.insert(0, calc_string)
        entry_pos = results_entry.index('insert')  
        result_just_calculated = False      
    else:
        entry_pos = results_entry.index('insert')  
        calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)

    calc_string = calc_string[:entry_pos] + '^' + calc_string[entry_pos:]
    results_entry.insert(entry_pos, '^')

def Sqrt():
    
    """
    This function may have a lot of bugs
    I'm just going to implement it simply
    nesting is probabbly not handled properly
    deleting is probabbly not handled properly
    user has to close sqrt bracket
    """

    global calc_string
    global result
    global result_just_calculated
    
    if result_just_calculated:
        clear(keep_result=True)
        calc_string = calc_string + '√('
        calc_string = calc_string + str(result)
        results_entry.insert(0, calc_string) 
        entry_pos = results_entry.index('insert')
        result_just_calculated = False             
        
    else:
        entry_pos = results_entry.index('insert') #get cursor position
        calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)
                
        number, index = is_number(calc_string) #check if the last thing in the entry is a number
        if number is not None and entry_pos >= len(calc_string): #cursor is at the end of the entry

            number = convert_number(number)
            number = str(number)
            calc_string = calc_string[:index] + '√(' + number

            results_entry.delete(0, 'end')
            results_entry.insert(0, calc_string)   

        else:
            calc_string = calc_string[:entry_pos] + '√(' + calc_string[entry_pos:]
            results_entry.insert(entry_pos, '√(')
        
def cbrt():
    """
    This function may have a lot of bugs
    I'm just going to implement it simply
    nesting is probabbly not handled properly
    deleting is probabbly not handled properly
    user has to close bracket
    """

    global calc_string
    global result
    global result_just_calculated
    
    if result_just_calculated:
        clear(keep_result=True)
        calc_string = calc_string + '∛('
        calc_string = calc_string + str(result)
        results_entry.insert(0, calc_string) 
        entry_pos = results_entry.index('insert')
        result_just_calculated = False             
        
    else:
        entry_pos = results_entry.index('insert') #get cursor position
        calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)
                
        number, index = is_number(calc_string) #check if the last thing in the entry is a number
        if number is not None and entry_pos >= len(calc_string): #cursor is at the end of the entry

            number = convert_number(number)
            number = str(number)
            calc_string = calc_string[:index] + '∛(' + number

            results_entry.delete(0, 'end')
            results_entry.insert(0, calc_string)   

        else:
            calc_string = calc_string[:entry_pos] + '∛(' + calc_string[entry_pos:]
            results_entry.insert(entry_pos, '∛(')

def inverse():
    
    global MAX_DECIMAL_PLACES
    global calc_string
    global result
    global result_just_calculated

    if result_just_calculated:
        clear(keep_result=True)
        result = 1/result
        calc_string = str(result)
        results_entry.delete(0, 'end')
        results_entry.insert(0, calc_string)
    else:
        entry_pos = results_entry.index('insert') #get cursor position        
        calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)
        number, index = is_number(calc_string) #check if the last thing in the entry is a number
        if number is not None and entry_pos >= len(calc_string): #cursor is at the end of the entry:
            number = convert_number(number)
            number = float(1/number)
            calc_string = calc_string[:index] + f'{number:.{MAX_DECIMAL_PLACES}f}'.rstrip('0').rstrip('.')
            
            results_entry.delete(0, 'end')
            results_entry.insert(0, calc_string)

        else:
            calc_string = calc_string[:entry_pos] + '1/' + calc_string[entry_pos:]
            results_entry.insert(entry_pos, '1/')

def absolute():
    """
    This function may have a lot of bugs
    I'm just going to implement it simply
    nesting is probabbly not handled properly
    deleting is probabbly not handled properly
    user has to close bracket
    """

    global calc_string
    global result
    global result_just_calculated
    
    if result_just_calculated:
        clear(keep_result=True)
        calc_string = calc_string + 'abs('
        calc_string = calc_string + str(result)
        results_entry.insert(0, calc_string) 
        entry_pos = results_entry.index('insert')
        result_just_calculated = False             
        
    else:
        entry_pos = results_entry.index('insert') #get cursor position
        calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)
                
        number, index = is_number(calc_string) #check if the last thing in the entry is a number
        if number is not None and entry_pos >= len(calc_string): #cursor is at the end of the entry

            number = convert_number(number)
            number = str(number)
            calc_string = calc_string[:index] + 'abs(' + number

            results_entry.delete(0, 'end')
            results_entry.insert(0, calc_string)   

        else:
            calc_string = calc_string[:entry_pos] + 'abs(' + calc_string[entry_pos:]
            results_entry.insert(entry_pos, 'abs(')

def log():
    
    """
    This function may have a lot of bugs
    I'm just going to implement it simply
    nesting is probabbly not handled properly
    deleting is probabbly not handled properly
    user has to close bracket
    """

    global calc_string
    global result
    global result_just_calculated
    
    if result_just_calculated:
        clear(keep_result=True)
        calc_string = calc_string + '㏒('
        calc_string = calc_string + str(result)
        results_entry.insert(0, calc_string) 
        entry_pos = results_entry.index('insert')
        result_just_calculated = False             
        
    else:
        entry_pos = results_entry.index('insert') #get cursor position
        calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)
                
        number, index = is_number(calc_string) #check if the last thing in the entry is a number
        if number is not None and entry_pos >= len(calc_string): #cursor is at the end of the entry

            number = convert_number(number)
            number = str(number)
            calc_string = calc_string[:index] + '㏒(' + number

            results_entry.delete(0, 'end')
            results_entry.insert(0, calc_string)   

        else:
            calc_string = calc_string[:entry_pos] + '㏒(' + calc_string[entry_pos:]
            results_entry.insert(entry_pos, '㏒(')

def ln():
    """
    ㏒
    """
    
    """
    This function may have a lot of bugs
    I'm just going to implement it simply
    nesting is probabbly not handled properly
    deleting is probabbly not handled properly
    user has to close bracket
    """

    global calc_string
    global result
    global result_just_calculated
    
    if result_just_calculated:
        clear(keep_result=True)
        calc_string = calc_string + '㏑('
        calc_string = calc_string + str(result)
        results_entry.insert(0, calc_string) 
        entry_pos = results_entry.index('insert')
        result_just_calculated = False             
        
    else:
        entry_pos = results_entry.index('insert') #get cursor position
        calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)
                
        number, index = is_number(calc_string) #check if the last thing in the entry is a number
        if number is not None and entry_pos >= len(calc_string): #cursor is at the end of the entry

            number = convert_number(number)
            number = str(number)
            calc_string = calc_string[:index] + '㏑(' + number

            results_entry.delete(0, 'end')
            results_entry.insert(0, calc_string)   

        else:
            calc_string = calc_string[:entry_pos] + '㏑(' + calc_string[entry_pos:]
            results_entry.insert(entry_pos, '㏑(')

def sin():
  
    """
    This function may have a lot of bugs
    I'm just going to implement it simply
    nesting is probabbly not handled properly
    deleting is probabbly not handled properly
    user has to close sqrt bracket
    """

    global calc_string
    global result
    global result_just_calculated
    
    if result_just_calculated:
        clear(keep_result=True)
        calc_string = calc_string + 'sin('
        calc_string = calc_string + str(result)
        results_entry.insert(0, calc_string) 
        entry_pos = results_entry.index('insert')
        result_just_calculated = False             
        
    else:
        entry_pos = results_entry.index('insert') #get cursor position
        calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)
                
        number, index = is_number(calc_string) #check if the last thing in the entry is a number
        if number is not None and entry_pos >= len(calc_string): #cursor is at the end of the entry

            number = convert_number(number)
            number = str(number)
            calc_string = calc_string[:index] + 'sin(' + number

            results_entry.delete(0, 'end')
            results_entry.insert(0, calc_string)   

        else:
            calc_string = calc_string[:entry_pos] + 'sin(' + calc_string[entry_pos:]
            results_entry.insert(entry_pos, 'sin(')

def cos():
    """
    This function may have a lot of bugs
    I'm just going to implement it simply
    nesting is probabbly not handled properly
    deleting is probabbly not handled properly
    user has to close sqrt bracket
    """

    global calc_string
    global result
    global result_just_calculated
    
    if result_just_calculated:
        clear(keep_result=True)
        calc_string = calc_string + 'cos('
        calc_string = calc_string + str(result)
        results_entry.insert(0, calc_string) 
        entry_pos = results_entry.index('insert')
        result_just_calculated = False             
        
    else:
        entry_pos = results_entry.index('insert') #get cursor position
        calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)
                
        number, index = is_number(calc_string) #check if the last thing in the entry is a number
        if number is not None and entry_pos >= len(calc_string): #cursor is at the end of the entry

            number = convert_number(number)
            number = str(number)
            calc_string = calc_string[:index] + 'cos(' + number

            results_entry.delete(0, 'end')
            results_entry.insert(0, calc_string)   

        else:
            calc_string = calc_string[:entry_pos] + 'cos(' + calc_string[entry_pos:]
            results_entry.insert(entry_pos, 'cos(')

def tan():
    """
    This function may have a lot of bugs
    I'm just going to implement it simply
    nesting is probabbly not handled properly
    deleting is probabbly not handled properly
    user has to close sqrt bracket
    """

    global calc_string
    global result
    global result_just_calculated
    
    if result_just_calculated:
        clear(keep_result=True)
        calc_string = calc_string + 'tan('
        calc_string = calc_string + str(result)
        results_entry.insert(0, calc_string) 
        entry_pos = results_entry.index('insert')
        result_just_calculated = False             
        
    else:
        entry_pos = results_entry.index('insert') #get cursor position
        calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)
                
        number, index = is_number(calc_string) #check if the last thing in the entry is a number
        if number is not None and entry_pos >= len(calc_string): #cursor is at the end of the entry

            number = convert_number(number)
            number = str(number)
            calc_string = calc_string[:index] + 'tan(' + number

            results_entry.delete(0, 'end')
            results_entry.insert(0, calc_string)   

        else:
            calc_string = calc_string[:entry_pos] + 'tan(' + calc_string[entry_pos:]
            results_entry.insert(entry_pos, 'tan(')

def asin():
    """
    This function may have a lot of bugs
    I'm just going to implement it simply
    nesting is probabbly not handled properly
    deleting is probabbly not handled properly
    user has to close sqrt bracket
    """

    global calc_string
    global result
    global result_just_calculated
    
    if result_just_calculated:
        clear(keep_result=True)
        calc_string = calc_string + 'asin('
        calc_string = calc_string + str(result)
        results_entry.insert(0, calc_string) 
        entry_pos = results_entry.index('insert')
        result_just_calculated = False             
        
    else:
        entry_pos = results_entry.index('insert') #get cursor position
        calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)
                
        number, index = is_number(calc_string) #check if the last thing in the entry is a number
        if number is not None and entry_pos >= len(calc_string): #cursor is at the end of the entry

            number = convert_number(number)
            number = str(number)
            calc_string = calc_string[:index] + 'asin(' + number

            results_entry.delete(0, 'end')
            results_entry.insert(0, calc_string)   

        else:
            calc_string = calc_string[:entry_pos] + 'asin(' + calc_string[entry_pos:]
            results_entry.insert(entry_pos, 'asin(')

def acos():
    """
    This function may have a lot of bugs
    I'm just going to implement it simply
    nesting is probabbly not handled properly
    deleting is probabbly not handled properly
    user has to close sqrt bracket
    """

    global calc_string
    global result
    global result_just_calculated
    
    if result_just_calculated:
        clear(keep_result=True)
        calc_string = calc_string + 'acos('
        calc_string = calc_string + str(result)
        results_entry.insert(0, calc_string) 
        entry_pos = results_entry.index('insert')
        result_just_calculated = False             
        
    else:
        entry_pos = results_entry.index('insert') #get cursor position
        calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)
                
        number, index = is_number(calc_string) #check if the last thing in the entry is a number
        if number is not None and entry_pos >= len(calc_string): #cursor is at the end of the entry

            number = convert_number(number)
            number = str(number)
            calc_string = calc_string[:index] + 'acos(' + number

            results_entry.delete(0, 'end')
            results_entry.insert(0, calc_string)   

        else:
            calc_string = calc_string[:entry_pos] + 'acos(' + calc_string[entry_pos:]
            results_entry.insert(entry_pos, 'acos(')

def atan():
    """
    This function may have a lot of bugs
    I'm just going to implement it simply
    nesting is probabbly not handled properly
    deleting is probabbly not handled properly
    user has to close sqrt bracket
    """

    global calc_string
    global result
    global result_just_calculated
    
    if result_just_calculated:
        clear(keep_result=True)
        calc_string = calc_string + 'atan('
        calc_string = calc_string + str(result)
        results_entry.insert(0, calc_string) 
        entry_pos = results_entry.index('insert')
        result_just_calculated = False             
        
    else:
        entry_pos = results_entry.index('insert') #get cursor position
        calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)
                
        number, index = is_number(calc_string) #check if the last thing in the entry is a number
        if number is not None and entry_pos >= len(calc_string): #cursor is at the end of the entry

            number = convert_number(number)
            number = str(number)
            calc_string = calc_string[:index] + 'atan(' + number

            results_entry.delete(0, 'end')
            results_entry.insert(0, calc_string)   

        else:
            calc_string = calc_string[:entry_pos] + 'atan(' + calc_string[entry_pos:]
            results_entry.insert(entry_pos, 'atan(')

def calc_cube_root(x):
    return x**(1/3)

def calc_log_10(x):
    return math.log(x, 10)

def calc_sin(x):

    units = angle_choice.get()

    if units == 'deg':
        return math.sin(x*math.pi/180)
    else:
        return math.sin(x)

def calc_cos(x):

    units = angle_choice.get()

    if units == 'deg':
        return math.cos(x*math.pi/180)
    else:
        return math.cos(x)
    
def calc_tan(x):

    units = angle_choice.get()

    if units == 'deg':
        return math.tan(x*math.pi/180)
    else:
        return math.tan(x)

def calc_ASIN(x):

    units = angle_choice.get()

    if units == 'deg':
        return math.asin(x)*180/math.pi
    else:
        return math.asin(x)

def calc_ACOS(x):

    units = angle_choice.get()

    if units == 'deg':
        return math.acos(x)*180/math.pi
    else:
        return math.acos(x)

def calc_ATAN(x):

    units = angle_choice.get()

    if units == 'deg':
        return math.atan(x)*180/math.pi
    else:
        return math.atan(x)

def equals(event=None):
    
    global MAX_DECIMAL_PLACES
    
    global calc_string
    global result
    global result_just_calculated
    
    calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)

    if not result_just_calculated:
        calc_string_formatted = format_string_numbers(calc_string) #gets rid of uncessesary leading 0's

        try:
            expression = get_expression(calc_string_formatted)
            result = eval(expression)
            result = convert_number(result)

            if isinstance(result, float):
                result = f'{result:.{MAX_DECIMAL_PLACES}f}'.rstrip('0').rstrip('.')
                calc_string = calc_string + " = " + result
            else:
                result = str(result)
                calc_string = calc_string + " = " + result
        
            results_entry.delete(0, 'end')
            results_entry.insert(0, calc_string)
            update_expression_history(calc_string)       
            calc_string = ''
            result_just_calculated = True
            results_entry.config(state="readonly")
    
        except:
            #cannot do calculation
            result = 0
            result_just_calculated = False    
            calc_string = 'Error!~'
            results_entry.delete(0, 'end')
            results_entry.insert(0, calc_string)
            calc_string = ''   

def get_expression(st):
    
    new_string = ''

    #put negative numbers inside brackets for the purposes of order of operations. a negative number is a negative number
    #it is not -1 * number
    #capture numbers. both ints and floats
    numbers = re.finditer(r'-+(?:\d+\.\d+|\.\d+|\d+|\d+\.)',st)
    negative_numbers_found = False
    end_index = 0
    for match in numbers:
        negative_numbers_found = True
        number = match.group()
        start_index = match.start()
        
        negative = 1
        num_part = False
        num_temp = ''
        for c in number:
            #accounting if for whatever reason therea are multiple ------. Though I would consider this as part of "do stupid things get stupid results"
            if c == '-':
                #I only expect - at the beggining of a number   
                negative = negative * -1
            else:
                if not num_part:
                    if negative < 0:
                        num_temp = '(-'
                    num_part = True       
                num_temp = num_temp + c
        
        if negative < 0:
            num_temp = num_temp + ')' 

        new_string = new_string + st[end_index:start_index] + num_temp
        end_index = match.end()

    if negative_numbers_found:
        #if negative numbers are involved, do a final concatenation
        new_string = new_string + st[end_index:]
    else:
        new_string = st

    new_string = new_string.replace('−', '-')
    new_string = new_string.replace('x', '*')
    new_string = new_string.replace('X', '*')
    new_string = new_string.replace('÷', '/')
    new_string = new_string.replace('^', '**')
    new_string = new_string.replace('√', 'math.sqrt')
    new_string = new_string.replace('∛', 'calc_cube_root')
    new_string = new_string.replace('㏒', 'calc_log_10')
    new_string = new_string.replace('㏑', 'math.log') #base e
    
    new_string = new_string.replace('asin', 'calc_ASIN') #CAPITAL SO IT DOESN'T INTERFERE WITH THE NEXT SIN REPLACEMENTS
    new_string = new_string.replace('acos', 'calc_ACOS')
    new_string = new_string.replace('atan', 'calc_ATAN')
    
    new_string = new_string.replace('sin', 'calc_sin')
    new_string = new_string.replace('cos', 'calc_cos')
    new_string = new_string.replace('tan', 'calc_tan')


    return new_string    

def format_string_numbers(st):
    
    """
    function gets rid of uneccessary leading 0's
    """
    
    new_string = ''
    
    #capture numbers. both ints and floats
    numbers = re.finditer(r'-?(?:\d+\.\d+|\.\d+|\d+|\d+\.)',st)
 
    #-? find "-" 0 or 1 more occurrence for negative numbers
    #(?: this is starting a grouping for logic but does not save it as a match. Key here is the ?: | is an OR operator
    #next is an OR of three different patterns
    
    #\d+\.\d+   3.14
    #\.\d+      .14
    #\d+        345
    #\d+\.      3.


    end_index = 0
    for match in numbers:
        
        number = match.group() # group is the matched number as int
        number = convert_number(number) #returns an int or float
        start_index = match.start()   

        new_string = new_string + st[end_index:start_index] + str(number) 

        end_index = match.end()  
    
    new_string = new_string + st[end_index:]
    return new_string
    
def convert_number(num_str):
    
    """
    convert number to float or int from string
    """
    
    converted_num = None

    try:
        if '.' in str(num_str):
            converted_num = float(num_str)
        else:
            converted_num = int(num_str)
        return converted_num
    except:
        print("Cannot convert number")
        return None

def is_number(st):

    """
    if last thing in the entry field is a number, it will return that number
    and also the starting position of that number
    """

    #capture numbers. both ints and floats
    numbers = list(re.finditer(r'-?(?:\d+\.\d+|\.\d+|\d+|\d+\.)',st))
    if len(numbers) > 0:
        last_number_match = numbers[len(numbers)-1]
        last_number = last_number_match.group()
        last_number_start_index = last_number_match.start()
        last_number_end_index = last_number_match.end()
    else:
        return None, None

    if last_number_end_index == len(st):
        return last_number, last_number_start_index
    else:
        return None, None

def delete():
    global calc_string
    global result
    global result_just_calculated

    entry_pos = results_entry.index('insert') #get position of cursor
    calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)

    if not result_just_calculated and calc_string != '' and entry_pos > 0:
        
        if entry_pos == len(calc_string):
            #cursor is at the end
            calc_string = calc_string[:-1]
        else:       
            calc_string = calc_string[:entry_pos-1] + calc_string[entry_pos:]
        
        results_entry.delete(entry_pos-1)

def clear(keep_result=False):
    global calc_string
    global result
    global result_just_calculated

    results_entry.config(state="normal")  
    results_entry.delete(0, 'end')
    calc_string = '' 
    
    if not keep_result:
        result = 0
    
    result_just_calculated = False

def store():

    global stored_value

    if result_just_calculated:
        stored_value = str(convert_number(result)) #should be a string
        stored_value_label['text'] = 'ST: ' + stored_value
    else:
        entry_pos = results_entry.index('insert') #get cursor position  
        number, index = is_number(calc_string) #check if the last thing in the entry is a number
        if number is not None and entry_pos >= len(calc_string): #cursor is at the end of the entry:
            stored_value = str(convert_number(number))
            stored_value_label['text'] = 'ST: ' + stored_value

def recall():

    global calc_string

    if result_just_calculated:
        clear()

    entry_pos = results_entry.index('insert')  
    calc_string = results_entry.get() #input whatever is displayed in the entry just in case it's different then what you generated with the buttons (manual input)
    calc_string = calc_string[:entry_pos] + str(stored_value) + calc_string[entry_pos:]
    results_entry.insert(entry_pos, str(stored_value))

def update_expression_history(expression):
    global result
    global expression_history

    for i in range(len(expression_history)-1, -1, -1): #start at end, go backwards 1 step, stop at 0
        
        if i == 0:
            expression_history[i]['text'] = expression
        else:        
            expression_history[i]['text'] = expression_history[i-1]['text']    

def close_window(event):
    window.destroy()    


window = tk.Tk()
window.geometry("600x600")
window.bind("<Escape>", close_window)
window.title("Calculator")

main_frame = tk.Frame(master=window, relief='ridge', borderwidth=5)
# Create a frame with NUM_COLUMNS columns
for i in range(NUM_COLUMNS):
    main_frame.columnconfigure(i, weight=1)

main_frame.pack(fill='both', padx=5, pady=5)
#main_frame.pack_propagate(False) # This keeps the size fixed

angle_choice = tk.StringVar(value="rad")

rb1 = tk.Radiobutton(master=main_frame, text="rad", font=("Arial", 10), width=5, variable=angle_choice, value="rad")
rb2 = tk.Radiobutton(master=main_frame, text="deg", font=("Arial", 10), width=5, variable=angle_choice, value="deg")

rb1.grid(row=0, column=0, sticky='w', padx=1, pady=1)
rb2.grid(row=0, column=1, sticky='w', padx=1, pady=1)

results_entry = tk.Entry(master=main_frame, font=("Arial", 12), relief='sunken', background='white', borderwidth=5)
results_entry.grid(row=1, column=0, sticky='we', columnspan=NUM_COLUMNS, pady=5)
results_entry.bind("<Return>", equals)

button_0 = tk.Button(master=main_frame, font=("Arial", 12), text="0", command=zero, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_1 = tk.Button(master=main_frame, font=("Arial", 12), text="1", command=one, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_2 = tk.Button(master=main_frame, font=("Arial", 12), text="2", command=two, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_3 = tk.Button(master=main_frame, font=("Arial", 12), text="3", command=three, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT) 
button_4 = tk.Button(master=main_frame, font=("Arial", 12), text="4", command=four, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_5 = tk.Button(master=main_frame, font=("Arial", 12), text="5", command=five, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_6 = tk.Button(master=main_frame, font=("Arial", 12), text="6", command=six, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_7 = tk.Button(master=main_frame, font=("Arial", 12), text="7", command=seven, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_8 = tk.Button(master=main_frame, font=("Arial", 12), text="8", command=eight, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_9 = tk.Button(master=main_frame, font=("Arial", 12), text="9", command=nine, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_pm = tk.Button(master=main_frame, font=("Arial", 12), text="+/-", command=neg, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_dot = tk.Button(master=main_frame, font=("Arial", 12), text=".", command=dot, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_plus = tk.Button(master=main_frame, font=("Arial", 12), text="+", command=plus, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_minus = tk.Button(master=main_frame, font=("Arial", 12), text="−", command=minus, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_mult = tk.Button(master=main_frame, font=("Arial", 12), text="X", command=mult, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_div = tk.Button(master=main_frame, font=("Arial", 12), text="÷", command=div, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_mod = tk.Button(master=main_frame, font=("Arial", 12), text="%", command=mod, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_pow = tk.Button(master=main_frame, font=("Arial", 12), text="^", command=power, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_sq_root = tk.Button(master=main_frame, font=("Arial", 12), text="√", command=Sqrt, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_cube_root = tk.Button(master=main_frame, font=("Arial", 12), text="∛", command=cbrt, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_inverse = tk.Button(master=main_frame, font=("Arial", 12), text="1/x", command=inverse, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_abs = tk.Button(master=main_frame, font=("Arial", 12), text="|x|", command=absolute, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_equals = tk.Button(master=main_frame, font=("Arial", 12), text="=", command=equals, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_clear = tk.Button(master=main_frame, font=("Arial", 12), text="Clear", command=clear, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_store = tk.Button(master=main_frame, font=("Arial", 12), text="Str", command=store, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_recall = tk.Button(master=main_frame, font=("Arial", 12), text="Rcl", command=recall, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_log = tk.Button(master=main_frame, font=("Arial", 12), text="㏒", command=log, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_ln = tk.Button(master=main_frame, font=("Arial", 12), text="㏑", command=ln, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_open_bracket = tk.Button(master=main_frame, font=("Arial", 12), text="(", command=open_bracket, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_close_bracket = tk.Button(master=main_frame, font=("Arial", 12), text=")", command=close_bracket, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_delete = tk.Button(master=main_frame, font=("Arial", 12), text="⌫", command=delete, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_sin = tk.Button(master=main_frame, font=("Arial", 12), text="sin", command=sin, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_cos = tk.Button(master=main_frame, font=("Arial", 12), text="cos", command=cos, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_tan = tk.Button(master=main_frame, font=("Arial", 12), text="tan", command=tan, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_asin = tk.Button(master=main_frame, font=("Arial", 12), text="asin", command=asin, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_acos = tk.Button(master=main_frame, font=("Arial", 12), text="acos", command=acos, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_atan = tk.Button(master=main_frame, font=("Arial", 12), text="atan", command=atan, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_pi = tk.Button(master=main_frame, font=("Arial", 12), text="π", command=insert_pi, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_e = tk.Button(master=main_frame, font=("Arial", 12), text="e", command=insert_e, relief='raised', borderwidth=BUTTON_BORDER, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

stored_value_label = tk.Label(master=main_frame, text="ST: 0", height=BUTTON_HEIGHT, font = ("Arial", 10), anchor='w')

expression_history = []
for _ in range(EXPRESSION_HISTORY_SIZE):
    expression_history.append(tk.Label(master=main_frame, text="", height=BUTTON_HEIGHT, font = ("Arial", 10), anchor='w'))    

tk.Label(master=main_frame, text="test", height=BUTTON_HEIGHT, font = ("Arial", 10), anchor='w')

button_1.grid(row=2, column=0, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_2.grid(row=2, column=1, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_3.grid(row=2, column=2, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_4.grid(row=3, column=0, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_5.grid(row=3, column=1, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_6.grid(row=3, column=2, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_7.grid(row=4, column=0, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_8.grid(row=4, column=1, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_9.grid(row=4, column=2, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_pm.grid(row=5, column=0, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_0.grid(row=5, column=1, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_dot.grid(row=5, column=2, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)

button_plus.grid(row=2, column=3, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_minus.grid(row=3, column=3, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_mult.grid(row=4, column=3, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_div.grid(row=5, column=3, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_mod.grid(row=6, column=3, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_equals.grid(row=6, column=1, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_pow.grid(row=2, column=4, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_sq_root.grid(row=3, column=4, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_cube_root.grid(row=4, column=4, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_inverse.grid(row=5, column=4, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_abs.grid(row=6, column=4, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_open_bracket.grid(row=6, column=0, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_close_bracket.grid(row=6, column=2, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)

button_pi.grid(row=7, column=0, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_e.grid(row=7, column=1, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_log.grid(row=7, column=3, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_ln.grid(row=7, column=4, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)

button_delete.grid(row=7, column=2, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)

button_store.grid(row=8, column=0, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_recall.grid(row=8, column=1, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_clear.grid(row=8, column=2, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)

button_sin.grid(row=2, column=5, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_cos.grid(row=3, column=5, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_tan.grid(row=4, column=5, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_asin.grid(row=5, column=5, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_acos.grid(row=6, column=5, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)
button_atan.grid(row=7, column=5, sticky='we', padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)

stored_value_label.grid(row=9, column=0, sticky='w', padx=5, pady=10, columnspan=3)

for i, e in enumerate(expression_history):
    e.grid(row=10+i, column=0, sticky='w', padx=5, pady=1, columnspan=5)

window.mainloop()