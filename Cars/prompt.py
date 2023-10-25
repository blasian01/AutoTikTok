import openai
import random 
import os
import requests
import json
# This program is used to test the functionality of getting a new prompt from Chatgpt

def generate_prompt(sentence):
    # api_key = os.environ.get("OPENAI_API_KEY")
    openai.api_key = "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"
    print("sentence was this: " + sentence)
    
    model = "text-davinci-003"
    
    response = openai.Completion.create(
    engine=model,
    prompt="Please rewrite the following sentence to only focus on a car in a specific location and/or time period, and include details about the weather and time of day: " + sentence,
    max_tokens=60,
    n = 1,
    )
    
    replyGPT = response.choices[0].text
    print("getting GPT reply: " + replyGPT)
    return replyGPT

def prepare_sentence(sentence):
    # Replace double quotes with single quotes
    sentence = sentence.replace('"', "'")
    
    # Remove newline characters
    sentence = sentence.replace('\n', ' ')
    
    # Remove question marks
    sentence = sentence.replace('?', '')
    
    return sentence

# List of different cars
cars = [
    "Porsche gt3",
    "Ferrari 488",
    "Lamborghini Huracan",
    "Tesla Model S",
    "McLaren P1",
    "Bugatti Chiron",
    "Aston Martin Vantage",
    "Chevrolet Corvette Z06",
    "Dodge Viper",
    "Nissan GT-R",
    "BMW M4",
    "Ford Mustang Shelby GT500",
    "Audi R8",
    "Jaguar F-Type",
    "Mercedes-AMG GT",
    "Alfa Romeo 4C",
    "Koenigsegg Jesko",
    "Pagani Huayra",
    "Lotus Evora",
    "Porsche 918 Spyder",
    "Lamborghini Aventador",
    "Ferrari LaFerrari",
    "McLaren 720S",
    "Bugatti Veyron",
    "Aston Martin DBS",
    "Chevrolet Camaro ZL1",
    "Maserati GranTurismo",
    "BMW M8",
    "Dodge Challenger Hellcat",
    "Ford GT",
    "Audi RS 6 Avant",
    "Cadillac CTS-V",
    "Lexus LC 500",
    "Mercedes-Benz SLR McLaren",
    "Alpine A110",
    "Koenigsegg Regera",
    "Pagani Zonda",
    "Lotus Exige",
    "Porsche Carrera GT",
    "Lamborghini Gallardo",
    "Ferrari F40",
    "McLaren F1",
    "TVR Sagaris",
    "Aston Martin One-77",
    "Chevrolet Corvette Stingray",
    "Maserati MC12",
    "BMW M5",
    "Dodge Charger SRT Hellcat",
    "Audi RS 7",
    "Jaguar XKR",
    "Mercedes-Benz SLS AMG",
    "Noble M600",
    "Koenigsegg Agera",
    "Pagani Huayra Roadster",
    "Lotus Elise",
    "Porsche Taycan",
    "Lamborghini Murcielago",
    "Ferrari F50",
    "McLaren 600LT",
    "Rimac C_Two",
    "Aston Martin DB11",
    "Chevrolet Corvette C8",
    "Maserati Alfieri",
    "BMW i8",
    "Dodge Challenger SRT Demon",
    "Audi TT RS",
    "Jaguar XJ220",
    "Mercedes-Benz CLK GTR",
    "W Motors Lykan Hypersport",
    "Koenigsegg Gemera",
    "Pagani Huayra BC",
    "Lotus Esprit",
    "Porsche Boxster",
    "Lamborghini Diablo",
    "Ferrari Enzo",
    "McLaren 570S",
    "Rimac Nevera",
    "Aston Martin Valkyrie",
    "Chevrolet Camaro SS",
    "Maserati Quattroporte",
    "BMW Z4",
    "Dodge Viper ACR",
    "Audi S5",
    "Jaguar XK",
    "Mercedes-AMG Project One",
    "W Motors Fenyr SuperSport",
    "Koenigsegg One:1",
    "SSC Tuatara",
    "Lotus 3-Eleven",
    "Porsche Panamera",
    "Lamborghini Veneno",
    "Ferrari 812 Superfast",
    "McLaren GT",
    "Rimac Concept One",
    "Aston Martin Rapide",
    "Chevrolet Camaro IROC-Z",
    "Maserati Levante Trofeo",
    "BMW M2",
    "Dodge Dart Swinger",
    "Audi RS Q8",
]

if __name__ == "__main__":
    # picking random car
    car_name = random.choice(cars)

    # Making Diffusion Prompt for car
    print(f"Generating prompt for {car_name}...")
    
    # manually splitting sentences in the json prompt
    # This allows ChatGPT to rewrite sentences without messing up the layout of the json format
    sentence1 = f"{car_name} parked in a lot, gleaming in the midday sun, 'Ordinary Day' text overlay"
    sentence2 = f"{car_name} idling at a stoplight, under a cloudy sky, 'Ready to Roll' text"
    sentence3 = f"{car_name} cruising on a highway during sunset, 'Capturing Moments' text"
    sentence4 = f"{car_name} zipping through a tunnel at night, 'Living on the Edge' text"
    sentence5 = f"{car_name} on an open road, sports cars in the distance, overcast weather, 'Drawing Attention' text"
    sentence6 = f"{car_name} stopped on a rainy roadside, 'Something's Off' text"
    sentence7 = f"{car_name} parked at a scenic overlook, surrounded by sports cars, dusk setting in, 'Showdown' text"
    sentence8 = f"{car_name} parked under a streetlight, dawn breaking, 'Critical Moments' text"
    sentence9 = f"{car_name} noticed from a pedestrian bridge, early morning fog, 'Unexpected Savior' text"
    sentence10 = f"{car_name} parked near a beach, conversation nearby, sunny afternoon, 'Clearing the Air' text"
    sentence11 = f"{car_name} parked at an overlook, reviewing journey highlights, twilight, 'The Revelation' text"
    sentence12 = f"{car_name} in a parking lot, sports cars nearby, clear evening, 'Misunderstanding Cleared' text"
    sentence13 = f"{car_name} parked in a driveway, moonlit night, 'Close Call' text"
    sentence14 = f"{car_name} in the garage, missing items noted, rainy evening, 'The Real Loss' text"
    sentence15 = f"{car_name} parked under a tree, reflecting on the day, sunset, 'Reflecting' text"
    sentence16 = f"{car_name} in an empty parking lot, overcast morning, 'Lesson Learned' text"
    sentence17 = f"{car_name} getting a wash, sunny afternoon, 'New Beginnings' text"
    sentence18 = f"{car_name} parked with a view of the city skyline, twilight, 'Drive Safe, Capture Wisely' text"
    sentence19 = f"{car_name} driving through various landscapes, different weather conditions, epic music crescendo, 'An Ordinary Drive Made Extraordinary' text overlay"



