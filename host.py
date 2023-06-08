from flask import Flask, Response, render_template
import subprocess
import signal
from flask import request
import os
from flaskwebgui import FlaskUI
app = Flask(__name__)


def strms(magnet_link):

    @app.route('/')
    def index():
        print('index loaded')
        return render_template('index.html')

    @app.route('/stream')
    def stream():
        def generate():
            cmd = 'webtorrent "{0}" --stdout'.format(magnet_link)
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
            while True:
                line = p.stdout.readline()
                if not line:
                    break
                yield line
        return Response(generate(), content_type='video/mp4')

    @app.route('/shutdown', methods=['POST'])
    def shutdown():
        os._exit(0)
        shutdown_server()
        return 'Server shutting down...'

    def shutdown_server():
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RuntimeError('Not running with the Werkzeug Server')
        func()

    signal.signal(signal.SIGINT, lambda s, f: shutdown_server())

    return app
