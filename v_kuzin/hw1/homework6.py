#!/usr/bin/env python
# -*- coding: utf-8 -*-
# task 6

print '*****************************************'

print "Please, enter A: "
a=raw_input()
print "Please, enter B: "
b=raw_input()
# ������ ������
if type(a)==str or type(b)==str:
    print 'get the string', u'(�������� ������)'
elif a>b:
    print 'more', u'(������)'
elif a<b:
    print 'less', u'(������)'
else:
    print'equally', u'(�����)'
print '*****************************************'
