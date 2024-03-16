from application import create_app

app = create_app()

@app.route('/')
def hello():
    return 'hello world'

if __name__ == '__main__':
    app.run(host='0.0.0.0')