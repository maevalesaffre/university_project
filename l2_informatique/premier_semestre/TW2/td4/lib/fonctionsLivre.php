<?php

/**
 * renvoie le code HTML d'un élément
 * @return string
 */
function elementBuilder(string $elementType,string  $content,string $elementClass="") : string {
	$attClass = "";
	if ($elementClass!="")
		$attClass=" class=\"$elementClass\"";
	return "<{$elementType}{$attClass}>{$content}</{$elementType}>";
}
/**
 * représentation HTML des auteurs
 * @param string $authors :  chaîne avec des noms d'auteurs séparés par ' - '
 *
 * @return string : code HTML avec chaque nom dans un span 
 */
function authorsToHTML(string $authors) : string {
	$tab = explode($authors,' - ');
	return '<span>'.implode($tab,'</span> <span>').'</span>';
}
/**
 * représentation HTML de la couverture d'un livre
 * @param string $fileName  om du fichier image
 * @return string
 * 
 */
function coverToHTML(string $fileName) : string {
	return "<img src=\"couvertures/$fileName\" alt=\"image de couverture\" />";
}
/**
 * représentation HTML d'une propriété
 * @param string $propName : nom de la proriété
 * @param string $propValue : sa valeur
 * @return string : code HTML
 */
function propertyToHTML(string $propName, string $propValue) : string {
	switch ($propName){
		case 'titre' : $elt = 'h2'; break;
		case 'année' : $elt = 'time'; break;
		default : $elt = 'div';	
	}
	switch ($propName){
		case 'authors' : $content  = authorsToHTML($propValue); break;
		case 'couverture' : $content  = coverToHTML($propValue); break;
		default : $content = $propValue;
	}
	return elementBuilder($elt,$content,$propName);
}
/**
 * représentation HTML d'un livre
 * @param array $book : livre sous la forme d'une table de propriétés
 * @return string : code HTML
 */
function bookToHTML(array $book) : string {
	$book = array_filter($book); // supprime toutes les clés de valeur NULL
	$description = '<div class="description">'."\n";
	foreach ($book as $propName=>$propValue){
		if ($propName != 'couverture' ){
			$description .= propertyToHTML($propName,$propValue)."\n";
		}
	}
	$description .= '</div>'."\n";
	$cover = propertyToHTML('couverture', $book['couverture']);
	return "<article class=\"livre\">\n$cover\n$description</article>";	
}

/**
 * représentation HTML d'une liste de livres
 * @param array $booksArray : tableau de livres
 * @return string : code HTML
 */        
function booksArrayToHTML(array $booksArray) : string {
    return implode("\n",array_map("bookToHTML",$booksArray));
}

function authorToOption(array $author) : string{
	$id=$author['id'];
	$nom=$author['nom'];
	return "<option value=\"$id\">$nom</option>";
}

function authorsArrayToOptions(array $authorsArray) : string{
	$res='';
	foreach($authorsArray as $author){
		$res.=authorToOption($author);
	}
	return $res;
}


?>
