# ask the user for a topic
from playsound import playsound
from gtts import gTTS
import os
import openai

# Set up the OpenAI API key
os.environ['OPENAI_API_KEY'] = "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"
openai.api_key = os.environ["OPENAI_API_KEY"]

# Ask the user for a topic
topic = input("What is your topic? ")

# Set up the prompt
prompt = "Generate a hypnotherapy script to help with " + topic + ".\n\n"

# Set up the completions parameters
model_engine = "text-davinci-002"
temperature = 0.7

# The maximum number of tokens to generate
max_tokens = 2048

# Generate the completion
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens,
)

# Text to be converted to audio
# Concatenate all the responses
text = "".join([choice.text for choice in response.choices])

# Print the generated script
print(text)

# Language code
language = 'en'

# Create a gTTS object and set language
tts = gTTS(text=text, lang=language, slow=True)

# Save the audio file
tts.save(topic + '.mp3')

# Save the audio file
#tts.save(topic + '.wav')

# Play the audio file
playsound(topic + '.mp3')