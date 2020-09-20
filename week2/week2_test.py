import unittest
from week2 import MatchParentheses 


class MatchParenthesesTest(unittest.TestCase):

    def test_empty_strings(self):
        match_func = MatchParentheses('','')
        self.assertEqual(match_func.match(), 0)

    def test_target_empty(self):
        match_func = MatchParentheses('(((()))','')
        self.assertEqual(match_func.match(), 0)

    def test_base_longer_than_target(self):
        match_func = MatchParentheses('()()()()','))))')
        self.assertEqual(match_func.match(), 3)

    def test_base_longer_than_target2(self):
        match_func = MatchParentheses('((((()()()()))))','(()(()(')
        self.assertEqual(match_func.match(), 1)

    def test_base_shorter_than_target(self):
        match_func = MatchParentheses('(()(()(','(()(()())))()()')
        self.assertEqual(match_func.match(), 8)

    def test_base_shorter_than_target2(self):
        match_func = MatchParentheses('(())','((()((()))')
        self.assertEqual(match_func.match(), 8)


test = MatchParenthesesTest()
test.test_empty_strings()
test.test_target_empty()
test.test_base_longer_than_target()
test.test_base_longer_than_target2()
test.test_base_shorter_than_target()
test.test_base_shorter_than_target2()