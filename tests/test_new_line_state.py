# coding=utf-8
"""New Line State feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers
)
import pytest
from markdownparser.states import *


@scenario('features/new_line_state.feature', 'Bold or Enum parsing')
def test_bold_or_enum_parsing():
    """Bold or Enum parsing."""


@scenario('features/new_line_state.feature', 'Header parsing')
def test_header_parsing():
    """Header parsing."""


@scenario('features/new_line_state.feature', 'Setting Document Node')
def test_setting_document_node():
    """Setting Document Node."""


@scenario('features/new_line_state.feature', 'Should ingore starting whitespace')
def test_should_ingore_starting_whitespace():
    """Should ingore starting whitespace."""


@scenario('features/new_line_state.feature', 'Text parsing')
def test_text_parsing():
    """Text parsing."""


@given('A NewLineState instance')
def a_newlinestate_instance():
    """A NewLineState instance."""
    return NewLineState()


@given('A StateManager instance')
def a_statemanager_instance(mocker):
    """A StateManager instance."""
    state_manager = mocker.MagicMock()

    return state_manager


@pytest.fixture
@when(parsers.parse('The state accepts "{str}"'))
def the_state_accepts(str, a_newlinestate_instance, a_statemanager_instance):
    """The state accepts " "."""
    return a_newlinestate_instance.accept(str, a_statemanager_instance)


@when('a new document node is set')
def a_new_document_node_is_set(a_newlinestate_instance, mocker):
    """a new document node is set."""
    a_newlinestate_instance.document_node = mocker.MagicMock()


@then(parsers.parse('The state should ask the state manager for a "{name}" state'))
def the_state_should_ask_the_state_manager_for_state(name, a_statemanager_instance):
    """The state should ask the state manager for a "bold_or_enum" state."""
    a_statemanager_instance.get.assert_called_with(name)


@then('The state should return itself')
def the_state_should_return_itself(the_state_accepts, a_newlinestate_instance):
    """The state should return itself."""
    assert the_state_accepts is a_newlinestate_instance


@then('no error should be returned')
def no_error_should_be_returned():
    """no error should be returned."""
    assert True
