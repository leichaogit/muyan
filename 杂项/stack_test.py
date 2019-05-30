def isValid(s):
    if not s: return True
    stack_ls = []
    hash_ls = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    for i in s:
        if i not in hash_ls:
            stack_ls.append(i)
            #     elif not stack_ls or hash_ls[i] != stack_ls.pop():
            #         return False
            # return not stack_ls
        elif not stack_ls or hash_ls[i] != stack_ls[-1]:
            return False
        stack_ls.pop()
    return not stack_ls
s = "(]"
print(isValid(s))