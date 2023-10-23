import openai
import random 
import os
import requests
import json
import io
import base64
from PIL import Image, PngImagePlugin
from moviepy.editor import *
from api import *
import moviepy.editor as mp
import logging
from datetime import datetime


openai.api_key = "OPENAI-API"

def generate_car_prompt(car_name):
    prompt = f"""Generate a 900-second deform prompt for a cool car edit featuring a {car_name}. Make the format look like this but have the prompt in each text different.{{
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
    }}"""

    try:
        completion = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=600
        )
        text = completion.choices[0].text.strip()
        print(text)
        return completion.choices[0].text.strip()
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        return None



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

# # temp prompt for testing
# generated_prompt = {
# "0": "Robotic explorer booting up on an alien terrain",
# "50": "Explorer navigating through rocky outcrops",
# "100": "Explorer analyzing exotic flora with built-in sensors",
# "150": "Explorer trekking towards a distant water source",
# "200": "Explorer observing alien fauna near the water",
# "250": "Explorer collecting water samples for analysis",
# "300": "Explorer encountering a sandstorm, initiating protective shields",
# "350": "Explorer traversing through a field of geysers",
# "400": "Explorer scaling a steep hill to gain a vantage point",
# "450": "Explorer capturing panoramic views of the alien landscape",
# "500": "Explorer discovering ancient alien ruins",
# "550": "Explorer decoding alien inscriptions on the ruins",
# "600": "Explorer uncovering a hidden underground cave",
# "650": "Explorer mapping the cave's extensive tunnel network",
# "700": "Explorer finding rare minerals in the cave",
# "750": "Explorer transmitting data back to Earth",
# "800": "Explorer powering down, mission accomplished"
# }
#----------------------------------------------------------------------------------------------------

# Replacing prompt with new deform prompt from GPT
def replace_prompts(file_path, new_prompts):
    # Load the existing data
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Replace the 'prompts' field with new values
    data['prompts'] = new_prompts

    # Save the modified data back to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)  # indent for pretty formatting
        
# Functions for creating video with sound
def get_latest_file(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path, x)), reverse=True)
    return os.path.join(folder_path, files[0]) if files else None

def get_random_file(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    return os.path.join(folder_path, random.choice(files)) if files else None

def add_audio_to_video(video_path, audio_path, output_path):
    try:
        video = VideoFileClip(video_path)
        audio = AudioFileClip(audio_path)
    except Exception as e:
        print(f"Error loading media files: {e}")
        return

    # Handling different durations between video and audio
    if video.duration < audio.duration:
        # Looping the video to match the audio duration
        video = video.fx(vfx.loop, duration=audio.duration)
    elif video.duration > audio.duration:
        # Shortening the video to match the audio duration
        video = video.subclip(0, audio.duration)

    video_with_audio = video.set_audio(audio)

    # Ensure the output_path ends with .mp4
    if not output_path.endswith('.mp4'):
        output_path += '.mp4'

    try:
        video_with_audio.write_videofile(output_path, codec="libx264")
        print(f"Successfully combined {video_path} with {audio_path}. Output saved to {output_path}.")
    except Exception as e:
        print(f"Error writing video file: {e}")
        
#----------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    
    # picking random car
    random_car = random.choice(cars)

    #Making Diffusion Prompt for car
    print(f"Generating prompt for {random_car}...")
    generated_prompt = generate_car_prompt(random_car)
    print(generated_prompt)
    
    # Setting the path for deforum settings
    settings_file_path = 'deforum_settings.txt'

    # Call the function to replace the prompts
    replace_prompts(settings_file_path, generated_prompt)
    
    job_id = send_post_request('deforum_settings.txt', 'output_folder')
    if job_id:
        print(f"The job_id is: {job_id}")
        output_directory = get_output_directory(job_id)
        if output_directory:
            print(f"The output directory is: {output_directory}")
            copy_video_to_output_folder(output_directory, 'output_folder')
    else:
        print("Failed to get the job_id.")
    
    # File locations for video and audio
    video_folder = "output_folder"
    audio_folder = "output_folder/Music"
    
    # Get the current date and format it as YYYYMMDD
    current_date = datetime.now().strftime('%Y%m%d')
    
    # Setting output file path and name for the tiktok
    output_file_name = f"output_video_{current_date}.mp4"  # Appending the date to the file name
    output_path = f"output_folder/FinishedTikToks/{output_file_name}"  # Full path to the output file

    # Getting latest video and a random sound to pair with
    latest_video = get_latest_file(video_folder)
    random_audio = get_random_file(audio_folder)

    # If there is video and audio that go together then combine them to make the tiktok
    if latest_video and random_audio:
        add_audio_to_video(latest_video, random_audio, output_path)
        print(f"Successfully combined {latest_video} with {random_audio}. Output saved to {output_path}.")
    else:
        print("Couldn't find files to process.")
