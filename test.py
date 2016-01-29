try:
    import unittest2 as unittest
except ImportError:
    import unittest

from db_connector import DBConnector, GitHubData, PackageManagerData
import datetime

class TestDBConnector(unittest.TestCase):
    def setUp(self):
        self.db = DBConnector()

    def test_add_and_delete_data(self):
        github_data_import = GitHubData(
                                date_updated=datetime.datetime.now(),
                                language='repo_name',
                                pull_requests=0,
                                open_issues=0,
                                number_of_commits=0,
                                number_of_branches=0,
                                number_of_releases=0,
                                number_of_contributors=0,
                                number_of_watchers=0,
                                number_of_stargazers=0,
                                number_of_forks=0
                                )
        res = self.db.add_data(github_data_import)
        self.assertTrue(isinstance(res, GitHubData))
        res = self.db.delete_data(res.id, 'github_data')
        self.assertTrue(res)
        
        packagedata = PackageManagerData(
                                date_updated=datetime.datetime.now(),
                                csharp_downloads=0,
                                nodejs_downloads=0,
                                php_downloads=0,
                                python_downloads=0,
                                ruby_downloads=0
                                )
        res = self.db.add_data(packagedata)
        self.assertTrue(isinstance(res, PackageManagerData))
        res = self.db.delete_data(res.id, 'package_manager_data')
        self.assertTrue(res)

    def test_get_data(self):
        github_data = self.db.get_data(GitHubData)
        self.assertTrue(isinstance(github_data, list))
        self.assertTrue(isinstance(github_data[0], GitHubData))

if __name__ == '__main__':
    unittest.main()