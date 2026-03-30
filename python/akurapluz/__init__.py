"""
AkuraPluz v1.0.1 — Sinhala Font CSS Library
Generated: 2026-03-30 10:05:19

Usage:
    from akurapluz import stylesheet_link, font_class

    # In Flask/Jinja2:
    {{ akurapluz.stylesheet_link() | safe }}
    <p class="{{ akurapluz.font_class('Bindumathi') }}">ආයුබෝවන් !</p>

    # In Django:
    from akurapluz import stylesheet_link
    # Add to context: {'akp_link': stylesheet_link()}
"""

__version__ = "1.0.1"
__author__  = "Samith D Dilshan"
__license__ = "MIT"

CDN_URL     = "https://cdn.akurapluz.dulaksha.com"
STYLE_URL   = "https://cdn.akurapluz.dulaksha.com/style.css"

# Map of font family name → woff2 CDN URL
FONT_URLS: dict[str, str] = {{
    "bindumathi": "https://cdn.akurapluz.dulaksha.com/fonts/bindumathi/bindumathi.woff2",
    "malithi": "https://cdn.akurapluz.dulaksha.com/fonts/malithi/malithi.woff2",
    "Roboto-Bold": "https://cdn.akurapluz.dulaksha.com/fonts/roboto-bold/roboto-bold.woff2",
    "emanee": "https://cdn.akurapluz.dulaksha.com/fonts/emanee/emanee.woff2",
    "ganganee": "https://cdn.akurapluz.dulaksha.com/fonts/ganganee/ganganee.woff2",
}}

# Available CSS class names
FONT_CLASSES: list[str] = [
    "font-bindumathi",
    "font-malithi",
    "font-roboto-bold",
    "font-emanee",
    "font-ganganee",
]


def stylesheet_link(media: str = "all") -> str:
    \"\"\"Return the HTML <link> tag to include the AkuraPluz CSS library.

    Args:
        media: CSS media attribute (default 'all')

    Returns:
        str: HTML link tag string

    Example::

        from akurapluz import stylesheet_link
        print(stylesheet_link())
        # <link rel="stylesheet" href="https://cdn.akurapluz.dulaksha.com/style.css" media="all">
    \"\"\"
    return f'<link rel="stylesheet" href="{{STYLE_URL}}" media="{{media}}">'


def font_class(family: str) -> str:
    \"\"\"Return the CSS class name for a given font family.

    Args:
        family: Font family name, e.g. 'Bindumathi'

    Returns:
        str: CSS class name, e.g. 'font-bindumathi'

    Example::

        from akurapluz import font_class
        cls = font_class('Bindumathi')  # 'font-bindumathi'
        html = f'<p class="{{cls}}">ආයුබෝවන් !</p>'
    \"\"\"
    slug = family.lower()
    slug = "".join(c if c.isalnum() else "-" for c in slug).strip("-")
    return f"font-{{slug}}"


def font_url(family: str) -> str:
    \"\"\"Return the CDN URL for a font's woff2 file.

    Args:
        family: Font family name, e.g. 'Bindumathi'

    Returns:
        str: Direct WOFF2 CDN URL, or empty string if not found
    \"\"\"
    return FONT_URLS.get(family, "")


def list_fonts() -> list[str]:
    \"\"\"Return a list of all available Sinhala font family names.\"\"\"
    return list(FONT_URLS.keys())


def django_context() -> dict:
    \"\"\"Return a dict for use in Django template context.

    Example::

        from akurapluz import django_context
        # In views.py:
        context = {{**your_context, **django_context()}}
        # In template:
        # {{ akp_link|safe }}
        # <p class="{{ akp_font_bindumathi }}">ආයුබෝවන් !</p>
    \"\"\"
    ctx = {{"akp_link": stylesheet_link()}}
    for family in FONT_URLS:
        slug = font_class(family).replace("-", "_")
        ctx[f"akp_{{slug}}"] = font_class(family)
    return ctx