# -*- coding: utf-8 -*-
import re

def replace(input):
    # replace each zawgyi code point with equivalent code point in unicode
    output = input

    output = output.replace(u'\u106a', u'\u1009') # nya_lay
    output = re.sub(u'\u106b', u'\u100a', output) # nya
    output = re.sub(u'\u1090', u'\u101b', output) # ya_guat
    output = re.sub(u'\u1033', u'\u102f', output) # ta_chuang_ngin
    output = re.sub(u'\u1034', u'\u1030', output) # na_chuang_ngin
    output = re.sub(u'[\u103d\u1087]', u'\u103e', output) # ha_toe
    output = re.sub(u'\u103c', u'\u103d', output) # wa_swe
    output = re.sub(u'\u1086', u'\u103f', output) # ta_gyi
    output = re.sub(u'[\u103b\u107e\u107f\u1080\u1081\u1082\u1083\u1084]', u'\u103c', output) # ya_yit
    output = re.sub(u'[\u103a\u107d]', u'\u103b', output) # ya_pint
    output = re.sub(u'\u1039', u'\u103a', output) # nga_tat
    output = re.sub(u'\u104e', u'\u104e\u1044\u103a\u1038', output) # la_guang
    output = re.sub(u'[\u1037\u1094\u1095]', u'\u1037', output) # aut_myit
    output = re.sub(u'\u108f', u'\u1014', output) # na_nge

    return output


def decompose(input):
    # decomposed combined characters to sequenced characters
    output = input

    output = re.sub(u'\u1025(?=[\u103a\u102c])', u'\u1009', output) # nyalay_yaychar
    ## nga_sint
    output = re.sub(u'([\u1000-\u1021])\u1064', u'\u1064\\1', output)
    output = re.sub(u'([\u1000-\u1021])\u108b', u'\u1064\\1\u102d', output)
    output = re.sub(u'([\u1000-\u1021])\u108c', u'\u1064\\1\u102e', output)
    output = re.sub(u'([\u1000-\u1021])\u108d', u'\u1064\\1\u1036', output)
    output = re.sub(u'\u108e', u'\u102d\u1036', output)

    output = re.sub(u'\u1088', u'\u103e\u102f', output)  # ha_toe and ta_chuang_ngin
    output = re.sub(u'\u1089', u'\u103e\u1030', output)  # ha_toe and na_chuang_ngin
    output = re.sub(u'\u105a', u'\u102b\u103a', output)  # yaycha_shayhtoe
    output = re.sub(u'\u108a', u'\u103d\u103e', output)  # waswe_hatoe

    # pr_sint
    output = re.sub(u'\u1060', u'\u1039\u1000', output) # ka_gyi
    output = re.sub(u'\u1061', u'\u1039\u1001', output) # ka_kway
    output = re.sub(u'\u1062', u'\u1039\u1002', output) # ga_nge
    output = re.sub(u'\u1063', u'\u1039\u1003', output) # ga_gyi
    output = re.sub(u'\u1065', u'\u1039\u1005', output) # sa_lone
    output = re.sub(u'[\u1066\u1067]', u'\u1039\u1006', output) # sa_lane
    output = re.sub(u'\u1068', u'\u1039\u1007', output) # sa_gwe
    output = re.sub(u'\u1069', u'\u1039\u1008', output) # sa_myin_zwe
    output = re.sub(u'\u106c', u'\u1039\u100b', output) # da_da_lin_gyake
    output = re.sub(u'\u106d', u'\u1039\u100c', output) # ta_wen_bae
    output = re.sub(u'\u106e', u'\u100d\u1039\u100d', output) # da_yin_guat
    output = re.sub(u'\u106f', u'\u100d\u1039\u100e', output) # da_yin_mot
    output = re.sub(u'\u1070', u'\u1039\u100f', output) # na_gyi
    output = re.sub(u'[\u1071\u1072]', u'\u1039\u1010', output) # da_wen_bu
    output = re.sub(u'[\u1073\u1074]', u'\u1039\u1011', output) # ta_sin_htoo
    output = re.sub(u'\u1075', u'\u1039\u1012', output) # da_dway
    output = re.sub(u'\u1076', u'\u1039\u1013', output) # da_auat_chai
    output = re.sub(u'\u1077', u'\u1039\u1014', output) # nga_nge
    output = re.sub(u'\u1078', u'\u1039\u1015', output) # pa_saut
    output = re.sub(u'\u1079', u'\u1039\u1016', output) # pa_ot_top
    output = re.sub(u'\u107a', u'\u1039\u1017', output) # ba_lat_chai
    output = re.sub(u'[\u107b\u1093]', u'\u1039\u1018', output) # ba_gone
    output = re.sub(u'\u107c', u'\u1039\u1019', output) # ma
    output = re.sub(u'\u1085', u'\u1039\u101c', output) # la
    output = re.sub(u'\u1091', u'\u100f\u1039\u100d', output) # ng&dyg
    output = re.sub(u'\u1092', u'\u100b\u1039\u100c', output) # ddlg&twb
    output = re.sub(u'\u1097', u'\u100b\u1039\u100b', output) # twiceddlg

    return output


def visual2logical(input):
    # reorder the sequence of characters from visual to logical
    output = input
    ## 1=tawaetoe 2=yayit 3=nga_sint 4=letter 5=pr_sint 6=yapint 7=waswe 8=hatoe 9=aumyit 10=yaychar
    output = re.sub(u'((?:\u1031)?)((?:\u103c)?)((?:\u1064)?)([\u1000-\u1021])((?:\u1039[\u1000-\u1021])?)((?:\u103b)?)((?:\u103d)?)((?:\u103e)?)((?:\u1037)?)((?:\u102c)?)', '\\3\\4\\5\\2\\6\\7\\8\\1\\9\\10', output)
    ## for ta/na_chuangngin and longgyitin(sanke)
    output = re.sub(u'(\u102f)([\u102d\u102e])', '\\2\\1', output)
    output = re.sub(u'(\u1030)([\u102d\u102e])', '\\2\\1', output)

    output = re.sub(u'\u1064', u'\u1004\u103a\u1039', output)

    return output



def convert(input):
    
    output = input

    output = replace(output)
    output = decompose(output)
    output = visual2logical(output)

    return output
