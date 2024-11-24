'''
Author: Eliza Malyshev 
KUID: 3122318
Date: 10/10/2024 
Lab: #6 
Purpose: finds the next permutation in lexocographic order 
''' 
def nextPerm(digits): #gets the next permutation of digits 
    before=len(digits)-2 #j; second to last element 
    while digits[before]>digits[before+1]: #compares two elements starting from the two last elements in the list and then moving down
        before=before-1 #until the one on left is greater than the right
    newSmall=len(digits)-1 #k; last element of list again 
    while digits[before]>digits[newSmall]: #compares the 2nd to last element to everything from last element and the before it 
        newSmall=newSmall-1 #digits at last is the smallest num greater than digits[blbeforeLast to the right of digits[beforeLast] 
    digits[before],digits[newSmall]=digits[newSmall],digits[before] #when it finds digit smaller than before last it switches them 
    right=len(digits)-1 #r; reset to get last index of list 
    left=before+1 #s; get the index of the value to the right of the current greater left 
    while right>left: #inverse/swap all values greater than pivot; so 12345-->54321 
        digits[right],digits[left]=digits[left],digits[right] 
        right=right-1
        left=left+1 
    return digits #return next permutation 
    
def main(): 
    digits=list(input("give string of 1<n<10 digits: "))
    digits=nextPerm(digits) 
    digits=''.join(digits) #make list back into strings
    print(digits)

main() 