import time

# insertion, selection, heap, merge, quick, python
res_insertion=[]
res_selection=[]
res_heap=[]
res_merge=[]
res_quick=[]
res_python=[]

def insertion_sort(arr):
    '''
    정렬 범위를 한 칸씩 늘리면서 기존 값과 비교하여 정렬하는 방식

    공간복잡도: 주어진 배열 내에서 원소들의 위치만 바꾸면 되기에 O(1)
    시간복잡도: 바깥의 반복문 O(N)-순방향, 안쪽에 값을 비교하는 반복문 O(N)-역방향 = O(N^2)

    아래의 개념과 같이 기본적으로 정렬된 부분을 스킵함으로서 부분적으로 O(N)까지도 단축가능

    [1,2,3,5]에서 4를 삽입할 때 5와 4를 비교 후 swap하고
    나머지 1,2,3은 while문 조건(arr[i-1]>arr[i])을 만족하지 않기에
    자동 스킵
    '''
    # for end in range(1,len(arr)): # 마지막 인덱스 값 end (순방향)
    #     i=end
    #     while i>0 and arr[i-1]>arr[i]: # i>0 이고 swap 조건을 만족하면
    #         arr[i-1],arr[i]=arr[i],arr[i-1] # swap 후 i-=1
    #         i-=1
    #     return arr
    # 최적화 안한 코드
    for end in range(1,len(arr)): # 마지막 인덱스 end 바깥은 순방향
        for i in range(end,0,-1): # end부터 end-1값을 비교 역방향
            if arr[i] < arr[i-1]: # end-1의 값이 더 크면 end와 swap
                arr[i], arr[i-1] = arr[i-1], arr[i]

def selection_sort(arr):
    '''
    배열에서 가장 작은 값을 넣고, 그 다음 작은 값, 그 다음 작은 값 넣어 정렬하는 방식

    공간복잡도: 주어진 배열 내에서 원소의 위치만 바꾸면 되기에 O(1)
    시간복잡도: O(N^2)
                바깥 반복문 (앞에서 마지막까지 비교할 값을 선택) O(N)
                안쪽 반복문 (비교할 값과 나머지 값을 비교하여 최솟값 갱신) O(N)
    '''
    for i in range(len(arr)-1):
        min_idx=i # 처음 최소 인덱스 번호
        for j in range(i+1, len(arr)):
            if arr[j]<arr[min_idx]: # 최솟값이 존재하면
                min_idx=j # 최솟값 idx 갱신
        arr[i], arr[min_idx]=arr[min_idx],arr[i] # swap
    return arr

def heapify(arr, n, i):
    largest=i
    l=2*i+1 # left
    r=2*i+2 # right

    if l<n and arr[i]<arr[l]:
        largest=l
    
    if r<n and arr[largest]<arr[r]:
        largest=r
    if largest !=i:
        arr[i],arr[largest] = arr[largest],arr[i] # swap
        heapify(arr,n,largest)

def heap_sort(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr,i,0)
    return arr

def merge_sort(arr):
    '''
    분할 & 정복
    배열을 재귀적으로 2개로 나눠서 배열의 원소가 1개가 될 때까지 나눔 - Merge
    그리고 다시 return할 때 값을 비교하여 정렬하며 올라감 - Conquer

    공간복잡도: 두 개의 배열을 병합할 때 병합 결과를 담아놓을 배열이 필요함 O(N)
    시간복잡도: O(NlogN)
                분할 시 1/2씩 줄어듬으로 O(logN)
                병합 시 모든 값들을 비교해야함으로 O(N)
    '''
    
    if len(arr) < 2: # 배열의 크기가 1이면 분할 중지 후 반환
        return arr
    # slice notation으로 배열 복제가 일어나 메모리 효율이 떨어짐
    mid = len(arr) // 2 # 분할할 때 가운데를 중심으로 분할 - 재귀로 접근
    low_arr = merge_sort(arr[:mid])  # idx: 0~mid가 low_arr
    high_arr = merge_sort(arr[mid:]) # idx: mid~last가 high_arr

    merged_arr = []
    l = h = 0 # l=low_arr의 idx, h=high_arr의 idx
    while l < len(low_arr) and h < len(high_arr):
        # 작은 값을 먼저 merge에 넣고 idx+=1
        if low_arr[l] < high_arr[h]: 
            merged_arr.append(low_arr[l])
            l += 1
        else: # low_arr[l] > high_arr[h] 
            merged_arr.append(high_arr[h])
            h += 1
    # 나머지 값들을 넣어줌
    merged_arr += low_arr[l:] 
    merged_arr += high_arr[h:]
    return merged_arr

