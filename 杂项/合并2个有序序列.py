import heapq

a = [1, 4, 7, 9, 10]
b = [2, 4, 6, 8, 9]
print(sorted(a + b))

for i in heapq.merge(a, b):
    print(i, end=' ')
print()


def loop_merge_sort(l1, l2):
    tmp = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            tmp.append(l1[i])
            i += 1
        else:
            tmp.append(l2[j])
            j += 1
    tmp.extend(l1[i:])
    tmp.extend(l2[j:])
    return tmp


c = loop_merge_sort(a, b)
print(c)
