import time
import copy
InitialState = []
GoalState=[]
PreState=[]
count=0
q=0
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
       
PreState = copy.deepcopy(InitialState)
 
def fun1(CurrentState):       
    for r in range(0,n):
        for c in range(0,n) : 
            if CurrentState[r][c]==0:
                return r,c
        
def con(PreState):
     if PreState in list2:
            list1.append(PreState)
            #print(PreState)     
        
list1=list()  
list1.append(PreState)

#print(list1) 
list2=list()    
list2.append(PreState)
while len(list1)!=0 and PreState!=GoalState:
    
    CurrentState=list1.pop()
    #print(CurrentState)
    r,c = fun1(CurrentState)
    #print(r,c)
    if(CurrentState == GoalState):
        print('Goal Found')
        print("No of visited nodes",count)
        print("Time in ms",(q-p))
        exit()
    
    if r>=0 and c==0:
        PreState=copy.deepcopy(CurrentState)
        PreState[r][c], PreState[r][c+1]= PreState[r][c+1], PreState[r][c]
        count=count+1
        if PreState not in list2:
                  list2.append(PreState)
                  con(PreState)
        PreState=copy.deepcopy(CurrentState)
        if r<n-1:
            PreState[r][c], PreState[r+1][c]= PreState[r+1][c], PreState[r][c]
            count=count+1
            if PreState not in list2:
                  list2.append(PreState)
                  con(PreState)
        PreState=copy.deepcopy(CurrentState)
        if r>0:
            PreState[r][c], PreState[r-1][c]= PreState[r-1][c], PreState[r][c]
            count=count+1
            if PreState not in list2:
                  list2.append(PreState)
                  con(PreState)
        
    if r>=0 and c==n-1:
        PreState=copy.deepcopy(CurrentState)
        PreState[r][c], PreState[r][c-1]= PreState[r][c-1], PreState[r][c]
        count=count+1
        if PreState not in list2:
                  list2.append(PreState)
                  con(PreState)
        PreState=copy.deepcopy(CurrentState)
        if r<n-1:
            PreState[r][c], PreState[r+1][c]= PreState[r+1][c], PreState[r][c]
            count=count+1
            if PreState not in list2:
                  list2.append(PreState)
                  con(PreState)
        PreState=copy.deepcopy(CurrentState)
        if r>0 :
            PreState[r][c], PreState[r-1][c]= PreState[r-1][c], PreState[r][c]
            count=count+1
            if PreState not in list2:
                  list2.append(PreState)
                  con(PreState)
        
        
    if c>=0 and r==0:
        PreState=copy.deepcopy(CurrentState)
        PreState[r][c],PreState[r+1][c]=PreState[r+1][c],PreState[r][c]
        count=count+1
        if PreState not in list2:
                  list2.append(PreState)
                  con(PreState)
        PreState=copy.deepcopy(CurrentState)
        if c<n-1:
            PreState[r][c], PreState[r][c+1]= PreState[r][c+1], PreState[r][c]
            count=count+1
            if PreState not in list2:
                  list2.append(PreState)
                  con(PreState)
        PreState=copy.deepcopy(CurrentState)
        if  c>0:
            PreState[r][c], PreState[r][c-1]= PreState[r][c-1], PreState[r][c]
            count=count+1
            if PreState not in list2:
                  list2.append(PreState)
                  con(PreState)
        
   
    if c>=0 and r==n-1:
        PreState=copy.deepcopy(CurrentState)
        PreState[r][c],PreState[r-1][c]=PreState[r-1][c],PreState[r][c]
        count=count+1
        if PreState not in list2:
                  list2.append(PreState)
                  con(PreState)
        PreState=copy.deepcopy(CurrentState)
        if c<n-1:
            PreState[r][c], PreState[r][c+1]= PreState[r][c+1], PreState[r][c]
            count=count+1
            if PreState not in list2:
                  list2.append(PreState)
                  con(PreState)
        PreState=copy.deepcopy(CurrentState)
        if  c>0:
            PreState[r][c], PreState[r][c-1]= PreState[r][c-1], PreState[r][c]
            count=count+1
            if PreState not in list2:
                  list2.append(PreState)
                  con(PreState)
        
        
    if c>0 and c<n-1 and r>0 and r<n-1: 
        PreState=copy.deepcopy(CurrentState)
        PreState[r][c],PreState[r][c+1]=PreState[r][c+1],PreState[r][c]
        count=count+1
        if PreState not in list2:
                  list2.append(PreState)
                  con(PreState)
        PreState=copy.deepcopy(CurrentState)
        PreState[r][c],PreState[r][c-1]=PreState[r][c-1],PreState[r][c]
        count=count+1
        if PreState not in list2:
                  list2.append(PreState)
                  con(PreState)
        PreState=copy.deepcopy(CurrentState)
        PreState[r][c],PreState[r+1][c]=PreState[r+1][c],PreState[r][c]
        count=count+1
        if PreState not in list2:
                  list2.append(PreState)
                  con(PreState)
        PreState=copy.deepcopy(CurrentState)
        PreState[r][c],PreState[r-1][c]=PreState[r-1][c],PreState[r][c]
        count=count+1
        if PreState not in list2:
                  list2.append(PreState)
                  con(PreState)
q=time.time()

    
    