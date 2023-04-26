# install requirements
# pip install -r requirements.txt

from playsound import playsound
from dotenv import load_dotenv
import elevenlabs 
import os
import openai

# Read API key from .env file
load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]
elevenlabs.set_api_key(os.environ["ELEVENLABS_API_KEY"])

# Ask the user for a topic
topic = input("What is your topic? ")

# Set up the prompt limit to 50 words to save cost
prompt = "Limit the result in maximum 50 words, generate a self hypnotherapy script I can listen to help me with " + topic + ".\n\n"

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
print("Generating audio...")

# Language code
language = 'en'

# Generate the audio
audio = elevenlabs.generate(text)

# Save the audio file
elevenlabs.save(audio, 'out/' + topic + '.mp3')

# Play the audio file
playsound('out/' + topic + '.mp3')
