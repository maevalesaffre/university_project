<?php
class FileBookReader implements BookReader{

	private $file; // file resource
	/**
	 * Ouvre le fichier .txt contenant les infos sur le livre
	 * @param : $fileName, type string
	 */
	function __construct(string $fileName){
		$this->file = fopen($fileName,'r');
	}
	/**
	 *Fonction readBook() demandée dans l'exercice 1
	 * tableau avec les infos du fichier .txt ou on lit ligne par ligne
	 * on coupe une ligne en 2 quand ":" apparait sinon on renvoie une exception
	 * la partie avant ":" est la clé de la table et la partie après est la valeur
	 * @return $result, le tableau des infos
	 */
/*
	function readBook() : ?array {
		$line = fgets($this->file);
    	$result = array();
    	while ($line !== FALSE && trim($line) != ""){
    	$pos = strpos($line,":");
      if ($pos === FALSE){
      	throw new Exception("Absence de : ");
            }
        $name = trim(substr($line,0,$pos));
      	$value = trim(substr($line, $pos+1));
        $result[$name] = $value;
        $line = fgets($this->file);
        }
    return $result;
	}
*/
	/**
	 *Fonction readBook() demandée dans l'exercice 2
	 * modification de readBook() pour passer les lignes vides avant qu'il y ai du texte
	 * si le fichier est vide on retourne NULL
	 * @return $result, le tableau des infos
	 * @return NULL si le fichier .txt est vide
	 */
function readBook() : ?array{
	$line = fgets($this->file);
	$result = array();
	while($line === ""){
			$line = fgets($this->file);
		}
	while ($line !== FALSE && trim($line) != "" ){
		$pos = strpos($line,":");
		if ($pos === FALSE){
			throw new Exception("Absence de : ");
					}
			$name = trim(substr($line,0,$pos));
			$value = trim(substr($line, $pos+1));
			$result[$name] = $value;
			$line = fgets($this->file);
	}
	if(count($result) == 0){
		return NULL;
	}
	return $result;
}

}

?>