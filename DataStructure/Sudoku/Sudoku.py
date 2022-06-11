import doctest
import copy

def solveSudoku2by2(sudoku):
    '''DFS, 백트래킹으로 최종 결과 값을 반환하는 함수

    전역변수 case에 sudoku의 기록들을 저장하며, empty함수로 빈 칸의 정보를,
    DFS와 백트래킹을 통해 최종 스도쿠 결과값을 반환한다.

    Args:
        sudoku(Array): 처음 문제에서 주어지는 스도쿠

    Return:
        전역변수 result[-1] 마지막 결과값을 반환한다.

    Note:
        result==None이라면 빈 칸에 들어갈 수 있는 수가 없음을 나타냄으로
        "Impossible"을 반환

    >>> solveSudoku2by2([[0,2,1,3], [0,0,0,0], [0,0,0,0], [2,1,3,0]])
    [[4, 2, 1, 3], [1, 3, 4, 2], [3, 4, 2, 1], [2, 1, 3, 4]]
    <BLANKLINE>
    tree depth, a
    <BLANKLINE>
    1, [[0, 2, 1, 3], [0, 0, 0, 0], [0, 0, 0, 0], [2, 1, 3, 0]]
    2, [[4, 2, 1, 3], [0, 0, 0, 0], [0, 0, 0, 0], [2, 1, 3, 0]]
    3, [[4, 2, 1, 3], [1, 0, 0, 0], [0, 0, 0, 0], [2, 1, 3, 0]]
    4, [[4, 2, 1, 3], [1, 3, 0, 0], [0, 0, 0, 0], [2, 1, 3, 0]]
    5, [[4, 2, 1, 3], [1, 3, 2, 0], [0, 0, 0, 0], [2, 1, 3, 0]]
    5, [[4, 2, 1, 3], [1, 3, 4, 0], [0, 0, 0, 0], [2, 1, 3, 0]]
    6, [[4, 2, 1, 3], [1, 3, 2, 4], [0, 0, 0, 0], [2, 1, 3, 0]]
    6, [[4, 2, 1, 3], [1, 3, 4, 2], [0, 0, 0, 0], [2, 1, 3, 0]]
    7, [[4, 2, 1, 3], [1, 3, 2, 4], [3, 0, 0, 0], [2, 1, 3, 0]]
    7, [[4, 2, 1, 3], [1, 3, 4, 2], [3, 0, 0, 0], [2, 1, 3, 0]]
    8, [[4, 2, 1, 3], [1, 3, 2, 4], [3, 4, 0, 0], [2, 1, 3, 0]]
    8, [[4, 2, 1, 3], [1, 3, 4, 2], [3, 4, 0, 0], [2, 1, 3, 0]]
    9, [[4, 2, 1, 3], [1, 3, 4, 2], [3, 4, 2, 0], [2, 1, 3, 0]]
    10, [[4, 2, 1, 3], [1, 3, 4, 2], [3, 4, 2, 1], [2, 1, 3, 0]]
    11, [[4, 2, 1, 3], [1, 3, 4, 2], [3, 4, 2, 1], [2, 1, 3, 4]]
    '''
    global case, blank, gamma, depth, result
    case=[] 
    blank=[] 
    result=[]
    gamma=None
    depth=1
    case.append([depth, copy.deepcopy(sudoku)]) 
    empty(sudoku)
    result=dfs(0,sudoku,depth+1) # DFS 돌림
    if result==None:
        return "Impossible"
    else:
        result.sort()
        print(result[-1][1])
        print()
        print('tree depth, a\n')
        for i in range(len(result)-1):
            print(*result[i],sep=', ')
        print(result[-1][0], end='')
        print(', ', end='')
        print(result[-1][1])
        return (result[-1][1]) # 결과값 반환


