# -*- coding: utf-8 -*-

import re


def replace(input):
    output = input

    output = re.sub(u'\u1000', u'\u0075', output)  # ka_gyi
    output = re.sub(u'\u1001', u'\u0063', output)  # ka_kway
    output = re.sub(u'\u1002', u'\u002a', output)  # ga_nge
    output = re.sub(u'\u1003', u'\u0043', output)  # ga_gyi
    output = re.sub(u'\u1004', u'\u0069', output)  # nga
    output = re.sub(u'\u1005', u'\u0070', output)  # sa_lone
    output = re.sub(u'\u1006', u'\u0071', output)  # sa_lane
    output = re.sub(u'\u1007', u'\u005a', output)  # za_gwe
    output = re.sub(u'\u1009', u'\u00da', output)  # nya_shay
    output = re.sub(u'\u100a', u'\u006e', output)  # nya
    output = re.sub(u'\u100b', u'\u0023', output)  # tata_lin_gyake
    output = re.sub(u'\u100c', u'\u005b', output)  # ta_wen_bae
    output = re.sub(u'\u100d', u'\u0021', output)  # da_yin_guat
    output = re.sub(u'\u100e', u'\u00a1', output)  # da_yin_mot
    output = re.sub(u'\u100f', u'\u0050', output)  # na_gyi
    output = re.sub(u'\u1010', u'\u0077', output)  # da_wen_bu
    output = re.sub(u'\u1011', u'\u0078', output)  # ta_sin_too
    output = re.sub(u'\u1012', u'\u0027', output)  # da_dway
    output = re.sub(u'\u1013', u'\u0022', output)  # da_aut_chai
    output = re.sub(u'\u1014', u'\u0065', output)  # na_nge
    output = re.sub(u'\u1015', u'\u0079', output)  # pa_saut
    output = re.sub(u'\u1016', u'\u007a', output)  # pa_oo_htoke
    output = re.sub(u'\u1017', u'\u0041', output)  # ba_lat_chai
    output = re.sub(u'\u1018', u'\u0062', output)  # ba_gone
    output = re.sub(u'\u1019', u'\u0072', output)  # ma
    output = re.sub(u'\u101a', u'\u002c', output)  # ya_pat_lat
    output = re.sub(u'\u101b', u'\u0026', output)  # ya_gaut
    output = re.sub(u'\u101c', u'\u0076', output)  # la
    output = re.sub(u'\u101d', u'\u0030', output)  # wa
    output = re.sub(u'\u101e', u'\u006f', output)  # ta
    output = re.sub(u'\u101f', u'\u005b', output)  # ha
    output = re.sub(u'\u1020', u'\u0056', output)  # la_gyi
    output = re.sub(u'\u1021', u'\u0074', output)  # aa
    output = re.sub(u'\u1023', u'\u00a3', output)  # 2kagyi
    output = re.sub(u'\u1024', u'\u00fe', output)  # II
    output = re.sub(u'\u1025', u'\u004f', output)  # oo
    output = re.sub(u'\u1027', u'\u007b', output)  # at_kayar_aa
    output = re.sub(u'\u102b', u'\u0067', output)  # yaychar_ashay
    output = re.sub(u'\u102c', u'\u006d', output)  # yaychar
    output = re.sub(u'\u102d', u'\u0064', output)  # long_gyi_tin
    output = re.sub(u'\u102e', u'\u0044', output)  # long_gyi_tin_sanke
    output = re.sub(u'\u102f', u'\u004b', output)  # 1_chuang_ngin
    output = re.sub(u'\u1030', u'\u004c', output)  # 2_chuang_ngin
    output = re.sub(u'\u1031', u'\u0061', output)  # ta_wai_toe
    output = re.sub(u'\u1032', u'\u004a', output)  # naut_htoe_pyit
    output = re.sub(u'\u1036', u'\u0048', output)  # tay_tay_tin
    output = re.sub(u'\u1037', u'\u0068', output)  # aut_myit
    output = re.sub(u'\u1038', u'\u003b', output)  # wa_sa_paut
    output = re.sub(u'\u103a', u'\u0066', output)  # nga_tat
    output = re.sub(u'\u103b', u'\u0073', output)  # ya_pint
    output = re.sub(u'\u103c', u'\u006a', output)  # ya_yit
    output = re.sub(u'\u103d', u'\u0047', output)  # wa_swe
    output = re.sub(u'\u103e', u'\u0053', output)  # ha_toe
    output = re.sub(u'\u103f', u'\u00f3', output)  # ta_gyi
    output = re.sub(u'\u1040', u'\u0030', output)  # 0
    output = re.sub(u'\u1041', u'\u0031', output)  # 1
    output = re.sub(u'\u1042', u'\u0032', output)  # 2
    output = re.sub(u'\u1043', u'\u0033', output)  # 3
    output = re.sub(u'\u1044', u'\u0034', output)  # 4
    output = re.sub(u'\u1045', u'\u0035', output)  # 5
    output = re.sub(u'\u1046', u'\u0036', output)  # 6
    output = re.sub(u'\u1047', u'\u0037', output)  # 7
    output = re.sub(u'\u1048', u'\u0038', output)  # 8
    output = re.sub(u'\u1049', u'\u0039', output)  # 9
    output = re.sub(u'\u104a', u'\u003f', output)  # pot_kalay
    output = re.sub(u'\u104b', u'\u002f', output)  # pot_ma
    output = re.sub(u'\u104c', u'\u00fc', output)  # nai
    output = re.sub(u'\u104d', u'\u00ed', output)  # yue
    output = re.sub(u'\u104e', u'\u00a4', output)  # la_guang
    output = output.replace(u'\u104f', u'\u005c')  # at_kayar_ee

    return output


