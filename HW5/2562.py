a = []; max_num = 0; max_i = -1
for i in range(9):
  num = int(input())
  a.append(num)
  if i == 0:
    max_num = num
    max_i = i

for i in range(1, 9):
  if a[i] > max_num:
    max_num = a[i]
    max_i = i

print(max_num)
print(max_i+1)