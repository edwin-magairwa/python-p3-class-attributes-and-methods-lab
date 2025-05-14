import unittest
from song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        # Reset class attributes for a clean test run
        Song.count = 0
        Song.genres = []
        Song.artists = []
        Song.genre_count = {}
        Song.artist_count = {}

        self.song1 = Song("99 Problems", "Jay-Z", "Rap")
        self.song2 = Song("Halo", "Beyonce", "Pop")
        self.song3 = Song("God's Plan", "Drake", "Rap")

    def test_song_count(self):
        self.assertEqual(Song.count, 3)

    def test_unique_artists(self):
        self.assertEqual(sorted(Song.artists), sorted(["Jay-Z", "Beyonce", "Drake"]))

    def test_unique_genres(self):
        self.assertEqual(sorted(Song.genres), sorted(["Rap", "Pop"]))

    def test_genre_count(self):
        self.assertEqual(Song.genre_count, {"Rap": 2, "Pop": 1})

    def test_artist_count(self):
        self.assertEqual(Song.artist_count, {"Jay-Z": 1, "Beyonce": 1, "Drake": 1})

if __name__ == '__main__':
    unittest.main()
