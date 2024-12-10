<?php
   /**
	 *Fonction elementBuilder() 
     *renvoie le code HTML contenant le type de balise, le contenu de la balise et la classe si il y en a une
     * @param $elementType le type de balise, type : string
     * @param $content le contenu de la balise, type : string
     * @param $elementClass le type de classe, type string
	 * @return $elementType, $content, $elementClass si il y a une classe
	 * @return $elementType, $content si il n'y a pas de classe
	 */
    function elementBuilder(string $elementType,string  $content,string $elementClass="") : string {
    if($elementType == ""){
        $rep = "<$elementType>$content</$elementType>";
    }
    else{
        $rep = "<$elementType class=\"$elementClass\">$content</$elementType>";
    }
    return $rep;
}

/**
 * Fonction qui renvoie l'auteur dans une balise span
 * @param $authors, type string
 * @return $nom, l'auteur avec un tiret
 */
function authorsToHTML(string $authors) : string {
    $authors = explode(" - ",$authors);
    $rep = implode("</span> <span>",$authors);
    return "<span>".$rep."</span>";
}

/**
 * Fonction qui prends en paramètre le fichier .jpg de la couverture du livre et qui retourne le code HTML qui inclut la couveture
 * @param $fileName, type string
 * @return $fileName 
 */
function coverToHTML(string $fileName) : string {
    return "<div class=\"couvertures\"><img src=\"couvertures/$fileName\" alt=\"image de couverture\" /></div>";
}

/**
 * Fonction qui prends en paramètre la catégorie et la valeur selon la table fournie, renvoie le type de balise, la valeur et la catégorie (qui correspond à la classe HTML)
 * grace à la fonction elementBuilder. Chaque return correspond à une classe diférente, le dernier en dehors des boucles corresponds à une catégorie "autre".
 * @return elementBuilder()
 */
function propertyToHTML(string $propName, string $propValue) : string {
    if ($propName == 'titre'){
        return elementBuilder("h2", $propValue, $propName);
    }
    else if ($propName == 'couverture'){
        return coverToHTML($propValue);
    }
    else if ($propName == 'auteurs') {
        return elementBuilder("div",authorsToHTML($propValue), $propName);
    }
    else if ($propName == 'année') {
        return elementBuilder("time",$propValue, $propName);
    }
    else {
        return elementBuilder("div",$propValue, $propName);
    }
}



/**
 * Fonction qui prends un tableau en paramètre qui correspond au contenu d'une balise article. Retourne le code HTML d'une balise article.
 * @param book, un tableau 
 * @return $couverture.$description (qui sont dans deux balises div différentes)
 */
function bookToHTML(array $book) : string {
    $couv="";
    $content = "";
    foreach($book as $key => $value){
        if ($key == 'couverture'){
            $couv = propertyToHTML($key, $value);
        }
        else{
            $content .= propertyToHTML($key, $value);
        }
    }
    $desctiption = elementBuilder("div", $content, "description");
    return elementBuilder('article', $couv.$desctiption, "livre");        
}

/**
 * Fonction qui retourne le code HTML présentant l’ensemble des livres du fichier.
 * @param $datalayer la couche d’accès aux données de descriptions de livres
 * @return $result
 */
function libraryToHTML($datalayer) : string {
    $result = '';
    $reader = $datalayer;
    $book = $reader ->readBook();
    while($book != NULL ){
      $result.= bookToHTML($book);
      $book = $reader -> readBook();
    }
    return $result;
    }
?>
