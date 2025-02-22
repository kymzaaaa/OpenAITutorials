from openai import OpenAI

client = OpenAI()

# 音声ストリーミングのリクエスト
response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="Hello world! This is a streaming test.",
)

# ストリーミングしながら MP3 ファイルに保存
with open("output.mp3", "wb") as f:
    for chunk in response.iter_bytes():  # チャンク単位でデータを受信
        f.write(chunk)

print("Audio saved as output.mp3")



# MP3：一般的な用途のためのデフォルトの応答形式です。
# Opus：インターネットストリーミングや通信に適しており、低遅延です。
# AAC：デジタルオーディオ圧縮用で、YouTube、Android、iOSなどで好まれています。
# FLAC：ロスレスオーディオ圧縮用で、音楽愛好家によってアーカイブ用に好まれます。
# WAV：非圧縮のWAVオーディオで、低遅延アプリケーション向けにデコードオーバーヘッドを回避するのに適しています。
# PCM：WAVに似ていますが、ヘッダーなしで24kHz（16ビット、低位エンディアン）の生のサンプルが含まれています。

