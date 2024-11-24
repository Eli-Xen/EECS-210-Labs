'''
Author: Eliza Malyshev 
KUID: 3122318
Date: 10/29/2024 
Lab: #8 
Purpose: takes a matrix of 0 and 1 and produces the transitive closure 
''' 
def matrixPrinter(matrix): 
    for i in matrix:
        print(i) 
    print("\n")

'''
def transClosure(matrix,n): #accidentally did algorithum 2 Warshall instead of algorithum 1 
    for i in range(n): 
        for j in range(n): 
            for k in range(n): 
                matrix[j][k]=matrix[j][k] or (matrix[j][i] and matrix[i][k])
'''
def orBandA(B,A): 
    C=[[0]*(len(B)) for i in range(len(B))] #initilizes list C nxn same as A and B wehere [0]*len(B) makes a list of n 0s 
    for i in range(len(B)): 
        for j in range(len(A)): 
            C[i][j]=B[i][j] or A[i][j]
    return C 

def matrixMult(A,matrix):
    C=[[0]*(len(A)) for i in range(len(A))] #initilizes list C nxn same as A where [0]*len(B) makes a list of n 0s 
    for i in range(len(A)):
        for j in range(len(A)): 
            for k in range(len(A)): #dot product of the i row of A and j column of matrix 
                C[i][j]+=A[i][k]*matrix[k][j] #keeps adding result for each k iteration as it goes through k row and k column 
    
    for i in range(len(C)):
        for j in range(len(C)):
            if C[i][j]>1: 
                C[i][j]=1
    return C
    
def transClosure(matrix,n): 
    A=matrix
    B=A
    for i in range(2,n):
        A=matrixMult(A, matrix) #call to do matrix multiplication 
        B=orBandA(B,A) #call to do or of matricies 
    return B 
                
        
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
    B=transClosure(matrix,n)
    print("matrix of transitive closure: ")
    matrixPrinter(B)
        
main()