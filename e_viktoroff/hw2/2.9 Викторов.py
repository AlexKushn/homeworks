# -*- coding: cp1251 -*-
"""������� 9: ��������� �����������. (��������)
�������:
�������� ����, ������� ��������� ������ �������, � ������ ������ "�������" -
������������ �������� ���������� ������� �� ��������� ������.
������:
[[1],[4,8],[6,3,7],[1,3]] >> [1,4,8,6,3,7,1,3]"""

a = [[1],[4,8],[6,3,7],[1,3]]
print a,
def flat(y):
    for i in y:
        if type(i) != list:
            flat = True

        else:
            flat = False
            break
    return flat

while flat(a) != True:
    index = -1
    for i in a:
        index += 1
        if type(i) == list:
            element = a.pop(index)
            while element !=[]:
                a.insert(index, element.pop())
            break

print '>>', a