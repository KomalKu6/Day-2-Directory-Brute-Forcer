# Day-2-Directory-Brute-Forcer
Build a Directory Brute-Forcer.
A simple Python tool to discover hidden directories on web servers. Built for bug bounty recon.

## Features

- Scans target URLs for common admin panels, sensitive files, and hidden folders.
- Detects `200 OK`, `403 Forbidden`, `404 Not Found`, and other HTTP responses.
- Built with `requests`, clean code, beginner-friendly.

  ## How It Works

1. User provides a target URL
2. Tool reads a wordlist (filelist.txt)
3. Appends each word to the URL
4. Sends HTTP GET requests
5. Displays results with status codes

## Demo Screenshot


## Real-World Usage

- Used in bug bounty recon to find exposed admin panels or sensitive files
- Demonstrates basic recon, HTTP response analysis, and file handling
- Can be extended with multithreading, logging, and advanced wordlists

  ## Tech Used

- Python 3.x
- Requests library
- OWASP Juice Shop (demo target)

## What I Learned

- HTTP protocol & response codes
- Python file I/O and error handling
- Building tools like a real bug bounty hunter
  
  

