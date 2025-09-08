from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__, static_folder='static', template_folder='templates') # Create a Flask application instance

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    message = request.form.get('message')
    print(f"Received message from {name}: {message}")
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)