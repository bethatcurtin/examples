
import requests
import json

#### Set up the API variables that won't be changed by the user ####


# Set your models
MODEL_NAME = "gpt-4o-mini"
MODELS_OPTIONS = ["google/gemini-2.0-flash-001","meta-llama/llama-3-8b-instruct","anthropic/claude-3-haiku"]


#### Set up the API and constants ####
# Enter your API Key
API_KEY = "sk-or-v1-apiKeyHere"


# Define the API endpoint
API_URL = "https://openrouter.ai/api/v1/completions"
# Define the headers
API_HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + API_KEY
}

# This is the base structure of the data we will send to the API.
api_send = {
    "model": MODEL_NAME,
    "prompt": "",
    "temperature": 0.7
}

# We will set the first part of the prompt and allow the user to choose what topic to use.
start_message = "Tell me a funny and unique joke about:  "

# Start & loop the bot!
while(1):

    # Ask the User for input and format it in the way we need
    
    user_message = input("Generate a joke about: ")

    # Append the message to our base message to make a single prompt
    message_send = start_message + user_message
 
    # Update the API message with the full prompt
    api_send["prompt"] = message_send
    
    # Call the API. 
    api_response = requests.post(API_URL, json=api_send, headers=API_HEADERS)
    
    # Check you've got the response you expected
    # print(f"response: {api_response}")
  
    # Get the data we need from the API response
    message_data=api_response.json()
    
    # Check the response got parsed properly
    # print(f"api_response: {api_response}\nmessage_data(json): {message_data}")
    
    # Get the text content of the message to show the user
    # message_text = message_data['output'][0] 
    message_text = message_data['choices'][0]['text']
    print(f"joke-bot: {message_text}")


# There is no error handling for the API in this script.
# api_response.status_code will have the response code for error catching. 
# If successful, api_response.status_code = 200.
# Add/un-comment some print() statements to see how the messages are formatted. 

  
   
