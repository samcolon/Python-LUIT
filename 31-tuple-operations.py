user_data = ('John', 'American', 1964)
print(len(user_data))

user_data = ('John', 'American', 1964)
if 'American' in user_data:
    print('This person comes from the US!')
    
user_data = ('John', 'American', 1964)
for element in user_data:
    print(element)
    
user_data = ('John', 'American', 1964) + ('teacher', 'male')
print(user_data)