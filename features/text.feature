Feature: Headers text

  Background: Launch browser and open website
    Given Open website

  Scenario Outline: Header text
    When Click menu item <number>
    Then Page with <header_text> opens

    Examples:
    | number | header_text              |
    | 1      | Monetary Policy          |
    | 2      | Financial Stability      |
    | 3      | Supervision              |
    | 4      | Payments and Settlements |
    | 5      | Financial Markets        |
    | 6      | Statistics               |
    | 7      | Hryvnia                  |
