from flask import Flask, render_template

app = Flask(__name__)

app.secret_key = 'db_secret'


@app.route('/')
def home():
    return render_template('generate-keys.html')


@app.route('/alive')
def alive():
    return 'Alive!'


@app.route('/generate-keys')
def generate_keys():
    return render_template('generate-keys.html')


def main():
    context = ('static/fullchain.pem', 'static/privkey.pem')
    app.run(host='0.0.0.0', ssl_context=context, port=9443)

if __name__ == '__main__':
    main()
