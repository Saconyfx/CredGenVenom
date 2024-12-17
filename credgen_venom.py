import os  
import requests  
import pyfiglet  
from colorama import Fore, Style  
import argparse  
import random  
import sys  
import itertools  
  
# List of wordlists URLs (restored only rockyou and 10_million)  
wordlist_urls = {  
   "rockyou": "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt",  
   "10_million": "https://weakpass.com/wordlists/10_million_password_list_top_10000.txt"  
}  
  
# Function to download wordlists  
def download_wordlist(wordlist_name):  
   url = wordlist_urls.get(wordlist_name)  
   if not url:  
      print(Fore.RED + f"Error: {wordlist_name} is not a valid wordlist option." + Style.RESET_ALL)  
      return  
  
   filename = url.split("/")[-1]  
   file_path = os.path.join(os.getcwd(), filename)  
  
   # Check if the file already exists  
   if os.path.exists(file_path):  
      print(Fore.YELLOW + f"{filename} already exists. Skipping download." + Style.RESET_ALL)  
   else:  
      print(Fore.GREEN + f"Downloading {filename}..." + Style.RESET_ALL)  
      try:  
        response = requests.get(url)  
        response.raise_for_status()  # Check if the request was successful  
        with open(file_path, 'wb') as file:  
           file.write(response.content)  
        print(Fore.GREEN + f"Downloaded {filename} successfully!" + Style.RESET_ALL)  
      except requests.exceptions.RequestException as e:  
        print(Fore.RED + f"Error downloading {filename}: {e}" + Style.RESET_ALL)  
  
