import unittest

def palindromo(word):
    word = word.lower()
    reverse = word[::-1]
    return word == reverse

class TestPalindrome(unittest.TestCase):
    def test_palindrome_simple1(self):
        result = palindromo('neuquen')
        self.assertEqual(result, True)
    
    def test_palindrome_simple2(self):
        result = palindromo('ooaaoo')
        self.assertEqual(result, True)
        
    def test_palindrome_simple3(self):
        result = palindromo('llaalI')
        self.assertEqual(result, False)        
if __name__ == '__main__':
    unittest.main()