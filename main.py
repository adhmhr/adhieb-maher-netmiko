'print("Hello, Git!")' 
from netmiko import ConnectHandler

def acces_netmiko():
    # Paramètres d'accès fournis dans l'énoncé
    cisco_device = {
        'device_type': 'cisco_ios', # Type pour Cisco IOS/IOS-XE
        'host': 'sandbox-iosxr-1.cisco.com',
        'username': 'admin',
        'password': 'C1sco12345',
        'port': 22,
    }

    try:
        # Initialisation de la connexion
        with ConnectHandler(**cisco_device) as net_connect:
            # A. Affiche la date côté routeur (show clock)
            clock_output = net_connect.send_command("show clock")
            print(f"Date du routeur : {clock_output}")

            # B. Affiche les interfaces dans un fichier interfaces.txt
            interfaces_output = net_connect.send_command("show ip interface brief")
            with open("interfaces.txt", "w") as f:
                f.write(interfaces_output)
            
            print("Le fichier interfaces.txt a été généré avec succès.")

    except Exception as e:
        print(f"Une erreur est survenue : {e}")

if __name__ == "__main__":
    # Instruction de l'étape II.3
    print("Hello, Git!")
    # Appel de la fonction créée à l'étape III.2
    acces_netmiko()
    . Modifiez 
main.py pour ajouter une fonction qui dit salut.
def dire_salut(): 
print("Salut, Git!") 
dire_salut()
