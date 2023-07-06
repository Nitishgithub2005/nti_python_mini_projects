import random
numbers=['0','1','2','3','4','5','6','7','8','9']
letters=['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C',
         'V','B','N','M','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k',
         'l','z','x','c','v','b','n','m']
symbols=['!','@','#','$','%','^','&','*','(',')','[',']']
print('-------Welcome to password generator-------')
no_let=int(input('Enter how many letters do u want?:\n'))
no_sym=int(input('Enter how many symbols do u want?:\n'))
no_num=int(input('Enter how many numbers do u want?:\n'))
password=[]
for i in range(1,no_num+1):
   char=random.choice(numbers)  
   password+=char
for i in range(1,no_sym+1):
   char=random.choice(symbols)  
   password+=char
for i in range(1,no_let+1):
   char=random.choice(letters)  
   password+=char 
random.shuffle(password)
passs=''
for char in password:
   passs+=char
print('Here! is your password =',passs)     
