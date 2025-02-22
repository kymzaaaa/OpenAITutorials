from typing import List
from pydantic import BaseModel
from openai import OpenAI

class EntitiesModel(BaseModel):
    attributes: List[str]
    colors: List[str]
    animals: List[str]

client = OpenAI()

with client.beta.chat.completions.stream(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Extract entities from the input text"},
        {
            "role": "user",
            "content": "The quick brown fox jumps over the lazy dog with piercing blue eyes",
        },
    ],
    response_format=EntitiesModel,
) as stream:
    for event in stream:
        if event.type == "content.delta":
            if event.parsed is not None:
                # Print the parsed data as JSON
                print("content.delta parsed:", event.parsed)
        elif event.type == "content.done":
            print("content.done")
        elif event.type == "error":
            print("Error in stream:", event.error)

final_completion = stream.get_final_completion()
print("Final completion:", final_completion)



# (base) steve@StevenoMacBook-Pro StructuredOutputs % python Streaming.py
# content.delta parsed: {}
# content.delta parsed: {}
# content.delta parsed: {'attributes': []}
# content.delta parsed: {'attributes': []}
# content.delta parsed: {'attributes': ['quick']}
# content.delta parsed: {'attributes': ['quick']}
# content.delta parsed: {'attributes': ['quick', 'brown']}
# content.delta parsed: {'attributes': ['quick', 'brown']}
# content.delta parsed: {'attributes': ['quick', 'brown', 'lazy']}
# content.delta parsed: {'attributes': ['quick', 'brown', 'lazy']}
# content.delta parsed: {'attributes': ['quick', 'brown', 'lazy']}
# content.delta parsed: {'attributes': ['quick', 'brown', 'lazy', 'piercing']}
# content.delta parsed: {'attributes': ['quick', 'brown', 'lazy', 'piercing']}
# content.delta parsed: {'attributes': ['quick', 'brown', 'lazy', 'piercing', 'blue']}
# content.delta parsed: {'attributes': ['quick', 'brown', 'lazy', 'piercing', 'blue']}
# content.delta parsed: {'attributes': ['quick', 'brown', 'lazy', 'piercing', 'blue']}
# content.delta parsed: {'attributes': ['quick', 'brown', 'lazy', 'piercing', 'blue'], 'colors': []}
# content.delta parsed: {'attributes': ['quick', 'brown', 'lazy', 'piercing', 'blue'], 'colors': []}
# content.delta parsed: {'attributes': ['quick', 'brown', 'lazy', 'piercing', 'blue'], 'colors': ['brown']}
# content.delta parsed: {'attributes': ['quick', 'brown', 'lazy', 'piercing', 'blue'], 'colors': ['brown']}
# content.delta parsed: {'attributes': ['quick', 'brown', 'lazy', 'piercing', 'blue'], 'colors': ['brown', 'blue']}
# content.delta parsed: {'attributes': ['quick', 'brown', 'lazy', 'piercing', 'blue'], 'colors': ['brown', 'blue']}
# content.delta parsed: {'attributes': ['quick', 'brown', 'lazy', 'piercing', 'blue'], 'colors': ['brown', 'blue']}
# content.delta parsed: {'attributes': ['quick', 'brown', 'lazy', 'piercing', 'blue'], 'colors': ['brown', 'blue'], 'animals': []}
# content.delta parsed: {'attributes': ['quick', 'brown', 'lazy', 'piercing', 'blue'], 'colors': ['brown', 'blue'], 'animals': []}
# content.delta parsed: {'attributes': ['quick', 'brown', 'lazy', 'piercing', 'blue'], 'colors': ['brown', 'blue'], 'animals': ['fox']}
# content.delta parsed: {'attributes': ['quick', 'brown', 'lazy', 'piercing', 'blue'], 'colors': ['brown', 'blue'], 'animals': ['fox']}
# content.delta parsed: {'attributes': ['quick', 'brown', 'lazy', 'piercing', 'blue'], 'colors': ['brown', 'blue'], 'animals': ['fox', 'dog']}
# content.delta parsed: {'attributes': ['quick', 'brown', 'lazy', 'piercing', 'blue'], 'colors': ['brown', 'blue'], 'animals': ['fox', 'dog']}
# content.done
# Final completion: ParsedChatCompletion[EntitiesModel](id='chatcmpl-B3jXkEOhPGuDmR7ARjzg8YhdagoxD', choices=[ParsedChoice[EntitiesModel](finish_reason='stop', index=0, logprobs=None, message=ParsedChatCompletionMessage[EntitiesModel](content='{"attributes":["quick","brown","lazy","piercing","blue"],"colors":["brown","blue"],"animals":["fox","dog"]}', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None, parsed=EntitiesModel(attributes=['quick', 'brown', 'lazy', 'piercing', 'blue'], colors=['brown', 'blue'], animals=['fox', 'dog'])))], created=1740229752, model='gpt-4o-2024-08-06', object='chat.completion', service_tier='default', system_fingerprint='fp_eb9dce56a8', usage=None)