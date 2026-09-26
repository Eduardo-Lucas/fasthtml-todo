from fasthtml.common import Link, fast_app, serve

from app.routes import register

app, rt = fast_app(hdrs=(Link(rel="stylesheet", href="/static/style.css"),))
register(app)

serve()
