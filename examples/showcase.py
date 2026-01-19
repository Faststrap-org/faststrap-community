from fasthtml.common import *
from faststrap import add_bootstrap, Container, Row, Col, Card, Button
from faststrap_community import (
    setup_community, FlipCard, TiltCard, RevealCard, 
    DotsLoader, RingLoader, TypewriterLoader, ShadowLoader, PolygonLoader,
    VerticalMegaMenu
)

app = FastHTML()

# 1. Initialize Faststrap Core
add_bootstrap(app, theme="pink-love", mode="dark")

# 2. Initialize Faststrap Community
setup_community(app)

@app.route("/")
def get():
    return Container(
        H1("Faststrap Community Showcase", cls="text-center my-5"),
        
        # Loaders Section
        H2("Loaders", cls="mb-4"),
        Row(
            Col(Card(DotsLoader(), body_cls="d-flex justify-content-center", title="Dots Loader")),
            Col(Card(RingLoader(size="50px"), body_cls="d-flex justify-content-center", title="Ring Loader")),
            Col(Card(DotsLoader(variant="success"), body_cls="d-flex justify-content-center", title="Success Variant")),
            cls="mb-5"
        ),

        # Cards Section
        H2("Premium Cards", cls="mb-4"),
        Row(
            # Flip Card
            Col(
                FlipCard(
                    front=H3("Front Side"),
                    back=Div(H3("Back Side"), P("With some details"), Button("Action")),
                )
            ),
            # Tilt Card
            Col(
                TiltCard(
                    H3("Tilt Card"),
                    P("Hover over me to see the 3D lift effect."),
                    # cls="p-4"
                ),
                cls="d-flex" # Ensure card fills column
            ),
            # Reveal Card
            Col(
                RevealCard(
                    img_src="https://images.unsplash.com/photo-1518770660439-4636190af475?w=500",
                    title="Reveal Card",
                    description="This content is revealed on hover over the background image.",
                    button=Button("View Link", variant="outline-light")
                )
            ),
            cls="mb-5"
        ),
        


        # New Loaders Section
        H2("New Text & Geometric Loaders", cls="mb-4"),
        Row(
            Col(Card(TypewriterLoader(text="Processing..."), body_cls="d-flex justify-content-center", title="Typewriter")),
            Col(Card(ShadowLoader(text="Loading"), body_cls="d-flex justify-content-center", title="Matrix Shadow")),
            Col(Card(PolygonLoader(), body_cls="d-flex justify-content-center", title="Polygon Shift")),
            cls="mb-5"
        ),

        # Menus Section
        H2("Mega Menus", cls="mb-4"),
        Row(
            Col(
                VerticalMegaMenu([
                    {"label": "Home", "icon": "home", "subtitle": "Dashboard", "href": "#", "active": True},
                    {"label": "Products", "icon": "box", "subtitle": "Manage", "children": [
                        {"label": "Electronics", "href": "#"},
                        {"label": "Fashion", "href": "#"},
                        {"label": "Home", "href": "#"}
                    ]},
                    {"label": "Analytics", "icon": "chart", "subtitle": "Reports", "href": "#"}
                ]),
                cls="d-flex justify-content-center"
            ),
            cls="mb-5"
        ),
        
        cls="py-5"
    )

serve(port=5014)
