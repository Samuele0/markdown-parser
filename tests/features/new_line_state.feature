Feature: New Line State
    NewLineState class is the default state when a new line begins

    Scenario: Should ingore starting whitespace
        Given A NewLineState instance
        When The state accepts " "
        Then The state should return itself

    Scenario: Header parsing
        Given A StateManager instance
        And A NewLineState instance
        When The state accepts "#"
        Then The state should ask the state manager for a "header" state
        And The state should return the "header" state

    Scenario: Bold or Enum parsing
        Given A StateManager instance
        And A NewLineState instance
        When The state accepts "*"
        Then The state should ask the state manager for a "bold_or_enum" state
        And The state should return a "bold_or_enum" state

    Scenario: Text parsing
        Given A StateManager instance
        And A NewLineState instance
        When The state accepts "a"
        Then The state should ask the state manager for a "text" state
        And The state should return a "text" state