# -*- coding: utf-8 -*-

import re


def replace(input):
    output = input

    output = re.sub(u'\u103a', u'\u1039', output)  # nga_tat
    output = re.sub(u'\u103b', u'\u103a', output)  # ya_pint
    output = re.sub(u'\u103c', u'\u103b', output)  # ya_yit
    output = re.sub(u'\u103d', u'\u103c', output)  # wa_swe
    output = re.sub(u'\u103e', u'\u103d', output)  # ha_toe
    output = re.sub(u'\u103f', u'\u1086', output)  # ta_gyi

    return output


def recompose(input):
    output = input

    # pr_sint
    output = re.sub(u'\u1039\u1000', u'\u1060', output)  # ka_gyi
    output = re.sub(u'\u1039\u1001', u'\u1061', output)  # ka_kway
    output = re.sub(u'\u1039\u1002', u'\u1062', output)  # ga_nge
    output = re.sub(u'\u1039\u1003', u'\u1063', output)  # ga_gyi

    return output


def logical2visual(input):
    output = input

    return output


def shape(input):
    output = input

    return output


def convert(input):
    output = input
    output = replace(output)
    output = recompose(output)
    output = logical2visual(output)
    output = shape(input)

    return output