# Display the ASCII banner  
def display_banner():  
   banner = pyfiglet.figlet_format("CredGen Venom")  
   print(Fore.RED + banner[:len(banner)//2] + Fore.BLUE + banner[len(banner)//2:] + Style.RESET_ALL)  
   print(Fore.BLUE + "-" * 50 + Style.RESET_ALL)  
   print(Fore.WHITE + "Developer: Saconyfx AKA Terminal Venom" + Style.RESET_ALL)  
   print(Fore.BLUE + "Portfolio: https://Saconychukwu.com" + Style.RESET_ALL)  
   print(Fore.RED + "GitHub Profile: https://github.com/Saconyfx" + Style.RESET_ALL)  
   print(Fore.BLUE + "GitHub Repo: https://github.com/Saconyfx/CredGenVenom" + Style.RESET_ALL)  
   print(Fore.YELLOW + "Other Profile:  https://linktr.ee/Chidubemc"  + Style.RESET_ALL)  
   print(Fore.BLUE + "-" * 50 + Style.RESET_ALL)  
   print(Fore.GREEN + "Welcome to CredGen Venom! Get ready to create powerful password profiling tools." + Style.RESET_ALL)  
  
# Function to ask questions and generate passwords  
def ask_questions():  
   questions = [  
      "First Name", "Last Name", "Nickname", "Date of Birth (Year)", "Date of Birth (Month)",  
      "Date of Birth (Day)", "Mother’s Name", "Partner’s Name", "Favorite Word", "Favorite Color",  
      "Pet’s Name", "Lucky Number", "Place of Birth"  
   ]  
  
   user_data = {}  
  
   print(Fore.GREEN + "Please answer the following questions:" + Style.RESET_ALL)  
  
   # Asking the user for input  
   for question in questions:  
      user_data[question] = input(f"{question}: ")  
  
   return user_data  
  
# Function to generate multiple password combinations based on user input  
def generate_passwords(user_data, num_passwords):  
   passwords = set()  # Use a set to avoid duplicates  
  
   while len(passwords) < num_passwords:  
      combinations = [  
        f"{user_data['First Name']}{user_data['Date of Birth (Year)']}",  
        f"{user_data['Last Name']}{user_data['Pet’s Name']}",  
        f"{user_data['Nickname']}{user_data['Favorite Color']}",  
        f"{user_data['Pet’s Name']}{user_data['Lucky Number']}",  
        f"{user_data['First Name']}{user_data['Partner’s Name']}"  
      ]  
  
      # Add unique passwords to the set  
      for combination in combinations:  
        if combination not in passwords:  
           passwords.add(combination)  
  
   return list(passwords)  
  
# Function to save the generated passwords to a file  
def save_wordlist(passwords):  
   filename = "generated_passwords.txt"  
   with open(filename, 'w') as f:  
      for password in passwords:  
        f.write(password + '\n')  
   print(f"Passwords saved to {filename}")  
  
# Function to generate wordlist from profile  
def generate_wordlist_from_profile(profile, num_passwords):  
   # Create a list of possible password combinations  
   combinations = [  
      # Combine first name with other fields  
      profile["First Name"] + profile["Date of Birth (Year)"],  
      profile["First Name"] + profile["Date of Birth (Month)"],  
      profile["First Name"] + profile["Date of Birth (Day)"],  
      profile["First Name"] + profile["Nickname"],  
      profile["First Name"] + profile["Favorite Color"],  
      profile["First Name"] + profile["Pet’s Name"],  
      profile["First Name"] + profile["Lucky Number"],  
  
      # Combine last name with other fields  
      profile["Last Name"] + profile["Date of Birth (Year)"],  
      profile["Last Name"] + profile["Date of Birth (Month)"],  
      profile["Last Name"] + profile["Date of Birth (Day)"],  
      profile["Last Name"] + profile["Nickname"],  
      profile["Last Name"] + profile["Favorite Color"],  
      profile["Last Name"] + profile["Pet’s Name"],  
      profile["Last Name"] + profile["Lucky Number"],  
  
      # Combine nickname with other fields  
      profile["Nickname"] + profile["Date of Birth (Year)"],  
      profile["Nickname"] + profile["Date of Birth (Month)"],  
      profile["Nickname"] + profile["Date of Birth (Day)"],  
      profile["Nickname"] + profile["Favorite Color"],  
      profile["Nickname"] + profile["Pet’s Name"],  
      profile["Nickname"] + profile["Lucky Number"],  
  
      # Combine favorite word with other fields  
      profile["Favorite Word"] + profile["Date of Birth (Year)"],  
      profile["Favorite Word"] + profile["Date of Birth (Month)"],  
      profile["Favorite Word"] + profile["Date of Birth (Day)"],  
      profile["Favorite Word"] + profile["Nickname"],  
      profile["Favorite Word"] + profile["Favorite Color"],  
      profile["Favorite Word"] + profile["Pet’s Name"],  
      profile["Favorite Word"] + profile["Lucky Number"],  
  
      # Combine mother's name with other fields  
      profile["Mother’s Name"] + profile["Date of Birth (Year)"],  
      profile["Mother’s Name"] + profile["Date of Birth (Month)"],  
      profile["Mother’s Name"] + profile["Date of Birth (Day)"],  
      profile["Mother’s Name"] + profile["Nickname"],  
      profile["Mother’s Name"] + profile["Favorite Color"],  
      profile["Mother’s Name"] + profile["Pet’s Name"],  
      profile["Mother’s Name"] + profile["Lucky Number"],  
  
      # Combine partner's name with other fields  
      profile["Partner’s Name"] + profile["Date of Birth (Year)"],  
      profile["Partner’s Name"] + profile["Date of Birth (Month)"],  
      profile["Partner’s Name"] + profile["Date of Birth (Day)"],  
      profile["Partner’s Name"] + profile["Nickname"],  
      profile["Partner’s Name"] + profile["Favorite Color"],  
      profile["Partner’s Name"] + profile["Pet’s Name"],  
      profile["Partner’s Name"] + profile["Lucky Number"],  
   ]  
  
   # Create combinations with different cases  
   combinations_with_cases = []  
   for combination in combinations:  
      combinations_with_cases.append(combination.lower())  # Lowercase  
      combinations_with_cases.append(combination.upper())  # Uppercase  
      combinations_with_cases.append(combination.title())  # Title case  
  
   # Remove duplicates and limit the list to the desired number of passwords  
   unique_passwords = list(set(combinations_with_cases))[:num_passwords]  
  
   return unique_passwords  
  
# Main function  
def main():  
   try:  
      display_banner()  
  
      parser = argparse.ArgumentParser(description="CredGen Venom: Password Profiling Tool")  
      parser.add_argument('-i', action='store_true', help='Interactive questions for password profiling')  
      parser.add_argument('-s', type=str, help='Save generated passwords to a file')  
      parser.add_argument('-v', action='version', version="CredGen Venom v1.0.0")  
      parser.add_argument('-n', type=int, default=10, help='Number of passwords to generate')  
      parser.add_argument('--download-wordlist', choices=wordlist_urls.keys(), help='Download a specific wordlist: rockyou or 10_million')  
      args = parser.parse_args()  
  
      # If --download-wordlist is selected, download the specified wordlist  
      if args.download_wordlist:  
        download_wordlist(args.download_wordlist)  
  
      # Display usage if no interactive mode is selected  
      if not args.i:  
        print(Fore.RED + "Please run the script with the '-i' flag for interactive mode." + Style.RESET_ALL)  
        print("Use '-h' for help on how to use the tool.")  
        return  
  
      # Ask questions and generate passwords if interactive mode is selected  
      user_data = ask_questions()  
  
      # Ask how many passwords to generate  
      try:  
        num_passwords = int(input(Fore.GREEN + "How many passwords would you like to generate? " + Style.RESET_ALL))  
      except ValueError:  
        print(Fore.RED + "Invalid input. Defaulting to 10 passwords." + Style.RESET_ALL)  
        num_passwords = 10  
  
      # Generate wordlist from profile  
      wordlist = generate_wordlist_from_profile(user_data, num_passwords)  
  
      print("\nGenerated Passwords:")  
      for password in wordlist:  
        print(password)  
  
      # Save the wordlist automatically to the current directory  
      save_wordlist(wordlist)  
   except KeyboardInterrupt:  
      print("\nInterrupt received. Exiting gracefully.")  
      sys.exit(0)  
  
# Entry point  
if __name__ == "__main__":  
   main()

