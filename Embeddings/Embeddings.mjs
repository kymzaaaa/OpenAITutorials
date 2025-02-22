import OpenAI from "openai";
const openai = new OpenAI();

const embedding = await openai.embeddings.create({
  model: "text-embedding-3-small",
  input: "Your text string goes here",
  encoding_format: "float",
});

console.log(embedding);


// Embeddings % node Embeddings.mjs 
// {
//   object: 'list',
//   data: [ { object: 'embedding', index: 0, embedding: [Array] } ],
//   model: 'text-embedding-3-small',
//   usage: { prompt_tokens: 5, total_tokens: 5 }
// }