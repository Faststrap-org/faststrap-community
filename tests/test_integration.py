from fasthtml.common import FastHTML

from faststrap_community import setup_community


def test_asset_loading():
    app = FastHTML()
    setup_community(app)

    # Check if community CSS links are in hdrs
    hrefs = [h.attrs.get("href") for h in app.hdrs if hasattr(h, "attrs") and h.tag == "link"]
    assert any("community-base.css" in h for h in hrefs)
    assert any("cards.css" in h for h in hrefs)


def test_idempotent_setup():
    app = FastHTML()
    setup_community(app)
    count_before = len(app.hdrs)
    setup_community(app)
    assert len(app.hdrs) == count_before
