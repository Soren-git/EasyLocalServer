import os
import sys
from downloaders import downloadArtifacts, downloadResources
from config import config
from colorama import Fore, Style, init

init(autoreset=True)

def install():
    input(f"{Fore.LIGHTBLUE_EX}Appuyez sur Entrée pour commencer...{Style.RESET_ALL}")
    os.system("cls")
    config()
    os.system("cls")
    downloadArtifacts()
    downloadResources()
    os.system("cls")
    
    print(f"{Fore.GREEN}{Style.BRIGHT}L'installation de votre serveur localhost est terminée !{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}---{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Pour démarrer votre serveur, vous pouvez ouvrir le fichier 'start.bat' dans le dossier 'data'.{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}---{Style.RESET_ALL}")
    input(f"{Fore.CYAN}Appuyez sur Entrée pour fermer le terminal...{Style.RESET_ALL}")
    sys.exit()

