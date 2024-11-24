'''
Author: Eliza Malyshev 
KUID: 3122318
Date: 11/22/2024 
Lab: #11 
Purpose: impliment dijkstra's algorithum to find the shortest path between two verticies for a simple undirect graph 
''' 
import math 
def matrixPrinter(matrix): 
    for i in matrix:
        print(i) 
    print("\n")

def cheap(distance, visited): #finds neighbor with cheapest cost to traverse 
    cheapest=math.inf #assumes no cost will ever be this great  
    index=-1
    for i in range(len(distance)): 
        if i not in visited and distance[i]<cheapest: #since infinity is marked by -1 we have to do i>0 and less than current cheapest 
            cheapest=distance[i]
            index=i
    return index #returns cheapest vertex 

def neighborRec(matrix, current, visited, distance):
    for neighbor in range(len(matrix[current])):
        if neighbor not in visited and matrix[current][neighbor]>0:  #find opposite neighbor that hasnt been visited yet 
            cost=distance[current]+matrix[current][neighbor] #add current distance plus whatever cost is at neighbor 
            if distance[neighbor]==math.inf or cost<distance[neighbor]:  #if cost is infinity or cost is cheaper than current neighbors cost... 
                distance[neighbor]=cost #...make that neighbors cost the newly found cheaper cost 
            neighborRec(matrix, neighbor, visited+[neighbor], distance) #recurse to all neighbors with new visited list that has neighbor 


def circuit(matrix, startEnd): 
    distance=[] #0=a each index corresponds, holds data for cost at current verted 
    previousNode=[] #0-a each index holds data for previous node of letter 
    for i in range(len(matrix)): #fills each list with infinity 
        distance.append(math.inf)
        previousNode.append(math.inf) 
        
    distance[startEnd[0]]=0 #updates cost of starting node to be 0 
    visited=[startEnd[0]] #nodes/verticies wthat we have alrdy visited; aka path; starts with the starting num 
    
    while startEnd[1] not in visited: 
        current=visited[-1] #last one visited is current vertex were at 
        neighborRec(matrix, current, visited, distance) #recuse through neighbors and update thier costs 
        neighbor=cheap(distance, visited) #finds next neighbor with shortest disatnce/cost 
        #neighbor=cheap(matrix[visited[-1]]) #sends row of matrix of most recently visited vertex         
        if neighbor==-1: 
            break #while loop stops becuase theres no more neighbors to visit 
        visited.append(neighbor)
    return distance, visited 

def main(): 
    alphabet={
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 
    'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 
    'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 
    'w': 22, 'x': 23, 'y': 24, 'z': 25
    }
    n=int(input("enter how many rows/columns will your nxn matrix have (max is 26): "))
    matrix=[]
    print("note: if you need to enter the infinity symbol input -1 with no spaces in following format")
    for i in range(n): #takes in each row and processes it from string to list then appends to grid 
        temp=input(f"enter {i+1}th row of {n} 1s and 0s seperated only by commas: ").split(",")
        temp=[int(x) if x!='-1' else math.inf for x in temp]
        matrix.append(temp)
    
    startEnd=input('enter the starting end ending vertecies in lowercase letters seperated only by a comma in format "a,b": ').split(",")
    startEnd=[alphabet[x] for x in startEnd] #replaces letters with corresponding nums, so now startEnd is just nums 
                
    print("matrix inputted: ")
    matrixPrinter(matrix)
    cost,path=circuit(matrix,startEnd) #finds shortest path from start to end vertex 
    path=[list(alphabet.keys())[list(alphabet.values()).index(i)] for i in path]
    ''' #idk y this doesnt work but the above works ig
    for i in path: 
        for key,val in alphabet.items(): 
            if i==val: 
                path[i]=key
                
    '''
    path=" ".join(path)
    print(f"path: {path} \t cost: {cost[startEnd[1]]}")
   
main() 