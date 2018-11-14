print("Fill in the blanks!".upper())
print()
name = input('Enter a name:')
verb = input('Enter a verb:')
noun = input('Enter a noun:')

Result = "%s is going to %s the town\'s %s tomorrow!" % (name, verb, noun)
print(Result)