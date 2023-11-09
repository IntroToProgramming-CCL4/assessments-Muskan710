# create a glossary (dictionary) of 5 programming terms and use these words as keys and their meaning as values.
glossary={'Variable':'These are containers that stores data value in a programe.',
'Function':'These are named blocks of code that are designed to do one specific job.',
'Loop':'These are used when we want to execute code statemens multiple times.',
'List':'A list is an ordered set of values where each value is identified by an index.',
'Dictionary':'These are collection of key-value pairs used to store data.'
}

# now we have to print each programe term and its meaning with blank line between each pair.
#we use (for) loop to iterate throught each (key-value-pairs) in 'glossary' dictionary.
for term, meaning in glossary.items():
# we will print the glossary using formatted text (f) and for blank line we use (\n).
    print(f"{term}:\n{meaning}\n")