for i in range(1, 100, 2):
    print(i, end=" ")

print()
i = 1
while i < 100:
    if i % 2 == 0:
        print(i)
    i += 1

i = 1
b = 0
while i <= 100:
    b += i
    i += 1
print(b)
