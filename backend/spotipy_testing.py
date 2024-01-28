from spotipy_searches import *
import unittest

class TestSearchingCases(unittest.TestCase):
    def test_search_1_artist_max_default_10_results(self):
        self.assertTrue(len(search_by_artist('DPR IAN')) <= 10)
        self.assertTrue(len(search_by_artist('keshi')) <= 10)
        self.assertTrue(len(search_by_artist('NewJeans')) <= 10)
    
    def test_search_3_artist_max_default_10_results_each(self):
        self.assertTrue(len(search_by_x_artists(('DPR IAN', 'keshi', 'NewJeans'))) <= 30)

if __name__=='__main__':
	unittest.main()