import unittest
import uni2zg


class TESTZG2UNI(unittest.TestCase):

    def test_header_one(self):
        zawgyi = u'အျပည္ျပည္ဆိုင္ရာ လူ႔အခြင့္အေရး ေၾကျငာစာတမ္း'
        unicode = u'အပြည်ပြည်ဆိုင်ရာ လူ့အခွင့်အရေး ကြေငြာစာတမ်း'
        result = uni2zg.convert(unicode)
        self.assertEqual(zawgyi, result, "Failed to Convert Header One")

if __name__ == "__main__":
    unittest.main()