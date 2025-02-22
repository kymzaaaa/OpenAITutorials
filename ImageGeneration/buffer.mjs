import OpenAI from "openai";
import fs from "fs"; // fs モジュールをインポート

const openai = new OpenAI();

// This is the Buffer object that contains your image data
const buffer = fs.readFileSync("mask.png"); // ローカルの PNG 画像を Buffer に変換
buffer.name = "mask.png";

// Set a `name` that ends with .png so that the API knows it's a PNG image
buffer.name = "mask.png";

async function main() {
  const image = await openai.images.createVariation({ model: "dall-e-2", image: buffer, n: 1, size: "1024x1024" });
  console.log(image.data);
}
main();