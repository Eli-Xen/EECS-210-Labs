'''
Author: Eliza Malyshev 
KUID: 3122318
Date: 9/24/2024 
Lab: #2 
Purpose: takes a list of positive integers and does a recursive binary search 
''' 
def listProcessor(ints): #splits the string of ints by comma and makes a list of ints
    ints=ints.split(",")
    for i in range(len(ints)):
        ints[i]=int(ints[i])
    return ints

def binarySearch(bot,top,x,ints): #takes bottom and top of range we are looking in the list, takes value we want to search, and the list
    mid=(bot+top)//2 #we start at the middle index of the list 
    if ints[mid]==x: #if the index at current middle is what we are looking for...
        return mid+1 #return that index +1 since indecies start at 0 
    elif x<ints[mid] and bot<mid: #if the value we are searching for is less than the current middle value and bottom<middle indecies...
        return binarySearch(bot,mid-1,x,ints) #recurse to the smaller side of the list, so the next middle is smaller 
    elif x>ints[mid] and top>mid: #if the value we are searching is greater than current middle...
        return binarySearch(mid+1,top,x,ints) #recuse to the larger side of the list 
    else: return 0 #if we dont find value 

def main(): #takes input string, processes it, then takes value to search and does search 
    ints=input("give a list of positive inputs seperated by a comma: ")
    ints=listProcessor(ints)
    searchingFor=int(input("give an integer you want to search: "))
    top=len(ints)
    print("your value was at index: ", binarySearch(0,top,searchingFor,ints))

main()