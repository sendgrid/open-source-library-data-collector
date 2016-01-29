try:
    import unittest2 as unittest
except ImportError:
    import unittest

from db_connector import DBConnector, GitHubData

class TestConfig(unittest.TestCase):
    def setUp(self):
        self.db = DBConnector()

    def test_get_data(self):
        github_data = self.db.get_data(GitHubData)
        self.assertTrue(isinstance(github_data, list))
        self.assertTrue(isinstance(github_data[0], GitHubData))

if __name__ == '__main__':
    unittest.main()