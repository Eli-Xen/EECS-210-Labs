'''
Author: Eliza Malyshev 
KUID: 3122318
Date: 9/10/2024 
Lab: #2 
Purpose: takes a pair of values, one from letters list and one from numbers list, output shows if its a function, one-to-one, and onto
''' 
def inputProcessor(pair): 
    pair=pair.strip() #if user enters a space after any of the (num,let) the Onto will be incorrectly counted 
    pair=pair.replace("(", "").replace(")", "").split(",") #calls each function seperatley to get rid of each and then split 
    #print(pair)
    return pair

def correspondence(allList, letters, nums): #process all pairs at once to check if a number goes to 2 diff letters (not function), or two nums go to same letter 
    dico={} #will correspond num and letters 
    for lst in allList: #for list in allList 
        if lst[0] in dico: #checks if num key is already in dictionary 
            raise Exception(f"not a function becuase {lst[0]} was previously mapped to a different letter element")
        else: 
            dico[lst[0]]=lst[1] #where lst[0] is num and lst[1] is letter 
        
    allValues=list(dico.values()) #makes a list of only values from dico
    #print(allValues)
    #check for one-to-one 
    one2one=None
    if len(allValues)>len(set(allValues)): #sets take only one copy of each value, if the set is smaller then there are duplicates 
        one2one=False #duplicates inducate that two values of num set are mapped to the same letter, making it not one-to-one
    elif len(allValues)==len(set(allValues)): #if there are no duplicates that means 
        one2one=True 
        
    #check for onto; all elements from letters list were used and other checks passed 
    #count=0
    onto=None #i spent 3 hours knowing i had to work 10hrs the next day, and the issue with the Onto i was having was because I forgot to put "D" in my letters list 
    for i in allValues: 
        i=i.upper() #will capitalize letter incase it isnt inputter correctly 
    uniqueLet=set(letters) #makes both of them sets so we can compare them 
    valuesSet=set(allValues) #gets rid of all duplicates that the user could have given us
    #print(uniqueLet)
    #print(valuesSet)
    if uniqueLet==valuesSet: #if the sets have the same value and length
        onto=True 
    else: 
        onto=False 
    
    return one2one,onto 


def main(): 
    letters=["A","B","C","D","E","F","G","H"]
    nums=["0","1","2","3","4","5","6","7"]
    allList=[] #this will hold all the pairs after processing 
    
    howManyPairs=int(input("how many pairs will you enter: "))
    for i in range(howManyPairs): #gets every pair that user wants to give 
        pair=input("enter pair in format (number,letter) for ranges 0-8,A-H: ")
        pairList=inputProcessor(pair) #takes pair for preprocessing and return list of two strings of num,letter 
        allList.append(pairList)
        #print(allList) 
    try: #runs something, if an exception is raised the except catches it and stops program from crashing 
    #this checks if set mapping is a function, if its not it doesnt continue and just says its not a function 
        one2one,onto=correspondence(allList, letters, nums) #function that takes all pairs and returns if it is a function and if it is a function if its one-to-one and onto
        #this return gives multiple things so i assign it to multiple variables 
        print(f"function: True \t one-to-one: {one2one} \t onto: {onto} ")
    except: 
        print("not a function becuase a num element was previously mapped to a different letter element")

main() 