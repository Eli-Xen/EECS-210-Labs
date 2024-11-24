'''
Author: Eliza Malyshev 
KUID: 3122318
Date: 10/10/2024 
Lab: #7 
Purpose: print all binary number of n length that dont have two consecutive 0s 
''' 

def tempFiller(n): #makes a list filled with n 0s 
    temp=[]
    for i in range(n): 
        temp.append(0)
    return temp 

def fullCheck(temp): #returns/checks if the temp list is all ones (meaning it has reached its max bit)
    for bit in temp:
        if bit==0:
            return False  #if there are any 0s return False 
    return True #otherwise return True 

def binAdder(temp,place): #adds to binary number; if LSB (right) is 1 then it becomes 0 and adds 1 to next left 
    if place < 0:  #if we reach the beggining of the list then return 
        return temp
    if temp[place]==0: #if the place we are currently at is 0 make it a 1 
        temp[place]=1
        return temp
    else: #if its not we have to move to the next MSB and check recursivley; makes current place 0 and adds 1 to next place recursivley 
        temp[place]=0 
        return binAdder(temp,place-1)
    
def generator(bits, arr): #will create a temporary array to 
    temp=tempFiller(bits)
    while not fullCheck(temp): #while temp list is not full (aka max bit)...
        temp=binAdder(temp,len(temp)-1)
        arr.append(temp.copy()) #if not for the .copy() it would edit every referance of the temp appended 
    return arr

def main(): 
    bits=int(input("enter an integer for how many bits: "))
    arr=[]
    arr=generator(bits, arr) #array of all possible bits 
    #for i in arr: 
        #print(i)
    #print("\n")
    
    final=[]
    for binary in arr: #goes through all binary nums in array and if they have 2 consecutive 0's then remove it from list 
        consec=False    
        for j in range(len(binary)-1): #only needs to check till to before last so doesnt go out of bounds  
            if binary[j]==0 and binary[j+1]==0:
                consec=True
                break #break for loop since we found consecutive 0s 
        if not consec: #if there arent consecutive 0s 
            final.append(binary)
   
    final=[''.join(map(str,i)) for i in final] #for each list in Final it joins all integers after making them strings 
    print("bit sequences without consecutive 0s")
    final=', '.join(final) #joins all strings into one string 
    print(final)

main()
