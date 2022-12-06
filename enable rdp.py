# Import de la bibliothèque os pour accéder aux fonctionnalités du système d'exploitation
import os

# Définition d'une fonction pour activer RDP sur un poste
def enable_rdp(hostname):
    # Exécution de la commande pour activer RDP sur le poste
    os.system(f"reg add \"HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server\" /v fDenyTSConnections /t REG_DWORD /d 0 /f")
    os.system(f"reg add \"HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server\\WinStations\\RDP-Tcp\" /v UserAuthentication /t REG_DWORD /d 1 /f")
    # Exécution de la commande pour vérifier que RDP est bien activé sur le poste
    result = os.popen(f"reg query \"HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server\" /v fDenyTSConnections").read()
    if "0x00000000" not in result:
        # Si RDP n'est pas activé, afficher un message d'erreur
        print(f"Error: RDP is not enabled on host {hostname}")
    else:
        # Si RDP est activé, redémarrer le service Terminal Services
        os.system(f"net stop termservice && net start termservice")

# Définition d'une fonction pour activer RDP sur une liste de postes
def enable_rdp_on_hosts(hostnames):
    # Pour chaque poste dans la liste
    for hostname in hostnames:
        # Activer RDP sur le poste
        enable_rdp(hostname)

# Utilisation de la fonction pour activer RDP sur une liste de postes
enable_rdp_on_hosts(["poste1", "poste2", "poste3"])