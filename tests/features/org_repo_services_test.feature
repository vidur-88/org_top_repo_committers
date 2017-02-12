Feature: Testing top repos and top commitees of each repo

  Scenario: Having result
    Given Test for '<org>' and '<num_top_repos>' and '<num_of_committees>'
    Then I get result '<result_org>' and '<result_num_top_repo>'

  Examples:
    |  org        |  num_top_repos   |  num_of_committees  |  result_org     |  result_num_top_repo  |
    |  google     |     3            |      2              |   google        |       3               |
    |  microsoft  |     5            |      4              |   microsoft     |       5               |
