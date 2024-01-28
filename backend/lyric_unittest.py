import unittest
from LyricAPI import *

class TestLyric(unittest.TestCase):

    def test_length(self):
        self.assertEqual(len(get_game_lyrics("keshi", get_lyrics("keshi", "understand"), "understand")), 4)


    def test_type(self):
        self.assertEqual(type(get_lyrics("keshi", "understand")), list)
        self.assertEqual(type(get_game_lyrics("keshi", get_lyrics("keshi", "understand"), "understand")), tuple)


if __name__ == '__main__':
    unittest.main()