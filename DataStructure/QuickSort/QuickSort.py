def quick_sort(arr):
    if len(arr)<2:
        return arr

    pivot=arr[len(arr)//2] # arr의 중간 인덱스를 pivot으로 설정
    # pivot보다 작은 거, 같은 거, 큰 거를 배열로 구분
    lesser_arr, equal_arr, greater_arr = [],[],[]
    
    for num in arr:
        if num<pivot:
            lesser_arr.append(num)
        elif num>pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
        
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)