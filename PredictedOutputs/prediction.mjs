import OpenAI from "openai";

const code = `
class User {
  firstName: string = "";
  lastName: string = "";
  username: string = "";
}

export default User;
`.trim();

const openai = new OpenAI();

const refactorPrompt = `
Replace the "username" property with an "email" property. Respond only 
with code, and with no markdown formatting.
`;

const completion = await openai.chat.completions.create({
  model: "gpt-4o",
  messages: [
    {
      role: "user",
      content: refactorPrompt
    },
    {
      role: "user",
      content: code
    }
  ],
  store: true,
  prediction: {
    type: "content",
    content: code
  }
});

// Inspect returned data
console.log(completion);
console.log(completion.choices[0].message.content);




// username to email 
//low token count

// (base) steve@StevenoMacBook-Pro PredictedOutputs % node prediction.mjs 
// {
//   id: 'chatcmpl-B3jweGm9tLJHpj1t2bNv8cSKN78GK',
//   object: 'chat.completion',
//   created: 1740231296,
//   model: 'gpt-4o-2024-08-06',
//   choices: [
//     {
//       index: 0,
//       message: [Object],
//       logprobs: null,
//       finish_reason: 'stop'
//     }
//   ],
//   usage: {
//     prompt_tokens: 65,
//     completion_tokens: 39,
//     total_tokens: 104,
//     prompt_tokens_details: { cached_tokens: 0, audio_tokens: 0 },
//     completion_tokens_details: {
//       reasoning_tokens: 0,
//       audio_tokens: 0,
//       accepted_prediction_tokens: 17,
//       rejected_prediction_tokens: 10
//     }
//   },
//   service_tier: 'default',
//   system_fingerprint: 'fp_eb9dce56a8'
// }
// class User {
//   firstName: string = "";
//   lastName: string = "";
//   email: string = "";
// }