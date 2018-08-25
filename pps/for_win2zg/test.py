import unittest
import win2uni
import uni2zg


class TESTZG2WIN(unittest.TestCase):
    def test_article_one(self):
        zawgyi = u'''အပိုဒ္ ၁
        လူတိုင္းသည္ တူညီ လြတ္လပ္ေသာ ဂုဏ္သိကၡာျဖင့္ လည္းေကာင္း၊ တူညီလြတ္လပ္ေသာ အခြင့္အေရးမ်ားျဖင့္ လည္းေကာင္း၊ ေမြးဖြားလာသူမ်ား ျဖစ္သည္။ 
        ထိုသူတို႔၌ ပိုင္းျခား ေဝဖန္တတ္ေသာ ဉာဏ္ႏွင့္ က်င့္ဝတ္ သိတတ္ေသာ စိတ္တို႔ရွိၾက၍ ထိုသူတို႔သည္ အခ်င္းခ်င္း ေမတၱာထား၍ ဆက္ဆံက်င့္သုံးသင့္၏။'''
        win = u'''tydk'f 1
        vlwdkif;onf wlnD vGwfvyfaom *kPfodu©mjzihf vnf;aumif;? wlnDvGwfvyfaom tcGihfta&;rsm;jzihf vnf;aumif;? arG;zGm;vmolrsm; jzpfonf/ 
        xdkolwdkYü ydkif;jcm; a0zefwwfaom ÓPfESihf usihf0wf odwwfaom pdwfwdkY&SdMuí xdkolwdkYonf tcsif;csif; arwÅmxm;í qufqHusihfokH;oihf\/'''
        result = win2uni.convert(win)
        result = uni2zg.convert(result)
        self.assertEqual(zawgyi, result, "Failed to Convert Article One")

    def test_article_two(self):
        zawgyi = u'''အပိုဒ္ ၂
        လူတိုင္းသည္ လူ႔အခြင့္ အေရး ေၾကညာစာတမ္းတြင္ ေဖာ္ျပထားသည့္ အခြင့္အေရး အားလုံး၊ လြတ္လပ္ခြင့္ အားလုံးတို႔ကို ပိုင္ဆိုင္ ခံစားခြင့္ရွိသည္။ 
        လူမ်ိဳးႏြယ္အားျဖင့္ ျဖစ္ေစ၊ အသားအေရာင္အားျဖင့္ ျဖစ္ေစ၊ က်ား၊ မ၊ သဘာဝအားျဖင့္ ျဖစ္ေစ၊ ဘာသာစကားအားျဖင့္ ျဖစ္ေစ၊ ကိုးကြယ္သည့္ ဘာသာအားျဖင့္ ျဖစ္ေစ၊ 
        ႏိုင္ငံေရးယူဆခ်က္၊ သို႔တည္းမဟုတ္ အျခားယူဆခ်က္အားျဖင့္ ျဖစ္ေစ၊ ႏိုင္ငံႏွင့္ ဆိုင္ေသာ၊ သို႔တည္းမဟုတ္ လူမႈအဆင့္အတန္းႏွင့္ ဆိုင္ေသာ ဇစ္ျမစ္ အားျဖင့္ျဖစ္ေစ၊ 
        ပစၥည္း ဥစၥာ ဂုဏ္အားျဖင့္ ျဖစ္ေစ၊ မ်ိဳး႐ိုးဇာတိအားျဖင့္ ျဖစ္ေစ၊ အျခား အဆင့္အတန္း အားျဖင့္ ျဖစ္ေစ ခြဲျခားျခင္းမရွိေစရ။ ထို႔ျပင္ လူတစ္ဦး တစ္ေယာက္ 
        ေနထိုင္ရာ ႏိုင္ငံ၏ သို႔တည္းမဟုတ္ နယ္ေျမေဒသ၏ ႏိုင္ငံေရးဆိုင္ရာ ျဖစ္ေစ စီရင္ပိုင္ခြင့္ဆိုင္ရာ ျဖစ္ေစ တိုင္းျပည္ အခ်င္းခ်င္း ဆိုင္ရာျဖစ္ေစ၊ အဆင့္အတန္း တစ္ခုခုကို 
        အေျချပဳ၍ ေသာ္လည္းေကာင္း၊ ေဒသနယ္ေျမတစ္ခုသည္ အခ်ဳပ္အျခာ အာဏာပိုင္ လြတ္လပ္သည့္ နယ္ေျမ၊ သို႔တည္းမဟုတ္ ကုလသမဂၢ ထိန္းသိမ္း ေစာင့္ေရွာက္ ထားရသည့္ 
        နယ္ေျမ၊ သို႔တည္းမဟုတ္ ကိုယ္ပိုင္ အုပ္ခ်ဳပ္ခြင့္ အာဏာတို႔ တစိတ္တေဒသေလာက္သာ ရရွိသည့္ နယ္ေျမ စသျဖင့္ ယင္းသို႔ ေသာ နယ္ေျမမ်ား ျဖစ္သည္ 
        ဟူေသာ အေၾကာင္းကို အေထာက္အထား ျပဳ၍ ေသာ္လည္းေကာင္း ခြဲျခားျခင္း လုံးဝ မရွိေစရ။'''
        win = u'''tydk'f 2
        vlwdkif;onf vlYtcGihf ta&; aMunmpmwrf;wGif azmfjyxm;onhf tcGihfta&; tm;vkH;? vGwfvyfcGihf tm;vkH;wdkYudk ydkifqdkif cHpm;cGihf&Sdonf/ 
        vlrsdK;EG,ftm;jzihf jzpfap? tom;ta&miftm;jzihf jzpfap? usm;? r? obm0tm;jzihf jzpfap? bmompum;tm;jzihf jzpfap? udk;uG,fonhf bmomtm;jzihf jzpfap? 
        EdkifiHa&;,lqcsuf? odkYwnf;r[kwf tjcm;,lqcsuftm;jzihf jzpfap? EdkifiHESihf qdkifaom? odkYwnf;r[kwf vlrItqihftwef;ESihf qdkifaom Zpfjrpf tm;jzihfjzpfap? 
        ypönf; Opöm *kPftm;jzihf jzpfap? rsdK;½dk;Zmwdtm;jzihf jzpfap? tjcm; tqihftwef; tm;jzihf jzpfap cGJjcm;jcif;r&Sdap&/ xdkYjyif vlwpfOD; wpfa,muf 
        aexdkif&m EdkifiH\ odkYwnf;r[kwf e,fajra'o\ EdkifiHa&;qdkif&m jzpfap pD&ifydkifcGihfqdkif&m jzpfap wdkif;jynf tcsif;csif; qdkif&mjzpfap? tqihftwef; wpfckckudk 
        tajcûyí aomfvnf;aumif;? a'oe,fajrwpfckonf tcsKyftjcm tmPmydkif vGwfvyfonhf e,fajr? odkYwnf;r[kwf ukvor*¾ xdef;odrf; apmihfa&Smuf xm;&onhf 
        e,fajr? odkYwnf;r[kwf udk,fydkif tkyfcsKyfcGihf tmPmwdkY wpdwfwa'oavmufom &&Sdonhf e,fajr pojzihf ,if;odkY aom e,fajrrsm; jzpfonf 
        [laom taMumif;udk taxmuftxm; ûyí aomfvnf;aumif; cGJjcm;jcif; vkH;0 r&Sdap&/'''
        result = win2uni.convert(win)
        result = uni2zg.convert(result)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Two")

    def test_article_three(self):
        zawgyi = u'''အပိုဒ္ ၃
        လူတိုင္း၌ အသက္ရွင္ရန္ လြတ္လပ္မႈခြင့္ႏွင့္ လုံျခဳံစိတ္ခ်ခြင့္ ရွိသည္။'''
        win = u'''tydk'f 3
        vlwdkif;ü touf&Sif&ef vGwfvyfrIcGihfESihf vkHûcHpdwfcscGihf &Sdonf/'''
        result = win2uni.convert(win)
        result = uni2zg.convert(result)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Three")

    def test_article_four(self):
        zawgyi = u'''အပိုဒ္ ၄
        မည္သူကိုမၽွ ေက်းကၽြန္အျဖစ္၊ သို႔တည္းမဟုတ္ အေစအပါးအျဖစ္၊ ႏိုင္ထက္စီးနင္း ေစခိုင္းျခင္း မျပဳရ၊ လူကို ေက်းကၽြန္သဖြယ္ အဓမၼ ေစခိုင္းျခင္း၊ 
        အေရာင္းအဝယ္ ျပဳျခင္းႏွင့္ ထိုသေဘာ သက္ေရာက္ေသာ လုပ္ငန္းဟူသမၽွကို ပိတ္ပင္ တားျမစ္ ရမည္။'''
        win = u'''tydk'f 4
        rnfoludkrQ aus;uReftjzpf? odkYwnf;r[kwf taptyg;tjzpf? EdkifxufpD;eif; apcdkif;jcif; rûy&? vludk aus;uRefozG,f t"r® apcdkif;jcif;? 
        ta&mif;t0,f ûyjcif;ESihf xdkoabm oufa&mufaom vkyfief;[lorQudk ydwfyif wm;jrpf &rnf/'''
        result = win2uni.convert(win)
        result = uni2zg.convert(result)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Four")

    def test_article_five(self):
        zawgyi = u'''အပိုဒ္ ၅
        မည္သူကိုမၽွ ညႇဥ္းပန္း ႏွိပ္စက္ျခင္း၊ သို႔တည္းမဟုတ္ ရက္စက္ၾကမ္းၾကဳတ္စြာ လူမဆန္စြာ ဂုဏ္ငယ္ေစေသာ ဆက္ဆံမႈ မျပဳရ၊ သို႔တည္းမဟုတ္ အျပစ္ဒဏ္ ေပးျခင္းမျပဳရ။'''
        win = u'''tydk'f 5
        rnfoludkrQ n§Of;yef; ESdyfpufjcif;? odkYwnf;r[kwf &ufpufMurf;êuwfpGm vlrqefpGm *kPfi,fapaom qufqHrI rûy&? odkYwnf;r[kwf tjypf'Pf ay;jcif;rûy&/'''
        result = win2uni.convert(win)
        result = uni2zg.convert(result)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Five")

    def test_article_six(self):
        zawgyi = u'''အပိုဒ္ ၆
        လူတိုင္းတြင္ ဥပေဒအရာ၌ လူပုဂၢိဳလ္တစ္ဦး အျဖစ္ျဖင့္ အရာခပ္သိမ္းတြင္ အသိအမွတ္ ျပဳျခင္းကို ခံယူပိုင္ခြင့္ရွိသည္။'''
        win = u'''tydk'f 6
        vlwdkif;wGif Oya't&mü vlyk*¾dKvfwpfOD; tjzpfjzihf t&mcyfodrf;wGif todtrSwf ûyjcif;udk cH,lydkifcGihf&Sdonf/'''
        result = win2uni.convert(win)
        result = uni2zg.convert(result)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Six")

    def test_article_seven(self):
        zawgyi = u'''အပိုဒ္ ၇
        လူအားလုံးတို႔သည္ ဥပေဒအရာ၌ တူညီၾကသည့္အျပင္၊ ဥပေဒ၏ အကာအကြယ္ကို ျခားနားျခင္း မခံရေစဘဲ တူညီစြာ ခံစားပိုင္ခြင့္ရွိသည္။ 
        ဤေၾကညာ စာတမ္းပါ သေဘာတရားမ်ားကို ဖီဆန္၍ ခြဲျခားျခင္းမွ လည္းေကာင္း၊ ထိုသို႔ခြဲျခားျခင္းကို လႈံ႕ေဆာ္ျခင္းမွ လည္းေကာင္း၊ 
        ကင္းလြတ္ ေစရန္ အကာအကြယ္ကို တူညီစြာ ခံစားပိုင္ခြင့္ ရွိသည္။'''
        win = u'''tydk'f 7
        vltm;vkH;wdkYonf Oya't&mü wlnDMuonhftjyif? Oya'\ tumtuG,fudk jcm;em;jcif; rcH&apbJ wlnDpGm cHpm;ydkifcGihf&Sdonf/ 
        þaMunm pmwrf;yg oabmw&m;rsm;udk zDqefí cGJjcm;jcif;rS vnf;aumif;? xdkodkYcGJjcm;jcif;udk vIHYaqmfjcif;rS vnf;aumif;? 
        uif;vGwf ap&ef tumtuG,fudk wlnDpGm cHpm;ydkifcGihf &Sdonf/'''
        result = win2uni.convert(win)
        result = uni2zg.convert(result)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Seven")

    def test_article_eight(self):
        zawgyi = u'''အပိုဒ္ ၈
        ဖြဲ႕စည္းပုံ အေျခခံဥပေဒက ေသာ္လည္းေကာင္း အျခား ဥပေဒက ေသာ္လည္းေကာင္း လူတိုင္းအတြက္ ေပးထားသည့္ အေျခခံ အခြင့္အေရး မ်ားသည္ 
        ခ်ိဳးေဖာက္ ဖ်က္ဆီးျခင္းခံခဲ့ရလၽွင္ ထိုသို႔ ခ်ိဳးေဖာက္ဖ်က္ဆီး ေသာ ျပဳလုပ္မႈေၾကာင့္ ျဖစ္ေပၚလာေသာ နစ္နာခ်က္ အတြက္ ထိုသူသည္ ႏိုင္ငံဆိုင္ရာ 
        အာဏာပိုင္တရား႐ုံးတြင္ ထိေရာက္စြာ သက္သာခြင့္ ရွိႏိုင္ေစရမည္။'''
        win = u'''tydk'f 8
        zGJUpnf;ykH tajccHOya'u aomfvnf;aumif; tjcm; Oya'u aomfvnf;aumif; vlwdkif;twGuf ay;xm;onhf tajccH tcGihfta&; rsm;onf 
        csdK;azmuf zsufqD;jcif;cHcJh&vQif xdkodkY csdK;azmufzsufqD; aom ûyvkyfrIaMumihf jzpfay:vmaom epfemcsuf twGuf xdkolonf EdkifiHqdkif&m 
        tmPmydkifw&m;½kH;wGif xda&mufpGm oufomcGihf &SdEdkifap&rnf/'''
        result = win2uni.convert(win)
        result = uni2zg.convert(result)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Eight")

    def test_article_nine(self):
        zawgyi = u'''အပိုဒ္ ၉
        မည္သူမၽွ ဥပေဒအရ မဟုတ္ေသာ ဖမ္းဆီးျခင္းကို ျဖစ္ေစ၊ ခ်ဳပ္ေႏွာင္ျခင္းကို ျဖစ္ေစ၊ ျပည္ႏွင္ျခင္းကိုျဖစ္ေစ မခံေစရ။'''
        win = u'''tydk'f 9
        rnfolrQ Oya't& r[kwfaom zrf;qD;jcif;udk jzpfap? csKyfaESmifjcif;udk jzpfap? jynfESifjcif;udkjzpfap rcHap&/'''
        result = win2uni.convert(win)
        result = uni2zg.convert(result)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Nine")

    def test_article_ten(self):
        zawgyi = u'''အပိုဒ္ ၁ဝ
        အခြင့္အေရးမ်ားႏွင့္ တာဝန္ ဝတၱရားမ်ားကို အဆုံးအျဖတ္ခံရာတြင္ လည္းေကာင္း၊ ျပစ္မႈေၾကာင့္ တရားစြဲဆို စီရင္ ဆုံးျဖတ္ခံရာတြင္ လည္းေကာင္း၊ 
        လူတိုင္းသည္ လြတ္လပ္၍ ဘက္မလိုက္ေသာ တရား႐ုံးေတာ္၏ လူအမ်ား ေရွ႕ေမွာက္တြင္ မၽွတစြာ ၾကားနာစစ္ေဆးျခင္းကို တူညီစြာ ခံစား ပိုင္ခြင့္ရွိသည္။'''
        win = u'''tydk'f 10
        tcGihfta&;rsm;ESihf wm0ef 0wÅ&m;rsm;udk tqkH;tjzwfcH&mwGif vnf;aumif;? jypfrIaMumihf w&m;pGJqdk pD&if qkH;jzwfcH&mwGif vnf;aumif;? 
        vlwdkif;onf vGwfvyfí bufrvdkufaom w&m;½kH;awmf\ vltrsm; a&SUarSmufwGif rQwpGm Mum;emppfaq;jcif;udk wlnDpGm cHpm; ydkifcGihf&Sdonf/'''
        result = win2uni.convert(win)
        result = uni2zg.convert(result)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Ten")

    def test_article_eleven(self):
        zawgyi = u'''အပိုဒ္ ၁၁
        လူအမ်ား ေရွ႕ေမွာက္၌ ဥပေဒအတိုင္း စစ္ေဆး၍ ျပစ္မႈက်ဴးလြန္သည္ဟု ထင္ရွား စီရင္ျခင္းခံရသည့္ အခ်ိန္အထိ ျပစ္မႈႏွင့္ 
        တရားစြဲဆိုျခင္း ခံရသူတိုင္းသည္ အျပစ္မဲ့သူဟူ၍ ယူဆ ျခင္းခံထိုက္သည့္ အခြင့္အေရးရွိသည္။ ထိုအမႈကို ၾကားနာစစ္ေဆးရာဝယ္ 
        စြပ္စြဲခံရသည့္ ျပစ္မႈအတြက္ ခုခံေခ်ပႏိုင္ရန္ လိုအပ္ေသာ အခြင့္အေရးမ်ားကို ထိုသူအား ေပးၿပီး ျဖစ္ေစရမည္။
        လူတစ္ဦးတစ္ေယာက္အား ႏိုင္ငံဥပေဒအရျဖစ္ေစ၊ အျပည္ျပည္ဆိုင္ရာ ဥပေဒအရ ျဖစ္ေစ၊ ျပစ္မႈမေျမာက္ေသာ လုပ္ရပ္ သို႔မဟုတ္ ပ်က္ကြက္မႈအရ 
        ဆြဲဆိုျပစ္ေပးျခင္း မျပဳရ။ ထို႔အျပင္ ျပစ္မႈက်ဴးလြန္စဥ္အခါက ထိုက္သင့္ေစႏိုင္ေသာ အျပစ္ဒဏ္ထက္ပိုမိုႀကီးေလးေသာ အျပစ္ဒဏ္ကို ထိုက္သင့္ျခင္းမရွိေစရ။'''
        win = u'''tydk'f 11
        vltrsm; a&SUarSmufü Oya'twdkif; ppfaq;í jypfrIusL;vGefonf[k xif&Sm; pD&ifjcif;cH&onhf tcsdeftxd jypfrIESihf 
        w&m;pGJqdkjcif; cH&olwdkif;onf tjypfrJhol[lí ,lq jcif;cHxdkufonhf tcGihfta&;&Sdonf/ xdktrIudk Mum;emppfaq;&m0,f 
        pGyfpGJcH&onhf jypfrItwGuf ckcHacsyEdkif&ef vdktyfaom tcGihfta&;rsm;udk xdkoltm; ay;NyD; jzpfap&rnf/
        vlwpfOD;wpfa,muftm; EdkifiHOya't&jzpfap? tjynfjynfqdkif&m Oya't& jzpfap? jypfrIrajrmufaom vkyf&yf odkYr[kwf ysufuGufrIt& 
        qGJqdkjypfay;jcif; rûy&/ xdkYtjyif jypfrIusL;vGefpOftcgu xdkufoihfapEdkifaom tjypf'PfxufydkrdkBuD;av;aom tjypf'Pfudk xdkufoihfjcif;r&Sdap&/'''
        result = win2uni.convert(win)
        result = uni2zg.convert(result)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Eleven")

    def test_article_twelve(self):
        zawgyi = u'''အပိုဒ္ ၁၂
        မည္သူမၽွ မိမိသေဘာအတိုင္း ေအးခ်မ္းလြတ္လပ္စြာ ေနထိုင္ျခင္းကို ေသာ္လည္းေကာင္း၊ မိမိ၏ မိသားစုကို ေသာ္လည္းေကာင္း၊ 
        မိမိ၏ ေနအိမ္ အသိုက္အဝန္းကို ေသာ္လည္းေကာင္း၊ စာေပးစာယူကို ေသာ္လည္းေကာင္း၊ ဥပေဒအရ မဟုတ္ေသာ ဝင္ေရာက္ စြက္ဖက္ျခင္း မခံေစရ။ 
        ထို႔ျပင္ မိမိ၏ဂုဏ္သိကၡာ ကိုလည္း အထက္ပါ အတိုင္း ပုတ္ခတ္ျခင္း မခံေစရ။ လူတိုင္းတြင္ ထိုသို႔ ဝင္ေရာက္စြက္ဖက္ျခင္းမွ ေသာ္လည္းေကာင္း 
        ပုတ္ခတ္ျခင္းမွ ေသာ္လည္းေကာင္း ဥပေဒအရ ကာကြယ္ ပိုင္ခြင့္ရွိသည္။'''
        win = u'''tydk'f 12
        rnfolrQ rdrdoabmtwdkif; at;csrf;vGwfvyfpGm aexdkifjcif;udk aomfvnf;aumif;? rdrd\ rdom;pkudk aomfvnf;aumif;? 
        rdrd\ aetdrf todkuft0ef;udk aomfvnf;aumif;? pmay;pm,ludk aomfvnf;aumif;? Oya't& r[kwfaom 0ifa&muf pGufzufjcif; rcHap&/ 
        xdkYjyif rdrd\*kPfodu©m udkvnf; txufyg twdkif; ykwfcwfjcif; rcHap&/ vlwdkif;wGif xdkodkY 0ifa&mufpGufzufjcif;rS aomfvnf;aumif; 
        ykwfcwfjcif;rS aomfvnf;aumif; Oya't& umuG,f ydkifcGihf&Sdonf/'''
        result = win2uni.convert(win)
        result = uni2zg.convert(result)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Twelve")

    def test_article_thirteen(self):
        zawgyi = u'''အပိုဒ္ ၁၃
        လူတိုင္းတြင္ မိမိ၏ႏိုင္ငံ နယ္နိမိတ္ အတြင္း၌ လြတ္လပ္စြာ သြားလာ ေရႊ႕ေျပာင္း ႏိုင္ခြင့္၊ ေနထိုင္ခြင့္ရွိသည္။
        လူတိုင္းတြင္ မိမိေနထိုင္ရာ တိုင္းျပည္မွ လည္းေကာင္း၊ အျခားတိုင္းျပည္မွလည္းေကာင္း ထြက္ခြာ သြားပိုင္ခြင့္ရွိသည့္အျပင္၊မိမိ၏ 
        တိုင္းျပည္သို႔ ျပန္လာ ပိုင္ခြင့္လည္းရွိသည္။'''
        win = u'''tydk'f 13
        vlwdkif;wGif rdrd\EdkifiH e,fedrdwf twGif;ü vGwfvyfpGm oGm;vm a½TUajymif; EdkifcGihf? aexdkifcGihf&Sdonf/
        vlwdkif;wGif rdrdaexdkif&m wdkif;jynfrS vnf;aumif;? tjcm;wdkif;jynfrSvnf;aumif; xGufcGm oGm;ydkifcGihf&Sdonhftjyif?rdrd\ 
        wdkif;jynfodkY jyefvm ydkifcGihfvnf;&Sdonf/'''
        result = win2uni.convert(win)
        result = uni2zg.convert(result)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Thirteen")

    def test_article_fourteen(self):
        zawgyi = u'''အပိုဒ္ ၁၄
        လူတိုင္းသည္ ညႇဥ္းပန္း ႏွိပ္စက္ ခံေနရျခင္းမွ လြတ္ကင္းရန္ အျခားတိုင္းျပည္ မ်ား၌ ေအးခ်မ္းစြာ ခိုလႈံေနႏိုင္ခြင့္ရွိသည္။
        ႏိုင္ငံေရးႏွင့္ မပတ္သက္သည့္ ျပစ္မႈမ်ားမွ ေသာ္လည္းေကာင္း၊ ကုလသမဂၢ၏ ရည္ရြက္ခ်က္ႏွင့္ သေဘာတရား မႈမ်ားကို 
        ဖီဆန္ေသာ အမႈမ်ားမွ ေသာ္လည္းေကာင္း၊ အမွန္ ေပၚေပါက္ လာေသာ ျပစ္မႈေၾကာင့္ တရားစြဲဆိုျခင္း ခံရသည့္ အမႈအခင္းမ်ားတြင္ 
        အထက္ပါ အခြင့္အေရးကို အသုံးမျပဳႏိုင္ေစရ။'''
        win = u'''tydk'f 14
        vlwdkif;onf n§Of;yef; ESdyfpuf cHae&jcif;rS vGwfuif;&ef tjcm;wdkif;jynf rsm;ü at;csrf;pGm cdkvIHaeEdkifcGihf&Sdonf/
        EdkifiHa&;ESihf rywfoufonhf jypfrIrsm;rS aomfvnf;aumif;? ukvor*¾\ &nf½GufcsufESihf oabmw&m; rIrsm;udk 
        zDqefaom trIrsm;rS aomfvnf;aumif;? trSef ay:ayguf vmaom jypfrIaMumihf w&m;pGJqdkjcif; cH&onhf trItcif;rsm;wGif 
        txufyg tcGihfta&;udk tokH;rûyEdkifap&/'''
        result = win2uni.convert(win)
        result = uni2zg.convert(result)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Fourteen")

    def test_article_fifteen(self):
        zawgyi = u'''အပိုဒ္ ၁၅
        လူတိုင္းသည္၊ ႏိုင္ငံ တစ္ႏိုင္ငံ၏ ႏိုင္ငံသားအျဖစ္ ခံယူခြင့္ရွိသည္။
        ဥပေဒအရ မဟုတ္လၽွင္ မည္သူမၽွ မိမိ၏ ႏိုင္ငံသားအျဖစ္ကို စြန႔္လႊတ္ျခင္း မခံေစရ၊ ႏိုင္ငံသားအျဖစ္ ေျပာင္းလဲႏိုင္ေသာ
        အခြင့္အေရးကို လည္း ျငင္းပယ္ျခင္း မခံေစရ။'''
        win = u'''tydk'f 15
        vlwdkif;onf? EdkifiH wpfEdkifiH\ EdkifiHom;tjzpf cH,lcGihf&Sdonf/
        Oya't& r[kwfvQif rnfolrQ rdrd\ EdkifiHom;tjzpfudk pGeYfvTwfjcif; rcHap&? EdkifiHom;tjzpf ajymif;vJEdkifaom
        tcGihfta&;udk vnf; jiif;y,fjcif; rcHap&/'''
        result = win2uni.convert(win)
        result = uni2zg.convert(result)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Fifteen")

    def test_article_sixteen(self):
        zawgyi = u'''အပိုဒ္ ၁၆
        အရြယ္ေရာက္ ၿပီးေသာ ေယာက်ာ္း ႏွင့္ မိန္းမတို႔တြင္ လူမ်ိဳးကို ေသာ္လည္းေကာင္း၊ ႏိုင္ငံသား အျဖစ္ကို ေသာ္လည္းေကာင္း 
        ကိုးကြယ္သည့္ ဘာသာကို ေသာ္လည္းေကာင္း၊ အေၾကာင္းျပဳ၍ ခ်ဳပ္ခ်ယ္ ကန႔္သတ္ျခင္း မရွိဘဲ၊ ထိမ္းျမားႏိုင္ခြင့္ ႏွင့္ မိသားစုထူေထာင္ႏိုင္ခြင့္ရွိသည္။ 
        အဆိုပါ ေယာက်ာ္းႏွင့္ မိန္းမ တို႔သည္ လင္မယားအျဖစ္ ေပါင္းသင္းေနစဥ္ အခ်ိန္ အတြင္း၌ ေသာ္လည္းေကာင္း၊ အိမ္ေထာင္ကို ဖ်က္သိမ္း၍ 
        ကြာရွင္းၾကသည့္ အခါ၌လည္းေကာင္း၊ လက္ထပ္ ေပါင္းသင္း အိမ္ေထာင္ျပဳျခင္းႏွင့္ စပ္လ်ဥ္းေသာ တူညီသည့္ အခြင့္အေရးမ်ားကို ရရွိထိုက္သည္။
        သတို႔သား ႏွင့္ သတို႔သမီး ႏွစ္ဦးႏွစ္ဘက္၏ လြတ္လပ္ေသာ သေဘာဆႏၵရွိမွသာလၽွင္ ထိမ္းျမားျခင္းကို ျပဳရမည္။
        မိသားစု တစ္ခုသည္ လူ႔အဖြဲ႕အစည္း၏ သဘာဝက်ေသာ အေျခခံအဖြဲ႕တစ္ရပ္ျဖစ္သည္၊ ထိုမိသားစုသည္ လူ႔ အဖြဲ႕အစည္းႏွင့္ 
        အစိုးရတို႔၏ ကာကြယ္ေစာင့္ေရွာက္ျခင္းကို ခံယူခြင့္ရွိသည္။'''
        win = u'''tydk'f 16
        t½G,fa&muf NyD;aom a,musmf; ESihf rdef;rwdkYwGif vlrsdK;udk aomfvnf;aumif;? EdkifiHom; tjzpfudk aomfvnf;aumif; 
        udk;uG,fonhf bmomudk aomfvnf;aumif;? taMumif;ûyí csKyfcs,f ueYfowfjcif; r&SdbJ? xdrf;jrm;EdkifcGihf ESihf rdom;pkxlaxmifEdkifcGihf&Sdonf/ 
        tqdkyg a,musmf;ESihf rdef;r wdkYonf vifr,m;tjzpf aygif;oif;aepOf tcsdef twGif;ü aomfvnf;aumif;? tdrfaxmifudk zsufodrf;í 
        uGm&Sif;Muonhf tcgüvnf;aumif;? vufxyf aygif;oif; tdrfaxmifûyjcif;ESihf pyfvsOf;aom wlnDonhf tcGihfta&;rsm;udk &&Sdxdkufonf/
        owdkYom; ESihf owdkYorD; ESpfOD;ESpfbuf\ vGwfvyfaom oabmqE´&SdrSomvQif xdrf;jrm;jcif;udk ûy&rnf/
        rdom;pk wpfckonf vlYtzGJUtpnf;\ obm0usaom tajccHtzGJUwpf&yfjzpfonf? xdkrdom;pkonf vlY tzGJUtpnf;ESihf 
        tpdk;&wdkY\ umuG,fapmihfa&Smufjcif;udk cH,lcGihf&Sdonf/'''
        result = win2uni.convert(win)
        result = uni2zg.convert(result)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Sixteen")

    def test_article_seventeen(self):
        zawgyi = u'''အပိုဒ္ ၁၇
        လူတိုင္းတြင္ မိမိ တစ္ဦးခ်င္းေသာ္လည္းေကာင္း ၊ အျခားသူမ်ားႏွင့္ ဖက္စပ္၍ ေသာ္လည္းေကာင္း၊ ပစၥည္းဥစၥာ တို႔ကို 
        ပိုင္ဆိုင္ရန္ အခြင့္အေရးရွိရမည္။ ဥပေဒအရ မဟုတ္လၽွင္၊ မည္သူမၽွ မိမိ၏ပစၥည္းဥစၥာပိုင္ဆိုင္ခြင့္ကို စြန႔္လႊတ္ျခင္း မခံေစရ။'''
        win = u'''tydk'f 17
        vlwdkif;wGif rdrd wpfOD;csif;aomfvnf;aumif; ? tjcm;olrsm;ESihf zufpyfí aomfvnf;aumif;? ypönf;Opöm wdkYudk 
        ydkifqdkif&ef tcGihfta&;&Sd&rnf/ Oya't& r[kwfvQif? rnfolrQ rdrd\ypönf;OpömydkifqdkifcGihfudk pGeYfvTwfjcif; rcHap&/'''
        result = win2uni.convert(win)
        result = uni2zg.convert(result)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Seventeen")

    def test_article_eighteen(self):
        zawgyi = u'''အပိုဒ္ ၁၈
        လူတိုင္းတြင္ လြတ္လပ္စြာ ေတြးေခၚ ႀကံဆႏိုင္ခြင့္၊ လြတ္လပ္စြာ ခံယူရပ္တည္ႏိုင္ခြင့္ ႏွင့္ လြတ္လပ္စြာ သက္ဝင္ ကိုးကြယ္ႏိုင္ခြင့္ရွိသည္။ 
        အဆိုပါ အခြင့္အေရးမ်ား၌ မိမိကိုးကြယ္သည့္ ဘာသာကို သို႔တည္းမဟုတ္ သက္ဝင္ယုံၾကည္ခ်က္ကို လြတ္လပ္စြာ ေျပာင္းလဲႏိုင္ခြင့္ ပါဝင္သည့္ အျပင္ 
        မိမိ တစ္ေယာက္ခ်င္းျဖစ္ေစ၊ အျခားသူမ်ားႏွင့္ စုေပါင္း၍ျဖစ္ေစ၊ ျပည္သူအမ်ား ေရွ႕ေမွာက္တြင္ ေသာ္လည္းေကာင္း၊ ေရွ႕ေမွာက္တြင္ 
        မဟုတ္ဘဲ ေသာ္လည္းေကာင္း၊ မိမိ ကိုးကြယ္ေသာ ဘာသာကို သို႔တည္းမဟုတ္ သက္ဝင္ ယုံၾကည္ခ်က္ကို လြတ္လပ္ စြာ သင္ျပႏိုင္ခြင့္၊ 
        က်င့္သုံးႏိုင္ခြင့္၊ ဝတ္ျပဳကိုးကြယ္ႏိုင္ခြင့္ႏွင့္ ေဆာက္တည္ ႏိုင္ခြင့္တို႔လည္း ပါဝင္သည္။'''
        win = u'''tydk'f 18
        vlwdkif;wGif vGwfvyfpGm awG;ac: BuHqEdkifcGihf? vGwfvyfpGm cH,l&yfwnfEdkifcGihf ESihf vGwfvyfpGm ouf0if udk;uG,fEdkifcGihf&Sdonf/ 
        tqdkyg tcGihfta&;rsm;ü rdrdudk;uG,fonhf bmomudk odkYwnf;r[kwf ouf0if,kHMunfcsufudk vGwfvyfpGm ajymif;vJEdkifcGihf yg0ifonhf tjyif 
        rdrd wpfa,mufcsif;jzpfap? tjcm;olrsm;ESihf pkaygif;íjzpfap? jynfoltrsm; a&SUarSmufwGif aomfvnf;aumif;? a&SUarSmufwGif 
        r[kwfbJ aomfvnf;aumif;? rdrd udk;uG,faom bmomudk odkYwnf;r[kwf ouf0if ,kHMunfcsufudk vGwfvyf pGm oifjyEdkifcGihf? 
        usihfokH;EdkifcGihf? 0wfûyudk;uG,fEdkifcGihfESihf aqmufwnf EdkifcGihfwdkYvnf; yg0ifonf/'''
        result = win2uni.convert(win)
        result = uni2zg.convert(result)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Eighteen")

    def test_article_nineteen(self):
        zawgyi = u'''အပိုဒ္ ၁၉
        လူတိုင္းတြင္ လြတ္လပ္စြာ ထင္ျမင္ ယူဆႏိုင္ခြင့္ႏွင့္ လြတ္လပ္စြာ ဖြင့္ဟ ေဖာ္ျပႏိုင္ခြင့္ရွိသည္။ အဆိုပါ အခြင့္အေရးမ်ား၌ 
        အေႏွာင့္ အယွက္မရွိဘဲ လြတ္လပ္စြာ ထင္ျမင္ယူဆႏိုင္ခြင့္ ပါဝင္ သည့္အျပင္၊ ႏိုင္ငံနယ္နိမိတ္မ်ားကို ေထာက္ထားရန္ မလိုဘဲ 
        သတင္းအေၾကာင္းအရာႏွင့္ သေဘာတရားမ်ားကို တနည္းနည္း ျဖင့္ လြတ္လပ္စြာ ရွာယူဆည္းပူးႏိုင္ခြင့္၊ လက္ခံႏိုင္ခြင့္ႏွင့္ ေဝငွ ျဖန႔္ခ်ိခြင့္တို႔လည္း ပါဝင္သည္။'''
        win = u'''tydk'f 19
        vlwdkif;wGif vGwfvyfpGm xifjrif ,lqEdkifcGihfESihf vGwfvyfpGm zGihf[ azmfjyEdkifcGihf&Sdonf/ tqdkyg tcGihfta&;rsm;ü 
        taESmihf t,Sufr&SdbJ vGwfvyfpGm xifjrif,lqEdkifcGihf yg0if onhftjyif? EdkifiHe,fedrdwfrsm;udk axmufxm;&ef rvdkbJ 
        owif;taMumif;t&mESihf oabmw&m;rsm;udk wenf;enf; jzihf vGwfvyfpGm &Sm,lqnf;yl;EdkifcGihf? vufcHEdkifcGihfESihf a0iS jzeYfcsdcGihfwdkYvnf; yg0ifonf/'''
        result = win2uni.convert(win)
        result = uni2zg.convert(result)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Nineteen")

    def test_article_twenty(self):
        zawgyi = u'''အပိုဒ္ ၂ဝ
        လူတိုင္းတြင္ လြတ္လပ္ ေအးခ်မ္းစြာ စုေဝးႏိုင္ခြင့္ ႏွင့္ ဖြဲ႕စည္းႏိုင္ခြင့္ တို႔ ရွိသည္။
        မည္သူ႔ကိုမၽွ အဖြဲ႕အစည္းတစ္ခုသို႔ ဝင္ေစရန္ အတင္းအက်ပ္မျပဳရ။'''
        win = u'''tydk'f 20
        vlwdkif;wGif vGwfvyf at;csrf;pGm pka0;EdkifcGihf ESihf zGJUpnf;EdkifcGihf wdkY &Sdonf/
        rnfolYudkrQ tzGJUtpnf;wpfckodkY 0ifap&ef twif;tusyfrûy&/'''
        result = win2uni.convert(win)
        result = uni2zg.convert(result)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Twenty")

    def test_article_twentyone(self):
        zawgyi = u'''အပိုဒ္ ၂၁
        လူတိုင္းတြင္ မိမိႏိုင္ငံ၏ အုပ္ခ်ဳပ္ေရး၌ ကိုယ္တိုင္ျဖစ္ေစ၊ လြတ္လပ္စြာ ေရြးခ်ယ္လိုက္သည့္ ကိုယ္စားလွယ္မ်ားမွ တစ္ဆင့္ျဖစ္ေစ ပါဝင္ ေဆာင္ရြက္ႏိုင္ခြင့္ ရွိသည္။
        လူတိုင္းတြင္ မိမိ၏ႏိုင္ငံရွိ ျပည္သူ႔ ဝန္ထမ္းအဖြဲ႕၌ ဝင္ေရာက္ႏိုင္ရန္ တူညီသည့္ အခြင့္ အေရးရွိသည္။
        ျပည္သူျပည္သားတို႔၏ ဆႏၵသည္ အုပ္ခ်ဳပ္ အာဏာ၏ အေျခခံျဖစ္ရမည္၊ အဆိုပါ ဆႏၵကို အခ်ိန္ကာလပိုင္းျခားလ်က္ စစ္မွန္ေသာေရြးေကာက္ပြဲမ်ားျဖင့္ 
        ထင္ရွားေစရမည္။ ေရြးေကာက္ ပြဲမ်ားတြင္လည္း လူတိုင္းအညီအမၽွ ဆႏၵမဲ ေပးႏိုင္ခြင့္ ရွိရမည့္အျပင္ ၊ ထိုေရြးေကာက္ပြဲမ်ားကို 
        လၽွိဳ႕ဝွက္ မဲေပး စနစ္ျဖင့္ ျဖစ္ေစ၊ အလားတူ လြတ္လပ္ေသာ မဲေပးစနစ္ ျဖင့္ျဖစ္ေစ က်င္းပရမည္။'''
        win = u'''tydk'f 21
        vlwdkif;wGif rdrdEdkifiH\ tkyfcsKyfa&;ü udk,fwdkifjzpfap? vGwfvyfpGm a½G;cs,fvdkufonhf udk,fpm;vS,frsm;rS wpfqihfjzpfap yg0if aqmif½GufEdkifcGihf &Sdonf/
        vlwdkif;wGif rdrd\EdkifiH&Sd jynfolY 0efxrf;tzGJUü 0ifa&mufEdkif&ef wlnDonhf tcGihf ta&;&Sdonf/
        jynfoljynfom;wdkY\ qE´onf tkyfcsKyf tmPm\ tajccHjzpf&rnf? tqdkyg qE´udk tcsdefumvydkif;jcm;vsuf ppfrSefaoma½G;aumufyGJrsm;jzihf 
        xif&Sm;ap&rnf/ a½G;aumuf yGJrsm;wGifvnf; vlwdkif;tnDtrQ qE´rJ ay;EdkifcGihf &Sd&rnhftjyif ? xdka½G;aumufyGJrsm;udk 
        vQdKY0Suf rJay; pepfjzihf jzpfap? tvm;wl vGwfvyfaom rJay;pepf jzihfjzpfap usif;y&rnf/'''
        result = win2uni.convert(win)
        result = uni2zg.convert(result)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Twenty One")

    def test_article_twentytwo(self):
        zawgyi = u'''အပိုဒ္ ၂၂
        လူတိုင္းတြင္ လူ႔အဖြဲ႕အစည္း၏ အဖြဲ႕ဝင္တစ္ဦးအေနႏွင့္ လူမႈေရးလုံျခဳံခြင့္ရယူပိုင့္ခြင့္ရွိသည့္ အျပင္ႏိုင္ငံေရး ႀကိဳးပမ္းမႈျဖင့္ျဖစ္ေစ၊ 
        ႏိုင္ငံတကာ ပူေပါင္းေဆာင္ရြက္မႈျဖင့္ျဖစ္ေစ၊ ႏိုင္ငံအသီးသီး၏ဖြဲ႕စည္းပုံႏွင့္ လည္းေကာင္း၊ သယံဇာတ အင္အားႏွင့္လည္းေကာင္း 
        ထိုလူ၏ ဂုဏ္သိကၡာႏွင့္ စ႐ိုက္လကၡဏာ လြတ္လပ္စြာ တိုးတက္ျမင့္မားေရးအတြက္ မရွိမျဖစ္လိုအပ္ေသာ စီးပြားေရး၊လူမႈေရးႏွင့္ 
        ယဥ္ေက်းမႈ အခြင့္အေရးမ်ားကို သုံးစြဲပိုင္ခြင့္ရွိသည္။'''
        win = u'''tydk'f 22
        vlwdkif;wGif vlYtzGJUtpnf;\ tzGJU0ifwpfOD;taeESihf vlrIa&;vkHûcHcGihf&,lydkihfcGihf&Sdonhf tjyifEdkifiHa&; BudK;yrf;rIjzihfjzpfap? 
        EdkifiHwum ylaygif;aqmif½GufrIjzihfjzpfap? EdkifiHtoD;oD;\zGJUpnf;ykHESihf vnf;aumif;? o,HZmw tiftm;ESihfvnf;aumif; 
        xdkvl\ *kPfodu©mESihf p½dkufvu©Pm vGwfvyfpGm wdk;wufjrihfrm;a&;twGuf r&Sdrjzpfvdktyfaom pD;yGm;a&;?vlrIa&;ESihf 
        ,Ofaus;rI tcGihfta&;rsm;udk okH;pGJydkifcGihf&Sdonf/'''
        result = win2uni.convert(win)
        result = uni2zg.convert(result)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Twenty Two")

    def test_article_twentythree(self):
        zawgyi = u'''အပိုဒ္ ၂၃
        လူတိုင္းတြင္ အလုပ္လုပ္ ရန္လည္းေကာင္း၊ မိမိႏွစ္သက္ရာ အသက္ေမြးမႈ အလုပ္ အကိုင္ကို လြတ္လပ္စြာေရြးခ်ယ္ရန္ လည္းေကာင္း၊ တရားမၽွတ၍ 
        လုပ္ေပ်ာ္ေသာ အလုပ္ခြင္၏ အေျခအေနကို ရရွိရန္ လည္းေကာင္း၊ အလုပ္လက္မဲ့ ျဖစ္ရျခင္းမွ အကာအကြယ္ ရရွိရန္ လည္းေကာင္း အခြင့္အေရးရွိသည္။
        လူတိုင္းတြင္ ခြဲျခားျခင္းမခံရေစဘဲ၊ တူညီေသာ အလုပ္အတြက္ တူညီေသာ အခေၾကးေငြ ရပိုင္ခြင့္ရွိသည္။
        အလုပ္လုပ္ကိုင္သည့္ လူတိုင္းတြင္၊ မိမိႏွင့္ မိမိ၏ မိသားစုအတြက္ လူ႔ဂုဏ္သိကၡာ ႏွင့္ ညီေအာင္ ေနထိုင္ စားေသာက္ႏိုင္ရန္၊ စိတ္ခ်ေလာက္သည့္ျပင္၊ 
        တရား မၽွတ၍ လုပ္ေပ်ာ္သည့္ လစာေၾကးေငြ ရပိုင္ခြင့္ရွိသည္။ လိုအပ္ခဲ့လၽွင္အျခား နည္းလမ္းမ်ားမွ လူမႈေရး အေထာက္အပံ့ကိုလည္း ထပ္မံ၍ ရပိုင္ခြင့္ ရွိသည္။
        လူတိုင္းတြင္ မိမိအက်ိဳး ခံစားခြင့္ကို ကာကြယ္ရန္ အလုပ္သမား အစည္းအ႐ုံးမ်ား ဖြဲ႕စည္းခြင့္ ၊ ပါဝင္ ေဆာင္ရြက္ခြင့္ ရွိသည္။'''
        win = u'''tydk'f 23
        vlwdkif;wGif tvkyfvkyf &efvnf;aumif;? rdrdESpfouf&m toufarG;rI tvkyf tudkifudk vGwfvyfpGma½G;cs,f&ef vnf;aumif;? w&m;rQwí 
        vkyfaysmfaom tvkyfcGif\ tajctaeudk &&Sd&ef vnf;aumif;? tvkyfvufrJh jzpf&jcif;rS tumtuG,f &&Sd&ef vnf;aumif; tcGihfta&;&Sdonf/
        vlwdkif;wGif cGJjcm;jcif;rcH&apbJ? wlnDaom tvkyftwGuf wlnDaom tcaMu;aiG &ydkifcGihf&Sdonf/
        tvkyfvkyfudkifonhf vlwdkif;wGif? rdrdESihf rdrd\ rdom;pktwGuf vlY*kPfodu©m ESihf nDatmif aexdkif pm;aomufEdkif&ef? pdwfcsavmufonhfjyif? 
        w&m; rQwí vkyfaysmfonhf vpmaMu;aiG &ydkifcGihf&Sdonf/ vdktyfcJhvQiftjcm; enf;vrf;rsm;rS vlrIa&; taxmuftyHhudkvnf; xyfrHí &ydkifcGihf &Sdonf/
        vlwdkif;wGif rdrdtusdK; cHpm;cGihfudk umuG,f&ef tvkyform; tpnf;t½kH;rsm; zGJUpnf;cGihf ? yg0if aqmif½GufcGihf &Sdonf/'''
        result = win2uni.convert(win)
        result = uni2zg.convert(result)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Three")

    def test_article_twentyfour(self):
        zawgyi = u'''အပိုဒ္ ၂၄
        လူတိုင္းတြင္ သင့္ျမတ္ေလ်ာ္ကန္စြာ ကန႔္သတ္ထားသည့္ အလုပ္လုပ္ခ်ိန္ အျပင္၊ လစာႏွင့္တကြ အခါကာလအားေလ်ာ္စြာ သတ္မွတ္ ထားသည့္ 
        အလုပ္ အားလပ္ရက္မ်ားပါဝင္သည့္ အနားယူခြင့္ႏွင့္ အားလပ္ခြင့္ ခံစားပိုင္ခြင့္ ရွိသည္။'''
        win = u'''tydk'f 24
        vlwdkif;wGif oihfjrwfavsmfuefpGm ueYfowfxm;onhf tvkyfvkyfcsdef tjyif? vpmESihfwuG tcgumvtm;avsmfpGm owfrSwf xm;onhf 
        tvkyf tm;vyf&ufrsm;yg0ifonhf tem;,lcGihfESihf tm;vyfcGihf cHpm;ydkifcGihf &Sdonf/'''
        result = win2uni.convert(win)
        result = uni2zg.convert(result)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Four")

    def test_article_twentyfive(self):
        zawgyi = u'''အပိုဒ္ ၂၅
        လူတိုင္းတြင္ မိမိႏွင့္တကြ မိမိ၏ မိသားစု က်န္းမာေရးႏွင့္တကြ ကိုယ္စိတ္ႏွစ္ျဖာ ေအးခ်မ္းစြာ ေနထိုင္ႏိုင္ေရး အတြက္ အစာအဟာရ၊ 
        အဝတ္အထည္ ေနအိမ္၊ ေဆးဝါး အကူအညီႏွင့္ လိုအပ္သည့္ လူမႈ အေထာက္အပံ့မ်ား ပါဝင္ေသာ သင့္ေတာ္ ေလၽွာက္ပတ္သည့္ လူမႈ အဆင့္အတန္းကို 
        ရယူခံစားခြင့္ ရွိသည္။ ထို႔ျပင္ အလုပ္လက္မဲ့ျဖစ္ေသာ အခါ၌ ေသာ္လည္းေကာင္း၊ မက်န္းမမာ ျဖစ္ေသာ အခါ၌ ေသာ္လည္းေကာင္း၊ 
        ကိုယ္အဂၤါ မစြမ္း မသန္ျဖစ္ေသာ အခါ၌ ေသာ္လည္းေကာင္း၊ မုဆိုးမျဖစ္ေသာအခါ၌ ေသာ္လည္းေကာင္း၊ အသက္အရြယ္အိုမင္းေသာ အခါ၌ 
        ေသာ္လည္းေကာင္း၊ မိမိကိုယ္တိုင္က မတတ္ႏိုင္ေသာ အေၾကာင္းေၾကာင့္ ဝမ္းစာ ရွာမွီးႏိုင္ေသာ နည္းလမ္း မရွိေသာ အခါ၌ 
        ေသာ္လည္းေကာင္း၊ ေနထိုင္စားေသာက္ေရးအတြက္ လုံျခဳံစိတ္ခ်ရမႈ အခြင့္အေရးရွိသည္။
        သားသည္ မိခင္မ်ားႏွင့္ ကေလးမ်ားသည္ အထူးေစာင့္ေရွာက္ျခင္းႏွင့္ အကူအညီေပးျခင္းကို ရခြင့္ ရွိသည္။ ဥပေဒအရ ထိမ္းျမားျခင္းျဖင့္ျဖစ္ေစ 
        အျခား နည္းျဖင့္ ျဖစ္ေစ ေမြးဖြားေသာ ကေလးအားလုံး သည္ တူညီေသာ လူမႈ ကာကြယ္ ေစာင့္ေရွာက္ေရးကို ရယူ ခံစားၾကရမည္။'''
        win = u'''tydk'f 25
        vlwdkif;wGif rdrdESihfwuG rdrd\ rdom;pk usef;rma&;ESihfwuG udk,fpdwfESpfjzm at;csrf;pGm aexdkifEdkifa&; twGuf tpmt[m&? 
        t0wftxnf aetdrf? aq;0g; tultnDESihf vdktyfonhf vlrI taxmuftyHhrsm; yg0ifaom oihfawmf avQmufywfonhf vlrI tqihftwef;udk 
        &,lcHpm;cGihf &Sdonf/ xdkYjyif tvkyfvufrJhjzpfaom tcgü aomfvnf;aumif;? rusef;rrm jzpfaom tcgü aomfvnf;aumif;? 
        udk,ft*Fg rpGrf; roefjzpfaom tcgü aomfvnf;aumif;? rkqdk;rjzpfaomtcgü aomfvnf;aumif;? touft½G,ftdkrif;aom tcgü 
        aomfvnf;aumif;? rdrdudk,fwdkifu rwwfEdkifaom taMumif;aMumihf 0rf;pm &SmrSD;Edkifaom enf;vrf; r&Sdaom tcgü 
        aomfvnf;aumif;? aexdkifpm;aomufa&;twGuf vkHûcHpdwfcs&rI tcGihfta&;&Sdonf/
        om;onf rdcifrsm;ESihf uav;rsm;onf txl;apmihfa&Smufjcif;ESihf tultnDay;jcif;udk &cGihf &Sdonf/ Oya't& xdrf;jrm;jcif;jzihfjzpfap 
        tjcm; enf;jzihf jzpfap arG;zGm;aom uav;tm;vkH; onf wlnDaom vlrI umuG,f apmihfa&Smufa&;udk &,l cHpm;Mu&rnf/'''
        result = win2uni.convert(win)
        result = uni2zg.convert(result)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Five")

    def test_article_twentysix(self):
        zawgyi = u'''အပိုဒ္ ၂၆
        လူတိုင္းသည္ ပညာသင္ ယူႏိုင္ခြင့္ရွိသည္၊ အနည္းဆုံးမူလတန္းႏွင့္ အေျခခံ အဆင့္ အတန္းမ်ားတြင္ ပညာ သင္ၾကားေရးသည္ အခမဲ့ျဖစ္ရမည္။ 
        မူလတန္းပညာသည္ မသင္မေနရ ပညာ ျဖစ္ရမည္။ စက္မႈလက္မႈပညာႏွင့္ အသက္ေမြးမႈ ပညာမ်ားကို ေယဘူယ်အားျဖင့္ သင္ၾကားရယူ ႏိုင္ေစရမည္။ 
        ထို႔ျပင္ အထက္တန္းပညာအတြက္ အရည္အခ်င္းကို အေျခခံျပဳ၍ တူညီေသာ အခြင့္အေရး ရရွိေစရမည္။
        ပညာသင္ၾကားေရးကို လူသားတို႔၏ စ႐ိုက္လကၡဏာ အျပည့္အဝ တိုးတက္မႈ အျပင္၊ လူ႔အခြင့္အေရးႏွင့္ အေျခခံလြတ္လပ္ခြင့္ ႐ိုေသ 
        ေလးစားမႈ တို႔ကို ရွင္သန္ဖြံ႕ၿဖိဳးလာေစရန္ ရည္ရြယ္၍ သင္ၾကား ေစရမည္။ ပညာသင္ၾကားေရးသည္ ႏိုင္ငံ အားလုံး တို႔တြင္ လည္းေကာင္း၊ 
        လူမ်ိဳးစုမ်ား တြင္လည္းေကာင္း၊ ဘာသာေရးအသင္းအဖြဲ႕မ်ားတြင္ လည္းေကာင္း၊ အခ်င္းခ်င္းနားလည္မႈ၊ သည္းခံ မႈႏွင့္ ခင္မင္ရင္းႏွီးမႈတို႔ကို အားေပးရမည္။ 
        ထို႔ျပင္ ၿငိမ္းခ်မ္းေရး တည္တံ့ေအာင္ ေဆာင္ရြက္ရန္ အလို႔ငွါ၊ ကုလသမဂၢ၏ ေဆာင္ရြက္မႈမ်ားကိုလည္း ျဖစ္ေျမာက္ ေအာင္ အားေပးရမည္။
        မိဘတို႔တြင္၊ မိမိတို႔၏ ကေလးမ်ား သင္ယူရမည့္ပညာ အမ်ိဳးအစားကို ေရြးခ်ယ္ႏိုင္ေသာ လက္ဦး အခြင့္အေရးရွိသည္။'''
        win = u'''tydk'f 26
        vlwdkif;onf ynmoif ,lEdkifcGihf&Sdonf? tenf;qkH;rlvwef;ESihf tajccH tqihf twef;rsm;wGif ynm oifMum;a&;onf tcrJhjzpf&rnf/ 
        rlvwef;ynmonf roifrae& ynm jzpf&rnf/ pufrIvufrIynmESihf toufarG;rI ynmrsm;udk a,bl,stm;jzihf oifMum;&,l Edkifap&rnf/ 
        xdkYjyif txufwef;ynmtwGuf t&nftcsif;udk tajccHûyí wlnDaom tcGihfta&; &&Sdap&rnf/
        ynmoifMum;a&;udk vlom;wdkY\ p½dkufvu©Pm tjynhft0 wdk;wufrI tjyif? vlYtcGihfta&;ESihf tajccHvGwfvyfcGihf ½dkao 
        av;pm;rI wdkYudk &SifoefzGHUNzdK;vmap&ef &nf½G,fí oifMum; ap&rnf/ ynmoifMum;a&;onf EdkifiH tm;vkH; wdkYwGif vnf;aumif;? 
        vlrsdK;pkrsm; wGifvnf;aumif;? bmoma&;toif;tzGJUrsm;wGif vnf;aumif;? tcsif;csif;em;vnfrI? onf;cH rIESihf cifrif&if;ESD;rIwdkYudk tm;ay;&rnf/ 
        xdkYjyif Nidrf;csrf;a&; wnfwHhatmif aqmif½Guf&ef tvdkYiSg? ukvor*¾\ aqmif½GufrIrsm;udkvnf; jzpfajrmuf atmif tm;ay;&rnf/
        rdbwdkYwGif? rdrdwdkY\ uav;rsm; oif,l&rnhfynm trsdK;tpm;udk a½G;cs,fEdkifaom vufOD; tcGihfta&;&Sdonf/'''
        result = win2uni.convert(win)
        result = uni2zg.convert(result)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Six")

    def test_article_twentyseven(self):
        zawgyi = u'''အပိုဒ္ ၂၇
        လူတိုင္းတြင္ သက္ဆိုင္ရာ ယဥ္ေက်းမႈ ေလာက၌ လြတ္လပ္စြာ ပါဝင္ေဆာင္ ရြက္ႏိုင္ခြင့္ သုခုမပညာရပ္ မ်ားကိုလြတ္လပ္စြာလိုက္စား ေမြ႕ေလ်ာ္ႏိုင္ခြင့္၊ 
        သိပၸံ ပညာထြန္းကားေရး လုပ္ငန္းမ်ားတြင္ လြတ္လပ္စြာ ဝင္ေရာက္ လုပ္ကိုင္ ႏိုင္ခြင့္ႏွင့္ ထိုပညာ၏ အက်ိဳး အာနိသင္မ်ားကို လြတ္လပ္စြာ ခံစားသုံးစြဲႏိုင္ခြင့္ ရွိသည္။
        လူတိုင္းတြင္ သိပၸံမွ ျဖစ္ေစ၊ စာေပမွျဖစ္ေစ၊ သုခုမပညာမွ ျဖစ္ေစ၊ မိမိကိုယ္ပိုင္ဉာဏ္ျဖင့္ႀကံစည္ ဖန္တီးမႈမွ ျဖစ္ထြန္းလာသည့္ ဂုဏ္ႏွင့္ ေငြေၾကး 
        အက်ိဳးအျမတ္မ်ားကို ခံစားရယူႏိုင္ရန္ အခြင့္အေရး အတြက္ ကာကြယ္မႈကို ရရွိရန္ အခြင့္အေရး ရွိသည္။'''
        win = u'''tydk'f 27
        vlwdkif;wGif oufqdkif&m ,Ofaus;rI avmuü vGwfvyfpGm yg0ifaqmif ½GufEdkifcGihf okckrynm&yf rsm;udkvGwfvyfpGmvdkufpm; arGUavsmfEdkifcGihf? 
        odyÜH ynmxGef;um;a&; vkyfief;rsm;wGif vGwfvyfpGm 0ifa&muf vkyfudkif EdkifcGihfESihf xdkynm\ tusdK; tmedoifrsm;udk vGwfvyfpGm cHpm;okH;pGJEdkifcGihf &Sdonf/
        vlwdkif;wGif odyÜHrS jzpfap? pmayrSjzpfap? okckrynmrS jzpfap? rdrdudk,fydkifÓPfjzihfBuHpnf zefwD;rIrS jzpfxGef;vmonhf *kPfESihf aiGaMu; 
        tusdK;tjrwfrsm;udk cHpm;&,lEdkif&ef tcGihfta&; twGuf umuG,frIudk &&Sd&ef tcGihfta&; &Sdonf/'''
        result = win2uni.convert(win)
        result = uni2zg.convert(result)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Seven")

    def test_article_twentyeight(self):
        zawgyi = u'''အပိုဒ္ ၂၈
        လူတိုင္းသည္ ဤေၾကညာ စာတမ္းတြင္ ေဖာ္ျပထားသည့္ အခြင့္အေရးမ်ား ႏွင့္ လြတ္လပ္ခြင့္မ်ားကို အျပည့္အစုံ ရယူႏိုင္ေသာ လူမႈ ဆက္ဆံေရး 
        အေျခအေနႏွင့္ အျပည္ျပည္ဆိုင္ရာ ဆက္ဆံေရး အေျခအေနတို႔၏ အက်ိဳးေက်းဇူးကို ခံစားႏိုင္ခြင့္ ရွိသည္။'''
        win = u'''tydk'f 28
        vlwdkif;onf þaMunm pmwrf;wGif azmfjyxm;onhf tcGihfta&;rsm; ESihf vGwfvyfcGihfrsm;udk tjynhftpkH &,lEdkifaom vlrI qufqHa&; 
        tajctaeESihf tjynfjynfqdkif&m qufqHa&; tajctaewdkY\ tusdK;aus;Zl;udk cHpm;EdkifcGihf &Sdonf/'''
        result = win2uni.convert(win)
        result = uni2zg.convert(result)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Twenty Eight")

    def test_article_twentynine(self):
        zawgyi = u'''အပိုဒ္ ၂၉
        မိမိ၏စ႐ိုက္လကၡဏာ လြတ္လပ္စြာ ဖြံ႕ၿဖိဳး တိုးတက္ႏိုင္သည့္ တစ္ခုတည္းေသာ လူ႔အသိုက္အဝန္း အတြက္လူတိုင္း၌ တာဝန္ ရွိသည္။
        မိမိ၏ အခြင့္အေရးမ်ားႏွင့္ လြတ္လပ္ ခြင့္မ်ားကို သုံးစြဲရာတြင္ လူတိုင္းသည္၊ အျခားသူမ်ား၏ အခြင့္အေရးမ်ားႏွင့္လြတ္လပ္ခြင့္မ်ားကို
        အသိအမွတ္ျပဳ၍ ႐ိုေသေလးစားေစရန္အလို႔ငွာ လည္းေကာင္း၊ ဒီမိုကေရစီက်င့္သုံးေသာ လူ႔အဖြဲ႕အစည္းတြင္ ကိုယ္က်င့္တရားအျပင္၊ 
        ရပ္ရြာေအးခ်မ္းသာယာေရးႏွင့္ ျပည္သူ႔ အက်ိဳး စီးပြား ျဖစ္ထြန္းေရးတို႔ အတြက္၊ တရားမၽွတစြာ က်င့္ေဆာင္ရန္ အလို႔ငွာ လည္းေကာင္း၊ 
        ဥပေဒက ျပဌာန္းထားသည့္ ခ်ဳပ္ခ်ယ္မႈမ်ားျဖင့္သာ ကန႔္သတ္ျခင္းခံရမည္။
        အဆိုပါ အခြင့္အေရးမ်ားႏွင့္ လြတ္လပ္ ခြင့္မ်ားကို မည္သည့္ အမႈကိစၥတြင္မၽွ ကုလသမဂၢ၏ ရည္ရြယ္ခ်က္မ်ားႏွင့္လည္းေကာင္း၊ 
        အေျခခံမူမ်ားႏွင့္ လည္းေကာင္း ဆန႔္က်င္၍ မသုံးစြဲရ။'''
        win = u'''tydk'f 29
        rdrd\p½dkufvu©Pm vGwfvyfpGm zGHUNzdK; wdk;wufEdkifonhf wpfckwnf;aom vlYtodkuft0ef; twGufvlwdkif;ü wm0ef &Sdonf/
        rdrd\ tcGihfta&;rsm;ESihf vGwfvyf cGihfrsm;udk okH;pGJ&mwGif vlwdkif;onf? tjcm;olrsm;\ tcGihfta&;rsm;ESihfvGwfvyfcGihfrsm;udk
        todtrSwfûyí ½dkaoav;pm;ap&eftvdkYiSm vnf;aumif;? 'Drdkua&pDusihfokH;aom vlYtzGJUtpnf;wGif udk,fusihfw&m;tjyif? 
        &yf½Gmat;csrf;om,ma&;ESihf jynfolY tusdK; pD;yGm; jzpfxGef;a&;wdkY twGuf? w&m;rQwpGm usihfaqmif&ef tvdkYiSm vnf;aumif;? 
        Oya'u jyXmef;xm;onhf csKyfcs,frIrsm;jzihfom ueYfowfjcif;cH&rnf/
        tqdkyg tcGihfta&;rsm;ESihf vGwfvyf cGihfrsm;udk rnfonhf trIudpöwGifrQ ukvor*¾\ &nf½G,fcsufrsm;ESihfvnf;aumif;? 
        tajccHrlrsm;ESihf vnf;aumif; qeYfusifí rokH;pGJ&/'''
        result = win2uni.convert(win)
        result = uni2zg.convert(result)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Twenty Nine")

    def test_article_thirty(self):
        zawgyi = u'''အပိုဒ္ ၃ဝ
        ဤေၾကညာစာတမ္းပါ အခြင့္အေရးႏွင့္တကြ လြတ္လပ္ခြင့္မ်ား ပ်က္စီးရာပ်က္စီးေၾကာင္းတို႔ကိုရည္ရြယ္၍၊ ႏိုင္ငံတစ္ႏိုင္ငံ အတြက္ ျဖစ္ေစ၊ 
        လူတစ္စုအတြက္ ျဖစ္ေစ၊ လူတစ္ဦးတစ္ေယာက္ အတြက္ ျဖစ္ေစ ပါဝင္ ေဆာင္ရြက္ရန္ အခြင့္ရွိသည္ဟု ေသာ္လည္းေကာင္း၊ ကိုယ္တိုင္ေဆာင္ရြက္ရန္ 
        အခြင့္ရွိသည္ ဟုေသာ္လည္းေကာင္းအဓိပၸါယ္ ပိုင္းျခားေကာက္ယူျခင္း မရွိေစရ။'''
        win = u'''tydk'f 30
        þaMunmpmwrf;yg tcGihfta&;ESihfwuG vGwfvyfcGihfrsm; ysufpD;&mysufpD;aMumif;wdkYudk&nf½G,fí? EdkifiHwpfEdkifiH twGuf jzpfap? 
        vlwpfpktwGuf jzpfap? vlwpfOD;wpfa,muf twGuf jzpfap yg0if aqmif½Guf&ef tcGihf&Sdonf[k aomfvnf;aumif;? udk,fwdkifaqmif½Guf&ef 
        tcGihf&Sdonf [kaomfvnf;aumif;t"dyÜg,f ydkif;jcm;aumuf,ljcif; r&Sdap&/'''
        result = win2uni.convert(win)
        result = uni2zg.convert(result)
        self.assertEqual(zawgyi, result, "Failed to Convert Article Thirty")


if __name__ == "__main__":
    unittest.main()