def precompose(input):
    output = input

    output = re.sub(u'\u1008', u'\u0070\u0073', output)  # za_myin_zwe
    output = re.sub(u'\u1026', u'\u004f\u0044', output)  # oo_with_longgyitinsanke
    output = re.sub(u'\u1029', u'\u006a\u006f', output)  # aww
    output = re.sub(u'\u102a', u'\u0061\u006a\u006f\u006d\u006f', output)  # aww_with_tawaetoe
    output = re.sub(u'\u0075\u0073\u0079\u0066', u'\u0024', output)  # kyat
    output = re.sub(u'\u0067\u0066', u'\u003a', output)  # yaychar_shayhtoe
    output = re.sub(u'\u007e\u0047', u'\u003c', output)  # yayit_agyi_with_waswe
    output = re.sub(u'\u0060\u0047', u'\u003e', output)  # yayit_with_waswe
    output = re.sub(u'\u0050\u1039\u0021', u'\u0040', output)  # nagyi_dayinguat
    output = re.sub(u'\u0053\u006b', u'\u0049', output)  # hatoe_1cn
    output = re.sub(u'\u0073\u0053', u'\u0051', output)  # yapint_hatoe
    output = re.sub(u'\u0073\u0047', u'\u0052', output)  # yapint_waswe
    output = re.sub(u'\u0047\u0053', u'\u0054', output)  # waswe_hatoe
    output = re.sub(u'\u0073\u0054', u'\u0057', output)  # yapint_waswe_hatoe
    output = re.sub(u'\u0053\u006c', u'\u00aa', output)  # hatoe_2cn
    output = re.sub(u'\u00da\u006d', u'\u00d3', output)  # nya_yaychar

    # pr_sint
    output = re.sub(u'\u0023\u1039\u0023', u'\u00a5', output)  # twice_ttlg
    output = re.sub(u'\u1039\u0043', u'\u00a2', output)  # gagyi
    output = re.sub(u'\u1039\u0078', u'\u00a6', output)  # ta_sin_too
    output = re.sub(u'\u1039\u0022', u'\u00a8', output)  # da_aut_chait
    output = re.sub(u'\u1039\u0063', u'\u00a9', output)  # ka_kway
    output = re.sub(u'\u1039\u0072', u'\u00ae', output)  # ma
    output = re.sub(u'\u1039\u0058', u'\u00b2', output)  # ta_wen_bae
    output = re.sub(u'\u1039\u0023', u'\u00b3', output)  # ddlg
    output = re.sub(u'\u1039\u0027', u'\u00b4', output)  # da_dway
    output = re.sub(u'\u0021\u1039\u00a1', u'\u00b9', output)  # dyg_dym
    output = output.replace(u'\u1039\u002a', u'\u00b3')  # ga_nge
    output = re.sub(u'\u1039\u0041', u'\u00c1', output)  # ba_lat_chai
    output = re.sub(u'\u1039\u0077', u'\u00c5', output)  # da_wen_bu
    output = re.sub(u'\u1039\u005a', u'\u00c6', output)  # za_gwe
    output = re.sub(u'\u1039\u0062', u'\u00c7', output)  # ba_gone
    output = re.sub(u'\u1039\u0077\u0047', u'\u00c9', output)  # dwa
    output = re.sub(u'\u1039\u0070\u0073', u'\u00d1', output)  # za_myin_zwe
    output = re.sub(u'\u1039\u0050', u'\u00d6', output)  # na_gyi
    output = re.sub(u'\u0021\u1039\u0021', u'\u00d7', output)  # twice_dyg
    output = re.sub(u'\u1039\u0079', u'\u00dc', output)  # pa_saut
    output = re.sub(u'\u1039\u0071', u'\u00e4', output)  # sa_lane
    output = re.sub(u'\u1039\u007a', u'\u00e6', output)  # pa_oo_htoke
    output = re.sub(u'\u1039\u0065', u'\u00e9', output)  # na_nge
    output = re.sub(u'\u1039\u0070', u'\u00f6', output)  # sa_lone
    output = re.sub(u'\u1039\u0075', u'\u00fa', output)  # ka_gyi
    output = re.sub(u'\u1039\u0076', u'\u2019', output)  # la

    return output


