
a=10 # global

def movies(): # global
    def heros(): # local
        nameHero="ntr" #local
        ageHero=42 #local
        print(name1,"8th line")

     
       
    name1="bahubali" # local
     
    heros()   
    name2="bahubali2" # local
    
    print(name1+name2)
    # heros() 
movies() 

# heros()

# print(name1+name2)