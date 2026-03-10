# marks=int(input("enter your marks"))

# if marks>92: # if 93>92:
#     print("A+")
# elif marks >81 and marks <=92 :
#     print("A")
# elif marks >71 and marks <=81  :
#     print("B+")
# else:
#     print("you got marks less than 71")         


# hotstar example

# name="ravi"
# print(f"welocome {name}")

# hotstar example :-- 

quality=input("enter the quality number 1.generalUser 2.premiumUser 3.goldUser 4.platinumUser :--      ") # "3"

if quality == "1":# "3" == "1"
    tMovies=["chirutha","temper","gg","nnn"]
    print("watch old telugu movies",tMovies)
elif quality == "2": # "3" == "2"
    cricketVisibility=True
    movies=["bahubali 1 ","bahubali 2","rrr"] 
    print(f"you can watch cricket along with these movies {movies}") #formatting str     str :-- varibles use   
elif quality == "3": # "3" == "3"
    cricketVisibility=True
    moviesT=["bahubali 1 ","bahubali 2","rrr"] 
    moviesH=["jawan","abcd-2","abcd"] 
    print(f"you can watch cricket along with telugu movies {moviesT} and hindi movies also {moviesH}") 
else:
    print("access all content")    

