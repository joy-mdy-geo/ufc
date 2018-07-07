import unittest
import uni2zg


class TESTZG2UNI(unittest.TestCase):

    def test_header_one(self):
        zawgyi = u'အျပည္ျပည္ဆိုင္ရာ လူ႔အခြင့္အေရး ေၾကျငာစာတမ္း'
        unicode = u'အပြည်ပြည်ဆိုင်ရာ လူ့အခွင့်အရေး ကြေငြာစာတမ်း'
        result = uni2zg.convert(unicode)
        self.assertEqual(zawgyi, result, "Failed to Convert Header One")

    def test_header_two(self):
        unicode = u'''ကမ္ဘာ့ကုလသမဂ္ဂ အထွေအထွေဆိုင်ရာ အစည်းအဝေးပွဲကြီးတွင် အပြည်ပြည်ဆိုင်ရာ လူ့အခွင့်အရေး ကြေညာစာတမ်း ကို ကြေညာအသုံးပြုခဲ့ပြီး 
        (၁၉၄၈ ခုနှစ် ဒီဇင်ဘာလ ၁ဝရက်နေ့တွင် ပြင်သစ်နိုင်ငံရှိ Palais de Chaillot တွင် အတည်ပြုခဲ့သည်။)။ ကမ္ဘာ့အံ့ဘွယ်အရာများရေးသားသည့် 
        The Guinness Book of Records စာအုပ်တွင် အပြည်ပြည်ဆိုင်ရာ လူ့အခွင့်အရေး ကြေညာစာတမ်းသည် ကမ္ဘာတွင် အများဆုံး ဘာသာပြန်ဆိုထားသည့် 
        စာတမ်းတစ်ခုအဖြစ် အသိအမှတ်ပြုခံရသည်။[၁] အဆိုပါ ကြေညာစာတမ်းသည် ဒုတိယကမ္ဘာစစ်ပွဲဖြစ်ပြီးနောက် တွေ့ကြုံရသော အခက်အခဲများ နှင့် ကမ္ဘာတဝှမ်းမှ 
        ပထမဦးဆုံး တောင်းဆိုခဲ့ကြသည့် လူသားတိုင်းသည် ညီတူညာတူ အခွင့်အရေးများ ရနိုင်ရန် ရည်ရွယ်၍ တောင်းဆိုခဲ့ကြခြင်းဖြစ်သည်။ အပိုဒ်ပေါင်း ၃၀ ပါရှိသော စာတမ်းတွင် 
        နိုင်ငံတကာနှင့် ဆက်ဆံမှု၊ ပြည်တွင်း လူ့အခွင့်အရေး တန်းတူရရှိနိုင်ဖို့ရန် အုတ်မြစ်တည်နိုင်စေရန်၊ ဥပေဒ နှင့် န
        ိုင်ငံတိုင်းတွင် အခြေခံ ဥပဒေ တည်ဆောက်နိုင်ရန် ရည်ရွယ်ရေးသားခဲ့ကြသည်။

        ကြေညာစာတမ်းတွင် ပါဝင်သော လူ့အခွင့်အရေးများ'''
        zawgyi = u'''ကမၻာ့ကုလသမဂၢ အေထြအေထြဆိုင္ရာ အစည္းအေဝးပြဲႀကီးတြင္ အျပည္ျပည္ဆိုင္ရာ လူ႔အခြင့္အေရး ေၾကညာစာတမ္း ကို ေၾကညာအသုံးျပဳခဲ့ၿပီး 
        (၁၉၄၈ ခုႏွစ္ ဒီဇင္ဘာလ ၁ဝရက္ေန႔တြင္ ျပင္သစ္နိုင္ငံရွိ Palais de Chaillot တြင္ အတည္ျပဳခဲ့သည္။)။ ကမၻာ့အံ့ဘြယ္အရာမ်ားေရးသားသည့္ 
        The Guinness Book of Records စာအုပ္တြင္ အျပည္ျပည္ဆိုင္ရာ လူ႔အခြင့္အေရး ေၾကညာစာတမ္းသည္ ကမၻာတြင္ အမ်ားဆုံး ဘာသာျပန္ဆိုထားသည့္ 
        စာတမ္းတစ္ခုအျဖစ္ အသိအမွတ္ျပဳခံရသည္။[၁] အဆိုပါ ေၾကညာစာတမ္းသည္ ဒုတိယကမၻာစစ္ပြဲျဖစ္ၿပီးေနာက္ ေတြ႕ၾကဳံရေသာ အခက္အခဲမ်ား ႏွင့္ ကမၻာတဝွမ္းမွ 
        ပထမဦးဆုံး ေတာင္းဆိုခဲ့ၾကသည့္ လူသားတိုင္းသည္ ညီတူညာတူ အခြင့္အေရးမ်ား ရနိုင္ရန္ ရည္ရြယ္၍ ေတာင္းဆိုခဲ့ၾကျခင္းျဖစ္သည္။ အပိုဒ္ေပါင္း ၃၀ ပါရွိေသာ စာတမ္းတြင္ 
        နိုင္ငံတကာႏွင့္ ဆက္ဆံမွု၊ ျပည္တြင္း လူ႔အခြင့္အေရး တန္းတူရရွိနိုင္ဖို႔ရန္ အုတ္ျမစ္တည္နိုင္ေစရန္၊ ဥေပဒ ႏွင့္ န
        ိုင္ငံတိုင္းတြင္ အေျခခံ ဥပေဒ တည္ေဆာက္နိုင္ရန္ ရည္ရြယ္ေရးသားခဲ့ၾကသည္။

        ေၾကညာစာတမ္းတြင္ ပါဝင္ေသာ လူ႔အခြင့္အေရးမ်ား'''
        result = uni2zg.convert(unicode)
        self.assertEqual(zawgyi, result, "Failed to Convert Header Two")

    def test_article_one(self):
        unicode = u'''အပိုဒ် ၁
        လူတိုင်းသည် တူညီ လွတ်လပ်သော ဂုဏ်သိက္ခာဖြင့် လည်းကောင်း၊ တူညီလွတ်လပ်သော အခွင့်အရေးများဖြင့် လည်းကောင်း၊ မွေးဖွားလာသူများ ဖြစ်သည်။ 
        ထိုသူတို့၌ ပိုင်းခြား ဝေဖန်တတ်သော ဉာဏ်နှင့် ကျင့်ဝတ် သိတတ်သော စိတ်တို့ရှိကြ၍ ထိုသူတို့သည် အချင်းချင်း မေတ္တာထား၍ ဆက်ဆံကျင့်သုံးသင့်၏။'''
        zawgyi = u'''အပိုဒ္ ၁
        လူတိုင္းသည္ တူညီ လြတ္လပ္ေသာ ဂုဏ္သိကၡာျဖင့္ လည္းေကာင္း၊ တူညီလြတ္လပ္ေသာ အခြင့္အေရးမ်ားျဖင့္ လည္းေကာင္း၊ ေမြးဖြားလာသူမ်ား ျဖစ္သည္။ 
        ထိုသူတို႔၌ ပိုင္းျခား ေဝဖန္တတ္ေသာ ဉာဏ္ႏွင့္ က်င့္ဝတ္ သိတတ္ေသာ စိတ္တို႔ရွိၾက၍ ထိုသူတို႔သည္ အခ်င္းခ်င္း ေမတၱာထား၍ ဆက္ဆံက်င့္သုံးသင့္၏။'''
        result = uni2zg.convert(unicode)
        self.assertEqual(zawgyi, result, "Failed to Convert Article One")

    def test_article_two(self):
        unicode = u'''အပိုဒ် ၂
        လူတိုင်းသည် လူ့အခွင့် အရေး ကြေညာစာတမ်းတွင် ဖော်ပြထားသည့် အခွင့်အရေး အားလုံး၊ လွတ်လပ်ခွင့် အားလုံးတို့ကို ပိုင်ဆိုင် ခံစားခွင့်ရှိသည်။ 
        လူမျိုးနွယ်အားဖြင့် ဖြစ်စေ၊ အသားအရောင်အားဖြင့် ဖြစ်စေ၊ ကျား၊ မ၊ သဘာဝအားဖြင့် ဖြစ်စေ၊ ဘာသာစကားအားဖြင့် ဖြစ်စေ၊ 
        ကိုးကွယ်သည့် ဘာသာအားဖြင့် ဖြစ်စေ၊ နိုင်ငံရေးယူဆချက်၊ သို့တည်းမဟုတ် အခြားယူဆချက်အားဖြင့် ဖြစ်စေ၊ နိုင်ငံနှင့် ဆိုင်သော၊ 
        သို့တည်းမဟုတ် လူမှုအဆင့်အတန်းနှင့် ဆိုင်သော ဇစ်မြစ် အားဖြင့်ဖြစ်စေ၊ ပစ္စည်း ဥစ္စာ ဂုဏ်အားဖြင့် ဖြစ်စေ၊ မျိုးရိုးဇာတိအားဖြင့် ဖြစ်စေ၊ 
        အခြား အဆင့်အတန်း အားဖြင့် ဖြစ်စေ ခွဲခြားခြင်းမရှိစေရ။ ထို့ပြင် လူတစ်ဦး တစ်ယောက် နေထိုင်ရာ နိုင်ငံ၏ သို့တည်းမဟုတ် နယ်မြေဒေသ၏ 
        နိုင်ငံရေးဆိုင်ရာ ဖြစ်စေ စီရင်ပိုင်ခွင့်ဆိုင်ရာ ဖြစ်စေ တိုင်းပြည် အချင်းချင်း ဆိုင်ရာဖြစ်စေ၊ အဆင့်အတန်း တစ်ခုခုကို အခြေပြု၍ သော်လည်းကောင်း၊ 
        ဒေသနယ်မြေတစ်ခုသည် အချုပ်အခြာ အာဏာပိုင် လွတ်လပ်သည့် နယ်မြေ၊ သို့တည်းမဟုတ် ကုလသမဂ္ဂ ထိန်းသိမ်း စောင့်ရှောက် ထားရသည့် နယ်မြေ၊ 
        သို့တည်းမဟုတ် ကိုယ်ပိုင် အုပ်ချုပ်ခွင့် အာဏာတို့ တစိတ်တဒေသလောက်သာ ရရှိသည့် နယ်မြေ စသဖြင့် ယင်းသို့ သော နယ်မြေများ ဖြစ်သည် 
        ဟူသော အကြောင်းကို အထောက်အထား ပြု၍ သော်လည်းကောင်း ခွဲခြားခြင်း လုံးဝ မရှိစေရ။'''
        zawgyi = u'''အပိုဒ္ ၂
        လူတိုင္းသည္ လူ႔အခြင့္ အေရး ေၾကညာစာတမ္းတြင္ ေဖာ္ျပထားသည့္ အခြင့္အေရး အားလုံး၊ လြတ္လပ္ခြင့္ အားလုံးတို႔ကို ပိုင္ဆိုင္ ခံစားခြင့္ရွိသည္။ 
        လူမ်ိဳးႏြယ္အားျဖင့္ ျဖစ္ေစ၊ အသားအေရာင္အားျဖင့္ ျဖစ္ေစ၊ က်ား၊ မ၊ သဘာဝအားျဖင့္ ျဖစ္ေစ၊ ဘာသာစကားအားျဖင့္ ျဖစ္ေစ၊ 
        ကိုးကြယ္သည့္ ဘာသာအားျဖင့္ ျဖစ္ေစ၊ နိုင္ငံေရးယူဆခ်က္၊ သို႔တည္းမဟုတ္ အျခားယူဆခ်က္အားျဖင့္ ျဖစ္ေစ၊ နိုင္ငံႏွင့္ ဆိုင္ေသာ၊ 
        သို႔တည္းမဟုတ္ လူမွုအဆင့္အတန္းႏွင့္ ဆိုင္ေသာ ဇစ္ျမစ္ အားျဖင့္ျဖစ္ေစ၊ ပစၥည္း ဥစၥာ ဂုဏ္အားျဖင့္ ျဖစ္ေစ၊ မ်ိဳးရိုးဇာတိအားျဖင့္ ျဖစ္ေစ၊ 
        အျခား အဆင့္အတန္း အားျဖင့္ ျဖစ္ေစ ခြဲျခားျခင္းမရွိေစရ။ ထို႔ျပင္ လူတစ္ဦး တစ္ေယာက္ ေနထိုင္ရာ နိုင္ငံ၏ သို႔တည္းမဟုတ္ နယ္ေျမေဒသ၏ 
        နိုင္ငံေရးဆိုင္ရာ ျဖစ္ေစ စီရင္ပိုင္ခြင့္ဆိုင္ရာ ျဖစ္ေစ တိုင္းျပည္ အခ်င္းခ်င္း ဆိုင္ရာျဖစ္ေစ၊ အဆင့္အတန္း တစ္ခုခုကို အေျချပဳ၍ ေသာ္လည္းေကာင္း၊ 
        ေဒသနယ္ေျမတစ္ခုသည္ အခ်ဳပ္အျခာ အာဏာပိုင္ လြတ္လပ္သည့္ နယ္ေျမ၊ သို႔တည္းမဟုတ္ ကုလသမဂၢ ထိန္းသိမ္း ေစာင့္ေရွာက္ ထားရသည့္ နယ္ေျမ၊ 
        သို႔တည္းမဟုတ္ ကိုယ္ပိုင္ အုပ္ခ်ဳပ္ခြင့္ အာဏာတို႔ တစိတ္တေဒသေလာက္သာ ရရွိသည့္ နယ္ေျမ စသျဖင့္ ယင္းသို႔ ေသာ နယ္ေျမမ်ား ျဖစ္သည္ 
        ဟူေသာ အေၾကာင္းကို အေထာက္အထား ျပဳ၍ ေသာ္လည္းေကာင္း ခြဲျခားျခင္း လုံးဝ မရွိေစရ။'''
        result = uni2zg.convert(unicode)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Two")

    def test_article_three(self):
        unicode = u'''အပိုဒ် ၃
        လူတိုင်း၌ အသက်ရှင်ရန် လွတ်လပ်မှုခွင့်နှင့် လုံခြုံစိတ်ချခွင့် ရှိသည်။'''
        zawgyi = u'''အပိုဒ္ ၃
        လူတိုင္း၌ အသက္ရွင္ရန္ လြတ္လပ္မွုခြင့္ႏွင့္ လုံျခဳံစိတ္ခ်ခြင့္ ရွိသည္။'''
        result = uni2zg.convert(unicode)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Three")

    def test_article_four(self):
        unicode = u'''အပိုဒ် ၄
        မည်သူကိုမျှ ကျေးကျွန်အဖြစ်၊ သို့တည်းမဟုတ် အစေအပါးအဖြစ်၊ နိုင်ထက်စီးနင်း စေခိုင်းခြင်း မပြုရ၊ လူကို ကျေးကျွန်သဖွယ် အဓမ္မ စေခိုင်းခြင်း၊ 
        အရောင်းအဝယ် ပြုခြင်းနှင့် ထိုသဘော သက်ရောက်သော လုပ်ငန်းဟူသမျှကို ပိတ်ပင် တားမြစ် ရမည်။'''
        zawgyi = u'''အပိုဒ္ ၄
        မည္သူကိုမၽွ ေက်းကၽြန္အျဖစ္၊ သို႔တည္းမဟုတ္ အေစအပါးအျဖစ္၊ နိုင္ထက္စီးနင္း ေစခိုင္းျခင္း မျပဳရ၊ လူကို ေက်းကၽြန္သဖြယ္ အဓမၼ ေစခိုင္းျခင္း၊ 
        အေရာင္းအဝယ္ ျပဳျခင္းႏွင့္ ထိုသေဘာ သက္ေရာက္ေသာ လုပ္ငန္းဟူသမၽွကို ပိတ္ပင္ တားျမစ္ ရမည္။'''
        result = uni2zg.convert(unicode)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Four")

    def test_article_five(self):
        unicode = u'''အပိုဒ် ၅
        မည်သူကိုမျှ ညှဉ်းပန်း နှိပ်စက်ခြင်း၊ သို့တည်းမဟုတ် ရက်စက်ကြမ်းကြုတ်စွာ လူမဆန်စွာ ဂုဏ်ငယ်စေသော ဆက်ဆံမှု မပြုရ၊ သို့တည်းမဟုတ် အပြစ်ဒဏ် ပေးခြင်းမပြုရ။'''
        zawgyi = u'''အပိုဒ္ ၅
        မည္သူကိုမၽွ ညႇဥ္းပန္း ႏွိပ္စက္ျခင္း၊ သို႔တည္းမဟုတ္ ရက္စက္ၾကမ္းၾကဳတ္စြာ လူမဆန္စြာ ဂုဏ္ငယ္ေစေသာ ဆက္ဆံမွု မျပဳရ၊ သို႔တည္းမဟုတ္ အျပစ္ဒဏ္ ေပးျခင္းမျပဳရ။'''
        result = uni2zg.convert(unicode)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Five")


if __name__ == "__main__":
    unittest.main()