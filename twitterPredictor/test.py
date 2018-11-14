import pytest

from twitterPredictor.hello_world import twitter_setup


def test_function():
    assert twitter_setup() != 0

test_function()
