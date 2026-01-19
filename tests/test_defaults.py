"""Tests for community defaults system."""

from faststrap_community.defaults import (
    get_community_defaults,
    list_community_components,
    reset_community_defaults,
    set_community_defaults,
)


class TestCommunityDefaults:
    def setup_method(self):
        """Reset defaults before each test."""
        reset_community_defaults()

    def test_get_defaults_returns_copy(self):
        """Ensure get_community_defaults returns a copy, not reference."""
        defaults1 = get_community_defaults("FlipCard")
        defaults2 = get_community_defaults("FlipCard")
        assert defaults1 == defaults2
        assert defaults1 is not defaults2  # Different objects

    def test_set_defaults(self):
        """Test setting custom defaults."""
        set_community_defaults("FlipCard", height="500px", duration="1s")
        defaults = get_community_defaults("FlipCard")
        assert defaults["height"] == "500px"
        assert defaults["duration"] == "1s"

    def test_set_defaults_updates_existing(self):
        """Test that set_defaults updates, not replaces."""
        set_community_defaults("FlipCard", height="500px")
        set_community_defaults("FlipCard", duration="1s")
        defaults = get_community_defaults("FlipCard")
        assert defaults["height"] == "500px"
        assert defaults["duration"] == "1s"
        assert "width" in defaults  # Original default still there

    def test_reset_defaults(self):
        """Test resetting defaults to original values."""
        original = get_community_defaults("FlipCard")
        set_community_defaults("FlipCard", height="999px")
        reset_community_defaults()
        after_reset = get_community_defaults("FlipCard")
        assert after_reset == original

    def test_list_components(self):
        """Test listing all components with defaults."""
        components = list_community_components()
        assert isinstance(components, list)
        assert "FlipCard" in components
        assert "DotsLoader" in components
        assert len(components) > 0

    def test_unknown_component_returns_empty(self):
        """Test that unknown component returns empty dict."""
        defaults = get_community_defaults("NonExistentComponent")
        assert defaults == {}
