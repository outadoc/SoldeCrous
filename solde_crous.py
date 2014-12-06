# coding: utf-8

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import requests
import re
import pushover

# Nom d'utilisateur/mot de passe pour le compte CROUS
CROUS_USERNAME = '12345678'
CROUS_PASSWORD = 'azerty1234'

# Seuil de solde sous lequel une alerte sera envoyée 
BALANCE_THRESHOLD = 3.20

# URL de base du site de monétique du CROUS
MONETIQUE_BASE_URL = 'https://monetique-caen.crous-caen.fr'

# Clés du compte/app Pushover, pour envoyer le message
PUSHOVER_TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
PUSHOVER_USER_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


def getInformationPage(username, password):
    """ Retourne la page d'information sur le compte CROUS. 

    username -- le code utilisateur CROUS du compte
    password -- le mot de passe du compte
    """
    payload = {
        'from': 'authentication', 
        'numeroPorteur': username, 
        'actualPassword': password, 
        'nomPorteur': '',
        'newPassword': '',
        'newPasswordConf': ''
    }

    login = requests.post(MONETIQUE_BASE_URL + '/CrousVAD/getInformation',
        data=payload, verify=False)

    return login.text.encode('utf8')


def getAccountBalance(html):
    """ Retourne le solde de la carte CROUS.

    html -- le code de la page d'information, retourné par getInformationPage
    """
    balanceRgx = re.compile("solde de votre compte est de ([0-9.]+)")
    match = balanceRgx.search(html)

    return float(match.group(1))
    

def main():
    # On récupère la page, puis le solde du compte
    page = getInformationPage(CROUS_USERNAME, CROUS_PASSWORD)
    balance = getAccountBalance(page)

    print("Solde actuel : {:.2f}€".format(balance))

    if balance < BALANCE_THRESHOLD:
        print("Attention, solde inférieur à {:.2f}€ !".format(BALANCE_THRESHOLD))

        # On créé un client Pushover (pour envoyer une alerte)
        pushover_client = pushover.Client(PUSHOVER_USER_KEY, 
            api_token=PUSHOVER_TOKEN)

        pushover_client.send_message("Attention, le solde est de {:.2f}€ !"
            .format(balance), title="Solde Léocarte")
    else:
        # Tout va bien ici
        print("Solde OK !")


if __name__ == "__main__":
    main()
