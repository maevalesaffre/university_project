<?php
class DataLayer {
	// private ?PDO $conn = NULL; // le typage des attributs est valide uniquement pour PHP>=7.4

	private  $conn = NULL; // connexion de type PDO   compat PHP<=7.3

	/**
	 * @param $DSNFileName : file containing DSN
	 */
	function __construct(string $DSNFileName){
		$dsn = "uri:$DSNFileName";
		$this->connexion = new PDO($dsn);
		// paramètres de fonctionnement de PDO :
		$this->connexion->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // déclenchement d'exception en cas d'erreur
		$this->connexion->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE,PDO::FETCH_ASSOC); // fetch renvoie une table associative
		// réglage d'un schéma par défaut :
		$this->connexion->query('set search_path=authent');
	}


    function authentificationProvisoire(string $login, string $password) : ?Identity{
			 $sql= <<<EOD
							 SELECT login, nom, prenom
							 FROM users
							 WHERE login = :login and password = :password
EOD;
			$stmt = $this->connexion->prepare($sql);
			$stmt->bindValue('login', $login);
			$stmt->bindValue('password', $password);
			$stmt->execute();
			$res = $stmt->fetch();
			if($res){
				return new Identity($res['login'],$res['nom'],$res['prenom']);
			}
			return NULL;
    }


    function authentification(string $login, string $password) : ?Identity{ // version password hash
			$sql= <<<EOD
							SELECT login, nom, prenom, password
							FROM users
							WHERE login = :login
EOD;
		 $stmt = $this->connexion->prepare($sql);
		 $stmt->bindValue('login', $login);
		 $stmt->execute();
		 $res = $stmt->fetch();
		 if($res){
			 if(crypt($password, $res['password']) == $res['password'])
			 		return new Identity($res['login'],$res['nom'],$res['prenom']);
		 }
		 	return NULL;
    }


    /**
    * @return bool indiquant si l'ajout a été réalisé
    */
    function createUser(string $login, string $password, string $nom, string $prenom) : bool	 {
        $sql = <<<EOD
        insert into "users" (login, password, nom, prenom)
        values (:login, :password, :nom, :prenom)
EOD;
				$stmt = $this->connexion->prepare($sql);
				$stmt->bindValue('login', $login);
				$stmt->bindValue('password', password_hash($password,CRYPT_BLOWFISH));
				$stmt->bindValue('nom', $nom);
				$stmt->bindValue('prenom', $prenom);
				try {
					$stmt->execute(); // en cas de violation des contraintes
					// -> déclenchement d'un exception
					return $stmt->rowCount() == 1; // renvoie le nombre de
					// ligne affectées pas la dernière requete
				} catch (PDOException $e) {
					return false;
				}

    }

}
?>
