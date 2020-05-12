# coding=utf-8
"""State Manager feature tests."""
from markdownparser import StateManager
from markdownparser.states import *
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers
)
import pytest


@scenario('features/state_manger.feature', 'Bold State request')
def test_bold_state_request():
    """Bold State request."""


@scenario('features/state_manger.feature', 'BoldOrEnum State request')
def test_boldorenum_state_request():
    """BoldOrEnum State request."""


@scenario('features/state_manger.feature', 'Enum State request')
def test_enum_state_request():
    """Enum State request."""


@scenario('features/state_manger.feature', 'Header State request')
def test_header_state_request():
    """Header State request."""


@scenario('features/state_manger.feature', 'Line State request')
def test_line_state_request():
    """Line State request."""


@scenario('features/state_manger.feature', 'Root state request')
def test_root_state_request():
    """Root state request."""


@scenario('features/state_manger.feature', 'Text State request')
def test_text_state_request():
    """Text State request."""


@given('A State Manager Instance')
def state_manager():
    """A State Manager Instance."""
    return StateManager()


@pytest.fixture
@when('The root state is requested')
def the_root_state_is_requested(state_manager, mocker):
    """The root state is requested."""
    return state_manager.get_root(mocker.MagicMock())


@pytest.fixture
@when(parsers.parse('the "{state}" state is requested'))
def the_state_is_requested(state_manager, state):
    """the "bold" state is requested."""
    return state_manager.get(state)


@then(parsers.parse('an instance of {clazz} should be returned'))
def an_instance_of_boldorenumstate_should_be_returned(the_state_is_requested, clazz):
    """an instance of BoldOrEnumState should be returned."""
    classes = {
        "NewLineState": NewLineState,
        "HeaderState": HeaderState,
        "BoldState": BoldState,
        "BoldOrEnumState": BoldOrEnumState,
        "EnumState": EnumState,
        "TextState": TextState
    }
    func = the_state_is_requested
    assert isinstance(func(), classes[clazz])


@then('any ParsingState should be returned')
def an_instance_of_boldorenumstate_should_be_returned(the_root_state_is_requested):
    """an instance of BoldOrEnumState should be returned."""
    assert isinstance(the_root_state_is_requested, ParsingState)
