import fs from "fs";
import OpenAI from "openai";

const openai = new OpenAI();

const transcription = await openai.audio.transcriptions.create({
  file: fs.createReadStream("speech.mp3"),
  model: "whisper-1",
  response_format: "verbose_json",
  timestamp_granularities: ["word"]
});

console.log(transcription.words);



// [
//   { word: 'Today', start: 0, end: 0.46000000834465027 },
//   { word: 'is', start: 0.46000000834465027, end: 0.8199999928474426 },
//   { word: 'a', start: 0.8199999928474426, end: 1.0199999809265137 },
//   {
//     word: 'wonderful',
//     start: 1.0199999809265137,
//     end: 1.3600000143051147
//   },
//   { word: 'day', start: 1.3600000143051147, end: 1.7000000476837158 },
//   { word: 'to', start: 1.7000000476837158, end: 1.9800000190734863 },
//   { word: 'build', start: 1.9800000190734863, end: 2.0999999046325684 },
//   {
//     word: 'something',
//     start: 2.0999999046325684,
//     end: 2.4800000190734863
//   },
//   { word: 'people', start: 2.4800000190734863, end: 2.859999895095825 },
//   { word: 'love', start: 2.859999895095825, end: 3.200000047683716 }
// ]