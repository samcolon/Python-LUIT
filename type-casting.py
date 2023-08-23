# height is  a string and you cannot divide by a float
# height_cm = input('Height converter: enter your height in cm: ')
# print('Your height in feet is:', height_cm / 30.48 )

# you can do it this way instead:

### method 1:
height_cm = input('Height converter: enter your height in cm: ')
float_height_cm = float(height_cm)
print('Your height in feet is:', float_height_cm / 30.48 )

### method 2:
height_cm = float(input('Height converter: enter your height in cm: '))
print('Your height in feet is:', height_cm / 30.48 )

# using integers
year_born = int(input('What year were you born?'))
print('In 2100, you will be', 2100 - year_born, 'years old, provided you live this long!')

# using strings
temp_c = input('Enter the temperature today in Celsius degrees: ')
temp_f = float(temp_c) * 1.8 + 32
temp_statement = str(temp_c) + ' degrees Celsius equal ' + str(temp_f) + ' degrees Fahrenheit.'
print(temp_statement)

