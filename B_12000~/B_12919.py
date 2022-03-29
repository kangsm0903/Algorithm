import sys
sys.setrecursionlimit(10**6)
S=list(map(str,sys.stdin.readline().rstrip('\n'))) # B

SLen=len(S)

T=list(map(str,sys.stdin.readline().rstrip('\n'))) # [A,B,B,A]

base=0

def step(): 
    global base
    global T

    if T[0]=='A' and T[-1]=='B':
        print(0)
        return 0
    elif T[0]!='B' and T[-1]=='A': # 맨 앞이 'B'가 아니고 맨 뒤만 'A'일 때 ABA
        del T[-1]
    elif T[0]=='B' and T[-1]!='A': # 맨 앞만 'B'이고 맨 뒤가 'A'가 아닐 때 BAB
        T.reverse()
        del T[-1]
    else: # 맨 앞이 B이고 맨 뒤가 A일 때 BAA
        if base==0:
            del T[-1]
        elif base==1:
            T.reverse()
            del T[-1]
            base=0

    if ''.join(S)==''.join(T):
        print(1)
        return
    elif len(S) == len(T):
        T.append('A')
        base=1
        step()
    else:
        step()

step()