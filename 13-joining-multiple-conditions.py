user_age = int(input('what is your age? '))
user_country = (input('what is your country? '))

if user_age < 25 and user_country == 'Germany':
    print('You can apply for a German student exchange program')
else:
    print('Sorry you do not qualify')
    
    
user_country = (input('what is your country? '))

if user_age == 'Sweden' or user_country == 'Denmark' or user_country == 'Norway':
    print('You can apply for a Scandinavian student exchange program')
else:
    print('Sorry, you do not qualify')
    
user_country = (input('what is your country? '))
if not user_country == 'Germany':
    print('You are not from Germany')
else:
    print('You are from Germany')  
    
user_age = int(input('What is your age? '))
user_country = (input('what is your country? '))

if not user_country == 'Germany' and user_age < 25 or \
user_country == 'Germany' and user_age < 23:
    print('You qualify!')
else:
    print('You don\'t qualify!')
    
user_age = int(input('What is your age? '))
user_country = (input('what is your country? '))

if ((not user_country == 'Germany') and user_age < 25) or \
   (user_country == 'Germany' and user_age < 23):
    print('You qualify!')
else:
    print('You don\'t qualify!')
