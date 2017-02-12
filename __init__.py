from org_repo_services import OrgTopReposAndCommittees
import sys


if __name__ == '__main__':
    if len(sys.argv) < 4 or len(sys.argv) > 4:
        print 'You entered wrong number of arguments: '
        for arg in sys.argv:
            print arg + ', '
        print 'Please enter <org name, num of repos, num of top committees>'
        sys.exit(1)

    organization = sys.argv[1]
    num_of_repos = int(sys.argv[2])
    num_of_committees = int(sys.argv[3])
    data = OrgTopReposAndCommittees(organization).get_top_n_repo_and_m_committees(num_of_repos, num_of_committees)
    print data
