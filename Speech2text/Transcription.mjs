import fs from "fs";
import OpenAI from "openai";

const openai = new OpenAI();

const transcription = await openai.audio.transcriptions.create({
  file: fs.createReadStream("speech.mp3"),
  model: "whisper-1",
});

console.log(transcription.text);


// node Transcription.mjs
// Today is a wonderful day to build something people love.