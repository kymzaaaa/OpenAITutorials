from openai import OpenAI
client = OpenAI()

response = client.moderations.create(
    model="omni-moderation-latest",
    input="...text to classify goes here...",
)

print(response)

# flagged=False  is safe text

# (base) steve@StevenoMacBook-Pro Moderation % python moderation.py 
# ModerationCreateResponse(id='modr-2b0b8d2c812a51a6e266547da7e8f422', model='omni-moderation-latest', 
# results=[Moderation(categories=Categories(harassment=False, harassment_threatening=False, hate=False, 
# hate_threatening=False, illicit=False, illicit_violent=False, self_harm=False, self_harm_instructions=False, 
# self_harm_intent=False, sexual=False, sexual_minors=False, violence=False, violence_graphic=False, harassment/threatening=False, 
# hate/threatening=False, illicit/violent=False, self-harm/intent=False, self-harm/instructions=False, self-harm=False, 
# sexual/minors=False, violence/graphic=False), category_applied_input_types=CategoryAppliedInputTypes(harassment=['text'], 
# harassment_threatening=['text'], hate=['text'], hate_threatening=['text'], illicit=['text'], illicit_violent=['text'], 
# self_harm=['text'], self_harm_instructions=['text'], self_harm_intent=['text'], sexual=['text'], sexual_minors=['text'], 
# violence=['text'], violence_graphic=['text'], harassment/threatening=['text'], hate/threatening=['text'], illicit/violent=['text'], 
# self-harm/intent=['text'], self-harm/instructions=['text'], self-harm=['text'], sexual/minors=['text'], violence/graphic=['text']),
# category_scores=CategoryScores(harassment=4.802972318863164e-05, harassment_threatening=6.605214485464791e-06, 
# hate=1.4202364022997911e-05, hate_threatening=8.664653147910923e-07, illicit=2.234163601827719e-05, 
# illicit_violent=1.9110431587777674e-05, self_harm=2.0462932829931794e-06, self_harm_instructions=1.0129990980873922e-06, 
# self_harm_intent=1.1125607488784412e-06, sexual=3.9821309061635425e-05, sexual_minors=1.0391067562761452e-05, 
# violence=1.6346470245419304e-05, violence_graphic=5.649793328376294e-06, harassment/threatening=6.605214485464791e-06, 
# hate/threatening=8.664653147910923e-07, illicit/violent=1.9110431587777674e-05, self-harm/intent=1.1125607488784412e-06, 
# self-harm/instructions=1.0129990980873922e-06, self-harm=2.0462932829931794e-06, sexual/minors=1.0391067562761452e-05, 
# violence/graphic=5.649793328376294e-06), flagged=False)])



# input="...text to classify goes here...japanese is yellow monky"
# flagged=True

# (base) steve@StevenoMacBook-Pro Moderation % python moderation.py
# ModerationCreateResponse(id='modr-443614b2a03b94711ee97d36ff882cac', model='omni-moderation-latest', 
# results=[Moderation(categories=Categories(harassment=True, harassment_threatening=False, hate=True, hate_threatening=False, 
# illicit=False, illicit_violent=False, self_harm=False, self_harm_instructions=False, self_harm_intent=False, 
# sexual=False, sexual_minors=False, violence=False, violence_graphic=False, harassment/threatening=False, 
# hate/threatening=False, illicit/violent=False, self-harm/intent=False, self-harm/instructions=False, self-harm=False, 
# sexual/minors=False, violence/graphic=False), category_applied_input_types=CategoryAppliedInputTypes(harassment=['text'], 
# harassment_threatening=['text'], hate=['text'], hate_threatening=['text'], illicit=['text'], illicit_violent=['text'], 
# self_harm=['text'], self_harm_instructions=['text'], self_harm_intent=['text'], sexual=['text'], sexual_minors=['text'], 
# violence=['text'], violence_graphic=['text'], harassment/threatening=['text'], hate/threatening=['text'], illicit/violent=['text'], 
# self-harm/intent=['text'], self-harm/instructions=['text'], self-harm=['text'], sexual/minors=['text'], violence/graphic=['text']), 
# category_scores=CategoryScores(harassment=0.7212198323065316, harassment_threatening=0.0010136830379240411, hate=0.694161608586147, 
# hate_threatening=0.0034061731233581585, illicit=2.846224015752145e-05, illicit_violent=1.0229985472581487e-05, 
# self_harm=9.461262661302227e-06, self_harm_instructions=5.064471653194114e-06, self_harm_intent=0.00021196745065203636, 
# sexual=8.167381046669487e-05, sexual_minors=1.2339457598623173e-05, violence=0.0005166197289884592, 
# violence_graphic=1.1061159714638084e-05, harassment/threatening=0.0010136830379240411, hate/threatening=0.0034061731233581585, 
# illicit/violent=1.0229985472581487e-05, self-harm/intent=0.00021196745065203636, self-harm/instructions=5.064471653194114e-06, 
# self-harm=9.461262661302227e-06, sexual/minors=1.2339457598623173e-05, violence/graphic=1.1061159714638084e-05), flagged=True)])