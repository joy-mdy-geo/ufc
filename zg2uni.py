# -*- coding: utf-8 -*-
import re


def convert(input):
    
    output = input

    output = output.replace(u'\u106a', u'\u1009')
    output = re.sub(u'[\u103b\u107e\u107f\u1080\u1081\u1082\u1083\u1084]', u'\u103c', output) # ya_yit
    output = re.sub(u'\u1039', u'\u103A', output) #nga_tat

    return output
