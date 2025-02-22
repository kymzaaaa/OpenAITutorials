from openai import OpenAI
client = OpenAI()

response = client.images.create_variation(
    model="dall-e-2",
    image=open("corgi_and_cat_paw.png", "rb"),
    n=1,
    size="1024x1024"
)

print(response.data[0].url)


# https://oaidalleapiprodscus.blob.core.windows.net/private/org-D2BLzRluryHGpRksno1DE7Rc/user-B6KABnjvAydHOUNa6jmnvjKv/img-OqzYnnJZ8o9IQ82xTtKgFW39.png?st=2025-02-21T17%3A52%3A46Z&se=2025-02-21T19%3A52%3A46Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-02-21T00%3A20%3A36Z&ske=2025-02-22T00%3A20%3A36Z&sks=b&skv=2024-08-04&sig=y2shwZfKlKfs8C2BdFI%2BY9OvcuApY0QWX5C/%2Bkp/DnY%3D

# each URL expires after an hour.
# node_modules/wsampletest/ImageGeneration/Variations.png