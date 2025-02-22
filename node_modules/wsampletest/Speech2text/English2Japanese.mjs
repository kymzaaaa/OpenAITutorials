import fs from "fs";
import OpenAI from "openai";

const openai = new OpenAI();

const transcription = await openai.audio.transcriptions.create({
  file: fs.createReadStream("speech.mp3"),
  model: "whisper-1",
  response_format: "text",
});

const translation = await openai.chat.completions.create({
  model: "gpt-4",
  messages: [{ role: "user", content: `Translate this to Japanese: ${transcription}` }],
});

console.log(translation.choices[0].message.content);


// Speech2text % node English2Japanese.mjs
// 今日は人々が愛する何かを作るのに最適な日です。