def logical2visual(input):
    output = input

    # 1=letters 2=yayit 3=yapint 4=waswe 5=hatoe 6=tawaetoe 7=nga_tat 8=aumyit 19=yaychar
    output = re.sub(u'([\u1000-\u1021])((?:\u103c)?)((?:\u103b)?)((?:\u103d)?)((?:\u103e)?)((?:\u1031)?)((?:\u103a)?)((?:\u1037)?)((:\u102c)?)','\\6\\2\\1\\3\\4\\5\\7\\8\\9', output)

    # ngatat and wasapaut
    output = re.sub(u'\u1038\u1039', u'\u1039\u1038', output)

    # nga_sint
    output = re.sub(u'\u102d\u1036\u1039', u'\u00f0', output)
    output = re.sub(u'\u1004\u103a\u1039', u'\u0046', output)  # normal
    output = re.sub(u'(\u0046)([\u1000-\u1021])', '\\2\\1', output)
    output = re.sub(u'([\u1000-\u1021])\u0046\u102d', u'\\1\u00d8', output)  # with_longyitin
    output = re.sub(u'([\u1000-\u1021])\u0046\u102e', u'\\1\u00d0', output)  # with_longgyitinsanke
    output = re.sub(u'([\u1000-\u1021])\u0046\u1036', u'\\1\u00f8', output)  # with_taytaytin

    return output


