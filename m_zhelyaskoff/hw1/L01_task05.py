# -*- coding: cp1251 -*-

# ������� 5: ����������� ����.
# �������:
# �������, ������� ��������� ������ � �������
# ������ � ������������� ���� ����� �������.
# ������:
# typer(666) == "int"
# typer("666") == "str"
# typer(typer) == "function"
# =========================================================================


print "==== Task 5: Type Definition  ===="
print "INPUT: <variable>"

def typer(arg):
    return type(arg).__name__

print "OUTPUT: "
print "666 == ", typer(666)
print "'666' == ", typer("666")
print "typer == ", typer(typer)





        
            
            













