'''
Author: Eliza Malyshev 
KUID: 3122318
Date: 9/4/2024 
Lab: #1 
Purpose: take two bits in the form of string and gives output of the AND, OR, XOR of them 
''' 
#create the function that does the whole if elif for etc stuff that i copy-pasted 
#make the lists go backwards right-->left 
def operator(bit1, bit2, resultList, operation): 
    if operation=="AND": 
        #operation= *
        pass
    elif operation=="OR": 
      #operation= +
      pass
    
    if len(bit1)>len(bit2):
        bit2= [0]*(len(bit1)-len(bit2)) +bit2  #this makes [0,0,0,0]+[1,0,1,0]=[0,0,0,0,1,0,1,0]
    elif len(bit1)<len(bit2):
        bit1= [0]*(len(bit2)-len(bit1)) +bit1  
    
    #AND them now that both have the same length 
    for i in range(len(bit1)-1, -1, -1):  #go backwards from end to start
        resultList.append(bit1[i] (operation) bit2[i])  #i wanna set a variable equal to operator like var= + and var= * but that impossible 
        print(bit1[i]*bit2[i])  # Debugging output

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
    
    for i in range(len(bit1)):
        bit1[i]=int(bit1[i])
        print(type(bit1[i]))
    for i in range(len(bit2)):
        bit1[i]=int(bit2[i])
        print(type(bit2[i]))
    
    AND=[] #AND output of the two bits
    #make the lists the same length by adding extra 0s to the shorter list 
    if len(bit1)>len(bit2):
        bit2= [0]*(len(bit1)-len(bit2)) +bit2  #this makes [0,0,0,0]+[1,0,1,0]=[0,0,0,0,1,0,1,0]
    elif len(bit1)<len(bit2):
        bit1= [0]*(len(bit2)-len(bit1)) +bit1  
    
    #AND them now that both have the same length 
    for i in range(len(bit1)-1, -1, -1):  #go backwards from end to start
        AND.append(bit1[i]*bit2[i])  # Perform AND operation on each corresponding bit
        print(bit1[i]*bit2[i])  # Debugging output
    
    AND=list(reversed(AND)) #since the list is backwards we need to reverse it again 
    print(AND) #make this into a string output l8r 

    
    OR=[]
    Ocounter=0 
    if len(bit1)>len(bit2): #we need to flip the bits so that they go from right--> left not left--> right  
        for i in range(len(bit2)): #uses smaller one so it doesnt go out of range 
            OR.append(bit1[i]+bit2[i])
            Ocounter+=1
            print(bit1[i]+bit2[i])
        for i in range(Ocounter, len(bit1)): #go through whatever might be left of bit1 since its bigger 
            OR.append(bit1[i])
    elif len(bit1)==len(bit2):
        for i in range(len(bit1)):
            OR.append(bit1[i]+bit2[i])
            print(bit1[i]+bit2[i])
    elif len(bit1)<len(bit2):
        for i in range(len(bit1)):
            OR.append(bit1[i]+bit2[i])
            Ocounter+=1
            print(bit1[i]+bit2[i])
        for i in range(Ocounter, len(bit2)): #go through whatever might be left of bit2 since its bigger 
            OR.append(bit2[i])
    for i in range(len(OR)): #this accounts for when 1+1=2 since theres no 2 in binary 
        if OR[i]==2:
            OR[i]=1
    print(OR) #later make this into an output 
    
    
    XOR=[] 
    Xcounter=0 
    if len(bit1)>len(bit2): #we need to flip the bits so that they go from right--> left not left--> right  
        for i in range(len(bit2)): #uses smaller one so it doesnt go out of range 
            XOR.append(XORlogic(bit1[i],bit2[i]))
            Xcounter+=1
            print(XORlogic(bit1[i],bit2[i]))
        for i in range(Xcounter, len(bit1)): #go through whatever might be left of bit1 since its bigger 
            XOR.append(bit1[i])
    elif len(bit1)==len(bit2):
        for i in range(len(bit1)):
            XOR.append(XORlogic(bit1[i],bit2[i]))
            print(XORlogic(bit1[i],bit2[i]))
    elif len(bit1)<len(bit2):
        for i in range(len(bit1)):
            XOR.append(XORlogic(bit1[i],bit2[i]))
            Xcounter+=1
            print(XORlogic(bit1[i],bit2[i]))
        for i in range(Xcounter, len(bit2)): #go through whatever might be left of bit2 since its bigger 
            XOR.append(bit2[i])
            
    print(XOR) #later make this into an output 
    
    
    
main() 