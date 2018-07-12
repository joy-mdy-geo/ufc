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

    def test_article_thirteen(self):
        win = u'''tydk'f 13
        vlwdkif;wGif rdrd\edkifiH e,fedrdwf twGif;ü vGwfvyfpGm oGm;vm a&GShajymif; edkifcGihf? aexdkifcGihf&Sdonf/
        vlwdkif;wGif rdrdaexdkif&m wdkif;jynfrS vnf;aumif;? tjcm;wdkif;jynfrSvnf;aumif; xGufcGm oGm;ydkifcGihf&Sdonhftjyif?rdrd\ wdkif;jynfodkh jyefvm ydkifcGihfvnf;&Sdonf/'''
        unicode = u'''အပိုဒ် ၁၃
        လူတိုင်းတွင် မိမိ၏နိုင်ငံ နယ်နိမိတ် အတွင်း၌ လွတ်လပ်စွာ သွားလာ ရွှေ့ပြောင်း နိုင်ခွင့်၊ နေထိုင်ခွင့်ရှိသည်။
        လူတိုင်းတွင် မိမိနေထိုင်ရာ တိုင်းပြည်မှ လည်းကောင်း၊ အခြားတိုင်းပြည်မှလည်းကောင်း ထွက်ခွာ သွားပိုင်ခွင့်ရှိသည့်အပြင်၊မိမိ၏ တိုင်းပြည်သို့ ပြန်လာ ပိုင်ခွင့်လည်းရှိသည်။'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed to Convert Article Thirteen")

    def test_article_fourteen(self):
        win = u'''tydk'f 14
        vlwdkif;onf nSÚf;yef; eSdyfpuf cHae&jcif;rS vGwfuif;&ef tjcm;wdkif;jynf rsm;ü at;csrf;pGm cdkvIHaeedkifcGihf&Sdonf/
        edkifiHa&;eSihf rywfoufonhf jypfrIrsm;rS aomfvnf;aumif;? ukvor*¾\ &nf&GufcsufeSihf oabmw&m; rIrsm;udk zDqefaom trIrsm;rS aomfvn;faumif;? 
        trSef ay:ayguf vmaom jypfrIajumihf w&m;pGJqdkjcif; cH&onhf trItcif;rsm;wGif txufyg tcGihfta&;udk tokH;rjykedkifap&/'''
        unicode = u'''အပိုဒ် ၁၄
        လူတိုင်းသည် ညှဉ်းပန်း နှိပ်စက် ခံနေရခြင်းမှ လွတ်ကင်းရန် အခြားတိုင်းပြည် များ၌ အေးချမ်းစွာ ခိုလှုံနေနိုင်ခွင့်ရှိသည်။
        နိုင်ငံရေးနှင့် မပတ်သက်သည့် ပြစ်မှုများမှ သော်လည်းကောင်း၊ ကုလသမဂ္ဂ၏ ရည်ရွက်ချက်နှင့် သဘောတရား မှုများကို ဖီဆန်သော အမှုများမှ သော်လညး်ကောင်း၊ 
        အမှန် ပေါ်ပေါက် လာသော ပြစ်မှုကြောင့် တရားစွဲဆိုခြင်း ခံရသည့် အမှုအခင်းများတွင် အထက်ပါ အခွင့်အရေးကို အသုံးမပြုနိုင်စေရ။'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed to Convert Article Fourteen")

    def test_article_fifteen(self):
        win = u'''tydk'f 15
        vlwdkif;onf? edkifiH wpfedkifiH\ edkifiHom;tjzpf cH,lcGihf&Sdonf/
        Oya't& r[kwfvsSif rnfolrsS rdrd\ edkifiHom;tjzpfudk pGehfvGSwfjcif; rcHap&? edkifiHom;tjzpf ajymif;vJedkifaomtcGihfta&;udk vnf; jiif;y,fjcif; rcHap&/'''
        unicode = u'''အပိုဒ် ၁၅
        လူတိုင်းသည်၊ နိုင်ငံ တစ်နိုင်ငံ၏ နိုင်ငံသားအဖြစ် ခံယူခွင့်ရှိသည်။
        ဥပဒေအရ မဟုတ်လျှင် မည်သူမျှ မိမိ၏ နိုင်ငံသားအဖြစ်ကို စွန့်လွှတ်ခြင်း မခံစေရ၊ နိုင်ငံသားအဖြစ် ပြောင်းလဲနိုင်သောအခွင့်အရေးကို လည်း ငြင်းပယ်ခြင်း မခံစေရ။'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed to Convert Article Fifteen")

    def test_article_sixteen(self):
        win = u'''tydk'f 16
        t&G,fa&muf jyD;aom a,musmf; eSihf rdef;rwdkhwGif vlrsdk;udk aomfvnf;aumif;? edkifiHom; tjzpfudk aomfvnf;aumif; udk;uG,fonhf bmomudk aomfvnf;aumif;? 
        tajumif;jykí cskyfcs,f uehfowfjcif; r&SdbJ? 
        xdrf;jrm;edkifcGihf eSihf rdom;pkxlaxmifedkifcGihf&Sdonf/ tqdkyg a,musmf;eSihf rdef;r wdkhonf vifr,m;tjzpf aygif;oif;aepÚf tcsdef twGif;ü aomfvnf;aumif;? 
        tdrfaxmifudk zsufodrf;í uGm&Sif;juonhf tcgüvnf;aumif;? vufxyf aygif;oif; tdrfaxmifjykjcif;eSihf pyfvsÚf;aom wlnDonhf tcGihfta&;rsm;udk &&Sdxdkufonf/
        owdkhom; eSihf owdkhorD; eSpfOD;eSpfbuf\ vGwfvyfaom oabmqe´&SdrSomvsSif xdrf;jrm;jcif;udk jyk&rnf/
        rdom;pk wpfckonf vlhtzGJhtpnf;\ obm0usaom tajccHtzGJhwpf&yfjzpfonf? xdkrdom;pkonf vlh tzGJhtpnf;eSihf tpdk;&wdkh\ umuG,fapmihfa&Smufjcif;udk cH,lcGihf&Sdonf/'''
        unicode = u'''အပိုဒ် ၁၆
        အရွယ်ရောက် ပြီးသော ယောကျာ်း နှင့် မိန်းမတို့တွင် လူမျိုးကို သော်လည်းကောင်း၊ နိုင်ငံသား အဖြစ်ကို သော်လည်းကောင်း ကိုးကွယ်သည့် ဘာသာကို သော်လည်းကောင်း၊ 
        အကြောင်းပြု၍ ချုပ်ချယ် ကန့်သတ်ခြင်း မရှိဘဲ၊ 
        ထိမ်းမြားနိုင်ခွင့် နှင့် မိသားစုထူထောင်နိုင်ခွင့်ရှိသည်။ အဆိုပါ ယောကျာ်းနှင့် မိန်းမ တို့သည် လင်မယားအဖြစ် ပေါင်းသင်းနေစဉ် အချိန် အတွင်း၌ သော်လည်းကောင်း၊ 
        အိမ်ထောင်ကို ဖျက်သိမ်း၍ ကွာရှင်းကြသည့် အခါ၌လည်းကောင်း၊ လက်ထပ် ပေါင်းသင်း အိမ်ထောင်ပြုခြင်းနှင့် စပ်လျဉ်းသော တူညီသည့် အခွင့်အရေးများကို ရရှိထိုက်သည်။
        သတို့သား နှင့် သတို့သမီး နှစ်ဦးနှစ်ဘက်၏ လွတ်လပ်သော သဘောဆန္ဒရှိမှသာလျှင် ထိမ်းမြားခြင်းကို ပြုရမည်။
        မိသားစု တစ်ခုသည် လူ့အဖွဲ့အစည်း၏ သဘာဝကျသော အခြေခံအဖွဲ့တစ်ရပ်ဖြစ်သည်၊ ထိုမိသားစုသည် လူ့ အဖွဲ့အစည်းနှင့် အစိုးရတို့၏ ကာကွယ်စောင့်ရှောက်ခြင်းကို ခံယူခွင့်ရှိသည်။'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed to Convert Article Sixteen")

    def test_article_seventeen(self):
        win = u'''tydk'f 17
        vlwdkif;wGif rdrd wpfOD;csif;aomfvnf;aumif; ? tjcm;olrsm;eSihf zufpyfí aomfvnf;aumif;? ypönf;Opöm wdkhudk ydkifqdkif&ef tcGihfta&;&Sd&rnf/ 
        Oya't& r[kwfvsSif? rnfolrsS rdrd\ypönf;OpömydkifqdkifcGihfudk pGehfvGSwfjcif; rcHap&/'''
        unicode = u'''အပိုဒ် ၁၇
        လူတိုင်းတွင် မိမိ တစ်ဦးချင်းသော်လည်းကောင်း ၊ အခြားသူများနှင့် ဖက်စပ်၍ သော်လည်းကောင်း၊ ပစ္စည်းဥစ္စာ တို့ကို ပိုင်ဆိုင်ရန် အခွင့်အရေးရှိရမည်။ 
        ဥပဒေအရ မဟုတ်လျှင်၊ မည်သူမျှ မိမိ၏ပစ္စည်းဥစ္စာပိုင်ဆိုင်ခွင့်ကို စွန့်လွှတ်ခြင်း မခံစေရ။'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed to Convert Article Seventeen")

    def test_article_eighteen(self):
        win = u'''tydk'f 18
        vlwdkif;wGif vGwfvyfpGm awG;ac: juHqedkifcGihf? vGwfvyfpGm cH,l&yfwnfedkifcGihf eSihf vGwfvyfpGm ouf0if udk;uG,fedkifcGihf&Sdonf/ 
        tqdkyg tcGihfta&;rsm;ü rdrdudk;uG,fonhf bmomudk odkhwnf;r[kwf ouf0if,kHjunfcsufudk vGwfvyfpGm ajymif;vJedkifcGihf yg0ifonhf tjyif 
        rdrd wpfa,mufcsif;jzpfap? tjcm;olrsm;eSihf pkaygif;íjzpfap? jynfoltrsm; a&SharSmufwGif aomfvnf;aumif;? a&SharSmufwGif r[kwfbJ aomfvnf;aumif;? rdrd udk;uG,faom bmomudk 
        odkhwnf;r[kwf ouf0if ,kHjunfcsufudk vGwfvyf pGm oifjyedkifcGihf? usihfokH;edkifcGihf? 0wfjykudk;uG,fedkifcGihfeSihf aqmufwnf edkifcGihfwdkhvnf; yg0ifonf/'''
        unicode = u'''အပိုဒ် ၁၈
        လူတိုင်းတွင် လွတ်လပ်စွာ တွေးခေါ် ကြံဆနိုင်ခွင့်၊ လွတ်လပ်စွာ ခံယူရပ်တည်နိုင်ခွင့် နှင့် လွတ်လပ်စွာ သက်ဝင် ကိုးကွယ်နိုင်ခွင့်ရှိသည်။ 
        အဆိုပါ အခွင့်အရေးများ၌ မိမိကိုးကွယ်သည့် ဘာသာကို သို့တည်းမဟုတ် သက်ဝင်ယုံကြည်ချက်ကို လွတ်လပ်စွာ ပြောင်းလဲနိုင်ခွင့် ပါဝင်သည့် အပြင် 
        မိမိ တစ်ယောက်ချင်းဖြစ်စေ၊ အခြားသူများနှင့် စုပေါင်း၍ဖြစ်စေ၊ ပြည်သူအများ ရှေ့မှောက်တွင် သော်လည်းကောင်း၊ ရှေ့မှောက်တွင် မဟုတ်ဘဲ သော်လည်းကောင်း၊ မိမိ ကိုးကွယ်သော ဘာသာကို 
        သို့တည်းမဟုတ် သက်ဝင် ယုံကြည်ချက်ကို လွတ်လပ် စွာ သင်ပြနိုင်ခွင့်၊ ကျင့်သုံးနိုင်ခွင့်၊ ဝတ်ပြုကိုးကွယ်နိုင်ခွင့်နှင့် ဆောက်တည် နိုင်ခွင့်တို့လည်း ပါဝင်သည်။'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed to Convert Article Eighteen")

    def test_article_nineteen(self):
        win = u'''tydk'f 19
        vlwdkif;wGif vGwfvyfpGm xifjrif ,lqedkifcGihfeSihf vGwfvyfpGm zGihf[ azmfjyedkifcGihf&Sdonf/ tqdkyg tcGihfta&;rsm;ü taeSmihf t,Sufr&SdbJ vGwfvyfpGm xifjrif,lqedkifcGihf yg0if onhftjyif? 
        edkifiHe,fedrdwfrsm;udk axmufxm;&ef rvdkbJ owif;tajumif;t&meSihf oabmw&m;rsm;udk wenf;enf; jzihf vGwfvyfpGm &Sm,lqnf;yl;edkifcGihf? vufcHedkifcGihfeSihf a0iS jzehfcsdcGihfwdkhvnf; yg0ifonf/'''
        unicode = u'''အပိုဒ် ၁၉
        လူတိုင်းတွင် လွတ်လပ်စွာ ထင်မြင် ယူဆနိုင်ခွင့်နှင့် လွတ်လပ်စွာ ဖွင့်ဟ ဖော်ပြနိုင်ခွင့်ရှိသည်။ အဆိုပါ အခွင့်အရေးများ၌ အနှောင့် အယှက်မရှိဘဲ လွတ်လပ်စွာ ထင်မြင်ယူဆနိုင်ခွင့် ပါဝင် သည့်အပြင်၊ 
        နိုင်ငံနယ်နိမိတ်များကို ထောက်ထားရန် မလိုဘဲ သတင်းအကြောင်းအရာနှင့် သဘောတရားများကို တနည်းနည်း ဖြင့် လွတ်လပ်စွာ ရှာယူဆည်းပူးနိုင်ခွင့်၊ လက်ခံနိုင်ခွင့်နှင့် ဝေငှ ဖြန့်ချိခွင့်တို့လည်း ပါဝင်သည်။'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed to Convert Article Nineteen")

    def test_article_twenty(self):
        win = u'''tydk'f 20
        vlwdkif;wGif vGwfvyf at;csrf;pGm pka0;edkifcGihf eSihf zGJhpnf;edkifcGihf wdkh &Sdonf/
        rnfolhudkrsS tzGJhtpnf;wpfckodkh 0ifap&ef twif;tusyfrjyk&/'''
        unicode = u'''အပိုဒ် ၂ဝ
        လူတိုင်းတွင် လွတ်လပ် အေးချမ်းစွာ စုဝေးနိုင်ခွင့် နှင့် ဖွဲ့စည်းနိုင်ခွင့် တို့ ရှိသည်။
        မည်သူ့ကိုမျှ အဖွဲ့အစည်းတစ်ခုသို့ ဝင်စေရန် အတင်းအကျပ်မပြုရ။'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed to Convert Article Twenty")

    def test_article_twentyone(self):
        win = u'''tydk'f 21
        vlwdkif;wGif rdrdedkifiH\ tkyfcskyfa&;ü udk,fwdkifjzpfap? vGwfvyfpGm a&G;cs,fvdkufonhf udk,fpm;vS,frsm;rS wpfqihfjzpfap yg0if aqmif&GufedkifcGihf &Sdonf/
        vlwdkif;wGif rdrd\edkifiH&Sd jynfolh 0efxrf;tzGJhü 0ifa&mufedkif&ef wlnDonhf tcGihf ta&;&Sdonf/
        jynfoljynfom;wdkh\ qe´onf tkyfcskyf tmPm\ tajccHjzpf&rnf? tqdkyg qe´udk tcsdefumvydkif;jcm;vsuf ppfrSefaoma&G;aumufyGJrsm;jzihf xif&Sm;ap&rnf/ 
        a&G;aumuf yGJrsm;wGifvnf; vlwdkif;tnDtrsS qe´rJ ay;edkifcGihf &Sd&rnhftjyif ? xdka&G;aumufyGJrsm;udk vsSdkh0Suf rJay; pepfjzihf jzpfap? 
        tvm;wl vGwfvyfaom rJay;pepf jzihfjzpfap usif;y&rnf/'''
        unicode = u'''အပိုဒ် ၂၁
        လူတိုင်းတွင် မိမိနိုင်ငံ၏ အုပ်ချုပ်ရေး၌ ကိုယ်တိုင်ဖြစ်စေ၊ လွတ်လပ်စွာ ရွေးချယ်လိုက်သည့် ကိုယ်စားလှယ်များမှ တစ်ဆင့်ဖြစ်စေ ပါဝင် ဆောင်ရွက်နိုင်ခွင့် ရှိသည်။
        လူတိုင်းတွင် မိမိ၏နိုင်ငံရှိ ပြည်သူ့ ဝန်ထမ်းအဖွဲ့၌ ဝင်ရောက်နိုင်ရန် တူညီသည့် အခွင့် အရေးရှိသည်။
        ပြည်သူပြည်သားတို့၏ ဆန္ဒသည် အုပ်ချုပ် အာဏာ၏ အခြေခံဖြစ်ရမည်၊ အဆိုပါ ဆန္ဒကို အချိန်ကာလပိုင်းခြားလျက် စစ်မှန်သောရွေးကောက်ပွဲများဖြင့် ထင်ရှားစေရမည်။ 
        ရွေးကောက် ပွဲများတွင်လည်း လူတိုင်းအညီအမျှ ဆန္ဒမဲ ပေးနိုင်ခွင့် ရှိရမည့်အပြင် ၊ ထိုရွေးကောက်ပွဲများကို လျှို့ဝှက် မဲပေး စနစ်ဖြင့် ဖြစ်စေ၊ 
        အလားတူ လွတ်လပ်သော မဲပေးစနစ် ဖြင့်ဖြစ်စေ ကျင်းပရမည်။'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed to Convert Article TwentyOne")

    def test_article_twentytwo(self):
        win = u'''tydk'f 22
        vlwdkif;wGif vlhtzGJhtpnf;\ tzGJh0ifwpfOD;taeeSihf vlrIa&;vkHjckHcGihf&,lydkihfcGihf&Sdonhf tjyifedkifiHa&; judk;
        yrf;rIjzihfjzpfap? edkifiHwum ylaygif;aqmif&GufrIjzihfjzpfap? 
        edkifiHtoD;oD;\zGJhpnf;ykHeSihf vnf;aumif;? o,HZmw tiftm;eSihfvnf;aumif; xdkvl\ *kPfodu©meSihf p&dkufvu©Pm vGwfvyfpGm 
        wdk;wufjrihfrm;a&;twGuf r&Sdrjzpfvdktyfaom pD;yGm;a&;?vlrIa&;eSihf ,Úfaus;rI tcGihfta&;rsm;udk okH;pGJydkifcGihf&Sdonf/'''
        unicode = u'''အပိုဒ် ၂၂
        လူတိုင်းတွင် လူ့အဖွဲ့အစည်း၏ အဖွဲ့ဝင်တစ်ဦးအနေနှင့် လူမှုရေးလုံခြုံခွင့်ရယူပိုင့်ခွင့်ရှိသည့် အပြင်နိုင်ငံရေး ကြိုး
        ပမ်းမှုဖြင့်ဖြစ်စေ၊ နိုင်ငံတကာ ပူပေါင်းဆောင်ရွက်မှုဖြင့်ဖြစ်စေ၊ 
        နိုင်ငံအသီးသီး၏ဖွဲ့စည်းပုံနှင့် လည်းကောင်း၊ သယံဇာတ အင်အားနှင့်လည်းကောင်း ထိုလူ၏ ဂုဏ်သိက္ခာနှင့် စရိုက်လက္ခဏာ လွတ်လပ်စွာ 
        တိုးတက်မြင့်မားရေးအတွက် မရှိမဖြစ်လိုအပ်သော စီးပွားရေး၊လူမှုရေးနှင့် ယဉ်ကျေးမှု အခွင့်အရေးများကို သုံးစွဲပိုင်ခွင့်ရှိသည်။'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed to Convert Article TwentyTwo")

    def test_article_twentythree(self):
        win = u'''tydk'f 23
        vlwdkif;wGif tvkyfvkyf &efvnf;aumif;? rdrdeSpfouf&m toufarG;rI tvkyf tudkifudk vGwfvyfpGma&G;cs,f&ef vnf;aumif;? w&m;rsSwí 
        vkyfaysmfaom tvkyfcGif\ tajctaeudk &&Sd&ef vnf;aumif;? tvkyfvufrJh jzpf&jcif;rS tumtuG,f &&Sd&ef vnf;aumif; tcGihfta&;&Sdonf/
        vlwdkif;wGif cGJjcm;jcif;rcH&apbJ? wlnDaom tvkyftwGuf wlnDaom tcaju;aiG &ydkifcGihf&Sdonf/
        tvkyfvkyfudkifonhf vlwdkif;wGif? rdrdeSihf rdrd\ rdom;pktwGuf vlh*kPfodu©m eSihf nDatmif aexdkif pm;aomufedkif&ef? 
        pdwfcsavmufonhfjyif? w&m; rsSwí vkyfaysmfonhf vpmaju;aiG &ydkifcGihf&Sdonf/ vdktyfcJhvsSiftjcm; enf;vrf;rsm;rS vlrIa&; taxmuftyHhudkvnf; xyfrHí &ydkifcGihf &Sdonf/
        vlwdkif;wGif rdrdtusdk; cHpm;cGihfudk umuG,f&ef tvkyform; tpnf;t&kH;rsm; zGJhpnf;cGihf ? yg0if aqmif&GufcGihf &Sdonf/'''
        unicode = u'''အပိုဒ် ၂၃
        လူတိုင်းတွင် အလုပ်လုပ် ရန်လည်းကောင်း၊ မိမိနှစ်သက်ရာ အသက်မွေးမှု အလုပ် အကိုင်ကို လွတ်လပ်စွာရွေးချယ်ရန် လည်းကောင်း၊ တရားမျှတ၍ 
        လုပ်ပျော်သော အလုပ်ခွင်၏ အခြေအနေကို ရရှိရန် လည်းကောင်း၊ အလုပ်လက်မဲ့ ဖြစ်ရခြင်းမှ အကာအကွယ် ရရှိရန် လည်းကောင်း အခွင့်အရေးရှိသည်။
        လူတိုင်းတွင် ခွဲခြားခြင်းမခံရစေဘဲ၊ တူညီသော အလုပ်အတွက် တူညီသော အခကြေးငွေ ရပိုင်ခွင့်ရှိသည်။
        အလုပ်လုပ်ကိုင်သည့် လူတိုင်းတွင်၊ မိမိနှင့် မိမိ၏ မိသားစုအတွက် လူ့ဂုဏ်သိက္ခာ နှင့် ညီအောင် နေထိုင် စားသောက်နိုင်ရန်၊ 
        စိတ်ချလောက်သည့်ပြင်၊ တရား မျှတ၍ လုပ်ပျော်သည့် လစာကြေးငွေ ရပိုင်ခွင့်ရှိသည်။ လိုအပ်ခဲ့လျှင်အခြား နည်းလမ်းများမှ လူမှုရေး အထောက်အပံ့ကိုလည်း ထပ်မံ၍ ရပိုင်ခွင့် ရှိသည်။
        လူတိုင်းတွင် မိမိအကျိုး ခံစားခွင့်ကို ကာကွယ်ရန် အလုပ်သမား အစည်းအရုံးများ ဖွဲ့စည်းခွင့် ၊ ပါဝင် ဆောင်ရွက်ခွင့် ရှိသည်။'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed to Convert Article TwentyThree")

    def test_article_twentyfour(self):
        win = u'''tydk'f 24
        vlwdkif;wGif oihfjrwfavsmfuefpGm uehfowfxm;onhf tvkyfvkyfcsdef tjyif? vpmeSihfwuG tcgumvtm;avsmfpGm owfrSwf 
        xm;onhf tvkyf tm;vyf&ufrsm;yg0ifonhf tem;,lcGihfeSihf tm;vyfcGihf cHpm;ydkifcGihf &Sdonf/'''
        unicode = u'''အပိုဒ် ၂၄
        လူတိုင်းတွင် သင့်မြတ်လျော်ကန်စွာ ကန့်သတ်ထားသည့် အလုပ်လုပ်ချိန် အပြင်၊ လစာနှင့်တကွ အခါကာလအားလျော်စွာ သတ်မှတ် 
        ထားသည့် အလုပ် အားလပ်ရက်များပါဝင်သည့် အနားယူခွင့်နှင့် အားလပ်ခွင့် ခံစားပိုင်ခွင့် ရှိသည်။'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed to Convert Article TwentyFour")


if __name__ == "__main__":
    unittest.main()