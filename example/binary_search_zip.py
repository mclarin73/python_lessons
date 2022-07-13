# Example of binary search
# https://www.youtube.com/watch?v=JQhciTuD3E8 - good explain

def binarySearch(array:list, x:int, low:int, high:int) -> str:

    while low <= high:
        mid = low + (high - low)//2
        if array[mid] == x:
            return f'Index of {x} is {mid}'
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return 'Try again!'

arr = sorted([67, 1,2,3,4, 89, -1, 0, 57]) # список должен быть отсортирован
find_x = 67

#print(binarySearch(array = arr, x =  find_x,  low= 0 , high= len(arr) - 1))


''' 
Функция должна принять список, 
на основе этого списка создать словарь 
с видом ключ(индекс) - значение
'''
def zip_to_dict(arr:list) -> dict:
    index_arr = [i for i in range(0, len(arr))] # сохраняем индексы
    res_dict = dict()

    for i in zip(index_arr,arr): # проходим по кортежу и создаем словарь
        res_dict[i[0]] = i[1]

    return res_dict

print(zip_to_dict([-1,5,7,9,10, 12]))
print(zip_to_dict(['a', 'b', 'c', 'd', 'e', 'f', 'g']))