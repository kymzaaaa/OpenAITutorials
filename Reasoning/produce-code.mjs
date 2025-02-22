import OpenAI from "openai";
const openai = new OpenAI();

const prompt = `
Instructions:
- Given the React component below, change it so that nonfiction books have red
  text. 
- Return only the code in your reply
- Do not include any additional formatting, such as markdown code blocks
- For formatting, use four space tabs, and do not allow any lines of code to 
  exceed 80 columns

const books = [
  { title: 'Dune', category: 'fiction', id: 1 },
  { title: 'Frankenstein', category: 'fiction', id: 2 },
  { title: 'Moneyball', category: 'nonfiction', id: 3 },
];

export default function BookList() {
  const listItems = books.map(book =>
    <li>
      {book.title}
    </li>
  );

  return (
    <ul>{listItems}</ul>
  );
}
`.trim();

const completion = await openai.chat.completions.create({
  model: "gpt-4o", 
  messages: [
    {
      role: "user",
      content: prompt,
    },
  ],
});

console.log(completion.choices[0].message.content);


console.log(completion.usage);


// node produce-code.mjs

// const books = [
//     { title: 'Dune', category: 'fiction', id: 1 },
//     { title: 'Frankenstein', category: 'fiction', id: 2 },
//     { title: 'Moneyball', category: 'nonfiction', id: 3 },
// ];

// export default function BookList() {
//     const listItems = books.map(book =>
//         <li style={{ color: book.category === 'nonfiction' ? 'red' : 'black' }}>
//             {book.title}
//         </li>
//     );

//     return (
//         <ul>{listItems}</ul>
//     );
// }
// {
//   prompt_tokens: 184,
//   completion_tokens: 127,
//   total_tokens: 311,
//   prompt_tokens_details: { cached_tokens: 0, audio_tokens: 0 },
//   completion_tokens_details: {
//     reasoning_tokens: 0,
//     audio_tokens: 0,
//     accepted_prediction_tokens: 0,
//     rejected_prediction_tokens: 0
//   }
// }