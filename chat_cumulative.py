# This is a python3 online IDE. Enter your code here and click 'Run' when you are ready. 
# You can use the 'requests' library in trinket, which allows you to call Model APIs with your code. 



import requests
import json

#### Set up the API variables that won't be changed by the user ####
SYSTEM_INSTRUCTIONS = "You are a friendly assistant."
MODEL_NAME = "gpt-4o-mini"


#### Set up the API and constants ####
#Enter your API Key
API_KEY = "your_api_key_here"

# Define the API endpoint
API_URL = "https://api.openai.com/v1/responses"
# Define the headers
API_HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + API_KEY
}


# Set up the System Prompt and get ready to append the first user_message
SYSTEM_MESSAGE = {
    "role": "system",
    "content": [
        {
            "type": "input_text",
            "text": SYSTEM_INSTRUCTIONS
        }
    ]
}

message_history = [SYSTEM_MESSAGE]

# Below is the API input with the system prompt, ready to be sent with subsequent messages.
# This is outside of the loop because we only want the system prompt set once. 
API_INPUT = {
    "model": MODEL_NAME,
    "input": [message_history],
    "temperature": 0.7
}


# This is the var we will use in the loop:
api_send = API_INPUT
 


# This function formats each message to the json format so that we can append messages to message_history.
def message_format(role, type, text):
    NEW_MESSAGE = {
    "role": "",
    "content": [
            {
                "type": "",
                "text": ""
            }
        ]
    }
    message=NEW_MESSAGE
    message["role"] = role
    message["content"][0]["type"] = type
    message["content"][0]["text"] = text
    
    return message




# Start & loop the chat!
while(1):
    # Ask the User for input and format it in the way we need
    
    message_text = input("Enter your message: ")
    user_message = message_format("user","input_text",message_text)
  
    # Append the message to message_history so that our bot can remember previous messages. 
    message_history.append(user_message) 
 
    # Update the API message with the new message_history
    api_send["input"] = message_history
    # Call the API. Remember to convert to json!
    api_response = requests.post(API_URL, data=json.dumps(api_send), headers=API_HEADERS)

  
    # Get the data we need from the API response
    message_data=api_response.json()
    #print(f"api_response: {api_response}\nmessage_data(json): {message_data}")
    message_text = message_data['output'][0]['content'][0]['text']    
    print(f"assistant: {message_text}")

    # Format the message so we can append it to message_history
    ai_message=message_format("assistant","output_text",message_text)
    # Append the message to message_history
    message_history.append(ai_message) 

# There is no error handling for the API in this script.
# api_response.status_code will have the response code for error catching. 
# If successful, api_response.status_code = 200.
# Add some print() statements to see how the messages are formatted. 

  
   


