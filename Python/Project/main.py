
# # class DashBoard:

# #     def __init__(self,loggedInUser):
# #         print("welcome to HDFC BANK ")
# #         print(f"welcome {i[1]} to HDFC BANK")
# from regis import Register__
# from login import Login
# while True:
#     print("choose one option from below ")
#     print("1. register ..")
#     print("2. login ..")

#     o=int(input("enter the option from above"))

#     if o == 1:
#         name_input=input("enter your name :--- ")
#         accNumber_input=input("enter your acc_number :--- ")
#         first_Bal_input=input("enter your first_balance :--- ")
#         o=Register__(name_input,accNumber_input,first_Bal_input)    # objec
#     else :
#         accNumber_input_Login=input("enter your acc_number :--- ")
#         p_Login=input("enter password here :-- ")
#         Login(accNumber_input_Login,p_Login)    



while True:
    print("1.Register")
    print("2.Login")

    o = int(input("Enter option: "))

    if o == 1:
        from regis import Register__

    elif o == 2:
        from login import Login
       