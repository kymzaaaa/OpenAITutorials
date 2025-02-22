import OpenAI from "openai";
const openai = new OpenAI();

const completion = await openai.chat.completions.create({
    model: "gpt-4o",
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
                }
            ],
        },
    ],
    store: true,
});

console.log(completion.choices[0].message);

// {
//     role: 'assistant',
//     content: 'The image shows a wooden boardwalk pathway leading through a green, grassy field. The sky above is blue with scattered clouds. There are trees and shrubs in the distance, creating a peaceful natural landscape.',
//     refusal: null
//   }