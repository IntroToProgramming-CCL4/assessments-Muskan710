# create a glossary (dictionary) of  programming terms and use these words as keys and their meaning as values.
glossary={'Variable':'These are containers that stores data value in a program.', 
'Function':'These are named blocks of code that are designed to do one specific job.',
'Loop':'These are used when we want to execute code statemens multiple times.',
'List':'A list is an ordered set of values where each value is identified by an index.',
'Dictionary':'These are collection of key- value pairs  usedto store data',
'If statement':'Its a decision- making statement that guides a program to make decision based on specified criteria',
'String':'It is a collection of alphabets, words or other characters',
'Float':'Its a function or reusable code that converts values into floating point numbers.',
'Boolean':'It is used to test whether the result of an expression is true or false.',
'Integer':'its a whole number positive or negative number without decimals',
}
# now we have toprint each programe term and its meaning with blank line between each pair.
#we use (for) loop to iterate throught each (key-value-pairs) in 'glossary' dictionary.
for term, meaning in glossary.items():
# we will print the glossary using formatted text (f) and for blank line we use (\n)
    print(f"{term}:\n{meaning}\n")