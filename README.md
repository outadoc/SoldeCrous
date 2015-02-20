# Solde CROUS

Juste un petit script en Python qui vérifie le solde de votre compte CROUS et 
vous envoie une notification Pushbullet si le solde est trop faible.

# Configuration

Ouvrez solde_crous.py et remplacez la valeur des variables par les valeurs
adaptées. Vous devrez créer un compte Pushbullet si nécessaire, et récupérer
votre access token sur https://www.pushbullet.com/account.

# Installation

Déposez le .py quelque-part.  

Installez les dépendences en root :

	pip install requests
	pip install pushbullet.py

Lancez le script :

	python solde_crous.py

# Licence

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.
