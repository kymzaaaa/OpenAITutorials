from pathlib import Path
from openai import OpenAI

client = OpenAI()
speech_file_path = Path(__file__).parent / "speech.mp3"

response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="Today is a wonderful day to build something people love!",
).with_streaming_response()

response.stream_to_file(speech_file_path)

# voice=
# alloy, ash, coral, echo, fable, onyx, nova, sage, shimmer