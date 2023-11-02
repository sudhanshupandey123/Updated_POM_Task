@Phase1
Feature: Amazon Page

  Scenario Outline: Add To Cart
    Given User Is On Amazon Page
    When User Search For "<product_name>"
    And Filtered Product Based On "<rating>" star rating
    Then He Added "<product_count>" Product To Cart
    And Actual Price Should Be Same As Cart Price
    Examples:
      | product_name  | rating | product_count |
      | HP Laptop     | 4      | 1             |
      | Lenovo Laptop | 3      | 2             |

