import random
human=input(" --rock--\n --paper--\n --sciccor--\n pick your chocie: ")
list=['rock','paper','sciccor']
computer=(random.choice(list))
print(" Computer="+computer)
if human==computer:                             print('-----ITS A TIE-----')   
if human=='rock' and computer=='sciccor':       print("------YOU WON------")
elif computer=='rock' and human=='sciccor':     print('------YOU LOST------')
elif human=='sciccor' and computer=='paper':    print("------YOU WON------")
elif computer=='sciccor' and human=='paper':    print('------YOU LOST------')       
elif human=='paper' and computer=='rock':       print("------YOU WON------")
elif computer=='paper' and human=='rock':       print('------YOU LOST------')