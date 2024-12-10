 # TP #1

## UDP

---

1/ IPV4  192.168.5.70/24

2/ The socket identifier is 3

3/ On peut voir notre socket dans la liste

4/ On bind notre socket à une IP/port avec bind id_socket adresse_ip port

5/ On envoie un message avec sendto

6/ Il doit indiquer son adresse IP et son port de destination

7/ On reçoit juste le message avec recvfrom

8/ Il est mieux de choisir les deux car chaque port est normalement attribué à un service

9/ On supprime le socket avec close

10/ on crée un socket udp avec :

    `socket udp`

    Puis on va l'assigner à toutes les adresses et à un port automatiquement choisi

    `bind 3 * 0`

    Pareil pour le second
    

11/ On lance Wireshark

12/ `inet 127.0.0.1/8`

13/ `sendto 3 127.0.0.1 54586 "Comment allez vous?"`

14/ `sendto 3 127.0.0.1 55545 "Je vais bien merci?"`

15/ a) On remarque dans Wireshark que deux paquets ont été envoyés.

En analysant ces derniers, on remarque dans la partie UDP des paquets les ports que l'on a dans Socklab

    b) Addr_envoi -> 127.0.0.1 54586

      Addr_recev -> 127.0.0.1 55545

      Message -> Comment allez vous?

    c) On va envoyer un segment par message (si on a 2 messages, on a deux         segments)

    d) On remarque qu'on envoi beaucoup d'octets au total pour seulement quelques         données envoyés. Par exemple notre premier paquet va envoyer 49 octets pour         seulement 20 octets de data réelles

## TCP

---

1/ Création de deux sockets TCP sur lo :

- `socket TCP` 2 fois

- `bind 3 127.0.0.1 3000`

- `bind 4 127.0.0.1 4000`

4/ On remarque que la connexion nous est refusé

6/ Le serveur va être s2 car c'est lui qui listen pour les connexions ainsi, celui qui va     se connecter (s1) est le client

7/ On remarque l'envoi de 3 paquets:

- S1 va envoyer un paquet contenant le flag SYN (pour initier la connexion)

- S2 va envoyer à son tour un paquet SYN-ACK (pour notifier le client que la connexion a été accepté et que S1 peut commencer une connexion )

- S3 va à son tour envoyer un paquet ACK 

9/ On remarque qu'une connexion a été crée entre les deux sockets

11/ a) Le flag PSH va servir à envoyer les données même si le tampon n'est pas rempli

     b) SEQ nous donne la taille totale d'éléments envoyés durant la session courante

     c) ACK va être envoyer par le serveur pour assurer qu'il ait bien récupérer les         données envoyés par le client.

    d) 20 -1 = 19. c'est la taille du message envoyé par le client.

12/ Il contient 19, autrement dit, la taille du message envoyé.

14/ La valeur est maintenant 0

15/ On remarque que la commande shutdown 3 out a mis fin à la connexion entre S1 et S2 en sortie seulement. Sur Wireshark, cela se traduit par S1 qui envoi un paquet avec les flags FIN et S2 qui réponds FIN ACK. C'est la fin de la communication. (Attention, S2 peut toujours envoyer à S1).

16/ `write 5 "Je vais bien merci"`

      `read 3`

17/ `shutdown  3 in`

18/ a) cf schéma

       b) On a 7 segments transmis au total ce qui est beaucoup plus que UDP

       c) si l'on prend en compte le handshake, on a un total de 365 octets (et ce sans         la fermeture de connexion). On remarque que l'on doit envoyer beaucoup plus         via TCP que via UDP pour un même message.
       
