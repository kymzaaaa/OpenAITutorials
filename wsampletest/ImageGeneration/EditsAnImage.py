from openai import OpenAI
client = OpenAI()

response = client.images.edit(
    model="dall-e-2",
    image=open("sunlit_lounge.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="A sunlit indoor lounge area with a pool containing a flamingo",
    n=1,
    size="1024x1024",
)

print(response.data[0].url)


# https://oaidalleapiprodscus.blob.core.windows.net/private/org-D2BLzRluryHGpRksno1DE7Rc/user-B6KABnjvAydHOUNa6jmnvjKv/img-acwYBBFyrTpG5cAAKKUwHZ26.png?st=2025-02-21T17%3A46%3A15Z&se=2025-02-21T19%3A46%3A15Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-02-21T00%3A26%3A31Z&ske=2025-02-22T00%3A26%3A31Z&sks=b&skv=2024-08-04&sig=AP6iORG542MGjfJ4Tytd2DhyUkS1m49vxzHDSn2WlbA%3D


# each URL expires after an hour.
# node_modules/wsampletest/ImageGeneration/EditedImage.png