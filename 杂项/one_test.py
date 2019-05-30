# test_ls = [[1 for j in range(i + 1)] for i in range(10)]
# print(test_ls)
# test_ls[3][2] = 2
# print(test_ls)
a = [[1]]

b = a*3
print(b)
a[0][0] = 'hello world'
print(b)
# a = [1]
# print(id(a))
# a[0] = 2
# # print(a)
# print(id(a))