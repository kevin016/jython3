import unittest
import sys

from test import support


class EnumerateJyTestCase(unittest.TestCase):

    enum = enumerate
    seq, start, res = 'abc', 5, [(5, 'a'), (6, 'b'), (7, 'c')]

    def test_start_kwarg_1(self):
        e = self.enum(self.seq, start=self.start)
        self.assertEqual(iter(e), e)
        self.assertEqual(list(e), self.res)

    def test_start_kwarg_2(self):
        e = self.enum(start=self.start, sequence=self.seq)
        self.assertEqual(iter(e), e)
        self.assertEqual(list(e), self.res)

    def test_start_pos(self):
        e = self.enum(self.seq, self.start)
        self.assertEqual(iter(e), e)
        self.assertEqual(list(e), self.res)

    def test_start_maxint(self):
        e = self.enum(self.seq, sys.maxsize)
        self.assertEqual(list(e), [(2147483647, 'a'), (2147483648, 'b'), (2147483649, 'c')])


def test_main(verbose=None):
    testclasses = (EnumerateJyTestCase,)
    support.run_unittest(*testclasses)


if __name__ == "__main__":
    test_main(verbose=True)

