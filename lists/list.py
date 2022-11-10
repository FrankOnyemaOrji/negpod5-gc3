#!/usr/bin/python3

class SumTwo:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def solution(self):
        length = len(self.a)

        for i in range(length + 1):
            for j in range(i+i, length):
                if self.a[i] + self.b[j] == self.b:
                    new_list = i, j
                    return list(new_list)
        return -1
a = [2,7,11,15]
b = 9
c = SumTwo(a, b)
print(c.solution())