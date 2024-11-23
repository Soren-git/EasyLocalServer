import os
from assets.templates import resources, server
from colorama import Fore, Style, init

init(autoreset=True)

def config():
    os.system("cls")
    
    server_name = input(f"{Fore.CYAN}Nom du serveur: {Style.RESET_ALL}")
    server_description = input(f"{Fore.CYAN}Description du serveur: {Style.RESET_ALL}")
    tags = []
    
    while (tag := input(f"{Fore.CYAN}Ajouter un tag (ou appuyez sur Entrée pour terminer) : {Style.RESET_ALL}")) != "":
        tags.append(tag)
        
    server_patreon = input(f"{Fore.CYAN}Clé patréon: {Style.RESET_ALL}")
    
    os.makedirs("artifacts", exist_ok=True)
    os.makedirs("data/resources/[cfx]", exist_ok=True)
    
    server_cfg_content = server.replace("{serverName}", server_name).replace("{serverDescription}", server_description).replace("{tags}", ",".join(tags)).replace("{serverPatreon}", server_patreon)
    resources_cfg_content = resources 
    
    with open("data/server.cfg", "w") as cfg:
        cfg.write(server_cfg_content)
    
    with open("data/resources.cfg", "w") as cfg:
        cfg.write(resources_cfg_content)
    
    with open("data/start.bat", "w") as batch:
        batch.write("..\\artifacts\\FXServer.exe +exec ./server.cfg")
    
    print(f"{Fore.GREEN}Configurations créées dans 'data/server.cfg', 'data/resources.cfg', et 'data/start.bat'.{Style.RESET_ALL}")
