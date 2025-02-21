import base64
from openai import OpenAI

client = OpenAI()

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


# Path to your image
image_path = "0.png"

# Getting the Base64 string
base64_image = encode_image(image_path)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What is in this image?",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                },
            ],
        }
    ],
)

print(response.choices[0])



# Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='The image features a cartoon-style chicken. It has a white body, a red comb on its head, and a red wattle under its beak. The chicken is animated in appearance, with a cheerful expression and yellow beak and feet.', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None))