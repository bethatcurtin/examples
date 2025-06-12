
# These libraries are for image.xyz() which will work in VS Code once you have installed the pillow library (pip install pillow).
# from PIL import Image
# from io import BytesIO


##############################

import requests
import json
import time



#### Set up the API variables that won't be changed by the user ####

# Set your models
MODEL_NAME = "fal-ai/hidream-i1-fast"
MODELS_OPTIONS = ["fal-ai/aura-flow", "fal-ai/sana", "fal-ai/flux/dev", "fal-ai/flux/schnell", "fal-ai/hidream-i1-dev", "fal-ai/hidream-i1-fast", "fal-ai/hidream-i1-full", "fal-ai/stable-diffusion-v35-large", "fal-ai/stable-diffusion-v35-large/turbo", "fal-ai/stable-diffusion-v35-medium"]


#### Set up the API and constants ####
# Enter your API Key
API_KEY = "hf_apiKeyHere"




# Define the API endpoint
# We are only using fal-provided models from huggingface.
API_URL = f"https://router.huggingface.co/fal-ai/{MODEL_NAME}"
# Define the headers
API_HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + API_KEY
}




# Start & loop the chat!
while(1):
    # print(f"message_history: {message_history}")
    # print(f"api_input: {api_send}")
    
    # Ask the User for input and format it in the way we need for the api
    message_text = input("Generate an image of: ")
    api_send = {
        "prompt": message_text
    }
    
    # Call the API. Remember to convert to json!
    api_response = requests.post(API_URL, data=json.dumps(api_send), headers=API_HEADERS)
    
    # Check you've got the response you expected
    # print(f"response: {api_response}")

  
    # Get the data we need from the API response
    message_data=api_response.json()
    
    # Check the response got parsed properly
    # print(f"api_response: {api_response}\nmessage_data(json): {message_data}")
    
    image_url = message_data['images'][0]['url']
    print(f"image url: {image_url}")
    response = requests.get(image_url)

    # Save the image to a file
    with open("output.jpg", "wb") as f:
        f.write(response.content)

    # Show the image (uses the pillow & io libraries - this works in IDEs like VS Code, and opens a new window with the image.)
    # image = Image.open(BytesIO(response.content))
    # image.show()

    # Give the image a chance to load in the trinket output before asking for input again.
    # If you're using the Trinket online IDE, uncomment this line:
    # time.sleep(1)





# There is no error handling for the API in this script.
# api_response.status_code will have the response code for error catching. 
# If successful, api_response.status_code = 200.
# Add/un-comment some print() statements to see how the messages are formatted. 

  
   


