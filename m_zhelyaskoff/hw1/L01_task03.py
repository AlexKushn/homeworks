# -*- coding: cp1251 -*-

# ������� 3: �������� ��������� ���������.
# �������:
# ����������� ������� ���������� ��������� ��������� "wow" � ������.
# ����: ������
# �����: ����� ��������� ��������� "wow"
# ������:
# s = "wowhatamanwowowpalehche"
# ...
# > 3
# =========================================================================


print "==== Task 3: count entries of the substring ====="
input_str = "wowhatamanwowowpalehche"
sub_str = "wow"
print "INPUT:"
print "String: " + input_str
print "SubString: " + sub_str


print "OUTPUT: "
# variant #1
entry_amount = input_str.count(sub_str)
print "variant #1: ", entry_amount, "  (See the code !)"

# � ������� ������ ������� 3 ���������.-��� ������� ��� �������
# ������ ������� 2 �������� ������� c ������� ������������

# variant #2
entry_amount = 0
for s in range(len(input_str)):
    check_str = input_str[s:s+3]
    if check_str == sub_str:
        entry_amount += 1        
print "variant #2: ", entry_amount, "  (See the code !)"
        
raw_input()            
            













