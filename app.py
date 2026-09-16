import os

def app(environ, start_response):
    html_path = os.path.join(os.path.dirname(__file__), 'index.html')
    if not os.path.exists(html_path):
        html_path = os.path.join(os.path.dirname(__file__), 'case-study', 'index.html')
    
    if os.path.exists(html_path):
        with open(html_path, 'rb') as f:
            content = f.read()
    else:
        content = b'<h1>Composio AI Research Case Study</h1>'

    start_response('200 OK', [
        ('Content-Type', 'text/html; charset=utf-8'),
        ('Content-Length', str(len(content))),
    ])
    return [content]

application = app
handler = app
