Feature: Parser
    The parser class should work as intended

    Scenario: Parsing is starting
        Given An instance of the StateManager class
        And An instance of the Parser class
        When Any String is being parsed
        Then The parser should ask the state manager for the root state

    Scenario: Parsing step
        Given An instance of the StateManager class
        And An instance of the Parser class
        When Any String is being parsed
        Then The parser should delegate each letter to the appropriate state

    Scenario: Parsing return
        Given An instance of the StateManager class
        And An instance of the Parser class
        When Any String is being parsed
        Then The parser should return the input Node