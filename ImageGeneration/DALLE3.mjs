import OpenAI from "openai";
const openai = new OpenAI();

const response = await openai.images.generate({
  model: "dall-e-3",
  prompt: "a white siamese cat",
  n: 1,
  size: "1024x1024",
});

console.log(response.data[0].url);



// https://oaidalleapiprodscus.blob.core.windows.net/private/org-D2BLzRluryHGpRksno1DE7Rc/user-B6KABnjvAydHOUNa6jmnvjKv/img-p8wO4dynUAKx8fJIllYZTrMy.png?st=2025-02-21T17%3A00%3A33Z&se=2025-02-21T19%3A00%3A33Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-02-21T00%3A24%3A30Z&ske=2025-02-22T00%3A24%3A30Z&sks=b&skv=2024-08-04&sig=4nFUYSQ1NbNDfbBVPNkirqXOvZ6hafgaHp0/SyoRD9g%3D


// each URL expires after an hour.
// /Users/steve/Desktop/OpenAITutorials/node_modules/wsampletest/ImageGeneration/image.png