EXO 1:

Q1/ On effectue un connect (via le handshake) puis le serveur accept la connexion et il envoie le message vur l'output du socket client.

Q2/ On doit traiter une IOException pour permettre à l'admin du serveur de bien traiter ses dernières.

Q3/ On peut se connecter au serveur via un client netcat ou telnet : 
nc <ip_serv> <port>

Q4/ On peut créer une liste dans laquelle on stocke les sockets.

---
EXO 2:

Q1/ On va créer un thread à chaque accept, de ce fait, chaque thread va pouvoir s'occuper d'un socket spécifique.

Q2/ OutputStream output;
	output = socket.getOutputStream();
	PrintWriter writer = new PrintWriter(output, true);
	writer.println();
	
Q3/ Il suffit d'écrire sur l'output de l'ensemble des threads contenus dans la structure de donnée (foreach ligne 39)


Q4/ Encore une fois avec une strucuture de données de type liste qui va stocker l'ensemble des sockets.