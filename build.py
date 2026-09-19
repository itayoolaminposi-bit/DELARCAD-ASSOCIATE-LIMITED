import os

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NAV_ITEMS = [
    ("index.html", "Home"),
    ("about-us.html", "About Us"),
    ("about-delarcad.html", "The Practice"),
    ("resources.html", "Resources"),
    ("how-it-works.html", "How It Works"),
    ("contact.html", "Contact"),
]

def head(title, description):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · DELARCAD ASSOCIATE LIMITED</title>
<meta name="description" content="{description}">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><rect width=%22100%22 height=%22100%22 fill=%22%2316233A%22/><path d=%22M20 78 L50 22 L80 78 M32 78 L32 55 L68 55 L68 78%22 stroke=%22%23A9812C%22 stroke-width=%225%22 fill=%22none%22/></svg>">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
"""

def nav(active):
    items = ""
    for href, label in NAV_ITEMS:
        cls = ' class="active"' if href == active else ""
        items += f'<li><a href="{href}"{cls}>{label}</a></li>\n'
    return f"""<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html">
      <span class="brand-mark">D</span>
      <span class="brand-name">DELARCAD <b>ASSOCIATE</b> LTD</span>
    </a>
    <ul class="nav-links">
      {items}
    </ul>
    <div class="nav-cta">
      <a class="btn btn-ghost-light" href="get-started.html">Start a Project</a>
      <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false"><span></span></button>
    </div>
  </div>
</header>
"""

def footer():
    return """<footer class="site-footer">
  <div class="wrap footer-top">
    <div class="footer-brand">
      <span class="brand-name" style="color:#F6F4EF;">DELARCAD <b style="color:#A9812C;">ASSOCIATE</b> LTD</span>
      <p>An architecture and design practice working across residential, civic and commercial projects, with partners on five continents.</p>
    </div>
    <div>
      <h4>Practice</h4>
      <ul>
        <li><a href="about-us.html">About Us</a></li>
        <li><a href="about-delarcad.html">The Practice</a></li>
        <li><a href="how-it-works.html">How It Works</a></li>
      </ul>
    </div>
    <div>
      <h4>Work With Us</h4>
      <ul>
        <li><a href="resources.html">Resources</a></li>
        <li><a href="get-started.html">Start a Project</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </div>
    <div>
      <h4>Studio</h4>
      <ul>
        <li><a href="mailto:studio@delarcad.com">studio@delarcad.com</a></li>
        <li><a href="tel:+11234567890">+1 (123) 456 7890</a></li>
        <li>Lagos &middot; London &middot; Toronto</li>
      </ul>
    </div>
  </div>
  <div class="wrap footer-bottom">
    <span>&copy; 2026 Delarcad Associate Limited. All rights reserved.</span>
    <span>Registered architecture practice</span>
  </div>
</footer>
<script src="js/main.js"></script>
</body>
</html>
"""

def page(filename, title, description, body):
    with open(os.path.join(OUT, filename), "w") as f:
        f.write(head(title, description))
        f.write(nav(filename))
        f.write(body)
        f.write(footer())

PAGES = {}

def register(filename, title, description, body):
    PAGES[filename] = (title, description, body)
