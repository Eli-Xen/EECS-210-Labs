'''
Author: Eliza Malyshev 
KUID: 3122318
Date: 10/1/2024 
Lab: #5 
Purpose: takes in two integer lists and combines them into one list ordered smallest --> largest 
''' 
def listProcessor(ints): #splits the string of ints by comma and makes a list of ints
    ints=ints.split(",")
    for i in range(len(ints)):
        ints[i]=int(ints[i])
    return ints

'''
def bubbleSort(lst):
    for n in range(len(lst)-1,0,-1): #go through list n times
        for i in range(n): #goes from start to the point we are at in the list 
            if lst[i]>lst[i+1]: #if i is greater than next thing...
                lst[i],lst[i+1]=lst[i+1],lst[i] #...swap i and its neighbor 
    return lst

def sorter(list1,list2): 
    s1=set(list1)
    s2=set(list2)
    combined=s1|s2 #union of lists, no duplicates, ORDER OF COMBINED SETS IS NOT GUARENTEED 
    #this is bad this is organized
    #l1=list(s1)
    #l2=list(s2)
    #print(l1,l2)
    combined=bubbleSort(list(combined)) #calls supportive function that does bubble sort 
    
    return combined
'''

def sorter(l1,l2): #this combines lists 1 and 2 into combined list 
    combined=[] 
    while len(l1)!=0 and len(l2)!=0: #while both are non-empty 
        print(len(l1))
        if l1[0]<l2[0]: #if value at list1 is smaller than value at list2... 
            combined.append(l1[0]) #...add value at list 1 to the right end of combined...
            l1.pop(0) #and delete that value from list1 
        elif l2[0]<l1[0]: #if value at list2 is smaller do same but other way around 
            combined.append(l2[0])
            l2.pop(0)
        elif l1[0]==l2[0]: #if fvalues are equal add either value to combined and then remove values from btoh lists 
            combined.apend(l2[0])
            l1.pop(0)
            l2.pop(0)
        else: 
            print("error")
            
        if len(l1)==0: #if list1 is empty...
            for i in range(len(l2)): #...go through list2... 
                combined.append(l2[0]) #...and put all its elements to the right of combined list 
                l2.pop(0)
        elif len(l2)==0: #if list2 is empty do same as above but with list1 
            for i in range(len(l1)): 
                combined.append(l1[0])
                l1.pop(0)
    return combined 

def main(): #takes input string, processes it, then takes value to search and does search 
    list1=input("give first list, must ints 1<=n<=32 seperated by comma: ")
    list1=listProcessor(list1)
    #print(bubbleSort(list1))
    list2=input("give second list, must ints 1<=n<=32 seperated by comma: ")
    list2=listProcessor(list2)
    print(sorter(list1,list2)) #assume both lists are sorted least-->greatest 
    
main()