def shape(input):
    output = input

    # ya_yit
    output = re.sub(u'\u103c([\u1000\u1003\u1006\u100f\u1010\u1011\u1018\u101a\u101c\u101e\u101f\u1021])', u'\u004d\\1', output)  # ya_yit_agyi
    output = re.sub(u'\u103c([\u1000-\u1021])([\u102d\u102e\u1036])', u'\u004e\\1\\2', output)  # yayit with long_gyi_din(sanke)
    output = re.sub(u'\u004d([\u1000-\u1021])([\u102d\u102e\u1036])', u'\u0042\\1\\2', output)  # yayit_agi with long_gyi_din(sanke)
    output = re.sub(u'\u103c([\u1000-\u1021])(\u103d)', u'\u0060\\1\\2', output)  # yayit with waswe
    output = re.sub(u'\u004d([\u1000-\u1021])(\u103d)', u'\u007e\\1\\2', output)  # yayit_agyi with waswe

    # ta/na_chuang_ngin
    output = re.sub(u'([\u1000-\u1007])((?:[\u102d\u102e])?)((?:\u103e)?)\u102f', u'\\1\\2\\3\u006b', output)  # 1cn with some letters
    output = re.sub(u'([\u1009-\u100b])((?:[\u102d\u102e])?)((?:\u103e)?)\u102f', u'\\1\\2\\3\u006b', output)  # 1cn with some letters
    output = re.sub(u'([\u100e-\u101f])((?:[\u102d\u102e])?)((?:\u103e)?)\u102f', u'\\1\\2\\3\u006b', output)  # 1cn with some letters
    output = re.sub(u'(\u1021)((?:[\u102d\u102e])?)((?:\u103e)?)\u102f', u'\\1\\2\\3\u006b', output)  # 1cn with some letters
    output = re.sub(u'([\u1000-\u1007])((?:[\u102d\u102e])?)((?:\u103e)?)\u1030', u'\\1\\2\\3\u006c', output)  # 2cn with some letters
    output = re.sub(u'([\u1009-\u100b])((?:[\u102d\u102e])?)((?:\u103e)?)\u1030', u'\\1\\2\\3\u006c', output)  # 2cn with some letters
    output = re.sub(u'([\u100e-\u101f])((?:[\u102d\u102e])?)((?:\u103e)?)\u1030', u'\\1\\2\\3\u006c', output)  # 2cn with some letters
    output = re.sub(u'(\u1021)((?:[\u102d\u102e])?)((?:\u103e)?)\u1030', u'\\1\\2\\3\u006c', output)  # 2cn with some letters
    output = re.sub(u'\u004d([\u1000-\u1021])\u006b', u'\u00ea\\1', output)  # yayit_agyi_with_1cn
    output = re.sub(u'\u103c([\u1000-\u1021])\u006b', u'\u00fb\\1', output)  # yayit_with_1cn
    output = re.sub(u'([\u006a\u0042\u004d\u004e\u0060])([\u1000-\u1021])((?:[\u102d\u102e])?)((?:\u0047)?)\u006b', u'\\1\\2\\3\\4\u004b', output)  # 1cn
    output = re.sub(u'([\u006a\u0042\u004d\u004e\u0060])([\u1000-\u1021])((?:[\u102d\u102e])?)((?:\u0047)?)\u006c', u'\\1\\2\\3\\4\u004c', output)  # 2cn

    # hatoe
    output = re.sub(u'\u100a\u103e', u'\u100a\u00a7', output)  # nya with hatoe

    # oo
    output = re.sub(u'\u1009(\u103a)', u'\u1025\\1', output)  # nyapyat_to_oo

    # nag_nge_apyat
    output = re.sub(u'\u1014([\u103d\u103e])', u'\u0045\\1', output)
    output = re.sub(u'\u1014\u1039([\u1000-\u1021])', u'\u0045\u1039\\1', output)  # 2cn with prsint

    # aut_myit
    output = re.sub(u'([\u1014\u102f\u1030\u006b\u006c])((?:[\u1032\u1036])?)\u1037', u'\\1\\2\u0059', output)
    output = re.sub(u'([\u103d\u103e])((?:[\u1032\u1036])?)\u1037', u'\\1\\2\u0055', output)
    output = re.sub(u'(\u103d\u103e)\u1037', u'\\1\u0055', output)

    # yaguat
    output = re.sub(u'\u101b([\u102f\u1030])', u'\u00bd\\1', output)

    # nya
    output = re.sub(u'\u100a(\u103d\u103e)', u'\u00f1\\1', output)  # with waswe_hatoe

    return output


def convert(input):

    output = logical2visual(input)
    output = shape(output)
    output = replace(output)
    output = precompose(output)

    return output