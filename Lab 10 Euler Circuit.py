'''
Author: Eliza Malyshev 
KUID: 3122318
Date: 11/17/2024 
Lab: #10 
Purpose: makes Euler circuit for a connected simple undirected graph with all verticies of even degree 
''' 
def matrixPrinter(matrix): 
    for i in matrix:
        print(i) 
    print("\n")

def findEdge(row): #goes through a given row and finds if it has an edge/1, if not returns False 
    for i,col in enumerate(row): 
        if col==1:
            return i #thing at column
    return False 

def removeEdge(matrix,row,col): #if a vertex at [row][col] has an edge but other vertex [col][row] doesnt also have an edge, get rid of edge 
    if findEdge(matrix[row]): #if its true that there is a column with an edge...
        matrix[row][col]=0 #...remove edge from both verticies 
        matrix[col][row]=0 

def circuit(matrix): 
    circuit=[0] #circuit will hold path of verticies, initiate by finding vertex row/col of a 
    while any(1 in row for row in matrix): #while there is 1 in row for any row in matrix...
        currentRow=circuit[-1] #current vertex was the last one added to circuit that had an edge 
        colEdge=findEdge(matrix[currentRow]) #finds edge attached to the most recent vertex use 
        if colEdge is False: #only happens if there are no edges left 
            break 
        #rowOfNext=findEdge(matrix[colEdge]) #finds the opposite end of edge by doing col,row instead of row,col 
        circuit.append(colEdge) #appends the opposite edge vertex, now current will look at that vertex 
        removeEdge(matrix,currentRow,colEdge) #removes edge at both verticies 
        if circuit[0]==circuit[-1]: #if starting vertex = ending vertex 
            break 
    return circuit

def main(): 
    n=int(input("enter how many rows/columns will your nxn matrix have (max is 26): "))
    matrix=[]
    for i in range(n): #takes in each row and processes it from string to list then appends to grid 
        temp=input(f"enter {i+1}th row of {n} 1s and 0s seperated only by commas: ")
        temp=temp.split(",")
        temp=[int(i) for i in temp]
        matrix.append(temp)
    print("matrix inputted: ")
    matrixPrinter(matrix)
    path=circuit(matrix) #finds euler matrix of the given matrix 
    alphabet={
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 
    'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 
    'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 
    'w': 22, 'x': 23, 'y': 24, 'z': 25
    }
    for i in path: 
        for key,val in alphabet.items(): 
            if i==val: 
                print(key)
   
main() 
    