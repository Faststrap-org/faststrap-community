"""Integration tests for setup_community."""

import pytest
from fasthtml.common import fast_app
from faststrap import add_bootstrap

from faststrap_community import setup_community


class TestSetupCommunity:
    def test_requires_bootstrap_first(self):
        """Test that setup_community enforces order."""
        app, rt = fast_app()

        with pytest.raises(RuntimeError, match="must be called AFTER add_bootstrap"):
            setup_community(app)

    def test_works_after_bootstrap(self):
        """Test that setup_community works when called correctly."""
        app, rt = fast_app()
        add_bootstrap(app)
        setup_community(app)

        # Check that community CSS was added
        assert any("community" in str(h) for h in app.hdrs)

    def test_pwa_mode(self):
        """Test PWA mode integration."""
        app, rt = fast_app()
        add_bootstrap(app)

        # Simulate PWA being enabled
        app._faststrap_pwa_cache_urls = []

        setup_community(app, pwa_mode=True)

        # Check that cache URLs were added
        assert len(app._faststrap_pwa_cache_urls) > 0
        assert any("community-base.css" in url for url in app._faststrap_pwa_cache_urls)

    def test_no_duplicate_injection(self):
        """Test that calling setup_community twice doesn't duplicate headers."""
        app, rt = fast_app()
        add_bootstrap(app)
        setup_community(app)

        initial_count = len(app.hdrs)

        setup_community(app)  # Call again

        # Should not increase header count
        assert len(app.hdrs) == initial_count
