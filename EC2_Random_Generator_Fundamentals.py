import random
import string

print('''
 __         __                                    
(_  _  _   /   _  _ _                             
__)(_||||  \__(_)| |_)                            
                   |                              
 __ __ __                  __                     
|_ /    _)  |\ | _  _  _  / _  _ _  _ _ _ |_ _  _ 
|__\__ /__  | \|(_||||(-  \__)(-| )(-| (_||_(_)|                                                                                                                         
      ''')
name_quantity = int(input('How many EC2 instances would you like to create names for? '))
department_name = input('What department do you work for? ')

for _ in range(name_quantity):
    random_numbers = random.randint(10000, 90000)
    instance_name = f"{department_name}-{random_numbers}"
    print(instance_name)




