# DAY 2 
# starting from revising what i have learned yesterday 
# 1.i did not struggle on brick problem in first version

sx,sy = 0,0
tx,ty = 3,3
n= 4
solution =[[0]*n for _ in range(n)]

grid = [[0,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,1,0]]
def solve(solution,x,y):
    if x==tx and y == ty and grid[x][y]!=1:
        solution[x][y]=1
        return True
    if x<0 or y<0 or x>=n or y>=n or grid[x][y]==1:
        return False
    solution[x][y] = 1
    if solve(solution,x+1,y):
        return True
    if solve(solution,x,y+1):
        return True
    solution[x][y]=0
    return False
print(solve(solution,sx,sy))
print(solution)

# successfully coded the second version of the above problem 

sx,sy = 0,0
tx,ty = 3,3
n= 4
solution =[[0]*n for _ in range(n)]

grid = [[0,1,0,0],[0,0,1,0],[1,0,0,0],[1,1,1,0]]
def solve(solution,x,y):
    if x==tx and y == ty and grid[x][y]!=1:
        solution[x][y]=1
        return True
    if x<0 or y<0 or x>=n or y>=n or grid[x][y]==1 or solution[x][y]==1:
        return False
    solution[x][y] = 1
    if solve(solution,x+1,y):
        return True
    if solve(solution,x,y+1):
        return True
    if solve(solution,x-1,y):
        return True
    if solve(solution,x,y-1):
        return True
    solution[x][y]=0
    return False
print(solve(solution,sx,sy))
print(solution)

# 2.Print One Valid Path

sx,sy = 0,0
tx,ty = 3,3
n= 4
solution =[[0]*n for _ in range(n)]
path = []

grid = [[0,1,0,0],[0,0,1,0],[1,0,0,0],[1,1,1,0]]
def solve(solution,x,y):
    if x==tx and y == ty and grid[x][y]!=1:
        path.append([x,y])
        solution[x][y]=1
        return True
    if x<0 or y<0 or x>=n or y>=n or grid[x][y]==1 or solution[x][y]==1:
        return False
    solution[x][y] = 1
    path.append([x,y])
    if solve(solution,x+1,y):
        return True
    if solve(solution,x,y+1):
        return True
    if solve(solution,x-1,y):
        return True
    if solve(solution,x,y-1):
        return True
    solution[x][y]=0
    path.pop()
    return False
print(solve(solution,sx,sy))
print(path)
print(solution)
