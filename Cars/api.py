import json
import requests
import os
import time
import shutil 


# Function to send instructions to SD Deforum
def send_post_request(settings_file_path, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Load settings from file
    with open(settings_file_path, 'r') as settings_file:
        deforum_settings = json.load(settings_file)

    # Define the URL and payload
    url = "http://127.0.0.1:7860/deforum_api/batches"
    payload = {
        "deforum_settings": [deforum_settings],
        "options_overrides": {}  # Add any overrides here if necessary
    }

    # Send POST request
    response = requests.post(url, json=payload)

    # Check for successful response
    if response.status_code == 202:
        print(f'Success: {response.json()}')
        
        # Save the data to a file in the specified folder
        output_file_path = os.path.join(output_folder, 'output.txt')
        with open(output_file_path, 'w') as output_file:
            output_file.write(response.text)
        
        # Extract job_id from the response directly instead of reading the output.txt file again
        response_data = response.json()
        job_id = response_data["job_ids"][0]
        # print(job_id)
        
        return job_id  # Return the job_id
    else:
        print(f'Error: {response.status_code}')
        return None  # Return None in case of an error, you can handle this in your main part of the script

# Function to get the output directory of the job
def get_output_directory(job_id):
    job_status_url = f"http://127.0.0.1:7860/deforum_api/jobs/{job_id}"  # Adjust the URL as needed
    job_status = ""
    while job_status != "SUCCEEDED":
        response = requests.get(job_status_url)
        if response.status_code == 200:
            job_data = response.json()
            job_status = job_data['status']
            if job_status == "FAILED":
                print(f"Job failed. Status: {job_status}")
                return ""
            elif job_status == "SUCCEEDED":
                output_directory = job_data['outdir']
                return output_directory  # return the output_directory here
            else:
                print(f"Job status: {job_status}. Waiting for completion...")
                time.sleep(10)  # Adjust sleep time as needed
        else:
            print(f"Error checking job status: {response.status_code}")
            return ""

# Function to copy content generated to this current directory
def copy_video_to_output_folder(output_directory, output_folder):
    # Extract the numbers at the end of the output_directory string
    video_filename = output_directory.split('_')[-1] + '.mp4'
    
    # Construct the paths to the source video file and the destination location
    source_video_path = os.path.join(output_directory, video_filename)
    destination_video_path = os.path.join(output_folder, video_filename)
    
    # Copy the video file
    shutil.copy(source_video_path, destination_video_path)
    print(f'Video copied to: {destination_video_path}')


