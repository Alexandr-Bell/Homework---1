# получить от пользователя оценку

rate_as_str = input("оцените работу оператора от 1 до 5:")
# получить от пользователя оценку 

rate = (3)

if(rate<1):
    rate = 1

if(rate>5): 
    rate = 5

print(rate) 
# в зависимости от оценки дать обратную связь

feedback = ''
if rate == 1:
    feedback=input('расскажи почему мало')
else:
 if rate == 2:
    feedback=input('что бы лучше как нам быть?')
        
        
        
 else:
  if rate == 3:
    feedback=input('что тебе еще как нам быть?')

  else:
    if rate == 4:
       feedback=input('А уще кек нам лучше стать?')

    else:
       if rate == 5:
         feedback=input('радуемся мы!!!!')



    print(feedback)

# в зависимости от оценки дать обратную связь


    


 