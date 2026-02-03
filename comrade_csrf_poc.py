import sys
from urllib.parse import parse_qs

import pyfiglet
from colorama import Fore, Style

hi = pyfiglet.figlet_format("COMRADE_____CSRF--POC____GENERATOR ", font="slant")
print(Fore.RED + hi + Style.RESET_ALL)
print(Fore.RED + "*"*50 + Style.RESET_ALL)


print(Fore.WHITE +
    "Paste Burp REQUEST and press Ctrl+D (Linux/macOS)\n"
    "or Ctrl+Z + Enter (Windows):\n" + Style.RESET_ALL
)

# Read full request
request = sys.stdin.read()

# Split headers and body
headers, body = request.split("\n\n", 1)
lines = headers.splitlines()

# Get method and path
method, path = lines[0].split()[:2]

# Get host
host = ""
for line in lines:
    if line.lower().startswith("host:"):
        host = line.split(":", 1)[1].strip()
        break

# Parse POST parameters
params = parse_qs(body.strip())

# Build HTML (same required format)
html = "<html>\n"
html += "\t<body>\n"
html += f'\t\t<form method="{method}" action="https://{host}{path}">\n'

for key, values in params.items():
    html += f'\t\t\t<input type="hidden" name="{key}" value="{values[0]}"/>\n'

html += '\t\t\t<input type="submit" value="Submit">\n'
html += "\t\t</form>\n"
html += "\t</body>\n"
html += "</html>"

print(Fore.WHITE +"\n--- COMRADE CSRF PoC GENERATED ---\n"+ Style.RESET_ALL)
print(html)
