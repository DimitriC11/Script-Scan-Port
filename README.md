# ⚡ Simple Port Scanner

Un script Python léger, rapide et sans dépendances externes pour scanner les ports ouverts d'une machine locale ou distante.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

---

## ✨ Fonctionnalités

- 🚀 **Très rapide** : Utilise le multi-threading pour scanner 2000 ports en moins de 5 secondes
- 🎯 **Précis** : Détecte les ports ouverts et identifie automatiquement le service associé
- 🪶 **Zéro dépendance** : Utilise uniquement la librairie standard Python, aucun `pip install` nécessaire
- ⚙️ **Entièrement personnalisable** : Plage de ports, timeout et nombre de threads modifiables
- 🧹 Sortie propre et lisible

---

## 📋 Prérequis

- Python 3.6 ou supérieur
- Rien d'autre !

---

## 🚀 Installation

1. Clone le dépôt :
   ```bash
   git clone https://github.com/DimitriC11/Script-Scan-Port.git
   ```

## 2. Rend toi dans le dossier : 
```bash
 cd Script-Scan-Port

````

# 💻 Utilisation
## Mode interactif
### Lance le script sans argument, il te demandera la cible :
```bash
python3 script.py
```
## Mode direct
### Passe l'IP ou le nom de domaine directement en argument :
```bash
python3 script.py 192.168.1.1
```
# ⚙️ Configuration
## Tu peux modifier tous les paramètres très facilement sur la dernière ligne du script :
```python
port_scanner(target, start_port=1, end_port=2000, threads=200)
```
#### Paramètre	 |   Description	                     |  Valeur par défaut
#### start_port | Premier port de la plage à scanner	|    1
#### end_port	 | Dernier port de la plage à scanner	|    2000
#### threads	 | Nombre de connexions simultanées	   |    200
#### timeout    | Délai maximum d'attente par port	   |    0.8s

# 📄 Exemple de sortie

```text
============================================================
Scan de 192.168.1.1 | Ports 1-2000
Début : 2025-06-12 14:32:10
============================================================

[+] Port 22    OUVERT → ssh
[+] Port 80    OUVERT → http
[+] Port 443   OUVERT → https
[+] Port 8080  OUVERT → unknown

Scan terminé ! Ports ouverts trouvés : 4
Ports ouverts : [22, 80, 443, 8080]
```
   
