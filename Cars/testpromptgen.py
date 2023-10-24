import openai
import random 
import os
import requests
import json
# This program is used to test the functionality of getting a new prompt from Chatgpt

def generate_prompt(sentence):
    api_key = os.environ.get('OPENAI_API_KEY')
    
    headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json',
        }

    data = {
        'prompt': "Based on the following sentence, create a related new prompt: " + sentence,
        'model': "gpt-2.1-turbo",
        'max_tokens': 50,
        'temperature': 0.7
    }
    
    try:
        response = requests.post('https://api.openai.com/v1/engines/davinci/completions', headers=headers, json=data)
        response.raise_for_status() 
        
        result = response.json()
        return result['choices'][0]['text'].strip()
        
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    except KeyError:
        print(f"Unexpected response structure: {result}")

    return None

cars = ["Porsche gt3", "Ferrari 488", "Lamborghini Huracan"]

if __name__ == "__main__":
    # picking random car
    car_name = random.choice(cars)

    # Making Diffusion Prompt for car
    print(f"Generating prompt for {car_name}...")
    
    # manually splitting sentences in the json prompt
    # This allows ChatGPT to rewrite sentences without messing up the layout of the json format
    sentence1 = f"{car_name} in a parking lot, gleaming in daylight, 'Ordinary Day' text overlay" 
    sentence2 = f"Interior of {car_name}, music blaring, GPS set, 'Ready to Roll' text"
    sentence3 = f"Passenger in {car_name} messing with a GoPro, 'Capturing Moments' text"
    sentence4 = f"GoPro leaning out the window of {car_name}, capturing the car's speed, 'Living on the Edge' text"
    sentence5 = f"Rearview mirror view in {car_name} of multiple sports cars following, 'Drawing Attention' text"
    sentence6 = f"Close-up of {car_name} driver's worried face, 'Something's Off' text"
    sentence7 = f"Driver in {car_name} pulling over, sports cars surrounding, 'Showdown' text"
    sentence8 = f"Driver in {car_name} struggling with seatbelt, tension rising, 'Critical Moments' text"
    sentence9 = f"Bystander noticing {car_name}, 'Unexpected Savior' text"
    sentence10 =f"Bystander in {car_name} talking to sports car drivers, 'Clearing the Air' text"
    sentence11 = f"Drivers in {car_name} looking at GoPro footage, 'The Revelation' text"
    sentence12 = f"Sports car drivers around {car_name} laughing, giving thumbs up, 'Misunderstanding Cleared' text"
    sentence13 = f"{car_name} driver sitting back in car, sigh of relief, 'Close Call' text"
    sentence14 = f"Driver in {car_name} checking glove box, realizing sunglasses are missing, 'The Real Loss' text"
    sentence15 = f"{car_name} parked in a garage, driver contemplating, 'Reflecting' text"
    sentence16 = f"GoPro in {car_name} placed on a shelf, 'Lesson Learned' text"
    sentence17 = f"Driver polishing {car_name}, 'New Beginnings' text"
    sentence18 = f"{car_name} text about responsible driving and filming, 'Drive Safe, Capture Wisely' text"
    sentence19 = f"Montage of {car_name}'s journey, 'An Ordinary Drive Made Extraordinary' text overlay, epic music crescendo"


#Changing the sentences using chat
#---------------------------------------------------------------------------------------------------------------
    
    change_sentence1 = generate_prompt(sentence1)

    change_sentence2 = generate_prompt(sentence2)

    change_sentence3 = generate_prompt(sentence3)

    change_sentence4 = generate_prompt(sentence4)

    change_sentence5 = generate_prompt(sentence5)
    
#---------------------------------------------------------------------------------------------------------------

    change_sentence6 = generate_prompt(sentence6)
    
    change_sentence7 = generate_prompt(sentence7)
    
    change_sentence8 = generate_prompt(sentence8)
    
    change_sentence9 = generate_prompt(sentence9)
    
    change_sentence10 = generate_prompt(sentence10)
    
#---------------------------------------------------------------------------------------------------------------
    
    change_sentence11 = generate_prompt(sentence11)
    
    change_sentence12 = generate_prompt(sentence12)

    change_sentence13 = generate_prompt(sentence13)
 
    change_sentence14 = generate_prompt(sentence14)
    
    change_sentence15 = generate_prompt(sentence15)
    
#---------------------------------------------------------------------------------------------------------------

    change_sentence16 = generate_prompt(sentence16)

    change_sentence17 = generate_prompt(sentence17)
    
    change_sentence18 = generate_prompt(sentence18)
    
    change_sentence19 = generate_prompt(sentence19)
    
 #---------------------------------------------------------------------------------------------------------------   
    
    segments_str = f'''{{
        "0": "{change_sentence1}",
        "50": "{change_sentence2}",
        "100": "{change_sentence3}",
        "150": "{change_sentence4}",
        "200": "{change_sentence5}", 
        "250": "{change_sentence6}", 
        "300": "{change_sentence7}", 
        "350": "{change_sentence8}",
        "400": "{change_sentence9}",
        "450": "{change_sentence10}",
        "500": "{change_sentence11}",
        "550": "{change_sentence12}",
        "600": "{change_sentence13}",
        "650": "{change_sentence14}",
        "700": "{change_sentence15}",
        "750": "{change_sentence16}",
        "800": "{change_sentence17}",
        "850": "{change_sentence18}",
        "900": "{change_sentence19}"
}}'''
    
    print(segments_str)
    
    # Writing to a text file
    with open("Cars/output_folder/prompt.txt", "w") as f:
        f.write(segments_str)
