from abc import ABCMeta, abstractmethod

class MyList(object):
    __metaclass__=ABCMeta

    def len(self): # 길이 반환
        pass

    def getitem(self,j): # j인덱스 원소 반환 혹은 오류 / 항목의 값을 가져옴
        pass

    def setitem(self, val, j): # j번째에 val 값 넣기 / 항목에 값을 할당
        pass

    def insertItem(self, item, j=0): # j번째 위치에 항목 추가
        pass

    def printMyList(self): # 리스트에 있는 원소 출력
        pass
