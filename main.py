# 1 -misol
for i in range(1, 51):
    if i % 7 == 0:
        break
print(i)

# 2 - misol
for i in range(100, 151):
    if i == 137:
        print("Parolni toping:", {i})
        break

# 3
sum = 0
for i in range(1, 10):
    sum += i
    if sum >= 20:
        break
print(sum)

# 4
kop = 1
for i in range(1, 21):
    kop *= i
    if kop >= 10000:
        break
print(kop)
