@delivery
Feature: Test Stuart Login, Home and Delivery Order pages links consistency and functionality
  In order to check all existing links on Stuart Login, Home and Delivery pages
  As test automation engineer
  I need to create script checking availability of links

  @login
  Scenario: User can login
    Given I am on the home page
    When I login as Sandbox user
    Then I should see user menu element on Home page

  @logout
  Scenario: User can logout
    Given I am on the home page
    When I login as Sandbox user
    Then I should see user menu element on Home page
    When I click on user menu element on Home page
    And I click on user menu logout link element on Home page
    Then I should see email field element on Login page

  @order
  Scenario: User can order delivery
    Given I am on the home page
    When I login as Sandbox user
    Then I should see History text
    When I click on Request a delivery button element on Home page
    Then I should see vehicle element on Order page
    When I fill in pick up form
    Then I fill in drop off form
    Then I should see delivery price element on Order page
    When I click on request button element on Order page
    Then I should see share tracking button element on Order page
