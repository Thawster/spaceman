import unittest
from app import is_word_guessed, is_guess_in_word, load_word


class spacemanTests(unittest.TestCase):

    def test_word_gen(self):
        f = open('words.txt', 'r')
        words_list = f.readlines()
        f.close()
        words_list = words_list[0].split(' ')
        word = load_word()
        self.assertTrue(word.lower() in words_list)

    def test_word_guessed(self):
        self.assertTrue(is_word_guessed('lemon', ['l', 'e', 'm', 'o', 'n']))
        self.assertFalse(is_word_guessed('lemon', ['s', 'c', 'h', 'M', 'o', 'n','e', 'y']))
        self.assertFalse(is_word_guessed('lemon', ['c', 'e', 'm', 'o', 'n']))
        self.assertFalse(is_word_guessed('lemon', ['<', '*', 'm', 4, 'e']))

    def test_guess_in_word(self):
        self.assertTrue(is_guess_in_word("a", "arm"))
        self.assertFalse(is_guess_in_word("W", "arm"))
        self.assertFalse(is_guess_in_word("1", "arm"))


if __name__ == '__main__':
    unittest.main()
