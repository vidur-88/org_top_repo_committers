import requests
import json


git_api_url = 'https://api.github.com'


class OrgTopReposAndCommittees:
    def __init__(self, org):
        self.organization = org
        self.git_org_repo_url = self.__get_org_repo_url()
        self.headers = {'Accept': 'application/json', 'authorization': 'Basic dmlkdXItODg6aWlpdGEyMDEzMDk4OA=='}
        # self.flag = False

    def __get_org_repo_url(self):
        return '%s/orgs/%s/repos' % (git_api_url, self.organization)

    def __get_next_tab_link(self, headers):
        # if self.flag:
        #     return None
        # self.flag = True
        if not headers:
            return None
        if headers.find('rel="next"') >= 0:
            links = headers.split(',')
            for link in links:
                if link.find('rel="next"') >= 0:
                    link = link.split(';')
                    if len(link) != 2:
                        return None
                    else:
                        return link[0].replace('<', '').replace('>', '')

    def __get_github_all_pages_response(self, url):
        try:
            response = requests.get(url=url, headers=self.headers)
            if response.status_code == 200:
                repos = json.loads(response.text)
                if int(response.headers['x-ratelimit-remaining']) == 0:
                    print 'Your git hit url number limit exceed, please wait..'
                next_link = self.__get_next_tab_link(response.headers.get('link'))
                if next_link:
                    return repos + self.__get_github_all_pages_response(next_link)
                else:
                    return repos
            else:
                if int(response.headers.get('x-ratelimit-remaining')) == 0:
                    print 'Your git hit url number limit exceed, please wait..'
                print 'Got some error, status code: %s' % response.status_code
        except Exception as e:
            print 'get error to retrieve url: %s, error message: %s' % (url, e.message)

    def __get_all_repos(self, url):
        return self.__get_github_all_pages_response(url)

    def __get_n_top_repos(self, org_url, n):
        all_repos = self.__get_all_repos(org_url)
        all_repos.sort(key=lambda x: x['forks'])
        if len(all_repos) < n:
            print 'Total repos is lesser than top repos demanded, '\
                    'num of total repos: %s, num of top repos demanded: %s' % (len(all_repos), n)
            return all_repos
        return all_repos[:-n-1:-1]

    def __get_m_top_repo_committees(self, repo_url, m):
        committees = self.__get_github_all_pages_response(repo_url)
        committees.sort(key=lambda x: x['contributions'])
        if len(committees) < m:
            print 'Total committees is lesser than top commitees demanded, '\
                    'num of total committees: %s, num of top committees demanded: %s' % (len(committees), m)
            return committees
        return committees[:-m-1:-1]

    def get_top_n_repo_and_m_committees(self, num_of_repos, num_of_committees):
        n_top_repos = self.__get_n_top_repos(self.git_org_repo_url, num_of_repos)
        result = {'org': self.organization}
        top_repos = list()

        for repo in n_top_repos:
            repo_details = {'repo_name': repo.get('name'), 'forks': repo['forks']}
            repo_details['top_committees'] = list()
            m_top_committees = self.__get_m_top_repo_committees(repo.get('contributors_url'), num_of_committees)

            for committee in m_top_committees:
                repo_details['top_committees'].append(
                    {'username': committee['login'], 'contributions': committee['contributions']})
            top_repos.append(repo_details)
        result['top_repos'] = top_repos
        return result
