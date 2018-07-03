# -*- coding: utf-8 -*-
import re


def convert(input):
    
    output = input

    output = output.replace(u'\u106a', u'\u1009')
    output = re.sub(u'[\u103b\u107e\u107f\u1080\u1081\u1082\u1083\u1084]', u'\u103c', output) # ya_yit
    output = re.sub(u'\u1039', u'\u103A', output) #nga_tat

    # pr_sint
    output = re.sub(u'\u1060', u'\u1039\u1000', output) # ka_gyi
    output = re.sub(u'\u1061', u'\u1039\u1001', output) # ka_kway
    output = re.sub(u'\u1062', u'\u1039\u1002', output) # ga_nge
    output = re.sub(u'\u1063', u'\u1039\u1003', output) # ga_gyi
    output = re.sub(u'\u1065', u'\u1039\u1065', output) # sa_lone
    output = re.sub(u'[\u1066\u1067]', u'\u1039\u1066', output) # sa_lane
    output = re.sub(u'\u1068', u'\u1039\u1067', output) # sa_gwe
    output = re.sub(u'\u1069', u'\u1039\u1068', output) # sa_myin_zwe
    output = re.sub(u'\u106c', u'\u1039\u106b', output) # da_da_lin_gyake
    output = re.sub(u'\u106d', u'\u1039\u106c', output) # ta_wen_bae
    output = re.sub(u'\u106e', u'\u100d\u1039\u100d', output) # da_yin_guat
    output = re.sub(u'\u106f', u'\u100e\u1039\u100d', output) # da_yin_mot
    output = re.sub(u'\u1070', u'\u1039\u100f', output) # na_gyi
    output = re.sub(u'[\u1071\u1072]', u'\u1039\u1010', output) # da_wen_bu
    output = re.sub(u'[\u1073\u1074]', u'\u1039\u1011', output) # ta_sin_htoo
    output = re.sub(u'\u1075', u'\u1039\u1012', output) # da_dway
    output = re.sub(u'\u1076', u'\u1039\u1013', output) # da_auat_chai
    output = re.sub(u'\u1077', u'\u1039\u1014', output) # nga_nge
    output = re.sub(u'\u1078', u'\u1039\u1015', output) # pa_saut
    output = re.sub(u'\u1079', u'\u1039\u1016', output) # pa_ot_top
    output = re.sub(u'\u107a', u'\u1039\u1017', output) # ba_lat_chai
    output = re.sub(u'[\u107b\u1093', u'\u1039\u1018', output) # ba_gone
    output = re.sub(u'\u107c', u'\u1039\u1019', output) # ma
    output = re.sub(u'\u1085', u'\u1039\u101c', output) # la
    output = re.sub(u'\u1091', u'\u100f\u1039\u100d', output) # ng&dyg
    output = re.sub(u'\u1092', u'\u100a\u1039\u100b', output) # ddlg&twb
    output = re.sub(u'\u1097', u'\u100b\u1039\u100b', output) # twiceddlg

    return output
