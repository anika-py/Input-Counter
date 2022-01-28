import os
from os import path

def intro():
    print("\n\t\tOpen File Using:")
    print("\t\t\t 1. File Name (NOTE: File should be in the same location as this program)")
    print("\t\t\t 2. File Location")
    print("\t\t\tNote: This counter only opens .txt files")
    print("\t\t----------------------------------------------------------------------------------")
    k=input("\t\tEnter Choice: ")
    if k=='1':
        print("\t\t=========================================================================================")
        a=input("\t\tEnter File Name: ")
        b=".txt"
        x=a+b
        if path.exists(x):
            print("\n\t\t\t---- OPENING",x,"----")
            d=open(x,'r') #opening text file
            t=d.read()
            print(choose(t))
        else:
            print("\t\t=========================================================================================")
            print("\t\tFile does not exist, Please try again")
            print("\t\t=========================================================================================")
            intro()
    elif k=='2':
        print("\t\t=========================================================================================")
        print("\n\t\tFile location can be found in properties of the text file")
        print("\t\tExample: "r"C:\Users\Name\Desktop\file.txt")
        print("\t\t=========================================================================================")
        a=input("\t\tEnter File Location: ")
        if path.exists(a):
            print("\n\t\t\t---- OPENING",a,"----\n")
            d=open(a,'r') #opening text file
            t=d.read()
            print(choose(t))
        else:
            print("\t\t=========================================================================================")
            print("\t\tFile does not exist, Please try again")
            print("\t\t=========================================================================================")
            intro()
    else:
        print("\t\t=========================================================================================")
        print("\t\tInvalid Option, Try Again")
        print("\t\t=========================================================================================")
        intro()

def choose(t):

    print("\t\t\tWhat Would You Like To Count?:")
    print("\t\t\t1. Words")
    print("\t\t\t2. Characters (numbers, special characters, alphabets)")
    print("\t\t-----------------------------------------------------------------------------------------")
    k=input("\t\tEnter Choice: ")
    if k=='1':
        word_count(t)
        
    elif k=='2':
        character(t)

    else:
        print("\n\t\tInvalid Option, Try Again")
        print("\t\t=========================================================================================\n")
        choose(t)
    

def word_count(s):    
     
    #COUNTER
    word = dict()
    words = s.split()
    y=input("\t\tEnter Word to Count: ")
    cs=input("\t\tDo you want to match case? (Y/N) ")
    
    #case-insensitve
    if cs=='n' or cs=='N':
        n=y.lower() #makes input lowercase 
        word[y]=0
        for i in words:
            m=i.lower() #makes words in text file lowercase
            
            if m==n:
                word[y] += 1
           
            else: #for string with characters
                f=[".",",","!","?","/","-","+",":",";","#","@","*","^","%","'",'"']
                lhs=["(","[","{","<"]
                rhs=[")","]","}",">"]
                for j in range (len(f)):
                    if m==n+f[j] or m==f[j]+n or m==f[j]+n+f[j]:
                        word[y] += 1
                    else: None
                for u in range (len(lhs)):
                    if m==lhs[u]+n:
                        word[y] += 1
                    elif m==n+rhs[u]:
                        word[y] += 1
                    elif m==lhs[u]+n+rhs[u]:
                        word[y] += 1
                    else:
                        None                 
                     
        print("\t\t--------------------------------------")
        print("\t\t",word) #prints word count
        
    #case-sensitive
    elif cs=='y' or cs=='Y':
        word[y]=0
        for i in words:            
            
            if i==y:
                word[y] += 1
           
            else: #for string with characters
                f=[".",",","!","?","/","-","+",":",";","#","@","*","^","%","'",'"']
                lhs=["(","[","{","<"]
                rhs=[")","]","}",">"]
                for j in range (len(f)):
                    if i==y+f[j] or i==f[j]+y or i==f[j]+y+f[j]:
                        word[y] += 1
                    else: None
                for u in range (len(lhs)):
                    if i==lhs[u]+y:
                        word[y] += 1
                    elif i==y+rhs[u]:
                        word[y] += 1
                    elif i==lhs[u]+y+rhs[u]:
                        word[y] += 1
                    else:
                        None
                        
        print("\t\t--------------------------------------")
        print("\t\t",word) #print word count

    else:
        print("Invalid Input")
        word_count(s)

    
    #function for counting more words
    def count_more():
        print("\t\t=========================================================================================")
        q1=input("\t\tWant to count more WORDS from the SAME FILE? (Y/N) ")
        if q1=='y' or q1=='Y':
            print("\t\t=========================================================================================")
            word_count(s)
        elif q1=='n' or q1=='N':
            print("\t\t=========================================================================================")
            q2=input("\t\tWant to count CHARACTERS from the SAME FILE? (Y/N) ")
            if q2=='y' or q2=='Y':
                print("\t\t=========================================================================================")
                character(s)
            elif q2=='n' or q2=='N':
                print("\t\t=========================================================================================")
                q3=input("\t\tBACK TO MAIN MENU? (Y/N) ")
                if q3=='y' or q3=='Y':
                    print("\t\t=========================================================================================")
                    welcome()
                elif q3=='n' or q3=='N':
                    print("\t\t=========================================================================================")
                    print("\t\tEXITING")
                    exit()
                else:
                    print("\n")
                    print("\t\t\t Invalid Input, Please Try Again!")
                    count_more()
            else:
                print("\n")
                print("\t\t\t Invalid Input, Please Try Again!")
                count_more()
                    
        else:
            print("\n")
            print("\t\t\tInvalid Input, Please Try Again!")
            print("\n")
            count_more()
    count_more()

