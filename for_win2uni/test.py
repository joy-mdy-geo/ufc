import unittest
import win2uni


class TESTZG2UNI(unittest.TestCase):
    def test_artilce_one(self):
        win = u'''tydk'f 1
        vlwdkif;onf wlnD vGwfvyfaom *kPfodu©mjzihf vnf;aumif;? wlnDvGwfvyfaom tcGihfta&;rsm;jzihf vnf;aumif;? arG;zGm;vmolrsm; 
        jzpfonf/ xdkolwdkhü ydkif;jcm; a0zefwwfaom ÚmPfeSihf usihf0wf odwwfaom pdwfwdkh&Sdjuí xdkolwdkhonf tcsif;csif; arwÅmxm;í qufqHusihfokH;oihf\/'''
        unicode = u'''အပိုဒ် ၁
        လူတိုင်းသည် တူညီ လွတ်လပ်သော ဂုဏ်သိက္ခာဖြင့် လည်းကောင်း၊ တူညီလွတ်လပ်သော အခွင့်အရေးများဖြင့် လည်းကောင်း၊ မွေးဖွားလာသူများ 
        ဖြစ်သည်။ ထိုသူတို့၌ ပိုင်းခြား ဝေဖန်တတ်သော ဉာဏ်နှင့် ကျင့်ဝတ် သိတတ်သော စိတ်တို့ရှိကြ၍ ထိုသူတို့သည် အချင်းချင်း မေတ္တာထား၍ ဆက်ဆံကျင့်သုံးသင့်၏။'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed to Convert Article One")

    def test_article_two(self):
        win = u'''tydk'f 2
        vlwdkif;onf vlhtcGihf ta&; ajunmpmwrf;wGif azmfjyxm;onhf tcGihfta&; tm;vkH;? vGwfvyfcGihf tm;vkH;wdkhudk ydkifqdkif cHpm;cGihf&Sdonf/ 
        vlrsdk;eG,ftm;jzihf jzpfap? tom;ta&miftm;jzihf jzpfap? usm;? r? obm0tm;jzihf jzpfap? bmompum;tm;jzihf jzpfap? udk;uG,fonhf bmomtm;jzihf jzpfap? 
        edkifiHa&;,lqcsuf? odkhwnf;r[kwf tjcm;,lqcsuftm;jzihf jzpfap? edkifiHeSihf qdkifaom? odkhwnf;r[kwf vlrItqihftwef;eSihf qdkifaom Zpfjrpf tm;jzihfjzpfap? 
        ypönf; Opöm *kPftm;jzihf jzpfap? rsdk;&dk;Zmwdtm;jzihf jzpfap? tjcm; tqihftwef; tm;jzihf jzpfap cGJjcm;jcif;r&Sdap&/ xdkhjyif vlwpfOD; wpfa,muf aexdkif&m 
        edkifiH\ odkhwnf;r[kwf e,fajra'o\ edkifiHa&;qdkif&m jzpfap pD&ifydkifcGihfqdkif&m jzpfap wdkif;jynf tcsif;csif; qdkif&mjzpfap? 
        tqihftwef; wpfckckudk tajcjykí aomfvnf;aumif;? a'oe,fajrwpfckonf tcskyftjcm tmPmydkif vGwfvyfonhf e,fajr? odkhwnf;r[kwf ukvor*¾ 
        xdef;odrf; apmihfa&Smuf xm;&onhf e,fajr? odkhwnf;r[kwf udk,fydkif tkyfcskyfcGihf tmPmwdkh wpdwfwa'oavmufom &&Sdonhf e,fajr pojzihf 
        ,if;odkh aom e,fajrrsm; jzpfonf [laom tajumif;udk taxmuftxm; jykí aomfvnf;aumif; cGJjcm;jcif; vkH;0 r&Sdap&/'''
        unicode = u'''အပိုဒ် ၂
        လူတိုင်းသည် လူ့အခွင့် အရေး ကြေညာစာတမ်းတွင် ဖော်ပြထားသည့် အခွင့်အရေး အားလုံး၊ လွတ်လပ်ခွင့် အားလုံးတို့ကို ပိုင်ဆိုင် ခံစားခွင့်ရှိသည်။ 
        လူမျိုးနွယ်အားဖြင့် ဖြစ်စေ၊ အသားအရောင်အားဖြင့် ဖြစ်စေ၊ ကျား၊ မ၊ သဘာဝအားဖြင့် ဖြစ်စေ၊ ဘာသာစကားအားဖြင့် ဖြစ်စေ၊ ကိုးကွယ်သည့် ဘာသာအားဖြင့် ဖြစ်စေ၊ 
        နိုင်ငံရေးယူဆချက်၊ သို့တည်းမဟုတ် အခြားယူဆချက်အားဖြင့် ဖြစ်စေ၊ နိုင်ငံနှင့် ဆိုင်သော၊ သို့တည်းမဟုတ် လူမှုအဆင့်အတန်းနှင့် ဆိုင်သော ဇစ်မြစ် အားဖြင့်ဖြစ်စေ၊ 
        ပစ္စည်း ဥစ္စာ ဂုဏ်အားဖြင့် ဖြစ်စေ၊ မျိုးရိုးဇာတိအားဖြင့် ဖြစ်စေ၊ အခြား အဆင့်အတန်း အားဖြင့် ဖြစ်စေ ခွဲခြားခြင်းမရှိစေရ။ ထို့ပြင် လူတစ်ဦး တစ်ယောက် နေထိုင်ရာ 
        နိုင်ငံ၏ သို့တည်းမဟုတ် နယ်မြေဒေသ၏ နိုင်ငံရေးဆိုင်ရာ ဖြစ်စေ စီရင်ပိုင်ခွင့်ဆိုင်ရာ ဖြစ်စေ တိုင်းပြည် အချင်းချင်း ဆိုင်ရာဖြစ်စေ၊ 
        အဆင့်အတန်း တစ်ခုခုကို အခြေပြု၍ သော်လည်းကောင်း၊ ဒေသနယ်မြေတစ်ခုသည် အချုပ်အခြာ အာဏာပိုင် လွတ်လပ်သည့် နယ်မြေ၊ သို့တည်းမဟုတ် ကုလသမဂ္ဂ 
        ထိန်းသိမ်း စောင့်ရှောက် ထားရသည့် နယ်မြေ၊ သို့တည်းမဟုတ် ကိုယ်ပိုင် အုပ်ချုပ်ခွင့် အာဏာတို့ တစိတ်တဒေသလောက်သာ ရရှိသည့် နယ်မြေ စသဖြင့် 
        ယင်းသို့ သော နယ်မြေများ ဖြစ်သည် ဟူသော အကြောင်းကို အထောက်အထား ပြု၍ သော်လည်းကောင်း ခွဲခြားခြင်း လုံးဝ မရှိစေရ။'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed to Convert Article Two")

    def test_article_three(self):
        win = u'''tydk'f 3
        vlwdkif;ü touf&Sif&ef vGwfvyfrIcGihfeSihf vkHjckHpdwfcscGihf &Sdonf/'''
        unicode = u'''အပိုဒ် ၃
        လူတိုင်း၌ အသက်ရှင်ရန် လွတ်လပ်မှုခွင့်နှင့် လုံခြုံစိတ်ချခွင့် ရှိသည်။'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed to Convert Article Three")

    def test_article_four(self):
        win = u'''tydk'f 4
        rnfoludkrsS aus;usGeftjzpf? odkhwnf;r[kwf taptyg;tjzpf? edkifxufpD;eif; apcdkif;jcif; rjyk&? vludk aus;usGefozG,f t"r® apcdkif;jcif;? 
        ta&mif;t0,f jykjcif;eSihf xdkoabm oufa&mufaom vkyfief;[lorsSudk ydwfyif wm;jrpf &rnf/'''
        unicode = u'''အပိုဒ် ၄
        မည်သူကိုမျှ ကျေးကျွန်အဖြစ်၊ သို့တည်းမဟုတ် အစေအပါးအဖြစ်၊ နိုင်ထက်စီးနင်း စေခိုင်းခြင်း မပြုရ၊ လူကို ကျေးကျွန်သဖွယ် အဓမ္မ စေခိုင်းခြင်း၊ 
        အရောင်းအဝယ် ပြုခြင်းနှင့် ထိုသဘော သက်ရောက်သော လုပ်ငန်းဟူသမျှကို ပိတ်ပင် တားမြစ် ရမည်။'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed to Convert Article Four")

    def test_article_five(self):
        win = u'''tydk'f 5
        rnfoludkrsS nSÚf;yef; eSdyfpufjcif;? odkhwnf;r[kwf &ufpufjurf;jukwfpGm vlrqefpGm *kPfi,fapaom qufqHrI rjyk&? odkhwnf;r[kwf tjypf'Pf ay;jcif;rjyk&/'''
        unicode = u'''အပိုဒ် ၅
        မည်သူကိုမျှ ညှဉ်းပန်း နှိပ်စက်ခြင်း၊ သို့တည်းမဟုတ် ရက်စက်ကြမ်းကြုတ်စွာ လူမဆန်စွာ ဂုဏ်ငယ်စေသော ဆက်ဆံမှု မပြုရ၊ သို့တည်းမဟုတ် အပြစ်ဒဏ် ပေးခြင်းမပြုရ။'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed to Convert Article Five")

    def test_article_six(self):
        win = u'''tydk'f 6
        vlwdkif;wGif Oya't&mü vlyk*¾dkvfwpfOD; tjzpfjzihf t&mcyfodrf;wGif todtrSwf jykjcif;udk cH,lydkifcGihf&Sdonf/'''
        unicode = u'''အပိုဒ် ၆
        လူတိုင်းတွင် ဥပဒေအရာ၌ လူပုဂ္ဂိုလ်တစ်ဦး အဖြစ်ဖြင့် အရာခပ်သိမ်းတွင် အသိအမှတ် ပြုခြင်းကို ခံယူပိုင်ခွင့်ရှိသည်။'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed to Convert Article Six")

    def test_article_seven(self):
        win = u'''tydk'f 7
        vltm;vkH;wdkhonf Oya't&mü wlnDjuonhftjyif? Oya'\ tumtuG,fudk jcm;em;jcif; rcH&apbJ wlnDpGm cHpm;ydkifcGihf&Sdonf/ 
        þajunm pmwrf;yg oabmw&m;rsm;udk zDqefí cGJjcm;jcif;rS vnf;aumif;? xdkodkhcGJjcm;jcif;udk vIHhaqmfjcif;rS vnf;aumif;? uif;vGwf ap&ef tumtuG,fudk wlnDpGm cHpm;ydkifcGihf &Sdonf/'''
        unicode = u'''အပိုဒ် ၇
        လူအားလုံးတို့သည် ဥပဒေအရာ၌ တူညီကြသည့်အပြင်၊ ဥပဒေ၏ အကာအကွယ်ကို ခြားနားခြင်း မခံရစေဘဲ တူညီစွာ ခံစားပိုင်ခွင့်ရှိသည်။ 
        ဤကြေညာ စာတမ်းပါ သဘောတရားများကို ဖီဆန်၍ ခွဲခြားခြင်းမှ လည်းကောင်း၊ ထိုသို့ခွဲခြားခြင်းကို လှုံ့ဆော်ခြင်းမှ လည်းကောင်း၊ ကင်းလွတ် စေရန် အကာအကွယ်ကို တူညီစွာ ခံစားပိုင်ခွင့် ရှိသည်။'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed to Convert Article Seven")


if __name__ == "__main__":
    unittest.main();