# AutoTikTok
create tiktoks with the power of AI

## Tiktok Accounts Used for this Project
- Car Edits: @autofusionedits

- Anime Edits: @animemosaic

- Reddit Stories: @narrativenxt

## Overview
sub-script functions:
1. It generates a video prompt for a deform video using OpenAI's GPT-3 engine.
2. It sends the generated prompt to a local Stable Diffusion WebUI server to perform a Deform operation.

## Requirements
- Python 3.x
- `requests` library for API interaction
- `openai` library for GPT-3 API

## Installation
1. Clone this repository.
2. Run `pip install -r requirements.txt` to install dependencies.

## Setup
You'll need to set your OpenAI API key in the script:
```python
openai.api_key = "your-openai-api-key-here"
```

## Usage
Run the script using Python 3.x:
```bash
python your_script_name.py
```

## How it Works
1. The script starts the 3 scrips mainCar.py, mainAnime.py, and mainReddit.py
2. It sends a prompt generated based off of the specific scripts function as a prompt to the GPT-3 engine and receives a text output from GPT.
3. This text output is then sent to a Stable Diffusion WebUI server running locally via a POST request to create a cool looking stable diffusion video.
4. The video is then sent to tiktok via tiktoks api and a tiktok sound is applied to the video for the mainCar.py and mainAnime.py videos and posted to their respected accounts
5. the video generated from mainReddit.py takes the reddit story it was generated from and runs it through a text to speach agorithm to read the reddit story outloud and pairs that sound with the video and posts that to the reddit tiktok account

## Troubleshooting
- Make sure your OpenAI API key is correct.
- Ensure the Stable Diffusion WebUI server is running and accessible.
- If you encounter a 404 error, make sure the API endpoint is correct.

## License
This project is open-source, feel free to modify and distribute it under the terms of your preferred open-source license.

## Author
Bronson Woods
