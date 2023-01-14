# Creator : MR.D3F417
# Download-manager For Linux & Windows & Android
# Clearified bullshit code by LapizLTD :/

import os
import sys
import requests
from urllib.parse import urlparse

clear = lambda: os.system("cls" if os.name == "nt" else "clear")

clear()
link = input("Enter download link => ")
clear()
file_name = urlparse(link)
file_name = file_name.path.rsplit('/', 1)[-1]
with open(file_name, "wb") as f:
    print("Downloading %s" % file_name)
    response = requests.get(link, stream=True)
    total_length = response.headers.get('content-length')

    if total_length is None:
        f.write(response.content)
    else:
        dl = 0
        total_length = int(total_length)
        for data in response.iter_content(chunk_size=4096):
            dl += len(data)
            f.write(data)
            done = int(50 * dl / total_length)
            sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
            sys.stdout.flush()

print("\n\n\tDownload Finished...")
input()
