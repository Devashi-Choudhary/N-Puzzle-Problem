import copy
import heapq
import time
InitialState =[]
GoalState=[]
PreState=[]
CurrentState=[]
q=0
count=0
p=time.time()
n=int(input("Enter the order of puzzle"))
for r in range(n):
    InitialState.append([0]*n)
    for c in range(n):
        InitialState[r][c]=int(input())
m=1
for r in range(n):
    GoalState.append([0]*n)
    for c in range(n):
       GoalState[r][c]=m
       m=m+1
GoalState[n-1][n-1]=0

def find(Search,r1,c1,GoalState): 
    for r in range(n):
        for c in range(n):
            if Search==GoalState[r][c]:
                return abs(r-r1)+abs(c-c1)
def Manhathon(PreState):
    distance=0           
    for r in range(n):
        for c in range(n):
            if PreState[r][c]==0:
                continue
            else:
                distance=distance+find(PreState[r][c],r,c,GoalState)

    print(distance)
    return distance
            
#print(distance) 
PreState = copy.deepcopy(InitialState)
def fun1(CurrentState):       
    for r in range(0,n):
        for c in range(0,n) : 
            if CurrentState[r][c]==0:
                return r,c
        
def con(PreState,x):
     if PreState in list2:
            heapq.heappush(list1,(x,PreState))
            
            #print(PreState)     
list1=[]
x=Manhathon(PreState) 
heapq.heappush(list1,(x,PreState))
print(PreState)
list2=list()    
list2.append(PreState)
while len(list1)!=0 and PreState!=GoalState:
    
    heapq.heapify(list1)
    Current=heapq.heappop(list1)
    CurrentState=Current[1]
    print(CurrentState)
    r,c = fun1(CurrentState)
    print(r,c)
    if(CurrentState == GoalState):
        print('Goal Found')
        print("Number of iterations : ",count)
        print("Time required :",q-p)
        exit()
    
    
    
    if r>=0 and c==0:
        PreState=copy.deepcopy(CurrentState)
        PreState[r][c], PreState[r][c+1]= PreState[r][c+1], PreState[r][c]
        count=count+1
        if PreState not in list2:
                  x=Manhathon(PreState)
                  list2.append(PreState)
                  con(PreState,x+1)
                  
                 
        PreState=copy.deepcopy(CurrentState)
        if r<n-1:
            PreState[r][c], PreState[r+1][c]= PreState[r+1][c], PreState[r][c]
            count=count+1
            if PreState not in list2:
                  x=Manhathon(PreState)
                  list2.append(PreState)
                  con(PreState,x+1)
        PreState=copy.deepcopy(CurrentState)
        if r>0:
            PreState[r][c], PreState[r-1][c]= PreState[r-1][c], PreState[r][c]
            count=count+1
            if PreState not in list2:
                  x=Manhathon(PreState)
                  list2.append(PreState)
                  con(PreState,x+1)
        
    if r>=0 and c==n-1:
        PreState=copy.deepcopy(CurrentState)
        PreState[r][c], PreState[r][c-1]= PreState[r][c-1], PreState[r][c]
        count=count+1
        if PreState not in list2:
                  x=Manhathon(PreState)
                  list2.append(PreState)
                  con(PreState,x+1)
        PreState=copy.deepcopy(CurrentState)
        if r<n-1:
            PreState[r][c], PreState[r+1][c]= PreState[r+1][c], PreState[r][c]
            count=count+1
            if PreState not in list2:
                  x=Manhathon(PreState)
                  list2.append(PreState)
                  con(PreState,x+1)
        PreState=copy.deepcopy(CurrentState)
        if r>0 :
            PreState[r][c], PreState[r-1][c]= PreState[r-1][c], PreState[r][c]
            count=count+1
            if PreState not in list2:
                  x=Manhathon(PreState)
                  list2.append(PreState)
                  con(PreState,x+1)
        
        
    if c>=0 and r==0:
        PreState=copy.deepcopy(CurrentState)
        PreState[r][c],PreState[r+1][c]=PreState[r+1][c],PreState[r][c]
        count=count+1
        if PreState not in list2:
                  x=Manhathon(PreState)
                  list2.append(PreState)
                  con(PreState,x+1)
        PreState=copy.deepcopy(CurrentState)
        if c<n-1:
            PreState[r][c], PreState[r][c+1]= PreState[r][c+1], PreState[r][c]
            count=count+1
            if PreState not in list2:
                  x=Manhathon(PreState)
                  list2.append(PreState)
                  con(PreState,x+1)
        PreState=copy.deepcopy(CurrentState)
        if  c>0:
            PreState[r][c], PreState[r][c-1]= PreState[r][c-1], PreState[r][c]
            count=count+1
            if PreState not in list2:
                  x=Manhathon(PreState)
                  list2.append(PreState)
                  con(PreState,x+1)
        
   
    if c>=0 and r==n-1:
        PreState=copy.deepcopy(CurrentState)
        PreState[r][c],PreState[r-1][c]=PreState[r-1][c],PreState[r][c]
        count=count+1
        if PreState not in list2:
                  x=Manhathon(PreState)
                  list2.append(PreState)
                  con(PreState,x+1)
        PreState=copy.deepcopy(CurrentState)
        if c<n-1:
            PreState[r][c], PreState[r][c+1]= PreState[r][c+1], PreState[r][c]
            count=count+1
            if PreState not in list2:
                  x=Manhathon(PreState)
                  list2.append(PreState)
                  con(PreState,x+1)
        PreState=copy.deepcopy(CurrentState)
        if  c>0:
            PreState[r][c], PreState[r][c-1]= PreState[r][c-1], PreState[r][c]
            count=count+1
            if PreState not in list2:
                  x=Manhathon(PreState)
                  list2.append(PreState)
                  con(PreState,x+1)
        
        
    if c>0 and c<n-1 and r>0 and r<n-1: 
        PreState=copy.deepcopy(CurrentState)
        PreState[r][c],PreState[r][c+1]=PreState[r][c+1],PreState[r][c]
        count=count+1
        if PreState not in list2:
                  x=Manhathon(PreState)
                  list2.append(PreState)
                  con(PreState,x+1)
        PreState=copy.deepcopy(CurrentState)
        PreState[r][c],PreState[r][c-1]=PreState[r][c-1],PreState[r][c]
        count=count+1
        if PreState not in list2:
                  x=Manhathon(PreState)
                  list2.append(PreState)
                  con(PreState,x+1)
        PreState=copy.deepcopy(CurrentState)
        PreState[r][c],PreState[r+1][c]=PreState[r+1][c],PreState[r][c]
        count=count+1
        if PreState not in list2:
                  x=Manhathon(PreState)
                  list2.append(PreState)
                  con(PreState,x+1)
        PreState=copy.deepcopy(CurrentState)
        PreState[r][c],PreState[r-1][c]=PreState[r-1][c],PreState[r][c]
        count=count+1
        if PreState not in list2:
                  x=Manhathon(PreState)
                  list2.append(PreState)
                  con(PreState,x+1)
q=time.time()  

                     
