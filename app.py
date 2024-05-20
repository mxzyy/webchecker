import requests
import argparse
import bs4

banner = r"""
 __      __   _     ___ _           _           
 \ \    / /__| |__ / __| |_  ___ __| |_____ _ _ 
  \ \/\/ / -_) '_ \ (__| ' \/ -_) _| / / -_) '_|
   \_/\_/\___|_.__/\___|_||_\___\__|_\_\___|_| v0.1
------------------------------  created by h1lmy 
"""

def file_to_list(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        stripped_lines = [line.strip() for line in lines]  # Remove leading/trailing whitespace
        # print(stripped_lines)
        return stripped_lines

def app():
    domain = []

    # Parser
    parser = argparse.ArgumentParser(description='Tools untuk melakukan check terhadap website yang sedang aktif/tidak')
    parser.add_argument('-d', '--domain', type=str, action='append', nargs='*', help='Domain yang akan di-check')
    parser.add_argument('-f', '--file', type=str, action='append', nargs='*', help='Membaca teks dari file')
    args = parser.parse_args()

    # Main
    sites = args.domain
    files = args.file
    try:
        domain.extend(x[0] for x in sites)
    except:
        print("No Domain in Input")

    try:
        for i in files:
            tmp_domain = file_to_list(i[0])
            domain.extend(tmp_domain)
    except:
        print("No files to read")
    for j in domain:
        #print(j)
        if 'https://' in j:
            j = j[8:]
        try:
            req = requests.get(f"https://{j}")
            html = bs4.BeautifulSoup(req.text, "html.parser")
            if req.status_code == 200:
                print(f'https://{j:30} \033[1;32;40m[LIVE]\033[0;37;40m \033[0;34;40m[{html.title.text}] \033[0;37;40m')
            elif req.status_code == 404 or 403:
                print(f'https://{j:30} \033[1;31;40m[LIVE]\033[0;37;40m \033[0;34;40m[{req.status_code}] \033[0;37;40m')
        except:
            print(f'https://{j:30} \033[1;31;40m[DOWN]\033[0;37;40m')


if __name__ == "__main__":
    print(banner)
    app()
