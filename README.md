# CredGen Venom
## A Password Profiling Tool

CredGen Venom is a password profiling tool designed to generate a list of potential passwords based on user input. It's a useful tool for penetration testers, security researchers, and anyone interested in password security.

### Features
- Generates a list of potential passwords based on user input
- Supports various password formats and complexity levels
- Includes a built-in wordlist generator
- Allows users to customize password generation options
- Allows users to download wordlists (e.g., `rockyou` and `10_million`)

### Usage


```bash
To use CredGen Venom, simply run the script and follow the prompts:

python credgen_venom.py -i

This will launch the interactive mode, where you can input the required information to generate a list of potential passwords.

#Options

The following options are available:

  -i, --interactive      Run in interactive mode  
  -s, --save             Save generated passwords to a file  
  -v, --version          Display version information  
  -n, --num              Specify the number of passwords to generate  
  --download-wordlist    Download a specific wordlist

