# CredGen Venom
## A Password Profiling Tool

CredGen Venom is a password profiling tool designed to generate a list of potential passwords based on user input. It's a useful tool for penetration testers, security researchers, and anyone interested in password security.

### Features
- Generates a list of potential passwords based on user input
- Supports various password formats and complexity levels
- Includes a built-in wordlist generator
- Allows users to customize password generation options
- Allows users to download wordlists (e.g., `rockyou` and `10_million`)

### Installation & Usage

```bash
To use CredGen Venom, simply run the script and follow the prompts:

Clone the repository:

  git clone https://github.com/Saconyfx/CredGenVenom.git

Navigate to the repository directory

   cd CredGenVenom

Install the required dependencies

   pip install -r requirements.txt

Run the script

   python credgen_venom.py -i
 
This will launch the interactive mode, where you can input the required information to generate a list of potential passwords.

```

# Options

```bash

The following options are available:

  -i, --interactive      Run in interactive mode  
  -s, --save             Save generated passwords to a file  
  -v, --version          Display version information  
  -n, --num              Specify the number of passwords to generate
  -h, --help             Show the help menu  
  --download-wordlist    Download a specific wordlist
   
```
# Examples

```bash

Run in interactive mode:

   python credgen_venom.py -i

Save generated passwords to a file:
  
   python credgen_venom.py -i -s output.txt

Generate 10 passwords:
  
    python credgen_venom.py -i -n 10

Download the rockyou wordlist:

   python credgen_venom.py --download-wordlist rockyou

Generate passwords and download wordlist in one command:

    python credgen_venom.py -i -n 20 --download-wordlist 10_million

Display the help menu:

    python credgen_venom.py -h


```

# License

CredGen Venom is released under the GNU General Public License version 3 (GPL-3.0). See the LICENSE file for details.

GPL-3.0 License
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see https://www.gnu.org/licenses/.

# Contributing

Contributions are welcome! If you'd like to contribute to CredGen Venom, please fork the repository and submit a pull request.

# Disclaimer

CredGen Venom is designed for educational purposes only. It should not be used for malicious activities, such as cracking passwords without authorization. Use at your own risk.

By using CredGen Venom, you acknowledge that you have read and understood the terms of the GPL-3.0 License and agree to abide by them.
