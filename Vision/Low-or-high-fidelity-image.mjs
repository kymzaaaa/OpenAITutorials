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
            "detail": "low"
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
//     content: 'The image features a scenic landscape with a wooden pathway leading through a lush green field. The sky is blue with some clouds, and there are trees and shrubs in the background. The atmosphere appears peaceful and natural, suggesting an outdoor setting, possibly in a park or nature reserve.',
//     refusal: null
//   },
//   logprobs: null,
//   finish_reason: 'stop'
// }