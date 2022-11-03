s = input()
list1 = s.split(" ")
list2 = []
for ele in list1:
    a = int(ele)
    list2.append(a)
print(max(list2))
