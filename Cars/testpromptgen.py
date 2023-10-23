import openai
import random 
import os
import requests
import json

def generate_segment(car_name, segment_prompt):
    api_key = "OPENAI-API"  # Replace with your API key

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }

    data = {
        'prompt': segment_prompt,
        'max_tokens': 60
    }
    
    response = requests.post('https://api.openai.com/v1/engines/davinci/completions', headers=headers, json=data)
    result = response.json()
    generated_text = result['choices'][0]['text'].strip()
    return generated_text

def generate_car_prompt(car_name):
    segments = {
        "0": "{car_name} in a parking lot, gleaming in daylight, 'Ordinary Day' text overlay",
        "50": "Interior of {car_name}, music blaring, GPS set, 'Ready to Roll' text",
        "100": "Passenger in {car_name} messing with a GoPro, 'Capturing Moments' text",
        "150": "GoPro leaning out the window of {car_name}, capturing the car's speed, 'Living on the Edge' text",
        "200": "Rearview mirror view in {car_name} of multiple sports cars following, 'Drawing Attention' text",
        "250": "Close-up of {car_name} driver's worried face, 'Something's Off' text",
        "300": "Driver in {car_name} pulling over, sports cars surrounding, 'Showdown' text",
        "350": "Driver in {car_name} struggling with seatbelt, tension rising, 'Critical Moments' text",
        "400": "Bystander noticing {car_name}, 'Unexpected Savior' text",
        "450": "Bystander in {car_name} talking to sports car drivers, 'Clearing the Air' text",
        "500": "Drivers in {car_name} looking at GoPro footage, 'The Revelation' text",
        "550": "Sports car drivers around {car_name} laughing, giving thumbs up, 'Misunderstanding Cleared' text",
        "600": "{car_name} driver sitting back in car, sigh of relief, 'Close Call' text",
        "650": "Driver in {car_name} checking glove box, realizing sunglasses are missing, 'The Real Loss' text",
        "700": "{car_name} parked in a garage, driver contemplating, 'Reflecting' text",
        "750": "GoPro in {car_name} placed on a shelf, 'Lesson Learned' text",
        "800": "Driver polishing {car_name}, 'New Beginnings' text",
        "850": "{car_name} text about responsible driving and filming, 'Drive Safe, Capture Wisely' text",
        "900": "Montage of {car_name}'s journey, 'An Ordinary Drive Made Extraordinary' text overlay, epic music crescendo"
    }

    structured_output = {}
    for time, segment_prompt in segments.items():
        print(f"Generating segment for {time}...")
        generated_text = generate_segment(car_name, segment_prompt)
        structured_output[time] = segment_prompt + generated_text

    return json.dumps(structured_output, indent=4)

cars = ["Porsche gt3", "Ferrari 488", "Lamborghini Huracan"]

if __name__ == "__main__":
    
    # picking random car
    random_car = random.choice(cars)

    # Making Diffusion Prompt for car
    print(f"Generating prompt for {random_car}...")
    generated_prompt = generate_car_prompt(random_car)
    print(generated_prompt)
    
    with open("json_file.json", "w") as f:
        json.dump(generated_prompt, f)