print('Python lessons 3')

# Lesson 2, first var
arr = [12,34,31,12,4]

# First Var
new_arr = []
for i in arr:
    if i != 12:
        new_arr.append(i)

second_list = ['a', 'b', 'c', 'e', 'v']

# Second Var
#for i in range(0, len(arr)):
#    if arr[i] = 12:
#        arr.remove(12)

#for items in second_list:
#    print(items)

# [0:10:1]
new_list_for_ave = [3,5,8,7,12,0,1,23,-5, 56]
if len(new_list_for_ave) == 10:
    # First Variant
    counter = 0
    counter_len = 0
    for i in new_list_for_ave:
        counter += i
    for i in new_list_for_ave:
        counter_len += 1
    # Second Var
    #print(sum(new_list_for_ave)/ len(new_list_for_ave))


x = (1,2,3,4,4)
y = (5,6,7)
#x = list(x)
#x.append(6)
#x.append(True)
#print(tuple(x))

#print(x + y)
#print(x * 2)

#for i in range(0, len(x)):
#    print(x[i],i)
# [], (), {}
colors = {12, 5, 6, 12,8}  #set()
#colors.add('red')
#colors.update('wer')

#n = 24
#i = 2
#primfac = []
#while i * i <= n:
#    while n % i == 0:
#        primfac.append(i)
#        n = n / i
#    i = i + 1
#if n > 1:
#    primfac.append(n)
#print(primfac)








