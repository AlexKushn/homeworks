# -*- coding: cp1251 -*-
"""������� 5: ���������.
�������:
�������� ����, ������� ��������� ������ ����� ����� � ������������ ��� ��������� �������:
- � ������ ������ ���� �������� ����� � ������� �����������,
- ����� ���� ������ ����� � ������� ��������.
������:
[1,4,8,6,3,7,1] >> [1,1,3,7,8,6,4]"""


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



head = filter(odd, IN)
head.sort ()
tail = filter(even, IN)
tail.sort ()
tail.reverse ()
print head + tail





