from random import random

glob = True
coint = 100 #удалить
random_n = '380673451018'
tel = []
index = ["38067","38098","38093","38063"]



while coint > 0:
    tel.append(random_n)
    for z in range(1):
        n = str(int(random ()* 10))
        if coint >=75 :
            random_n = index [0] + n
            for z in range(6):
                n = str(int(random ()* 10))
                random_n += n
        elif coint >=50 and coint <=75 :
            random_n = index [1] + n
            for z in range(6):
                n = str(int(random ()* 10))
                random_n += n
        elif coint >=25 and coint <=50 :
            random_n = index [2] + n
            for z in range(6):
                n = str(int(random ()* 10))
                random_n += n
        elif coint >=0 and coint <=25 :
             random_n = index [3] + n
             for z in range(6):
                 n = str(int(random ()* 10))
                 random_n += n
        
      
                
    coint -=1
while glob:
    new_list = []
    k = 0
    new = input()

    if new == "stop":
        glob = False
        
    for i in tel:
      if i.startswith(new):
          new_list.append(i)
          k += 1
          if k == 10:
              break
     
    print(new_list)
    
    



