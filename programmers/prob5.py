participant = ["leo","kiki","eden"]
completion = ["eden","kiki"]

def solution(participant, completion):
    for i in completion:
        participant.remove(i)
    return print(participant[0])

# 효율성 테스트에서 불합격 - for문을 한줄 코딩해볼라고 했지만 안됨

# ------------------------------------------------------------------------
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return print(list(answer)[0])

# collections.Counter 컨테이너 안에 동일한 값이 몇개 있는지 Dictionary형태로 반환
# answer = Counter({"leo":1, "kiki":1,"eden":1}) - Counter({"eden":1,"kiki":1})
# answer = Counter({"leo":1}) 

# -----------------------------------------------------------------------
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return print(answer)

# hash를 이용 -> hash란? 문자열이든, 정수형이든 주소값처럼 고유의 값을 부여함
# a = 'first' b = 'first' 일때 hash(a) == hash(b) 주소값은 -6242998364382976424식으로 복잡할테지만 그게 중요한게 아님

# 1. 코드를 설명하면 hash로 고유 주소값을 dic의 key로 이름을 value로 넣음
# 2. temp에 주소값을 int로 처리하여 계속 더해줌
# 3. completion에 완주한 선수들의 hash 고유 주소값을 temp에서 빼주면 나머지 한 사람의 주소값이 남음
# 4. 주소값의 value를 반환