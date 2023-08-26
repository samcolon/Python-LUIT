#Ask the user to guess the year when Python 1.0 was released (the correct answer is 1994) with the following prompt:
#When was Python 1.0 released? << remember to add a space at the end of this prompt
#If the user answers 1994, show:
#Correct!
#and finish the program. If the user answers with any year that is later than 1994, show a hint and ask again for a new year on a new line:
#It was earlier than that!
#When was Python 1.0 released? << remember to add a space
#If the user answers with any year that is earlier than 1994, show a hint and ask again for a new year on a new line:
#It was later than that!
#When was Python 1.0 released? << remember to add a space

while True:
    python_release_year = 1994
    user_input = int(input('When was Python 1.0 released? '))
    if user_input > python_release_year:
        print('It was earlier than that!')
    elif user_input < python_release_year:
        print('It was later than that!')
    else:
        print('Correct!')
        break