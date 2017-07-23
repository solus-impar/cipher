"""cipher: HTTP server."""
from flask import Flask, render_template, request
from cipher import shift_text


app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])

def index():
    """index"""

    key = ''
    text = ''
    output = ''

    if request.method == 'POST':
        key = request.form.get('key')
        text = request.form.get('input')
        output = shift_text(text, key)

    return render_template('index.html', key=key, text=text, output=output)
