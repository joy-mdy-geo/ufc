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


def precompose(input):
    output = input

    # pr_sint
    output = re.sub(u'\u1039\u1000', u'\u1060', output)  # ka_gyi
    output = re.sub(u'\u1039\u1001', u'\u1061', output)  # ka_kway
    output = re.sub(u'\u1039\u1002', u'\u1062', output)  # ga_nge
    output = re.sub(u'\u1039\u1003', u'\u1063', output)  # ga_gyi
    output = re.sub(u'\u1039\u1005', u'\u1065', output)  # sa_lone
    output = re.sub(u'\u1039\u1006', u'\u1066', output)  # sa_lane
    output = re.sub(u'\u1039\u1007', u'\u1068', output)  # sa_gwe
    output = re.sub(u'\u1039\u1008', u'\u1069', output)  # sa_myin_zwe
    output = re.sub(u'\u1039\u100b', u'\u106c', output)  # da_da_lin_gyake
    output = re.sub(u'\u1039\u100c', u'\u106d', output)  # ta_wen_bae
    output = re.sub(u'\u100d\u1039\u100d', u'\u106e', output)  # da_yin_guat
    output = re.sub(u'\u100d\u1039\u100e', u'\u106f', output)  # da_yin_mot
    output = re.sub(u'\u1039\u100f', u'\u1070', output)  # na_gyi
    output = re.sub(u'\u1039\u1010', u'\u1071', output)  # da_wen_bu
    output = re.sub(u'\u1039\u1011', u'\u1073', output)  # ta_sin_htoo
    output = re.sub(u'\u1039\u1012', u'\u1075', output)  # da_dway
    output = re.sub(u'\u1039\u1013', u'\u1076', output)  # da_aut_chai
    output = re.sub(u'\u1039\u1014', u'\u1077', output)  # nga_nge
    output = re.sub(u'\u1039\u1015', u'\u1078', output)  # pa_saut
    output = re.sub(u'\u1039\u1016', u'\u1079', output)  # pa_ot_top
    output = re.sub(u'\u1039\u1017', u'\u107a', output)  # ba_lat_chai
    output = re.sub(u'\u1039\u1018', u'\u107b', output)  # ba_gone
    output = re.sub(u'\u1039\u1019', u'\u107c', output)  # ma
    output = re.sub(u'\u1039\u101c', u'\u1085', output)  # la
    output = re.sub(u'\u100f\u1039\u100d', u'\u1091', output)  # ng&dg
    output = re.sub(u'\u100b\u1039\u100c', u'\u1092', output)  # ddlg&twb
    output = re.sub(u'\u100b\u1039\u100b', u'\u1097', output)  # twiceddlg
    output = re.sub(u'\u102b\u103a', u'\u105a', output)  # yaycha_shayhtoe
    outptu = re.sub(u'\u103d\u103e', u'\u108a', output)  # waswe_hatoe

    # nga_sint
    output = re.sub(u'\u102d\u1036', u'\u108e', output) 
    output = re.sub(u'\u1004\u103a\u1039', u'\u1064', output)
    output = re.sub(u'(\u1064)([\u1000-\u1021])', '\\2\\1', output)
    output = re.sub(u'\u1064([\u1000-\u1021])\u102d', u'\\1\u108b', output)
    output = re.sub(u'\u1064([\u1000-\u1021])\u102e', u'\\1\u108c', output)
    output = re.sub(u'\u1064([\u1000-\u1021])\u1036', u'\\1\u108d', output)

    return output


def logical2visual(input):
    output = input

    # 1=letters 2=yayit 3=yapint 4=waswe 5=hatoe 6=tawaetoe 7=nga_tat 8=aumyit 9=yaychar
    output = re.sub(u'([\u1000-\u1021])((?:\u103b)?)((?:\u103a)?)((?:\u103c)?)((?:\u103d)?)((?:\u1031)?)((?:\u1039)?)((?:\u1037)?)((:\u102c)?)', '\\6\\2\\1\\3\\4\\5\\7\\8\\9', output)

    return output


def shape(input):
    output = input

    # ya_yit
    output = re.sub(u'\u103b([\u1000\u1003\u1006\u100f\u1010\u1011\u1018\u101a\u101c\u101e\u101f\u1021])', u'\u107e\\1', output)  # ya_yit_agyi
    output = re.sub(u'\u103b([\u1000-\u1021])([\u102d\u102e])', u'\u107f\\1\\2', output)  # yayit with long_gyi_din(sanke)
    output = re.sub(u'\u107e([\u1000-\u1021])([\u102d\u102e])', u'\u1080\\1\\2', output)  # yayit_agi with long_gyi_din(sanke)

    # ta/na_chuang_ngin
    output = re.sub(u'([\u103b\u107e\u107f\u1080])([\u1000-\u1021])\u102f', u'\\1\\2\u1033', output)  # yayit&1cn
    output = re.sub(u'(\u103a)((?:[\u102d\u102e])?)\u102f', u'\\1\\2\u1033', output)  # yapint&1cn

    # nag_nge_apyat
    output = re.sub(u'\u1014([\u103d])', u'\u108f\\1', output)

    # aut_myit
    output = re.sub(u'([\u1014\u102f\u1030])\u1037', u'\\1\u1094', output)
    output = re.sub(u'([\u103c])\u1037', u'\\1\u1095', output)

    return output


def convert(input):
    output = input
    
    output = precompose(output)
    output = replace(output)
    output = logical2visual(output)
    output = shape(output)

    return output
