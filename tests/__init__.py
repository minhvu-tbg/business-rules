try:
    from unittest2 import TestCase
except ImportError:
    from unittest import TestCase

assert TestCase


# older unittest2.TestCase (centos6) have only the now-deprecated
# assertRaisesRegex. Simple assignment makes pylint complain, about
# users of assertRaisesRegex so we use getattr to trick it.
if not hasattr(TestCase, 'assertRaisesRegex'):
    TestCase.assertRaisesRegex = (
        getattr(TestCase, 'assertRaisesRegex'))