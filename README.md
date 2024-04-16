# vmzoom

# DEMO
## イメージ動画
https://youtu.be/-WAq3qzAun0?t=41

## ブラウザ画面イメージ
![image](https://github.com/iwatadive28/vmzoom/assets/62125060/e77ef353-8986-4955-97a8-8989023940b1)

## 構成図（仮）
![image](https://github.com/iwatadive28/vmzoom/assets/62125060/5cf8d17d-1485-4afe-a031-9c851f39ef6b)

## ユースケース（仮）
- スタッフ：施設の従業員. 遠隔から私用or施設のスマホからZoomで通話する. ロボットを操作する.
- お客様：施設利用者. 困ったときにブラウザ画面上でスタッフにコールする.

# Requirement

- Flask==3.0.1
- numpy==1.24.4
- opencv-python==4.9.0.80
- PyAudio==0.2.14
- urllib3==2.1.0

# Installation
 
# Usage

```bash
git clone https://github.com/iwatadive28/vmzoom.git
cd vmzoom
python main.py
```
# Note
作業中.以下、これから作っていきたい. 
## 開発したい項目
### アバター
- オリジナルキャラクターのアバターを作成したい.

### Zoom連携機能
- "Call"ボタンを押すとスタッフにコールする
- "End Call"ボタンを押すと通話を切る

### OBS連携機能
- アプリ起動時に仮想カメラ開始

### VmagicMirror連携機能
- アプリ起動時にVmagicMirror起動

### ローカルサーバーからクラウドへの移行
- AWSで動作するアプリにしたい

### ブラウザだけで動作させたい
- 参考：[WEB SEREEN](https://web-screen.net/ja/streaming/)

### フロントエンドの画面を充実させる
- ユーザーフレンドリーな画面表示にする.

### AIアシスタント機能
- スタッフではなくAIが音声応答するモード追加.

# Author

# License
