import base64
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-audio-preview",
    modalities=["text", "audio"],
    audio={"voice": "alloy", "format": "wav"},
    messages=[
        {
            "role": "user",
            "content": "Is a golden retriever a good family dog?"
        }
    ]
)

print(completion.choices[0])

wav_bytes = base64.b64decode(completion.choices[0].message.audio.data)
with open("dog.wav", "wb") as f:
    f.write(wav_bytes)



# JAAtAC4AKgAzACQAFgAdACgAHgAiACgAIQAfADQANgAuADEALgApACwAMQAuACoAJgAbABcAGgAbABcAHAAaAAoAFwAiAA0AEQAbABgAJgA8AD4ALgAmACAA/f/5/wwAAAD4/xgAFQAKAA4AIwD9/wAAFgAKAAQAGAAfAAcACwAjAAQAAgAqABoA+f8RABgA9v8BADIAIQADACoAJgD4/x0AOwAAAAQAIwAJAPL/FQAuAPn/BAAVAAgAAwAWACYA//8IABcA+f/9/xUAAwD6//7//v/1//3/+v/7/+z//f8OAPf/9P8RAPz/5P/4/wAA9P/2/wcADgAOABIAEgAhACgAGQAKAA4AGQAJAAsADAAIAP//CAAcABwAEwAUABIA/P/+/xcAIQANAAwADwASAAkA+f8GAAwAEgAYACIAJQAKAAIABQABAAIADAAgADUANAAeAAcA9v/y/+//8P/t//H/8f8AABAAIwA4AD0AHQATABgAFAD6//7/AQD2//3/CQATAB4ALgAsACkAIAACAP7/8f/w//z/EQALABUANgARAAAAJAAoAAkAHgAnAPn/+P8YAAsABgAvACYABQAXACoABAAKACgADAD6/xsAHwD+/w4ADwDn/+b/FQAbAAUABADe/5b/oP/D/+L/CgAuABEA0f+0/57/pv/V/wsAHQACABEADADh/9z/6P/B/6f/1//k/+X/CwAKAOL/8P8AAOP/zv/V/97/4v/t//H/3f/L/9P/wv+g/6D/t/+n/5n/vf/f/8L/3v8UAPX/+/8sAP3/w//O/6f/Y/+p/xcA2P/G/xEA/f/f/xAA/v+8/+n/EADM/8v/AQD8/+r/BgALANH/4f/n/8j/1P/K/9L/1v/7/wIA0P+o/8r/9P/0/+T/8f/n/8v/2f/R/9b/7v8fACIANAA9AOn/ov+n/7v/k/+k/7v/xf/i/wEA/f/F/73/xP8QACMAMQAiAAcA5f/2/w8ACQBEAFgAFwAOAFIANQAEAEAAHwDF/77/DAAQADsAcAA7APz/FgADAL//AQBXADcASgBTAOb/y//w/3b/G/+Q/+X/zf8HAGMAVQA/AAYA0P++/+f/t/+9/wkA2/+j/8D/8v8gADkAAQDu/zgABQDN/xEAOABSAJIApQBZACgA7v+b/67/1/8bAEkAXwA/ABAA2/+y/+T/4P/c//n/+v/T/9r/OwBNADcAKwA7ADoAUQBMABMALQBaADsACwAwAEgARgBtAFIATQBhABsAEQD+/wYADAAIAC0AIwBQADYAFgA0ACsAHAAlACoAEAARACYAFAAZACAA+f/f/wwAAwDd/wcAMgBPAFoAgwB9AEIAJQD8/8f/sv/U/9X/9f8dAAoAKAAUAPf/7/8HAOj/of+a/77//v/S/8T/1f8YAC8AKgAfAJb/UP9p/3P/d/+N/47/ef99/5n/kv+q/6b/yP/F/7L/5f/X/7H/4f8GAML/lP+2/9b/9v8rACgAEAAlAB0A5P/V/wAAAgDv/z4AaQBJAFcANgAjABsAMQAiAPL//v/4/8X/0f8DAPH/vf++/8P////Q/2v//v8uALP/7P9gAFgAKABCAAQA1P+d/xAA4f/j/ycAmgDJALoAjwDs/ygAewBKACAAXQDq/6j/oP+Q/wUANQAVAN3/eAArAe//MwArAKD/SACRABEAFQDgAD0BKADO/9n/OwAyACwAkABdACYAyP8=', expires_at=1740203600, transcript='Yes, a golden retriever is often considered a great family dog. They are known for being friendly, gentle, and good with children. These dogs are also intelligent and eager to please, making them relatively easy to train. They tend to get along well with other pets and enjoy being a part of family activities. Keep in mind, golden retrievers require regular exercise and grooming due to their energetic nature and thick coats.'), function_call=None, tool_calls=None))
# Generated Text is base64 encoded audio. Save it to a file and decode it to listen to the audio.

# node_modules/wsampletest/Vision/dog.wav