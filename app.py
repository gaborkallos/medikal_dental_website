from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/mobile')
def m_index():
    return render_template("m.index.html")


if __name__ == '__main__':
    app.run()

