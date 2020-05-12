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


    Scenario: Bold or Enum parsing
        Given A StateManager instance
        And A NewLineState instance
        When The state accepts "*"
        Then The state should ask the state manager for a "bold_or_enum" state


    Scenario: Text parsing
        Given A StateManager instance
        And A NewLineState instance
        When The state accepts "a"
        Then The state should ask the state manager for a "text" state


    Scenario: Setting Document Node
        Given A NewLineState instance
        When a new document node is set
        Then no error should be returned