#Note - for the purpose of this example driving age is assumed at 16 years

name = input( 'What is your name?' )
age = int(input('What is your age?'))

if age ==16:
    print ('%s, you can get your license' % name)
elif age < 16:
    print ('%s,you are too young to get your license' % name)
else:
    print ('%s,you already have your license' % name)          
