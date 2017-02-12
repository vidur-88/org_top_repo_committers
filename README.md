# org_top_repo_committers
This is for getting m top repos of any organization and top committees of each repos

Run this app
-------------
+ first install all requirements

  `pip install -r requirement.txt`

+ Then run

  `python __init__.py <org_name> <num_top_repo> <num_of_committees>`

+ Run test cases

   `lettuce tests/`

+ Changing in test cases

  You can change test case to change in file: test/features/org_repo_services_test.feature
  By adding in example, like:
  
        |  org        |  num_top_repos   |  num_of_committees  |  result_org     |  result_num_top_repo  |
        |  microsoft  |     3            |      4              |   microsoft     |       3               |
        |  google     |     5            |      2              |   google        |       5               |

