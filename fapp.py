from flask import Flask, render_template

# Basic endpoint, no html, good for test
app = Flask(__name__)
@app.route('/')
def index():
    return "hello from pi"

# Passing a different endpoint - note html markup
@app.route('/h')
def index1():
    return render_template('index.html')

# Using Jinja templates, passing a parameter
@app.route('/n/<name>')
def index2(name):
    return render_template('index2.html', my_name=name)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
