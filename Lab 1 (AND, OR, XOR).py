'''
Author: Eliza Malyshev 
KUID: 3122318
Date: 9/5/2024 
Lab: #1 
Purpose: take two bits in the form of string and gives output of the AND, OR, XOR of them 
''' 
import operator
    
def operate(bit1, bit2, resultList, operation): 
    #adds padding to either list incase one is longer than another; i l8r learned that we didnt have to account for this case
    if len(bit1)>len(bit2):
        bit2= [0]*(len(bit1)-len(bit2)) +bit2 #this makes [0,0,0,0]+[1,0,1,0]=[0,0,0,0,1,0,1,0]
    elif len(bit1) < len(bit2):
        bit1= [0]*(len(bit2)-len(bit1)) +bit1  
        
    #check if we need to do XOR and if so run this and return, otherwise go on to AND/OR
    if operation=="XOR": 
        for i in range(len(bit1)-1, -1, -1):  #go backwards from end to start
                resultList.append(XORlogic(bit1[i],bit2[i])) #sends off to XOR supporting function
        
        #print(list(reversed(resultList))) 
        resultList=list(reversed(resultList)) #have to make reversed since right now its backwards 
        return resultList #only returns if operation=="XOR" 
    
    
    #link operation names to actual operator functions; we dont use all of them but i want to keep for future referance 
    operations= {
        #"AND": operator.and_,
        #"OR": operator.or_,
        "ADD": operator.add,
        #"SUB": operator.sub,
        "MUL": operator.mul,
    } 
    function=operations[operation] #we chose the function earlier
    
    
    #do AND or OR depending on what we chose earlier
    for i in range(len(bit1)-1, -1, -1):  
        result=function(bit1[i], bit2[i]) #use the operation chosen earlier 
        resultList.append(result)
        
    for i in range(len(resultList)): #this accounts for when 1+1=2 since theres no 2 in binary 
        if resultList[i]==2:
            resultList[i]=1
    
    #print(list(reversed(resultList))) 
    resultList=list(reversed(resultList)) #have to make reversed since right now its backwards 
    return resultList 


def XORlogic(num1,num2): #supporting function for XOR 
    if num1==num2: 
        return 0
    else: 
        return 1


def main(): 
    bit1=input("give the first  bit: ")
    bit2=input("give the second bit: ")
    bit1=list(bit1) #convert each string to list of strings 
    bit2=list(bit2)
    #converts each list to ints 
    bit1=[int(i) for i in bit1]
    bit2=[int(i) for i in bit2]
    #print(bit1,"\n",bit2)
    
    #initalize lists for AND,OR,XOR and send parameters to operate function that will do each operation
    AND=[]
    OR=[]
    XOR=[]
    ANDed=operate(bit1,bit2,AND,"MUL")
    ORed=operate(bit1,bit2,OR,"ADD")
    XORed=operate(bit1,bit2,XOR,"XOR")
    
    print("AND:")
    print(''.join([str(i) for i in ANDed])) #join operator and between each thing we join we put nothing but we could put ',' to get 0,1,0,0 
    print("OR:")
    print(''.join([str(i) for i in ORed]))
    print('XOR:')
    print(''.join([str(i) for i in XORed]))

    
main() 