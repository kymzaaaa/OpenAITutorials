import OpenAI from "openai";
const openai = new OpenAI();

const response = await openai.chat.completions.create({
  model: "gpt-4o-mini",
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "What's in this image?" },
        {
          type: "image_url",
          image_url: {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
          },
        },
      ],
    },
  ],
  store: true,
});

console.log(response.choices[0]);


// {
//   index: 0,
//   message: {
//     role: 'assistant',
//     content: 'The image depicts a landscape featuring a wide, wooden boardwalk or pathway that stretches through a lush green field. The background includes trees and bushes, and the sky above is filled with soft clouds, creating a serene and natural setting. The grass appears vibrant and is interspersed with variations in sunlight. Overall, it captures a peaceful outdoor scene, likely in a wetland or grassy area.',
//     refusal: null
//   },
//   logprobs: null,
//   finish_reason: 'stop'
// }