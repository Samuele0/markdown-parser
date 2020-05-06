# coding=utf-8
"""Parser feature tests."""
from pytest import fixture
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
import unittest.mock as mock
from markdownparser import Parser


@fixture
def context():
    class Context(object):
        pass

    return Context()


@scenario('features/parser.feature', 'Parsing is starting')
def test_parsing_is_starting():
    """Parsing is starting."""


@scenario('features/parser.feature', 'Parsing step')
def test_parsing_step():
    """Parsing step."""


@given('An instance of the Parser class')
def parser_class(context):
    """An instance of the Parser class."""
    context.parser = Parser(context.statemanager)


@given('An instance of the StateManager class')
def statemanager_class(mocker, context):
    """An instance of the StateManager class."""
    mock = mocker.MagicMock()
    state = mocker.MagicMock()
    state.accept.return_value = state
    mock.root_state.return_value = state
    context.statemanager = mock
    context.state = state


@when('Any String is being parsed')
def any_string_is_being_parsed(context):
    """Any String is being parsed."""
    context.parser.parse("abcd")


@then('The parser should ask the state manager for the root state')
def the_parser_should_ask_the_state_manager_for_the_root_state(context):
    """The parser should ask the state manager for the root state."""
    context.statemanager.root_state.assert_called()


@then('The parser should delegate each letter to the appropriate state')
def parser_delegation(context):
    """The parser should delegate each letter to the appropriate state"""
    context.state.accept.assert_has_calls(
        [mock.call('a'), mock.call('b'), mock.call('c'), mock.call('d')])
