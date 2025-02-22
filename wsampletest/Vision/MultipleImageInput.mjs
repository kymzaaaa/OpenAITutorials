import OpenAI from "openai";
const openai = new OpenAI();

const response = await openai.chat.completions.create({
  model: "gpt-4o-mini",
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "What are in these images? Is there any difference between them?" },
        {
          type: "image_url",
          image_url: {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
          },
        },
        {
          type: "image_url",
          image_url: {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
          },
        }
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
//     content: "The images you've provided appear to be identical, showcasing a scenic landscape with a wooden boardwalk leading through a grassy area under a blue sky with clouds. Since they are the same, there would be no differences to compare. If you have any specific aspects you'd like to discuss about the images, feel free to ask!",
//     refusal: null
//   },
//   logprobs: null,
//   finish_reason: 'stop'
// }