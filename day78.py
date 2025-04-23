import requests
import os

def download_file(url, destination_folder='.'):
    """
    Download a file from a URL and save it to the specified folder.
    
    Args:
        url (str): The URL of the file to download.
        destination_folder (str): Folder where the file will be saved.
    """
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    local_filename = os.path.join(destination_folder, url.split('/')[-1])
    
    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()  # Raise an error for bad status
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192): 
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
        print(f"Downloaded: {local_filename}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}. Reason: {e}")

# Example usage
url = 'https://example.com/path/to/file.jpg'  # Replace with your URL
download_file(url, destination_folder='downloads')