def empty(arr):
    '''스도쿠의 빈 칸의 위치를 반환하는 함수

    스도구의 빈 칸(0)의 위치 정보를 blank 리스트에 삽입하고 blank 리스트를 반환한다.

    Args:
        arr(Array): 스도쿠의 현 상태를 나타내는 리스트

    Return:
        blank(Array): 스도쿠 빈 칸의 위치 정보를 담은 리스트

    >>> empty([[0,2,1,3], [0,0,0,0], [0,0,0,0], [2,1,3,0]])
    [(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 3), (0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 3)]
    '''

    for i in range(4): 
        for k in range(4): 
            if arr[i][k]==0:
                blank.append((i,k)) # [0, 0], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3], [3, 3]
    return blank 

def is_promising(sudoku,i,j):
    '''스도쿠 빈 칸에 들어갈 수 있는 유망한 수를 걸러내는 함수
    
    스도쿠 빈 칸의 정보를 토대로 가로줄, 세로줄, 2*2 정사각형 범위 내 겹치지 않는 수가 있는지 확인한다.

    Args:
        arr(Array): 스도쿠의 현 상태를 나타내는 리스트
        i(int): 빈 칸 중 가로(행)를 나타내는 값
        j(int): 빈 칸 중 세로(열)를 나타내는 값

    Return:
        promising(Array): 빈 칸 (i,j) 위치에 들어갈 수 있는 수를 나타낸 리스트

    Note:
        빈 칸에 들어갈 수 있는 수가 없는 경우 빈 리스트가 반환된다.

    >>> is_promising([[0,2,1,3], [0,0,0,0], [0,0,0,0], [2,1,3,0]],0,0)
    [4]
    '''
    promising=[1,2,3,4]

    for k in range(4):
        if sudoku[i][k] in promising: # 행, 가로 검사
            promising.remove(sudoku[i][k])
        if sudoku[k][j] in promising: # 열, 세로 검사
            promising.remove(sudoku[k][j])

    i=i//2
    j=j//2
    for p in range(i*2, (i+1)*2): # 2*2 검사
        for q in range(j*2,(j+1)*2):
            if sudoku[p][q] in promising:
                promising.remove(sudoku[p][q])

    return promising

def dfs(count, sudoku, depth):
    '''DFS와 백트래킹을 통해 스도쿠를 채우는 함수

    blank 리스트의 첫번째 빈 칸부터 filter 함수를 통해 유망한 값을 하나씩 넣어 스도쿠 규칙에 맞는 지 봄

    Args: 
        count(int): blank 리스트의 원소에 접근하기 위한 인덱스
        sudoku(Array): 현재 스도쿠 상태

    Return:
        count==len(blank)일 때, 최종 스도쿠 결과 값을 gamma에 복사하여 반환한다.

    Note:
        83번 del case[-1]: 백트래킹으로 이전으로 돌아갈 때 맨 마지막 기록을 삭제한다. == del case[-1]
        88번 except NameError: gamma 값이 존재하지 않는다면 계속 dfs를 진행한다.
    '''
    if count == len(blank):
        global gamma
        gamma=copy.deepcopy(case) # case 자체를 복사
        return gamma
    (i,j)=blank[count]
    promise=is_promising(sudoku,i,j) # 빈 칸에 들어갈 수 있는 숫자 후보
    for num in promise:
        sudoku[i][j]=num
        case.append([depth, copy.deepcopy(sudoku)])
        dfs(count+1, sudoku, depth+1)
        # del case[-1]
        sudoku[i][j]=0
    try:
        return gamma
    except NameError:
        pass

if __name__=='__main__':
    a=[[0,3,1,2], [0,0,0,0], [0,0,0,0], [2,1,3,0]]
    print(solveSudoku2by2(a))

    doctest.testmod()

# a=[[2,3,1,4], [1,2,4,0], [3,4,0,2], [0,0,0,1]] impossible
# a=[[2,3,1,4], [1,2,3,0], [3,4,0,2], [0,0,0,1]] impossible

# a=[[0,2,1,3], [0,0,0,0], [0,0,0,0], [2,1,3,0]] possible
# a=[[0,3,1,2], [0,0,0,0], [0,0,0,0], [2,1,3,0]] possible