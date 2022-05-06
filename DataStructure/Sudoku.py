import copy

blank=[] # graph의 빈 칸의 위치정보를 넣어줌

def solveSudoku2by2(sudoku):
    global case
    case=[]
    case.append(copy.deepcopy(sudoku))
    for i in range(4):
        for j in range(4):
            if sudoku[i][j]==0:
                blank.append((i,j))
    result=dfs(0,sudoku)
    print(result[-1])
    print()
    for i in result:
        print(i)

def is_promising(sudoku,i,j):
    promising=[1,2,3,4]

    for k in range(4):
        if sudoku[i][k] in promising: # 행, 가로 검사
            promising.remove(sudoku[i][k])
        if sudoku[k][j] in promising: # 열, 세로 검사
            promising.remove(sudoku[k][j])

    i=i//2
    j=j//2
    for p in range(i*2, (i+1)*2):
        for q in range(j*2,(j+1)*2):
            if sudoku[p][q] in promising:
                promising.remove(sudoku[p][q])

    return promising

def dfs(count, sudoku):
    if count == len(blank):
        global gamma
        gamma=copy.deepcopy(case)
        return gamma
    (i,j)=blank[count]
    promise=is_promising(sudoku,i,j) # 빈 칸에 들어갈 수 있는 숫자 후보
    for num in promise:
        sudoku[i][j]=num
        beta=copy.deepcopy(sudoku)
        case.append(beta)
        dfs(count+1, sudoku)
        sudoku[i][j]=0
    try:
        return gamma
    except NameError:
        pass

if __name__=='__main__':
    a=[[0, 2, 1, 3], [0, 0, 0, 0], [0, 0, 0, 0], [2, 1, 3, 0]]
    (solveSudoku2by2(a))