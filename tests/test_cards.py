"""Tests for community card components."""

from fasthtml.common import to_xml

from faststrap_community import (
    FlipCard,
    GlowCard,
    PricingCard,
    ProfileCard,
    RevealCard,
    StatCard,
    TiltCard,
    TimelineCard,
)


class TestFlipCard:
    def test_basic_rendering(self):
        card = FlipCard(front="Front Content", back="Back Content")
        html = to_xml(card)
        assert "fs-comm-flip-card" in html
        assert "Front Content" in html
        assert "Back Content" in html

    def test_custom_dimensions(self):
        card = FlipCard(front="A", back="B", height="400px", width="50%")
        html = to_xml(card)
        assert "400px" in html
        assert "50%" in html


class TestGlowCard:
    def test_basic_rendering(self):
        card = GlowCard("Content")
        html = to_xml(card)
        assert "fs-comm-glow-card" in html
        assert "Content" in html

    def test_custom_glow_color(self):
        card = GlowCard("Content", glow_color="#ff0000")
        html = to_xml(card)
        assert "#ff0000" in html

    def test_intensity_levels(self):
        for intensity in ["low", "medium", "high"]:
            card = GlowCard("Content", intensity=intensity)
            html = to_xml(card)
            assert f"glow-{intensity}" in html


class TestProfileCard:
    def test_basic_rendering(self):
        card = ProfileCard(name="John Doe")
        html = to_xml(card)
        assert "fs-comm-profile-card" in html
        assert "John Doe" in html

    def test_with_all_fields(self):
        card = ProfileCard(
            name="Jane Smith", title="Developer", avatar="/img/jane.jpg", bio="Python enthusiast"
        )
        html = to_xml(card)
        assert "Jane Smith" in html
        assert "Developer" in html
        assert "/img/jane.jpg" in html
        assert "Python enthusiast" in html


class TestPricingCard:
    def test_basic_rendering(self):
        card = PricingCard(title="Pro", price="$29")
        html = to_xml(card)
        assert "fs-comm-pricing-card" in html
        assert "Pro" in html
        assert "$29" in html

    def test_with_features(self):
        features = ["Feature 1", "Feature 2", "Feature 3"]
        card = PricingCard(title="Pro", price="$29", features=features)
        html = to_xml(card)
        for feat in features:
            assert feat in html

    def test_highlighted_plan(self):
        card = PricingCard(title="Pro", price="$29", highlighted=True)
        html = to_xml(card)
        assert "RECOMMENDED" in html or "border-primary" in html


class TestStatCard:
    def test_basic_rendering(self):
        card = StatCard(title="Revenue", value="$12,345")
        html = to_xml(card)
        assert "fs-comm-stat-card" in html
        assert "Revenue" in html
        assert "$12,345" in html

    def test_with_trend(self):
        card = StatCard(title="Sales", value="100", trend="+12%", trend_positive=True)
        html = to_xml(card)
        assert "+12%" in html
        assert "success" in html or "↑" in html


class TestTimelineCard:
    def test_basic_rendering(self):
        card = TimelineCard(title="Event")
        html = to_xml(card)
        assert "fs-comm-timeline-card" in html
        assert "Event" in html

    def test_with_all_fields(self):
        card = TimelineCard(
            title="Project Launch",
            description="Deployed to production",
            timestamp="2 hours ago",
            icon="🚀",
        )
        html = to_xml(card)
        assert "Project Launch" in html
        assert "Deployed to production" in html
        assert "2 hours ago" in html
        assert "🚀" in html


class TestTiltCard:
    def test_basic_rendering(self):
        card = TiltCard("Content")
        html = to_xml(card)
        assert "fs-comm-tilt-card" in html
        assert "Content" in html


class TestRevealCard:
    def test_basic_rendering(self):
        card = RevealCard(image="/img/test.jpg", content="Revealed!")
        html = to_xml(card)
        assert "fs-comm-reveal-card" in html
        assert "/img/test.jpg" in html
        assert "Revealed!" in html
