import unittest as ut
import sos

class TestCode(ut.TestCase):

    def test_shinedivide(self):
        self.assertEqual(sos.shinedivide(10, 5), 2)

if __name__ == '__main__':
    ut.main()
