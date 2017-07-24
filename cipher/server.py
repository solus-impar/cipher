"""cipher: HTTP server."""
from flask import Flask, render_template, request
from cipher.encode import shift_text, substitute_text


app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])

def index():
    """Renders the site `index.html` template."""

    key = ''
    text = ''
    output = ''

    if request.method == 'POST':
        key = request.form.get('key')
        text = request.form.get('input')
        if 'shift' in request.form:
            output = shift_text(text, key)
        elif 'sub' in request.form:
            output = substitute_text(text, key)

    return render_template('index.html', key=key, text=text, output=output)


def start_server(host, port):
    """Starts up flask app.

    Args:
        host (str): Host address.
        port (str): Port number.

    Returns:
        None

    Raises:
        None
    """

    app.run(host=host, port=port)
