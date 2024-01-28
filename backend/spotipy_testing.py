from spotipy_searches import *
import unittest

class TestSearchingCases(unittest.TestCase):
    def test_search_1_artist_max_default_10_results(self):
        self.assertTrue(len(search_by_artist('DPR IAN')) <= 10)
        self.assertTrue(len(search_by_artist('keshi')) <= 10)
        self.assertTrue(len(search_by_artist('NewJeans')) <= 10)
<<<<<<< HEAD
        self.assertTrue(len(search_by_artist('fake name')) <= 10)
    
    def test_search_1_valid_artist_gets_results(self):
        self.assertTrue(len(search_by_artist('DPR IAN')) > 0)
        self.assertTrue(len(search_by_artist('keshi')) > 0)
        self.assertTrue(len(search_by_artist('NewJeans')) > 0)
    
    def test_search_1_valid_artist_case_sensitive_same(self):
        self.assertEqual(search_by_artist('DPR IAN'), search_by_artist('dpR iAn'))
        self.assertEqual(search_by_artist('keshi'), search_by_artist('kEshI'))
        self.assertEqual(search_by_artist('NewJeans'), search_by_artist('nEWJeanS'))

    def test_search_1_invalid_artist_gets_0_results(self):
        self.assertEqual(len(search_by_artist('fake name')), 0)
        self.assertEqual(len(search_by_artist('randomnametest')), 0)
    
    def test_search_valid_1_artist_0_max_error(self):
        try:
            search_by_artist('DPR IAN', 0) # Will raise SpotifyException
            assert False # Should have raised SpotifyException
        except:
             pass

    def test_search_1_valid_artist_low_max_results(self):
        self.assertTrue(len(search_by_artist('DPR IAN', 5)) <= 5)
        self.assertTrue(len(search_by_artist('keshi', 2)) <= 2)
        self.assertTrue(len(search_by_artist('NewJeans', 1)) <= 1)
    
    def test_search_1_valid_artist_high_max_results(self):
        self.assertTrue(len(search_by_artist('DPR IAN', 25)) <= 25)
        self.assertTrue(len(search_by_artist('keshi', 30)) <= 30)
        self.assertTrue(len(search_by_artist('NewJeans', 15)) <= 15)

    def test_search_1_valid_artist_gets_list_of_tuples_of_str(self):
        result = search_by_artist('DPR IAN')
        self.assertEqual(type(result), list)
        self.assertEqual(type(result[0]), tuple)
        self.assertEqual(type(result[0][0]), str)
        self.assertEqual(type(result[0][1]), str)

    def test_search_3_valid_artists_gets_results(self):
        self.assertTrue(len(search_by_x_artists(('DPR IAN', 'keshi', 'NewJeans'))) > 0)
    
    def test_search_3_invalid_artists_gets_0_results(self):
        self.assertEqual(len(search_by_x_artists(('fakename1', 'fakename2', 'randomnametest'))), 0)
    
    def test_search_3_valid_artists_max_default_10_results_each(self):
        self.assertTrue(len(search_by_x_artists(('DPR IAN', 'keshi', 'NewJeans'))) <= 30)
    
    def test_search_3_valid_artists_low_max_results_each(self):
        self.assertTrue(len(search_by_x_artists(('DPR IAN', 'keshi', 'NewJeans'), 2)) <= 6)
    
    def test_search_3_valid_artist_gets_list_of_tuples_of_str(self):
        result = search_by_x_artists(('DPR IAN', 'keshi', 'NewJeans'))
        self.assertEqual(type(result), list)
        self.assertEqual(type(result[0]), tuple)
        self.assertEqual(type(result[0][0]), str)
        self.assertEqual(type(result[0][1]), str)
    
    def test_search_artists_0_max_results_error(self):
        try:
            search_by_x_artists(('DPR IAN', 'keshi', 'NewJeans'), 0) # Will raise SpotifyException
            assert False # Should have raised SpotifyException
        except:
             pass
    
    def test_search_valid_playlist_link_gets_results(self):
        self.assertTrue(len(search_by_playlist('https://open.spotify.com/playlist/3c8sZa0lI8eWU9aJpr3w2M')) > 0)
    
    def test_search_valid_playlist_link_with_query_gets_results(self):
        self.assertTrue(len(search_by_playlist('https://open.spotify.com/playlist/5iUayjyzc0JuftsOHIaWb1?si=d62809d69cf2406c')) > 0)
        
    def test_search_valid_playlist_link_gets_over_100_results(self):
        self.assertTrue(len(search_by_playlist('https://open.spotify.com/playlist/3c8sZa0lI8eWU9aJpr3w2M')) > 100)
    
    def test_search_valid_playlist_link_gets_list_of_tuples_of_str(self):
        result = search_by_playlist('https://open.spotify.com/playlist/3c8sZa0lI8eWU9aJpr3w2M')
        self.assertEqual(type(result), list)
        self.assertEqual(type(result[0]), tuple)
        self.assertEqual(type(result[0][0]), str)
        self.assertEqual(type(result[0][1]), str)

    def test_search_invalid_playlist_link_error(self):
        try:
            search_by_playlist('noturl')
            assert False # Should have raised SpotifyException
        except:
            pass
=======
    
    def test_search_3_artist_max_default_10_results_each(self):
        self.assertTrue(len(search_by_x_artists(('DPR IAN', 'keshi', 'NewJeans'))) <= 30)
>>>>>>> 695a641 (Started unittesting search functions)

if __name__=='__main__':
	unittest.main()