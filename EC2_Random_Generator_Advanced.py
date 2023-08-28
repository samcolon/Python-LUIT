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
allowed_departments = ('Marketing', 'marketing', 'Accounting', 'accounting', 'FinOps', 'finops', 'Finops')
department_name = input('What department do you work for? ')

if department_name not in allowed_departments:
    print("Sorry, you are not allowed to use this EC2 name generator. Please contact I.T. for further info")
else:
    name_quantity = int(input('How many EC2 instances would you like to create names for? '))

    for _ in range(name_quantity):
        random_numbers = random.randint(100000, 900000)
        instance_name = f"{department_name}-{random_numbers}"
        print(instance_name)
   