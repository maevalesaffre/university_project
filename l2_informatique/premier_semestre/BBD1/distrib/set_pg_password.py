#enregistrement d'un mot de passe dans le trousseau de clés
import keyring
import getpass

host='webtp.fil.univ-lille1.fr'
user= input('user ?')
password= getpass.getpass(f'password for {user} on {host} ?')
keyring.set_password(host+'_pg',user, password )
