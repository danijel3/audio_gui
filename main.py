from subprocess import run, PIPE

from flask import logging, Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/audio', methods=['POST'])
def audio():
    with open('/tmp/audio.wav', 'wb') as f:
        f.write(request.data)
    proc = run(['ffprobe', '-of', 'default=noprint_wrappers=1', '/tmp/audio.wav'], text=True, stderr=PIPE)
    return proc.stderr


if __name__ == "__main__":
    app.logger = logging.getLogger('audio-gui')
    app.run(debug=True)
