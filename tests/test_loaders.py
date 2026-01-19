from fasthtml.common import to_xml

from faststrap_community import DotsLoader, RingLoader


def test_dots_loader():
    loader = DotsLoader(variant="danger")
    xml = to_xml(loader)
    assert "fs-comm-dots-loader" in xml
    assert "background-color: var(--bs-danger)" in xml


def test_ring_loader():
    loader = RingLoader(variant="success", size="100px")
    xml = to_xml(loader)
    assert "fs-comm-ring-loader" in xml
    assert "border-color: var(--bs-success)" in xml
    assert "width: 100px" in xml
