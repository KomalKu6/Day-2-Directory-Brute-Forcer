import requests ## We're importing the requests library to send HTTP GET requests to URLs.

def scan_dir(URL, file_list): ## defining a function called scan_dir()
    ## URL: The base website URL
## file_list: The name of the file containing paths to check (like admin, login)

    try:
        with open(file_list, 'r') as file:
            paths = file.read().splitlines()

         ## This reads the wordlist (filelist.txt) and saves each line as an item in the list paths.
## .splitlines() makes sure each line becomes one directory name like: 
## paths = ['admin', 'robots.txt', 'login']

            print(f"[DEBUG] Loaded {len(paths)} paths from file")
    except FileNotFoundError:
        print("filelist.txt not found")
        return
    ## file is missing or misspelled, the script won't crash

    for path in paths:
        full_path = f"{URL.rstrip('/')}/{path}"

        ## For each path, we build a complete URL like:
        ## .rstrip('/') removes the ending / from the base URL so it doesn’t become double slashes like //admin.
        try:
            response = requests.get(full_path, timeout=5)
            ## This sends an HTTP GET request to the full URL and waits for a max of 5 seconds.
            print(f"[DEBUG] {full_path} → {response.status_code}") 
             # Always show status
             ## We print the status code for debugging and transparency
            if response.status_code == 200:
                print(f"Found: {full_path}")
                ## If the server responds OK → the folder exists → print it.
            elif response.status_code == 403:
                print(f" Forbidden: {full_path}")
                ## 403 means the folder exists but access is denied — still useful for hackers
            elif response.status_code == 404:
                print(f" Not Found: {full_path}")
                ## 404 means not found → ignore or log, depending on need.
            else:
                print(f" {response.status_code}: {full_path}")
                ## For any other status (like 301 redirect, 500 server error), we just show the code.

        except requests.RequestException as e:
            print(f" Error: {full_path} → {e}")
            continue
        ## If anything fails (network issues, SSL errors, timeouts), don’t crash — just skip and continue.


target = input("Enter target URL: ")
filelist = "filelist.txt"
scan_dir(target, filelist)

## This is the driver code: it asks for the URL and calls the scan_dir() function using "filelist.txt"
