"""Misc operator module tests

Made for Jython.
"""
import collections
import operator
import sys
import unittest
from test import support

class OperatorTestCase(unittest.TestCase):

    class NewStyle(object):
        pass
    class OldStyle:
        pass
    class HasGetitem(object):
        def __getitem__(self, name):
            return 'foo'
    class HasInt(object):
        def __int__(self):
            return 1
    class HasLong(object):
        def __long__(self):
            return 1
    class HasFloat(object):
        def __float__(self):
            return 1.0

    # obj, isNumberType, isMappingType, isSequenceType
    tests = (
        (type, False, False, False),
        (type.__dict__, False, True, False), # dictproxy
        (globals(), False, True, False), # stringmap
        ({}, False, True, False),
        ('', False, False, True),
        ('', False, False, True),
        ([], False, False, True),
        ((), False, False, True),
        (range(5), False, False, True),
        (set(), False, False, False),
        (frozenset(), False, False, False),
        (1, True, False, False),
        (2, True, False, False),
        (3.0, True, False, False),
        (4j, True, False, False),
        (None, False, False, False),
        (Ellipsis, False, False, False),
        (Exception(), False, False, True),
        (collections.deque(), False, False, True),
        (collections.defaultdict(), False, True, False),
        (collections.namedtuple('test', 't'), False, False, False),
        (NewStyle(), False, False, False),
        (OldStyle(), not sys.platform.startswith('java'), False, False),
        (HasGetitem(), False, True, True),
        (HasInt(), True, False, False),
        (HasFloat(), True, False, False),
        )

    def test_isNumberType(self):
        for obj, isNumberType, _, _ in self.tests:
            self.assert_istype(operator.isNumberType, obj, isNumberType)

    def test_isMappingType(self):
        for obj, _, isMappingType, _ in self.tests:
            self.assert_istype(operator.isMappingType, obj, isMappingType)

    def test_isSequenceType(self):
        for obj, _, _, isSequenceType in self.tests:
            self.assert_istype(operator.isSequenceType, obj, isSequenceType)

    def assert_istype(self, func, obj, result):
        self.assertEqual(func(obj), result, '%s %s should be: %s' %
                         (type(obj), func.__name__, result))


def test_main():
    support.run_unittest(OperatorTestCase)


if __name__ == "__main__":
    test_main()
