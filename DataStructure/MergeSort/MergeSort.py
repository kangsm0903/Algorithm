def merge_sort(arr):
    if len(arr)<2: # 분할하면서 arr길이가 1이되면 return
        return arr
    
    mid=len(arr)//2
    low_arr=merge_sort(arr[:mid]) # arr의 0부터 mid까지
    high_arr=merge_sort(arr[mid:]) # arr의 mid부터 끝까지

    merged_arr=[] # 추가적인 배열
    l=h=0

    while l<len(low_arr) and h<len(high_arr):
        if low_arr[l]<high_arr[h]: # 두 개의 값을 비교해서 작은 거 먼저 넣음
            merged_arr.append(low_arr[l])
            l+=1
        else:
            merged_arr.append(high_arr[h])
            h+=1

    # low,high에 각각 n개,n+2 있다고 치면 n번 비교 후 low,high에 남은 2개를 통째로 넣음
    # 어짜피 정렬되어 있기에 바로 삽입
    merged_arr+=low_arr[l:] 
    merged_arr+=high_arr[h:]
    return merged_arr

print(merge_sort([3,1,5,2,6,7,4]))