def quick_sort(arr):
    '''
    pivot을 기준으로 왼쪽은 피벗보다 작은 값, 오른쪽은 모두 큰 값으로 분할을 진행한다.
    이런 방식으로 분할을 하였기에 왼쪽과 오른쪽의 원소들은 더이상 비교 안해도 된다.(파티션 내의 원소들하고만 비교)
    
    공간복잡도: 구현방법에 따라 달라지는데, 입력배열이 차지하는 메모리만을 사용하면 O(1)의 복잡도를 가질 수 있음
    시간복잡도: 
                pivot을 기준으로 이상적으로 분할되었다면 O(NlogN)까지 기대할 수 있지만
                pivot을 기준으로 한쪽으로 쏠려있다면 O(N^2)의 시간복잡도를 가진다.
    '''
    if len(arr)<=1: # 배열의 원소가 1개면 반환
        return arr

    pivot=arr[len(arr)//2] # pivot을 가운데 값으로 설정
    # 피벗을 기준으로 작은 배열, 동일 배열, 큰 배열로 구분
    lesser_arr, equal_arr, greater_arr=[],[],[]

    for num in arr:
        if num<pivot: # 피벗기준 작으면 lesser
            lesser_arr.append(num)
        elif num>pivot: # 피벗기준 크면 greater
            greater_arr.append(num)
        else: # 피벗과 같으면 equal
            equal_arr.append(num)

    # 재귀호출의 결과를 다시 크기 순으로 합침
    return quick_sort(lesser_arr)+equal_arr+quick_sort(greater_arr)

def built_in_sort(arr):
    arr.sort()
    return arr

data_files=['test1.dat','test2.dat','test3.dat','test4.dat','test5.dat']

for f in data_files:
    data_file=open("C:/Users/ksm36/Desktop/dataset/{0}".format(f),'r',)
    data=data_file.readlines() # 시부럴

    start=time.time()*1000 # 과거 시간 기록
    selection_sort(data)
    end=time.time()*1000 # 마지막
    res_selection.append(round(end-start,2)) # round 반올림해서 2자리

    start=time.time()*1000 # 과거 시간 기록
    insertion_sort(data)
    end=time.time()*1000 # 마지막
    res_insertion.append(round(end-start,2)) # round 반올림해서 2자리

    start=time.time()*1000 # 과거 시간 기록
    heap_sort(data)
    end=time.time()*1000 # 마지막
    res_heap.append(round(end-start,2)) # round 반올림해서 2자리
    
    start=time.time()*1000 # 과거 시간 기록
    merge_sort(data)
    end=time.time()*1000 # 마지막
    res_merge.append(round(end-start,2)) # round 반올림해서 2자리

    start=time.time()*1000 # 과거 시간 기록
    quick_sort(data)
    end=time.time()*1000 # 마지막
    res_quick.append(round(end-start,2)) # round 반올림해서 2자리

    start=time.time()*1000 # 과거 시간 기록
    built_in_sort(data)
    end=time.time()*1000 # 마지막
    res_python.append(round(end-start,2)) # round 반올림해서 2자리

print(f'    {"500":>17} {"1K":>10} {"5K":>11} {"10K":>13} {"100K":>12}')
print(f" selection {res_selection[0]:>10}ms {res_selection[1]:>10}ms {res_selection[2]:>10}ms {res_selection[3]:>10}ms {res_selection[4]:>10}ms")
print(f"      heap {res_heap[0]:>10}ms {res_heap[1]:>10}ms {res_heap[2]:>10}ms {res_heap[3]:>10}ms {res_heap[4]:>10}ms")
print(f" insertion {res_insertion[0]:>10}ms {res_insertion[1]:>10}ms {res_insertion[2]:>10}ms {res_insertion[3]:>10}ms {res_insertion[4]:>10}ms")
print(f"     quick {res_quick[0]:>10}ms {res_quick[1]:>10}ms {res_quick[2]:>10}ms {res_quick[3]:>10}ms {res_quick[4]:>10}ms")
print(f"     merge {res_merge[0]:>10}ms {res_merge[1]:>10}ms {res_merge[2]:>10}ms {res_merge[3]:>10}ms {res_merge[4]:>10}ms")
print(f"    python {res_python[0]:>10}ms {res_python[1]:>10}ms {res_python[2]:>10}ms {res_python[3]:>10}ms {res_python[4]:>10}ms")

data_file.close()