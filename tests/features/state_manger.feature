Feature: State Manager
    State Manager should work as intended

    Scenario: Root state request
        Given A State Manager Instance
        When The root state is requested
        Then an instance of ParsingState should be returned

    Scenario: Line State request
        Given A State Manager Instance
        When the "line_start" state is requested
        Then an instance of LineStartState should be returned

    Scenario: Header State request
        Given A State Manager Instance
        When the "header" state is requested
        Then an instance of HeaderState should be returned

    Scenario: Text State request
        Given A State Manager Instance
        When the "text" state is requested
        Then an instance of TextState should be returned

    Scenario: Bold State request
        Given A State Manager Instance
        When the "bold" state is requested
        Then an instance of BoldState should be returned

    Scenario: BoldOrEnum State request
        Given A State Manager Instance
        When the "bold_or_enum" state is requested
        Then an instance of BoldOrEnumState should be returned

    Scenario: Enum State request
        Given A State Manager Instance
        When the "enum" state is requested
        Then an instance of EnumState should be returned

