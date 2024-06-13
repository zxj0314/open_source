import numpy as np
a = []
for x in range(2, 11):
    # print(x,int(np.sqrt(x)))
    for y in range(2, x):
        print(x,y)
        if (x % y == 0):
            break
    else:
        a.append(x)
print("素数", a)

# # 100以内的质数
# num = []
# i = 2
# for i in range(2, 100):
#     j = 2
#     for j in range(2, i):
#         if (i % j == 0):
#             break
#     else:
#         num.append(i)
# print(num)