#Changing the sentences using chat
#---------------------------------------------------------------------------------------------------------------
    
    change_sentence1 = generate_prompt(sentence1)
    prepared_sentence1 = prepare_sentence(change_sentence1)

    change_sentence2 = generate_prompt(sentence2)
    prepared_sentence2 = prepare_sentence(change_sentence2)

    change_sentence3 = generate_prompt(sentence3)
    prepared_sentence3 = prepare_sentence(change_sentence3)

    change_sentence4 = generate_prompt(sentence4)
    prepared_sentence4 = prepare_sentence(change_sentence4)
    
    change_sentence5 = generate_prompt(sentence5)
    prepared_sentence5 = prepare_sentence(change_sentence5)
    
#---------------------------------------------------------------------------------------------------------------

    change_sentence6 = generate_prompt(sentence6)
    prepared_sentence6 = prepare_sentence(change_sentence6)
    
    change_sentence7 = generate_prompt(sentence7)
    prepared_sentence7 = prepare_sentence(change_sentence7)
    
    change_sentence8 = generate_prompt(sentence8)
    prepared_sentence8 = prepare_sentence(change_sentence8)
    
    change_sentence9 = generate_prompt(sentence9)
    prepared_sentence9 = prepare_sentence(change_sentence9)
    
    change_sentence10 = generate_prompt(sentence10)
    prepared_sentence10 = prepare_sentence(change_sentence10)
    
#---------------------------------------------------------------------------------------------------------------
    
    change_sentence11 = generate_prompt(sentence11)
    prepared_sentence11 = prepare_sentence(change_sentence11)
    
    change_sentence12 = generate_prompt(sentence12)
    prepared_sentence12 = prepare_sentence(change_sentence12)

    change_sentence13 = generate_prompt(sentence13)
    prepared_sentence13 = prepare_sentence(change_sentence13)
 
    change_sentence14 = generate_prompt(sentence14)
    prepared_sentence14 = prepare_sentence(change_sentence14)
    
    change_sentence15 = generate_prompt(sentence15)
    prepared_sentence15 = prepare_sentence(change_sentence15)
    
#---------------------------------------------------------------------------------------------------------------

    change_sentence16 = generate_prompt(sentence16)
    prepared_sentence16 = prepare_sentence(change_sentence16)

    change_sentence17 = generate_prompt(sentence17)
    prepared_sentence17 = prepare_sentence(change_sentence17)
    
    change_sentence18 = generate_prompt(sentence18)
    prepared_sentence18 = prepare_sentence(change_sentence18)
    
    change_sentence19 = generate_prompt(sentence19)
    prepared_sentence19 = prepare_sentence(change_sentence19)
    
 #---------------------------------------------------------------------------------------------------------------   
    
    segments_str = f'''{{
        "0": "{prepared_sentence1}",
        "50": "{prepared_sentence2}",
        "100": "{prepared_sentence3}",
        "150": "{prepared_sentence4}",
        "200": "{prepared_sentence5}", 
        "250": "{prepared_sentence6}", 
        "300": "{prepared_sentence7}", 
        "350": "{prepared_sentence8}",
        "400": "{prepared_sentence9}",
        "450": "{prepared_sentence10}",
        "500": "{prepared_sentence11}",
        "550": "{prepared_sentence12}",
        "600": "{prepared_sentence13}",
        "650": "{prepared_sentence14}",
        "700": "{prepared_sentence15}",
        "750": "{prepared_sentence16}",
        "800": "{prepared_sentence17}",
        "850": "{prepared_sentence18}",
        "900": "{prepared_sentence19}"
}}'''


#     segments_str = f'''{{
#         "0": "{sentence1}",
#         "50": "{sentence2}",
#         "100": "{sentence3}",
#         "150": "{sentence4}",
#         "200": "{sentence5}", 
#         "250": "{sentence6}", 
#         "300": "{sentence7}", 
#         "350": "{sentence8}",
#         "400": "{sentence9}",
#         "450": "{sentence10}",
#         "500": "{sentence11}",
#         "550": "{sentence12}",
#         "600": "{sentence13}",
#         "650": "{sentence14}",
#         "700": "{sentence15}",
#         "750": "{sentence16}",
#         "800": "{sentence17}",
#         "850": "{sentence18}",
#         "900": "{sentence19}"
# }}'''

    print(segments_str)
    
    # Writing to a text file
    with open("Cars/output_folder/prompt.txt", "w") as f:
        f.write(segments_str)
