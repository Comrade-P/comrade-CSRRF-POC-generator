*COMRADE CSRF POC Generator* is a lightweight and educational tool designed to automatically generate CSRF Proof‑of‑Concept (PoC) HTML forms from raw Burp Suite HTTP requests.

This tool was specially created while solving PortSwigger Web Security Academy labs.
During hands‑on practice, I needed a faster and cleaner way to convert vulnerable requests into CSRF PoCs — so I built this tool to simplify that process for myself and other learners.

It is focused on learning, understanding, and demonstrating CSRF vulnerabilities, especially for students and beginners in web security.

<<<<<<<<   For educational and authorized testing purposes only.... >>>>>>>>




Features**********>>>>>>>

1️⃣ Accepts Raw Burp Request

2️⃣ Automatically Extracts Request Details

3️⃣ Parses Parameters Dynamically

4️⃣ Generates Clean CSRF HTML PoC

5️⃣ Beginner‑Friendly Output

6️⃣ Dockerized for Easy UsagE

7️⃣ Perfect for PortSwigger Labs & Learning





***>>>>>Run the tool using Docker:

STEPS:-


1..git clone https://github.com/Comrade-P/comrade-CSRRF-POC-generator.git


2..cd comrade-CSRRF-POC-generator

3..docker build -t csrf-poc-generator .
docker run -it csrf-poc-generator


4..Paste the Burp Suite HTTP request

5..Press Ctrl+D (Linux/macOS) or Ctrl+Z + Enter (Windows)

6..CSRF PoC HTML will be generated
