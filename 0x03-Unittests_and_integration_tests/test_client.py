#!/usr/bin/env python3

"""test_utils.py"""

from parameterized import parameterized
import unittest
from client import GithubOrgClient
from unittest.mock import Mock, PropertyMock, patch


class TestGithubOrgClient(unittest.TestCase):
    """test the GithubOrgClient"""

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_json):
        """test for correct output"""
        github_client = GithubOrgClient(org_name)
        github_client.org()
        mock_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    @patch('client.get_json')
    def test_public_repos_url(self, mock_json):
        """test for correct output"""
        payload = {"repos_url": "http://github.com/org/repos"}
        mock_json.return_value = payload

        client = GithubOrgClient("test")
        self.assertEqual(client._public_repos_url,
                         "http://github.com/org/repos")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """test for correct output"""
        # set up the mock response
        payload = [{'name': 'repo1', 'license': {'key': 'mit'}},
                   {'name': 'repo2', 'license': {'key': 'apache-2.0'}}]
        mock_get_json.return_value = payload

        # set up the mock property
        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            # set the expected value of _public_repos_url
            expected_url = 'https://api.github.com/orgs/google/repos'
            mock_public_repos_url.return_value = expected_url

            # instantiate the client and call public_repos()
            org_name = 'google'
            client = GithubOrgClient(org_name)
            repos = client.public_repos(license='mit')

            # assert that the expected calls were made
            mock_public_repos_url.assert_called_once_with()
            mock_get_json.assert_called_once_with(expected_url)

            # assert that the list of repos is what we expect
            self.assertEqual(repos, ['repo1'])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """test has_license method"""
        self.assertEqual(GithubOrgClient.has_license(
            repo, license_key), expected)


class TestIntegrationGithubOrgClient(unittest.TestCase):

    @classmethod
    @patch('requests.get')
    def setUpClass(cls, mock_get):
        cls.org_payload = {'login': 'test_org'}
        cls.repos_payload = [{'name': 'repo1', 'license': {'key': 'my_license'}},
                             {'name': 'repo2', 'license': {'key': 'other_license'}}]
        cls.expected_repos = ['repo1', 'repo2']
        cls.apache2_repos = ['repo2']

        mock_get.side_effect = [
            Mock(json=lambda: cls.org_payload),
            Mock(json=lambda: cls.repos_payload)
        ]

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.client = GithubOrgClient('test_org')

    def tearDown(self):
        pass

    def test_public_repos(self):
        repos = self.client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        repos = self.client.public_repos(license='my_license')
        self.assertEqual(repos, ['repo1'])

    def test_public_repos_with_other_license(self):
        repos = self.client.public_repos(license='apache-2.0')
        self.assertEqual(repos, self.apache2_repos)
