import os

from main import create_app

app = create_app()


def start():
    port = int(os.environ.get('PORT', 9000))
    app.run(host='0.0.0.0', port=port,
            use_reloader='prod')


if __name__ == '__main__':
    start()
