#json to write the output in a text file
import json
x = input('Enter 1 for replace utility and 2 for grep utility : ')

# for the replace utility
# here we are specifying the choices of the paramters and also the choices along with it
# choices are discarded by listing them in the eroor list
SIZE = {
    'empty':  '',
    'not_empty': 'NOT_EMPTY',
}

Number_of_occurrences_of_from_string_in_the_file = {
    'None':          0,
    'One':      1,
    'Many':  'Many'
}

Number_of_occurrences_of_from_string_in_one_line = {
    'One':      1,
    'Many':     'Many'
}

Position_of_the_from_string_in_the_file = {
    'First_line':      1,
    'Last_line':     'last',
    'any': 'any'  
}

filequantity = {
    'None': 'error',
    'One':  'single',
    'more_than_one': 'more_than_one'
}

presence_of_file = {
    'exist': 'error',
    'does_not_exist': 'single'
}

filename = {
    'good_file': '2020H1030121P_D3.ip1',
    'bad_file':  '2020H1030121_D3.ip1',
    'omitted': ''
}
length_first_string = {
     'zero':'single',
     'one':'single',
     'longer_then_file':'error'
}
length_second_string = {
     'zero':'single',
     'one':'single',
     'longer_then_file':'error'
}
# error list to add constraints
error = ['None', 'exist', 'longer_than_any_line', 'omitted', 'bad_file','longer_then_file']
########################################################################
# for the grep command
# specifying the constraints and choices for the grep command
SIZE1 = {
    'empty':  '',
    'not_empty': 'NOT_EMPTY',
}

Number_of_occurrences_of_pattern_in_the_file = {
    'None':          0,
    'One':      1,
    'Many':  'Many'
}

Number_of_occurrences_of_pattern_in_one_line = {
    'One':      1,
    'Many':     'Many'
}
Presence_of_enclosing_quotes ={
    'Not_enclosed': 0,
    'Enclosed' : 1,
    'Incorrect' : 'Incorrect'
}
Presence_of_blanks = {
    'Not_enclosed' : 0, 
    'Enclosed' :1,
    'Incorrect' : 'Incorrect'
}
Length_of_the_pattern = {
    'Empty' : 0,
    'One' :1,
     'More_than_one' :'2',
     'longer_than_the_file': 'error'    
}
Position_of_the_pattern_in_the_file={
    'First_line' : 1,
    'Last_line': -1,
    'any':'error' 
}
file_quality = {
   'None' : 0,
    'one': 1,
    'more_than_one':2
}
presence_of_file={
'exist' :1,
'not_exist' : 0 
}
filename = {
    'good_file': '2020H1030121P_D3.ip1',
    'bad_file':  '2020H1030121_D3.ip1',
    'omitted': ''
}
errors = ['None', 'exist', 'longer_than_any_line', 'omitted', 'bad_file','longer_then_file','any','Incorrect']

OUTPUT = {}

FILE_NAME = '2020H1030121P_D3.ip1'


#for grep utitlity we are creating a seprately method to return keys
def generateTestKeys1():
    keys = []
    for size in SIZE1:
        for sf in Number_of_occurrences_of_pattern_in_the_file:
             for sl in Number_of_occurrences_of_pattern_in_one_line:
                  for pos in Presence_of_enclosing_quotes:
                       for fq in Presence_of_blanks:
                            for pf in Position_of_the_pattern_in_the_file:
                                 for fn in file_quality:
                                      for lenf in presence_of_file:
                                           for lens in filename:	 
                                                k = [size, sf, sl, pos, fq, pf, fn,lenf,lens]
                                                keys.append(k)
    #keys = '\n'.join(list(keys))
    return keys

#for grep
def generateTestFrame1(key):
    TESTFRAME_PARAMS = ['PATTERN SIZE', 
                        'Number of occurrences of pattern in the file', 
                        'Number of occurrences of pattern in one line', 
                        'Presence of enclosing quotes',
                        'Presence of blanks',
                        'Position of the pattern in the file',
                        'file quality',
                        'presence of file', 
                        'filename',
 ]

    TESTFRAME = {
        'PATTERN SIZE': None,
        'Number of occurrences of pattern in the file': None,
        'Number of occurrences of pattern in one line': None,
        'Presence of enclosing quotes': None,
        'Presence of blanks': None,
        'Position of the pattern in the file': None,
        'file quality': None,
        'presence of file': None,
        'filename':None
    }

    for i in range(len(key)):
        TESTFRAME[TESTFRAME_PARAMS[i]] = key[i]

    return TESTFRAME





########################################################################
#for replace
def generateTestFrame(key):
    TESTFRAME_PARAMS = ['PATTERN SIZE', 
                        'Number of occurrences of from string in the file', 
                        'Number of occurrences of from string in one line', 
                        'Position of the from string in the file',
                        'file quantity',
                        'presence of file',
                        'file name',
                        'length of first string', 
                        'length of second string',
 ]

    TESTFRAME = {
        'PATTERN SIZE': None,
        'Number of occurrences of from string in the file': None,
        'Number of occurrences of from string in one line': None,
        'Position of the from string in the file': None,
        'file quantity': None,
        'presence of file': None,
        'file name': None,
        'length of first string': None,
        'length of second string':None
    }

    for i in range(len(key)):
        TESTFRAME[TESTFRAME_PARAMS[i]] = key[i]

    return TESTFRAME



##############################################

# for the replace command
def generateTestKeys():
    keys = []
    for size in SIZE1:
        for sf in Number_of_occurrences_of_from_string_in_the_file:
             for sl in Number_of_occurrences_of_from_string_in_one_line:
                  for pos in Position_of_the_from_string_in_the_file:
                       for fq in filequantity:
                            for pf in presence_of_file:
                                 for fn in filename:
                                      for lenf in length_first_string:
                                           for lens in length_second_string:	 
                                                k = [size, sf, sl, pos, fq, pf, fn,lenf,lens]
                                                keys.append(k)
    #keys = '\n'.join(list(keys))
    return keys


###############################################################33
#for replace
def generateCommand(IS_ERROR, key):
    if IS_ERROR:
        return 'ERROR IN TESTFRAME'
    else:
        return


if __name__ == "__main__":

    count = 1
    pairs = {
        'TESTFRAME': None,
    }
 # for replace
    if x == str(1):
        KEYSPACE = generateTestKeys()
    elif x == str(2):
 # for grep
        KEYSPACE = generateTestKeys1()
    for key in KEYSPACE:
        IS_ERROR = False
        for k in key:
            if k in errors:
                IS_ERROR = True
                break
        if x == str(1): 
        	TESTFRAME = generateTestFrame(key)
        elif x == str(2):
                TESTFRAME = generateTestFrame1(key)
        error = generateCommand(IS_ERROR,key)
        if error != 'ERROR IN TESTFRAME':
        	pairs['TESTFRAME'] = TESTFRAME
        	OUTPUT[count] = pairs
        	count += 1
    if x == str(1):
   	 with open('D3.txt', 'w') as f:
         	f.write(str(OUTPUT)+'\n')       

    elif x == str(2):
   	 with open('D3_2.txt', 'w') as f:
         	f.write(str(OUTPUT)+'\n')  	




