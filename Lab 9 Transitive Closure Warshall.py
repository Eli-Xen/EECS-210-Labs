'''
Author: Eliza Malyshev 
KUID: 3122318
Date: 11/5/2024 
Lab: #9 
Purpose: takes a matrix of 0 and 1 and produces the transitive closure 
''' 
def matrixPrinter(matrix): 
    letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    print(letters[0:5])
    for i in matrix:
        print(i) 
    print("\n")

def transClosure(matrix,n): #accidentally did algorithum 2 Warshall instead of algorithum 1 
    for i in range(n): 
        for j in range(n): 
            for k in range(n): 
                matrix[j][k]=matrix[j][k] or (matrix[j][i] and matrix[i][k])

def main(): 
    n=int(input("enter how many rows/columns will your nxn matrix have: "))
    matrix=[]
    for i in range(n): #takes in each row and processes it from string to list then appends to grid 
        temp=input(f"enter {i+1}th row of {n} 1s and 0s seperated only by commas: ")
        temp=temp.split(",")
        temp=[int(i) for i in temp]
        matrix.append(temp)
    print("matrix inputted: ")
    matrixPrinter(matrix)
    transClosure(matrix,n) #does the trans closure and changes original matrix 
    print("matrix of transitive closure: ")
    matrixPrinter(matrix) 
        
main()