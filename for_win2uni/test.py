import unittest
import win2uni


class TESTZG2UNI(unittest.TestCase):
    def test_header_one(self):
        win = u'''tjynfjynfqdkif&m vlhtcGihfta&; ajujimpmwrf;'''
        unicode = u'''အပြည်ပြည်ဆိုင်ရာ လူ့အခွင့်အရေး ကြေငြာစာတမ်း'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed to Convert Header One")


if __name__ == "__main__":
    unittest.main();