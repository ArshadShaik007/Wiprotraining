import requests

url = "https://example.com/largefile.zip"

response = requests.get(url, stream=True)

if response.status_code ==200:
    with open("largefile.zip", "wb") as file:
        for chunk in response.iter_content(chunk_size=4096):
            file.write(chunk)
    print("File downloaded successfully.")

else:
    print("Error downloading file:", response.status_code)
