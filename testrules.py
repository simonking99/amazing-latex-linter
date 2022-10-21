"""Unit testing file for rules"""
import unittest
import linecache

class TestStringMethods(unittest.TestCase):
    """Main class"""
    def test_space_after_procent(self):
        """Test rule space after %"""
        line1 = linecache.getline("input.tex", 1)
        line1_1 = linecache.getline("output.tex", 1)
        print(line1)
        print(line1_1)
        self.assertNotEqual(line1, line1_1) #Checking if line changes after rule applied

    def test_newline_after_dot(self):
        """Test rule newline after ."""
        line2 = linecache.getline("input.tex", 2)
        line2_2 = linecache.getline("output.tex", 2)
        self.assertNotEqual(line2, line2_2) #Checking if line changes after rule applied

    def test_intention_tabs(self):
        """Test rule intention_tabs"""
        line3 = linecache.getline("input.tex", 4)
        line3_3 = linecache.getline("output.tex", 7)
        self.assertNotEqual(line3, line3_3) #Checking if line changes after rule applied

if __name__ == '__main__':
    unittest.main()
    