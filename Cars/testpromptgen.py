import openai
import random 
import os
import requests
import json
# This program is used to test the functionality of getting a new prompt from Chatgpt

def generate_prompt(sentence):
    openai.api_key = "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"
    print("sentence was this: " + sentence)
    
    model = "text-davinci-003"
    
    response = openai.Completion.create(
    engine=model,
    prompt="Please rewrite the following sentence while keeping a similar length and without using quotations: " + sentence,
    max_tokens=1000,
    n = 1,
    )
    
    replyGPT = response.choices[0].text
    print("getting GPT reply: " + replyGPT)
    return replyGPT

def prepare_sentence(sentence):
    # Replace double quotes with single quotes
    sentence = sentence.replace('"', "'")
    
    return sentence

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
    
#     change_sentence1 = generate_prompt(sentence1)
#     prepared_sentence1 = prepare_sentence(change_sentence1)

#     change_sentence2 = generate_prompt(sentence2)
#     prepared_sentence2 = prepare_sentence(change_sentence2)

#     change_sentence3 = generate_prompt(sentence3)
#     prepared_sentence3 = prepare_sentence(change_sentence3)

#     change_sentence4 = generate_prompt(sentence4)
#     prepared_sentence4 = prepare_sentence(change_sentence4)
    
#     change_sentence5 = generate_prompt(sentence5)
#     prepared_sentence5 = prepare_sentence(change_sentence5)
    
# #---------------------------------------------------------------------------------------------------------------

#     change_sentence6 = generate_prompt(sentence6)
#     prepared_sentence6 = prepare_sentence(change_sentence6)
    
#     change_sentence7 = generate_prompt(sentence7)
#     prepared_sentence7 = prepare_sentence(change_sentence7)
    
#     change_sentence8 = generate_prompt(sentence8)
#     prepared_sentence8 = prepare_sentence(change_sentence8)
    
#     change_sentence9 = generate_prompt(sentence9)
#     prepared_sentence9 = prepare_sentence(change_sentence9)
    
#     change_sentence10 = generate_prompt(sentence10)
#     prepared_sentence10 = prepare_sentence(change_sentence10)
    
# #---------------------------------------------------------------------------------------------------------------
    
#     change_sentence11 = generate_prompt(sentence11)
#     prepared_sentence11 = prepare_sentence(change_sentence11)
    
#     change_sentence12 = generate_prompt(sentence12)
#     prepared_sentence12 = prepare_sentence(change_sentence12)

#     change_sentence13 = generate_prompt(sentence13)
#     prepared_sentence13 = prepare_sentence(change_sentence13)
 
#     change_sentence14 = generate_prompt(sentence14)
#     prepared_sentence14 = prepare_sentence(change_sentence14)
    
#     change_sentence15 = generate_prompt(sentence15)
#     prepared_sentence15 = prepare_sentence(change_sentence15)
    
# #---------------------------------------------------------------------------------------------------------------

#     change_sentence16 = generate_prompt(sentence16)
#     prepared_sentence16 = prepare_sentence(change_sentence16)

#     change_sentence17 = generate_prompt(sentence17)
#     prepared_sentence17 = prepare_sentence(change_sentence17)
    
#     change_sentence18 = generate_prompt(sentence18)
#     prepared_sentence18 = prepare_sentence(change_sentence18)
    
#     change_sentence19 = generate_prompt(sentence19)
#     prepared_sentence19 = prepare_sentence(change_sentence19)
    
#  #---------------------------------------------------------------------------------------------------------------   
    
#     segments_str = f'''{{
#         "0": "{prepared_sentence1}",
#         "50": "{prepared_sentence2}",
#         "100": "{prepared_sentence3}",
#         "150": "{prepared_sentence4}",
#         "200": "{prepared_sentence5}", 
#         "250": "{prepared_sentence6}", 
#         "300": "{prepared_sentence7}", 
#         "350": "{prepared_sentence8}",
#         "400": "{prepared_sentence9}",
#         "450": "{prepared_sentence10}",
#         "500": "{prepared_sentence11}",
#         "550": "{prepared_sentence12}",
#         "600": "{prepared_sentence13}",
#         "650": "{prepared_sentence14}",
#         "700": "{prepared_sentence15}",
#         "750": "{prepared_sentence16}",
#         "800": "{prepared_sentence17}",
#         "850": "{prepared_sentence18}",
#         "900": "{prepared_sentence19}"
# }}'''


    segments_str = f'''{{
        "0": "{sentence1}",
        "50": "{sentence2}",
        "100": "{sentence3}",
        "150": "{sentence4}",
        "200": "{sentence5}", 
        "250": "{sentence6}", 
        "300": "{sentence7}", 
        "350": "{sentence8}",
        "400": "{sentence9}",
        "450": "{sentence10}",
        "500": "{sentence11}",
        "550": "{sentence12}",
        "600": "{sentence13}",
        "650": "{sentence14}",
        "700": "{sentence15}",
        "750": "{sentence16}",
        "800": "{sentence17}",
        "850": "{sentence18}",
        "900": "{sentence19}"
}}'''
    print(sentence1)
    
    print(segments_str)
    
    # Writing to a text file
    with open("Cars/output_folder/prompt.txt", "w") as f:
        f.write(segments_str)
