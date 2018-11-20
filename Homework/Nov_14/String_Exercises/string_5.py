string = input("Enter text: ")

long_vowels = ['aa', 'ee', 'ii', 'oo', 'uu', 'yy']

result = ''
for i in range(len(string)):
        two_letters = string[i:i+2]
        if two_letters in long_vowels:
                result += string(i) * 4
        else:
                result += string(i)



print(string)

