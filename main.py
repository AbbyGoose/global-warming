from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def global_w():
    return render_template('index.html')

@app.route('/reason')
def reason():
    return render_template('reason.html')

@app.route('/next')
def next():
    return render_template('next.html')

@app.route('/choice')
def choice():
    return render_template('choice.html')

if __name__ == "__main__":
    app.run(debug=True)
