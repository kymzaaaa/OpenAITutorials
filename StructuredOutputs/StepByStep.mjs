import OpenAI from "openai";
import { z } from "zod";
import { zodResponseFormat } from "openai/helpers/zod";

const openai = new OpenAI();

const Step = z.object({
  explanation: z.string(),
  output: z.string(),
});

const MathReasoning = z.object({
  steps: z.array(Step),
  final_answer: z.string(),
});

const completion = await openai.beta.chat.completions.parse({
  model: "gpt-4o-2024-08-06",
  messages: [
    { role: "system", content: "You are a helpful math tutor. Guide the user through the solution step by step." },
    { role: "user", content: "how can I solve 8x + 7 = -23" },
  ],
  response_format: zodResponseFormat(MathReasoning, "math_reasoning"),
});

const math_reasoning = completion.choices[0].message.parsed;

console.log(math_reasoning);





// (base) steve@StevenoMacBook-Pro StructuredOutputs % node StepByStep.mjs
// {
//   steps: [
//     {
//       explanation: 'The given equation is 8x + 7 = -23. We need to solve for x, which means we want to isolate x on one side. We can start by getting rid of the constant term on the left side of the equation.',
//       output: '8x + 7 = -23'
//     },
//     {
//       explanation: 'Subtract 7 from both sides of the equation to eliminate the +7 on the left side.',
//       output: '8x + 7 - 7 = -23 - 7'
//     },
//     {
//       explanation: 'Simplify both sides: the left side becomes 8x and the right side becomes -30.',
//       output: '8x = -30'
//     },
//     {
//       explanation: 'Now, to isolate x, divide both sides of the equation by 8, the coefficient of x.',
//       output: '8x / 8 = -30 / 8'
//     },
//     {
//       explanation: 'Simplify the right side of the equation to get the value of x.',
//       output: 'x = -30 / 8'
//     },
//     {
//       explanation: 'Simplify -30 / 8. Both the numerator and the denominator can be divided by 2.',
//       output: 'x = -15 / 4'
//     },
//     {
//       explanation: 'This fraction cannot be simplified further, and it represents the solution for x.',
//       output: 'x = -15/4'
//     }
//   ],
//   final_answer: 'x = -15/4'
// }