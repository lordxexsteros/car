class engine :
  
  def __init__(self,key = 0) :
   __engine= False
   if key == 1 :
      __engine = True
     
   if __engine == True :
       print("Car started!")


     
     

     
class car(engine) :
  
  def get_key():
   while True :
    key = int(input("Enter 1 to start the car : "))

    if key == 1 : break
    elif key != 1 : continue
    else : continue

   return key
  
  key = get_key()

  engine(key)



  
   
   
   
       
     
     
   
   

car1 = car()