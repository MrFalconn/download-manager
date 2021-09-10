# Creator : MR.D3F417
# Download-manager For Linux & Windows & Android

import platform ,os
import sys
import requests
from urllib.parse import urlparse
import time
from colorama import Fore
def download():
    data0 = platform.uname()[0]
    if data0 == 'Linux':
        os.system('clear')
    else:
        os.system('cls')
    os.system("Color FC")
    os.system("Mode 60,20")
    os.system("Title BlackGuard-Download.Manager")

    link = input("Enter download link => ")

    if data0 == 'Linux':
        os.system('clear')
    else:
        os.system('cls')

    file_name = urlparse(link)
    file_name = file_name.path.rsplit('/', 1)[-1]

    with open(file_name, "wb") as f:
            print("Downloading %s"% file_name)
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

    print("\n\n\n\tDownload Shod...")
    input()

def passwords():
    data0 = platform.uname()[0]
    if data0 == 'Linux':
        os.system('clear')
    else:
        os.system('cls')
    p = input("Enter the Password:")
    if p == 'blackguard':
        print(Fore.GREEN + '[+]' + Fore.WHITE + 'Wellcome...')
        time.sleep(2)
        download()
    else:
        print()
        print('This is not password')
        print()
        time.sleep(1)
        passwords()

passwords()