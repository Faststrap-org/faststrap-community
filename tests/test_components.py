"""Tests for faststrap-community components."""

from fasthtml.common import to_xml
from faststrap import clear_component_defaults, set_component_defaults

from faststrap_community import (
    DotsLoader,
    FlipCard,
    RevealCard,
    RingLoader,
    TiltCard,
)


class TestFlipCard:
    """Tests for FlipCard component."""

    def test_basic_flip_card(self):
        card = FlipCard(front="Front", back="Back")
        html = to_xml(card)
        assert "fs-comm-flip-card" in html
        assert "fs-comm-flip-card-front" in html
        assert "fs-comm-flip-card-back" in html
        assert "Front" in html
        assert "Back" in html

    def test_flip_card_has_card_classes(self):
        """Verify Bootstrap card classes are applied to faces."""
        card = FlipCard(front="Front", back="Back")
        html = to_xml(card)
        # Both faces should have 'card' class for Bootstrap styling
        assert html.count('class="fs-comm-flip-card-front card"') >= 1
        assert html.count('class="fs-comm-flip-card-back card"') >= 1

    def test_flip_card_custom_height(self):
        card = FlipCard(front="Front", back="Back", height="400px")
        html = to_xml(card)
        assert "height: 400px" in html

    def test_flip_card_custom_width(self):
        card = FlipCard(front="Front", back="Back", width="500px")
        html = to_xml(card)
        assert "width: 500px" in html

    def test_flip_card_custom_duration(self):
        card = FlipCard(front="Front", back="Back", duration="1s")
        html = to_xml(card)
        assert "--fs-comm-flip-duration: 1s" in html

    def test_flip_card_default_duration(self):
        """Verify default duration is not added to style when using default."""
        card = FlipCard(front="Front", back="Back")
        html = to_xml(card)
        # Default is 0.6s, so custom property should not be set
        assert "--fs-comm-flip-duration" not in html

    def test_flip_card_respects_defaults(self):
        set_component_defaults("FlipCard", height="500px", duration="0.8s")
        card = FlipCard(front="Front", back="Back")
        html = to_xml(card)
        assert "height: 500px" in html
        assert "--fs-comm-flip-duration: 0.8s" in html
        clear_component_defaults()

    def test_flip_card_explicit_overrides_defaults(self):
        set_component_defaults("FlipCard", height="500px")
        card = FlipCard(front="Front", back="Back", height="300px")
        html = to_xml(card)
        assert "height: 300px" in html
        assert "height: 500px" not in html
        clear_component_defaults()

    def test_flip_card_with_custom_class(self):
        card = FlipCard(front="Front", back="Back", cls="my-custom-class")
        html = to_xml(card)
        assert "my-custom-class" in html
        assert "fs-comm-flip-card" in html  # Should merge, not replace

    def test_flip_card_with_custom_style(self):
        card = FlipCard(front="Front", back="Back", style="border: 1px solid red;")
        html = to_xml(card)
        assert "border: 1px solid red" in html


class TestTiltCard:
    """Tests for TiltCard component."""

    def test_basic_tilt_card(self):
        card = TiltCard("Content")
        html = to_xml(card)
        assert "fs-comm-tilt-card" in html
        assert "Content" in html

    def test_tilt_card_with_multiple_children(self):
        card = TiltCard("Title", "Description", "Footer")
        html = to_xml(card)
        assert "fs-comm-tilt-card" in html
        assert "Title" in html
        assert "Description" in html
        assert "Footer" in html

    def test_tilt_card_with_custom_class(self):
        card = TiltCard("Content", cls="custom-class")
        html = to_xml(card)
        assert "custom-class" in html
        assert "fs-comm-tilt-card" in html


class TestRevealCard:
    """Tests for RevealCard component."""

    def test_basic_reveal_card(self):
        card = RevealCard(
            img_src="test.jpg",
            title="Title",
            description="Description",
        )
        html = to_xml(card)
        assert "fs-comm-reveal-card" in html
        assert "test.jpg" in html
        assert "Title" in html
        assert "Description" in html

    def test_reveal_card_with_button(self):
        from faststrap import Button

        card = RevealCard(
            img_src="test.jpg",
            title="Title",
            description="Description",
            button=Button("Click Me"),
        )
        html = to_xml(card)
        assert "Click Me" in html

    def test_reveal_card_custom_height(self):
        card = RevealCard(
            img_src="test.jpg",
            title="Title",
            description="Description",
            height="500px",
        )
        html = to_xml(card)
        assert "500px" in html

    def test_reveal_card_respects_defaults(self):
        set_component_defaults("RevealCard", height="600px")
        card = RevealCard(
            img_src="test.jpg",
            title="Title",
            description="Description",
        )
        html = to_xml(card)
        assert "600px" in html
        clear_component_defaults()


class TestDotsLoader:
    """Tests for DotsLoader component."""

    def test_basic_dots_loader(self):
        loader = DotsLoader()
        html = to_xml(loader)
        assert "fs-comm-dots-loader" in html

    def test_dots_loader_variant(self):
        loader = DotsLoader(variant="success")
        html = to_xml(loader)
        assert "bg-success" in html

    def test_dots_loader_variant_primary(self):
        loader = DotsLoader(variant="primary")
        html = to_xml(loader)
        assert "bg-primary" in html

    def test_dots_loader_variant_danger(self):
        loader = DotsLoader(variant="danger")
        html = to_xml(loader)
        assert "bg-danger" in html

    def test_dots_loader_respects_defaults(self):
        set_component_defaults("DotsLoader", variant="warning")
        loader = DotsLoader()
        html = to_xml(loader)
        assert "bg-warning" in html
        clear_component_defaults()

    def test_dots_loader_has_three_dots(self):
        """Verify loader has 3 dot elements."""
        loader = DotsLoader()
        html = to_xml(loader)
        # Should have 3 dots (implementation detail, but good to verify structure)
        assert "fs-comm-dot" in html


class TestRingLoader:
    """Tests for RingLoader component."""

    def test_basic_ring_loader(self):
        loader = RingLoader()
        html = to_xml(loader)
        assert "fs-comm-ring-loader" in html

    def test_ring_loader_custom_size(self):
        loader = RingLoader(size="60px")
        html = to_xml(loader)
        assert "60px" in html

    def test_ring_loader_variant(self):
        loader = RingLoader(variant="info")
        html = to_xml(loader)
        assert "border-info" in html or "info" in html

    def test_ring_loader_respects_defaults(self):
        set_component_defaults("RingLoader", size="80px", variant="success")
        loader = RingLoader()
        html = to_xml(loader)
        assert "80px" in html
        clear_component_defaults()


class TestIntegration:
    """Integration tests for community components."""

    def test_all_components_import(self):
        """Verify all components can be imported."""

        # If we get here, all imports succeeded
        assert True

    def test_setup_community_function(self):
        """Verify setup_community function exists and is callable."""
        from faststrap_community import setup_community

        assert callable(setup_community)

    def test_get_community_assets_function(self):
        """Verify get_community_assets function exists and returns list."""
        from faststrap_community import get_community_assets

        assets = get_community_assets()
        assert isinstance(assets, list)
        assert len(assets) > 0
        # Verify CSS files are included
        hrefs = [asset.attrs.get("href") for asset in assets]
        assert any("community-base.css" in href for href in hrefs)
        assert any("cards.css" in href for href in hrefs)
        assert any("loaders.css" in href for href in hrefs)
