from lettuce import step, world, before
from org_repo_services import OrgTopReposAndCommittees


@step('Given Test for \'([^\']*)\' and \'([^\']*)\' and \'([^\']*)\'')
def given_test_for_group1_and_group2_and_group3(step, org, num_top_repo, num_of_committees):
    world.result = OrgTopReposAndCommittees(org).get_top_n_repo_and_m_committees(
        int(num_top_repo), int(num_of_committees))


@step('Then I get result \'([^\']*)\' and \'([^\']*)\'')
def then_i_get_result_group1_and_group2(step, org, num_top_repo):
    assert world.result['org'] == org and len(world.result['top_repos']) == int(num_top_repo)
