import os 
import time 
print("\n \U0001F600 Welcome to the Login Signup Page \U0001F600")
print("\n \n1. For Sign_up\n2. For Login")
def login_page(a):
    if a == 1:
        name=input('\n \U0001F970 Enter Your Name: ')
        e=1
        while e<=3:
            username  = input("\n \U0001F929 Enter a username: ")
            if username.isdigit():
                print("\nYou write the only integer :\n \nPlease enter valid username :") 
            else:
                password  = input("\n \U0001F61B enter a password: ")
                u,d,s = 0,0,0
                i=0
                while i<len(password):
                    if password[i].islower():
                        u+=1
                    elif password[i]=="@"or password[i]=="#":
                        s+=11
                    elif password[i].isdigit():
                        d+=1
                    i+=1
                print(u,d,s)
                if (u>=1 and d>=1 and s>=1):
                    file1 = open("lsp.txt", "a")
                    file1.write(name+':'+username+':'+password)
                    file1.close()
                    print('\n \U0001F44D You Successfully SignUp !')
                    a=int(input("2. For login:\n \n1. for back :\n \n second turn,what do you want to do? :"))
                    if a == 2:
                        f=1
                        while f<=3:
                            login1 = input("\n \U0001F49C enter the userName : ")
                            file1 = open("lsp.txt", "r")
                            fi=file1.read()
                            fil=fi.split(':')
                            if login1 == fil[1]:
                                print()
                                z=0
                                while z < 3:
                                    c=0
                                    for i in fil:
                                        password=input("\n \U0001F499Enter your password :")
                                        if password in fil:
                                            print("\n \U0001F49B Your login is succeesfully :")
                                            exit()         
                                        else:
                                            print("\nYou write the wrong password : \nPlease try again:")
                                        c+=1
                                        if c==3:
                                            os.system('cls' if os.name == 'nt' else 'clear') 
                                            second = 30
                                            for i in range (second):
                                                print(str(second-i))
                                                time.sleep(1)
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                            print("\nTime is Up")
                                    z+=1
                            elif f != 3:
                                print("\n \nYou did not write the valid user name \n \nTry again:_you have only",3-f,"more chance :")
                            else:
                                print("\n \nTry after some times :")
                            f+=1
                    else:
                        print("\n \nYou choose the back options : \n \nThanks for visit this page :")
                        exit()
                else:
                    print("\n \nYou did write the valid password :\n \n try again after some times :")
            e+=1
    if a == 2:
        f=1
        while f<=3:
            login1 = input("\n \U0001F63B enter the userName : ")
            file1 = open("lsp.txt", "r")
            fi=file1.read()
            fil=fi.split(':')
            if login1 == fil[1]:
                print()
                z=0
                while z < 3:
                    c=0
                    for i in fil:
                        password=input("\nEnter your password :")
                        if password in fil:
                            print("\n \U0001F44D Your login is succeesfully :")
                            exit()         
                        else:
                            print("\nYou write the wrong password : \nPlease try again:")
                        c+=1
                    z+=1
            elif f != 3:
                print("\n \nYou did not write the valid user name \n \nTry again:_you have only",3-f,"more chance :")
            else:
                print("\n \nTry after some times :")
            f+=1
me = int(input("\n \U0001F496  first time,What do you want to do ?...."))
login_page(me)






                 