def character(s):  
    #COUNTER
    word = dict()
    w = s.split()    
    ch=input("\t\tEnter Character to Count: ")
    word[ch]=0
    
    for i in range (len(w)):
        for j in range (len(w[i])):
            if len(ch)==1:
                if ch==w[i][j]:                
                    word[ch] += 1
                    
                else:
                   None
                            
            else:
                print("\t\t=========================================================================================")
                print("\t\tInvalid Input, Please Try Again")
                print("\t\t=========================================================================================")
                character(s)
            
                        
    print("\t\t",word)

    #function for counting more characters
    def count_more():
        print("\t\t=========================================================================================")
        q1=input("\t\tWant to count more CHARACTERS from the SAME FILE? (Y/N) ")
        if q1=='y' or q1=='Y':
            print("\t\t=========================================================================================")
            character(s)
        elif q1=='n' or q1=='N':
            print("\t\t=========================================================================================")
            q2=input("\t\tWant to count WORDS from the SAME FILE? (Y/N) ")
            if q2=='y' or q2=='Y':
                print("\t\t=========================================================================================")
                word_count(s)
            elif q2=='n' or q2=='N':
                q3=input("\t\tBACK TO MAIN MENU? (Y/N) ")
                if q3=='y' or q3=='Y':
                    print("\t\t=========================================================================================")
                    welcome()
                elif q3=='n' or q3=='N':
                    print("\t\t=========================================================================================")
                    exit()
                else:
                    print("\n")
                    print("\t\t\t Invalid Input, Please Try Again!")
                    count_more()
            else:
                print("\n")
                print("\t\t\t Invalid Input, Please Try Again!")
                count_more()
                    
        else:
            print("\n")
            print("\t\t\tInvalid Input, Please Try Again!")
            print("\n")
            count_more()
    count_more()


def welcome():
    print("\n\t\tDo you want to continue?")
    print("\t\t1. Yes \n\t\t2. No")
    print("\t\t------------------------")
    p=input("\t\tEnter Choice: ")
    if p=='1':
        print("\t\t=========================================================================================")
        intro()
    elif p=='2':
        exit()
    else:
        print("\n\t\t------------------------")
        print("\t\tInvalid Option, Try Again")
        print("\t\t------------------------\n")
        welcome()

print("\n\t\t\t-----------------------")
print("\t\t\tWELCOME TO STRING COUNTER")
print("\t\t\t-----------------------")            
welcome()  
    

