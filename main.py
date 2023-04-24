# ask the user for a topic
from playsound import playsound
from gtts import gTTS
from dotenv import load_dotenv
import os
import openai

# Read API key from .env file
load_dotenv()
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
tts.save('out/' + topic + '.mp3')

# Play the audio file
playsound('out/' + topic + '.mp3')