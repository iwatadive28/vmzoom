# coding: utf-8
from flask import Flask, render_template, redirect, url_for, request,send_from_directory
from app import myzoom
from flask_socketio import SocketIO, emit
import cv2
import base64
import pyaudio
import numpy as np

# Flaskアプリケーションの初期化
app = Flask(__name__)
socketio = SocketIO(app)

# ビデオキャプチャの初期化 # グローバル変数
cap = cv2.VideoCapture(1)

# マイクの初期化
p = pyaudio.PyAudio()
def callback(in_data, frame_count, time_info, status):
    return (in_data, pyaudio.paContinue)

audio_stream  = p.open( format=pyaudio.paInt16,
                        channels=1,
                        rate=44100,
                        input=True,
                        output = True, # inputとoutputを同時にTrueにする
                        input_device_index=2,    # 使用する入力デバイスのインデックスを指定
                        output_device_index=5,    # 使用する入力デバイスのインデックスを指定
                        frames_per_buffer=1024,
                        stream_callback=callback)
# URLのルーティング
# Home
@app.route('/')
def home():
    return render_template('home.html')

# Zoom通話の開始
@app.route('/start_zoom_call')
def start_zoom_call():
    # Zoom通話の開始処理（Zoom APIを使用）
    myzoom.myzoom()

    # 通話情報を取得
    zoom_url = 'url'

    return render_template('zoom_call.html', zoom_url=zoom_url)

# Zoom通話の終了
@app.route('/end_zoom_call')
def end_zoom_call():
    # Zoom通話の終了処理（Zoom APIを使用）
    return redirect(url_for('home'))

# ビデオフィードをリアルタイムでクライアントに送信
def video_feed():
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = base64.b64encode(buffer)
        frame_str = frame_bytes.decode('utf-8')

        # 'video_feed' イベントでクライアントにフレームを送信
        socketio.emit('video_feed', {'frame': frame_str})

        # サーバー負荷軽減のために少し待機
        socketio.sleep(0.20)

def audio_feed():
    while True:
        # audio_stream.start_stream()
        """
        audio_data = audio_stream.read(1024)
        audio_array = np.frombuffer(audio_data, dtype=np.int16)
        audio_str = base64.b64encode(audio_array.tobytes()).decode('utf-8')

        # socketio.emit('audio_feed', {'audio': audio_str})
        socketio.emit('audio_feed', {'audio': audio_array.tolist()})
        # socketio.sleep(0.03)
        """

# 音声ファイル再生(テスト)
"""
def play():
    return send_from_directory("music", filename)
"""

# サーバーが起動したときに video_feed 関数を非同期で開始
# クライアントが接続すると呼び出され、ビデオフィードとオーディオフィードを送信するバックグラウンドタスクを開始
@socketio.on('connect')
def connect():
    socketio.start_background_task(target=video_feed)
    # socketio.start_background_task(target=audio_feed)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=False)
