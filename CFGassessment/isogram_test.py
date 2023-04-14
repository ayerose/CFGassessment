import unittest
from pythonPart import isogram


class TestIsogram(unittest.TestCase):

    def test_no_isogram(self):
        """"
          to test if NON isograms are correctly classified as such non-isograms
        """
        self.assertFalse(isogram("banana"))
        self.assertFalse(isogram("giraffe"))
        self.assertFalse(isogram("existence"))
        self.assertFalse(isogram("apple"))

    def test_is_isogram(self):
        """"
        to test if actual isograms are correctly identified as such, which is
        essential for the logic of the actual code
        """
        self.assertTrue(isogram("background"))
        self.assertTrue(isogram("isogram"))
        self.assertTrue(isogram("bread"))
        self.assertTrue(isogram("honey"))

