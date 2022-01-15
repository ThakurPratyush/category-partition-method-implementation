# category-partition-method-implementation
CPM is a popular method in software testing methodologies used for generating test frames for maximum coverage .Here I have generated test frames for grep and replace utiity
GREP utility:

SYNTAX
grep <pattern> <filename>
pattern: sequence of characters that is to be searched
filename: file in which operation is performed

FUNCTION
Grep would search for pattern in the file whose name is specified.All the lines that have this specified pattern would be printed in the standard output.Multiple occurances taken in account for once only.
Sequence of characters form a pattern.To include blank  we use quotes(‘).Special characters are included using the (\’)

REPLACE utility:

SYNTAX
replace OPT <from> <to> -- <path-to-file/ >[<path-to-file>]*
from:  string which is getting replaced from the file.
to: string to which we would be changing.
filename: the file(s) on which replace utility is applied.
-b(backup): Backup copy of each file is created before operation.
-f(first): First found string would be replaced only.
-l(last): Only last occurrence in each file replaced.
-i(case insensitive) : Cases are not taken into account while replacing.

FUNCTION
Replace would be searching for all the <from> strings in the file and replacing them with the <to> string. Here we are using the default version of the utility .A number of files can be given as input to the system and we would be getting output in one go.





EXAMPLES
replace -b -f first second –- first.txt second.txtFirstly, a backup file would be created and then the ‘first’ word would be replaced with ‘second’ only at the first occurrence, rest not changed because of ‘-f’.  

replace -i first second –- first.txt second.txt
All the case insensitive versions of ‘first’ would be replaced with ‘second’ like FIRST , FirsT etc.

replace -f -l first second –- first.txt
Only the first and the last word would be replaced.


  
  
  
  
  
  
  
  
  
For grep command:

 Parametric conditions:
These conditions would be focusing on the pattern that is to be searched
How many times does pattern occur in the file?
How many occurrences are there in one line?
What is the positions of pattern in the file?
What is the length of the pattern?
Is there enclosing quotes present?

Environmental conditions:
Here the data file provided is the external environment so conditions related to it would be focused.
Whether the file is empty or not?
Whether the file quality provided is valid as per the utility specifications?
Whether the file exists on the system or not?


For replace command

Parametric conditions:
Includes the strings that are to be replaced that is the <for> and <to> strings
Is the string empty or not?
How many occurrences of that string are there in the file?
How many occurrences of string are there in one line?
Length of the first and second string?
Position of string in the file?

Environmental conditions:
Here the data file provided
Whether the file name provided is valid?
Whether the file quality provided is valid as per the utility specifications?
Whether the file exists on the system or not?

Partitioning each Category into Choices

The next step is to split each category into separate selections. These choices may indicate different cases that are expected to be handled differently or may indicate error-prone boundary conditions. This gives the first test specifications like this:

# Unrestricted Test Specification for grep command
Parameters:
    SIZE:
    empty
    not empty

    Number of occurrences of pattern in the file:
    None
    One
    Many

    Number of occurrences of pattern in one line:
    One
    Many

    Presence of enclosing quotes:
    Not enclosed
    Enclosed
    Incorrect
    
    Presence of blanks:
    Not enclosed 
    Enclosed
    Incorrect

    Presence of quotes withing pattern:
    None 
    One 
    Many

    Position of the pattern in the file:
    First line
    Last line
    any 
    
    Length of the pattern:
    Empty
    One
    More than one
    Longer than the file    

    File quantity:
    None
    One
    More than one

    Presence of file:
    exist
    does not exist

    filename:
    good file name 
    bad file name
    omitted


# Unrestricted Test Specification for replace command
Parameters:
    SIZE:
    empty
    not empty

    Number of occurrences of from string in the file:
    None
    One
    Many

    Number of occurrences of from string in one line:
    One
    Many

    Position of the from string in the file:
    First line
    Last line
    any 

    File quantity:
    None
    One
    More than one

    Presence of file:
    exist
    does not exist

    filename:
    good file name 
    bad file name
    omitted

    length first string:
    zero
    one
    longer than file

    length second string:
    zero
    one
    longer than file



Determining constraints among the choices and Processing Test Specification

Here we would be associating some constraints with choices , these would be limiting the number of test cases.

GREP

#Parameters:
    SIZE:
    Empty            [single][property emptyfile]                      
    not empty

    Number of occurrences of pattern in the file:
    None             [single][if !emptyfile][property noOccurances]
    One                      [if !emptyfile]
    Many		      [if !emptyfile]

    Number of occurrences of pattern in one line:
    One                      [if !noOccurances && ! emptyfile]
    Many	      [single][if !noOccurances && ! emptyfile]

    Presence of enclosing quotes:
    Not enclosed             [if !emptypattern]       
    Enclosed
    Incorrect        [error]
    
    Presence of blanks:
    Not enclosed              [if !emptypattern]
    Enclosed
    Incorrect        [error]

    Presence of quotes withing pattern:
    None 
    One                      [if !emptypattern]
    Many             [single][if! emptypattern && patternlength]

    Position of the pattern in the file:
    First line        [single][if !emptyfile]
    Last line         [single][if !emptyfile]
    any               [if !emptyfile]
 
    Length of the pattern:
    Empty            [single][property emptypattern]
    One              [single]
    More than one           [property patternlength]
    Longer than the file  [signle]

    File quantity:
    None             [error]   
    One              
    More than one     [error]

    Presence of file:
    Exist             [error]
    does not exist

    filename:
    good file name 
    bad file name     [error]
    omitted           [ommitted]


   #REPLACE


    SIZE:
    Empty            [single][property emptyfile]                      
    not empty

    Number of occurrences of from string in the file:
    None	    [single][if !emptyfile][property noOccurances]
    One             [if !emptyfile]
    Many            [if !emptyfile]

    Number of occurrences of from string in one line:
    One		       [single]   [if !emptyfile && !noOccurences]
    Many	    [if !emptyfile && !noOccurences]

    Position of the from string in the file:
    First line   [single]    [if !emptyfile && !noOccurences]
    Last line    [single]   [if !emptyfile && !noOccurences]
    any 	  [if !emptyfile && !noOccurences]

    File quantity:
    None	[error]
    One 	[single]
    More than one

    Presence of file:
    Exist             [error]
    does not exist    [single]

    filename:
    good file name 
    bad file name        [error]
    omitted

    length first string:
    zero
    one
    longer than file  [error]

    length second string:
    zero		[single]
    one
    longer than file  [single][error]
