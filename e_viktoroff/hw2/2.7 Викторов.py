# -*- coding: cp1251 -*-
"""������� 7: ���������.�������� (��������)
�������:
��������� ������� 5 ("���������") � �������������� ��������:
����� �������� ������ � ������ ������������ ���� ����� � ��� �� ��������, �.�.
������ ��������� ����������� ������, � �� ���������� ������.
start_list = [1,4,8,6,3,7,1]
end_list = [1,1,3,7,8,6,4]
(start_list is end_list) == True
������:
[1,4,8,6,3,7,1] is [1,1,3,7,8,6,4]"""


IN = [1,4,8,6,3,7,1]


def even(y):
    if y % 2 == 0:
        return True
    else:
        return False
def odd(y):
    if y % 2 != 0:
        return True
    else:
        return False

#������ Advenced �����:
IN.sort()
tail = []

while even(IN[-1]) == True:
    n = -1
    for i in IN:
        n += 1
        if even(i) == True:
            tail.append(IN.pop(n))
            break

tail.reverse()
IN.extend(tail)

print IN
# end
# ������ Advenced �����:
IN = [1,4,8,6,3,9,10,10,11,11,7,1]
IN.sort()
interation = None
back_position = 0
while interation != max(IN):

    front_position = -1
    for interation in IN:
        if interation == max(IN):
            break
        front_position += 1
        if even(interation) == True:

            if back_position == 0:
                IN.append(IN.pop(front_position))
                back_position -= 1
                break
            IN[back_position:back_position] = [IN.pop(front_position)]
            back_position -= 1
            break

print IN
