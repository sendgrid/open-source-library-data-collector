import os
import datetime
import github3
from db_connector import DBConnector, GitHubData


class GitHub(object):
    """Collect time stamped repository data from GitHub and store in a DB"""
    def __init__(self):
        # Check if we are not in heroku
        github_token = os.environ.get('GITHUB_TOKEN') if \
            os.environ.get('ENV') != 'prod' else os.environ['GITHUB_TOKEN']
        self.github = github3.login(token=github_token)
        self.db = DBConnector()

    def update_library_data(self, repo_user, repo_name):
        """Gets data from a given GitHub repo and adds it to the DB

        :param repo_user: the username of the repo's owner
        :param repo_name: the name of the GitHub repo
        :type repo_user:  string
        :type repo_name:  string

        :returns: Returns the data object that was added to the DB
        :rtype:   Data object
        """
        github_data = self.github.repository(repo_user, repo_name)
        lib_data = {}
        lib_data['num_pull_requests'] \
            = sum(1 for i in github_data.iter_pulls())
        lib_data['num_issues'] \
            = sum(1 for i in github_data.iter_issues())
        lib_data['num_commits'] \
            = sum(1 for i in github_data.iter_commits())
        lib_data['num_branches'] \
            = sum(1 for i in github_data.iter_branches())
        lib_data['num_releases'] \
            = sum(1 for i in github_data.iter_releases())
        lib_data['num_contributors'] \
            = sum(1 for i in github_data.iter_contributors())
        lib_data['num_watchers'] \
            = sum(1 for i in github_data.iter_subscribers())
        lib_data['num_stargazers'] \
            = sum(1 for i in github_data.iter_stargazers())
        lib_data['num_forks'] = github_data.forks_count
        github_data_import = GitHubData(
                        date_updated=datetime.datetime.now(),
                        language=repo_name,
                        pull_requests=lib_data['num_pull_requests'],
                        open_issues=lib_data['num_issues'],
                        number_of_commits=lib_data['num_commits'],
                        number_of_branches=lib_data['num_branches'],
                        number_of_releases=lib_data['num_releases'],
                        number_of_contributors=lib_data['num_contributors'],
                        number_of_watchers=lib_data['num_watchers'],
                        number_of_stargazers=lib_data['num_stargazers'],
                        number_of_forks=lib_data['num_forks']
                        )
        return self.db.add_data(github_data_import)
