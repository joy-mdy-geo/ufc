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

    def test_article_eight(self):
        win = u'''tydk'f 8
        zGJhpnf;ykH tajccHOya'u aomfvnf;aumif; tjcm; Oya'u aomfvnf;aumif; vlwdkif;twGuf ay;xm;onhf tajccH tcGihfta&; rsm;onf csdk;azmuf zsufqD;jcif;cHcJh&vsSif 
        xdkodkh csdk;azmufzsufqD; aom jykvkyfrIajumihf jzpfay:vmaom epfemcsuf twGuf xdkolonf edkifiHqdkif&m tmPmydkifw&m;&kH;wGif xda&mufpGm oufomcGihf &Sdedkifap&rnf/'''
        unicode = u'''အပိုဒ် ၈
        ဖွဲ့စည်းပုံ အခြေခံဥပဒေက သော်လည်းကောင်း အခြား ဥပဒေက သော်လည်းကောင်း လူတိုင်းအတွက် ပေးထားသည့် အခြေခံ အခွင့်အရေး များသည် ချိုးဖောက် ဖျက်ဆီးခြင်းခံခဲ့ရလျှင် 
        ထိုသို့ ချိုးဖောက်ဖျက်ဆီး သော ပြုလုပ်မှုကြောင့် ဖြစ်ပေါ်လာသော နစ်နာချက် အတွက် ထိုသူသည် နိုင်ငံဆိုင်ရာ အာဏာပိုင်တရားရုံးတွင် ထိရောက်စွာ သက်သာခွင့် ရှိနိုင်စေရမည်။'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed to Convert Article Eight")

    def test_article_nine(self):
        win = u'''tydk'f 9
        rnfolrsS Oya't& r[kwfaom zrf;qD;jcif;udk jzpfap? cskyfaeSmifjcif;udk jzpfap? jynfeSifjcif;udkjzpfap rcHap&/'''
        unicode = u'''အပိုဒ် ၉
        မည်သူမျှ ဥပဒေအရ မဟုတ်သော ဖမ်းဆီးခြင်းကို ဖြစ်စေ၊ ချုပ်နှောင်ခြင်းကို ဖြစ်စေ၊ ပြည်နှင်ခြင်းကိုဖြစ်စေ မခံစေရ။'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed to Convert Article Nine")

    def test_article_ten(self):
        win = u'''tydk'f 10
        tcGihfta&;rsm;eSihf wm0ef 0wÅ&m;rsm;udk tqkH;tjzwfcH&mwGif vnf;aumif;? jypfrIajumihf w&m;pGJqdk pD&if qkH;jzwfcH&mwGif vnf;aumif;? 
        vlwdkif;onf vGwfvyfí bufrvdkufaom w&m;&kH;awmf\ vltrsm; a&SharSmufwGif rsSwpGm jum;emppfaq;jcif;udk wlnDpGm cHpm; ydkifcGihf&Sdonf/'''
        unicode = u'''အပိုဒ် ၁ဝ
        အခွင့်အရေးများနှင့် တာဝန် ဝတ္တရားများကို အဆုံးအဖြတ်ခံရာတွင် လည်းကောင်း၊ ပြစ်မှုကြောင့် တရားစွဲဆို စီရင် ဆုံးဖြတ်ခံရာတွင် လည်းကောင်း၊ 
        လူတိုင်းသည် လွတ်လပ်၍ ဘက်မလိုက်သော တရားရုံးတော်၏ လူအများ ရှေ့မှောက်တွင် မျှတစွာ ကြားနာစစ်ဆေးခြင်းကို တူညီစွာ ခံစား ပိုင်ခွင့်ရှိသည်။'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed to Convert Article Ten")

    def test_article_eleven(self):
        win = u'''tydk'f 11
        vltrsm; a&SharSmufü Oya'twdkif; ppfaq;í jypfrIusl;vGefonf[k xif&Sm; pD&ifjcif;cH&onhf tcsdeftxd jypfrIeSihf w&m;pGJqdkjcif; cH&olwdkif;onf tjypfrJhol[lí ,lq jcif;cHxdkufonhf 
        tcGihfta&;&Sdonf/ xdktrIudk jum;emppfaq;&m0,f pGyfpGJcH&onhf jypfrItwGuf ckcHacsyedkif&ef vdktyfaom tcGihfta&;rsm;udk xdkoltm; ay;jyD; jzpfap&rnf/
        vlwpfOD;wpfa,muftm; edkifiHOya't&jzpfap? tjynfjynfqdkif&m Oya't& jzpfap? jypfrIrajrmufaom vkyf&yf odkhr[kwf ysufuGufrIt& qGJqdkjypfay;jcif; rjyk&/ 
        xdkhtjyif jypfrIusl;vGefpÚftcgu xdkufoihfapedkifaom tjypf'PfxufydkrdkjuD;av;aom tjypf'Pfudk xdkufoihfjcif;r&Sdap&/'''
        unicode = u'''အပိုဒ် ၁၁
        လူအများ ရှေ့မှောက်၌ ဥပဒေအတိုင်း စစ်ဆေး၍ ပြစ်မှုကျူးလွန်သည်ဟု ထင်ရှား စီရင်ခြင်းခံရသည့် အချိန်အထိ ပြစ်မှုနှင့် တရားစွဲဆိုခြင်း ခံရသူတိုင်းသည် အပြစ်မဲ့သူဟူ၍ ယူဆ ခြင်းခံထိုက်သည့် 
        အခွင့်အရေးရှိသည်။ ထိုအမှုကို ကြားနာစစ်ဆေးရာဝယ် စွပ်စွဲခံရသည့် ပြစ်မှုအတွက် ခုခံချေပနိုင်ရန် လိုအပ်သော အခွင့်အရေးများကို ထိုသူအား ပေးပြီး ဖြစ်စေရမည်။
        လူတစ်ဦးတစ်ယောက်အား နိုင်ငံဥပဒေအရဖြစ်စေ၊ အပြည်ပြည်ဆိုင်ရာ ဥပဒေအရ ဖြစ်စေ၊ ပြစ်မှုမမြောက်သော လုပ်ရပ် သို့မဟုတ် ပျက်ကွက်မှုအရ ဆွဲဆိုပြစ်ပေးခြင်း မပြုရ။ 
        ထို့အပြင် ပြစ်မှုကျူးလွန်စဉ်အခါက ထိုက်သင့်စေနိုင်သော အပြစ်ဒဏ်ထက်ပိုမိုကြီးလေးသော အပြစ်ဒဏ်ကို ထိုက်သင့်ခြင်းမရှိစေရ။'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed to Convert Article Eleven")

    def test_article_twelve(self):
        win = u'''tydk'f 12
        rnfolrsS rdrdoabmtwdkif; at;csrf;vGwfvyfpGm aexdkifjcif;udk aomfvnf;aumif;? rdrd\ rdom;pkudk aomfvnf;aumif;? rdrd\ aetdrf todkuft0ef;udk aomfvnf;aumif;? 
        pmay;pm,ludk aomfvnf;aumif;? Oya't& r[kwfaom 0ifa&muf pGufzufjcif; rcHap&/ xdkhjyif rdrd\*kPfodu©m udkvnf; txufyg twdkif; ykwfcwfjcif; rcHap&/ 
        vlwdkif;wGif xdkodkh 0ifa&mufpGufzufjcif;rS aomfvnf;aumif; ykwfcwfjcif;rS aomfvnf;aumif; Oya't& umuG,f ydkifcGihf&Sdonf/'''
        unicode = u'''အပိုဒ် ၁၂
        မည်သူမျှ မိမိသဘောအတိုင်း အေးချမ်းလွတ်လပ်စွာ နေထိုင်ခြင်းကို သော်လည်းကောင်း၊ မိမိ၏ မိသားစုကို သော်လည်းကောင်း၊ မိမိ၏ နေအိမ် အသိုက်အဝန်းကို သော်လည်းကောင်း၊ 
        စာပေးစာယူကို သော်လည်းကောင်း၊ ဥပဒေအရ မဟုတ်သော ဝင်ရောက် စွက်ဖက်ခြင်း မခံစေရ။ ထို့ပြင် မိမိ၏ဂုဏ်သိက္ခာ ကိုလည်း အထက်ပါ အတိုင်း ပုတ်ခတ်ခြင်း မခံစေရ။ 
        လူတိုင်းတွင် ထိုသို့ ဝင်ရောက်စွက်ဖက်ခြင်းမှ သော်လည်းကောင်း ပုတ်ခတ်ခြင်းမှ သော်လည်းကောင်း ဥပဒေအရ ကာကွယ် ပိုင်ခွင့်ရှိသည်။'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed to Convert Article Twelve")


if __name__ == "__main__":
    unittest.main()