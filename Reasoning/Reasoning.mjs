import OpenAI from "openai";
const openai = new OpenAI();

const prompt = `
Write a bash script that takes a matrix represented as a string with 
format '[1,2],[3,4],[5,6]' and prints the transpose in the same format.
`;
 
const completion = await openai.chat.completions.create({
  model: "gpt-4o",
  reasoning_effort: "medium",
  messages: [
    {
      role: "user", 
      content: prompt
    }
  ],
  store: true,
});

console.log(completion.choices[0].message.content);