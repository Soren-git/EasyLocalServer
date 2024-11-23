import os
import time
import requests
import py7zr
import zipfile
from colorama import Fore, Style, init

init(autoreset=True)

def spinning_effect(message, delay=0.25, max_iterations=10):
    """Affiche une animation de rotation d'un bâton en boucle."""
    spinner = ['\\', '|', '/', '-']
    iteration = 0
    while iteration < max_iterations:
        for i in range(len(spinner)):
            print(f"{Fore.CYAN}{message} {spinner[i]}{Style.RESET_ALL}", end="\r", flush=True)
            time.sleep(delay)
            iteration += 1
            if iteration >= max_iterations:
                break
    print()

def downloadArtifacts():
    url = "https://runtime.fivem.net/artifacts/fivem/build_server_windows/master/7290-a654bcc2adfa27c4e020fc915a1a6343c3b4f921/server.7z"
    archivePath = os.path.join("artifacts", "server.7z")
    
    if not os.path.exists(archivePath):
        spinning_effect("Téléchargement des artifacts", 0.2, 45)
        response = requests.get(url, stream=True)
        with open(archivePath, "wb") as file:
            file.write(response.content)
        os.system("cls")
        print(f"{Fore.GREEN}Les artifacts ont été correctement téléchargés !{Style.RESET_ALL}")
    
    os.system("cls")
    spinning_effect("Extraction des fichiers", 0.2, 45)
    with py7zr.SevenZipFile(archivePath, mode="r") as archive:
        archive.extractall(path="artifacts")
    os.system("cls")
    print(f"{Fore.GREEN}Les fichiers ont été extraits dans le dossier 'artifacts' !{Style.RESET_ALL}")
    os.remove(archivePath)

def downloadResources():
    url = "https://github.com/citizenfx/cfx-server-data/archive/refs/heads/master.zip"
    archivePath = os.path.join("data/resources/[cfx]", "server-resources.zip")
    
    if not os.path.exists(archivePath):
        os.system("cls")
        spinning_effect("Téléchargement des ressources", 0.2, 45)
        response = requests.get(url, stream=True)
        with open(archivePath, "wb") as file:
            file.write(response.content)
        os.system("cls")
        print(f"{Fore.GREEN}Les ressources ont été correctement téléchargées !{Style.RESET_ALL}")
    
    os.system("cls")
    spinning_effect("Extraction des fichiers", 0.2, 45)
    with zipfile.ZipFile(archivePath, "r") as archive:
        for member in archive.namelist():
            if member.startswith("cfx-server-data-master/resources/") and not member.endswith("/"):
                destinationPath = os.path.join("data/resources/[cfx]", member.replace("cfx-server-data-master/resources/", ""))
                os.makedirs(os.path.dirname(destinationPath), exist_ok=True)
                with archive.open(member) as source, open(destinationPath, "wb") as target:
                    target.write(source.read())
    
    os.system("cls")
    print(f"{Fore.GREEN}Les ressources ont été extraites dans le dossier 'resources' !{Style.RESET_ALL}")
    os.remove(archivePath)
