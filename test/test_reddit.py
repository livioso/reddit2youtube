import unittest
from unittest.mock import Mock
from src.reddit import extract_video_id_from_url, extract_video_ids_from_subreddit


class VideoIdExtractionTest(unittest.TestCase):

    def test_extract_video_id_from_url(self):
        self.assertEqual('6mXl8C4-M_4', extract_video_id_from_url('https://www.youtube.com/watch?v=6mXl8C4-M_4'))
        self.assertEqual('M7lc1UVf-VE', extract_video_id_from_url('https://www.youtube.com/embed/M7lc1UVf-VE'))
        self.assertEqual('PEzTFmiCeks', extract_video_id_from_url('https://youtu.be/PEzTFmiCeks'))
        self.assertEqual(None, extract_video_id_from_url('https://www.pbs.org/wgbh/frontline/'))

    def test_extract_video_ids_from_subreddit(self):
        subreddit = Mock()
        subreddit.new.return_value = [
            Mock(url='https://www.youtube.com/watch?v=6mXl8C4-M_4'),
            Mock(url='https://www.youtube.com/embed/M7lc1UVf-VE'),
            Mock(url='https://youtu.be/PEzTFmiCeks'),
            Mock(url='https://www.pbs.org/wgbh/frontline/')
        ]

        video_ids = extract_video_ids_from_subreddit(subreddit)

        self.assertEqual(1, subreddit.new.called)
        self.assertEqual(3, len(video_ids))
        self.assertListEqual(['6mXl8C4-M_4', 'M7lc1UVf-VE', 'PEzTFmiCeks'], video_ids)
