<?php
interface BookReader{
	/**
	 * lit les données d'un livre et renvoie une table associative représentant le livre lu
	 * @return : array ou NULL
	 *  attributs possibles : couverture,titre,serie,auteurs,année,catégorie
	 *  renvoie NULL si les données ne contiennent plus de livre.
	 */
	function readBook() : ?array;
}
?>
