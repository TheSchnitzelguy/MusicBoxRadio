#!/usr/bin/env python3

import nowplaying
from Radio import Radio
from flask import Flask, render_template, request


localhost = '127.0.0.1'
app = Flask(__name__)
radio = Radio()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('vNext') == 'Volgende zender':
            print("Volgende zender pushed!")
            radio.next_ch()
            print(nowplaying.np)
        elif request.form.get("vPause") == 'Start/stop':
            print("Pause!")
            radio.pause_ch()
            print(nowplaying.np)
        elif request.form.get("vPrev") == 'Vorige zender':
            print("Vorige zender pushed!")
            radio.prev_ch()
            print(nowplaying.np)
        else:
            pass
    elif request.method == 'GET':
        return render_template('index.html', form = request.form)
    return render_template('index.html', currentStation = nowplaying.np)


def main():
    #app.run(host, port, debug, options)
    app.run(localhost, 8000, 0)

if __name__ == '__main__':
    main()
