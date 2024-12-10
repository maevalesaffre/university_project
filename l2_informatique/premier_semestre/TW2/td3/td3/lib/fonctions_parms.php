<?php
 require(__DIR__."/color_defs.php"); // definit la constante COLOR_KEYWORDS

 /**
  *  prend en compte le paramètre $name passé en mode GET
  *   qui doit représenter une couleur CSS
  *  @return : valeur retenue
  *   - si le paramètre est absent ou vide, renvoie  $defaultValue
  *   - si le paramètre est incorrect, déclenche une exception ParmsException
  *
  */
  function checkColor(string $name, string $defaultValue) : string {
   if(! isset($_GET[$name]) || $_GET[$name] == "") return $defaultValue;
   $val = $_GET[$name];
   if(! isset(COLOR_KEYWORDS[$val]) && ! preg_match(COLOR_REGEXP, $val) && $val != "transparent") throw new ParmsException("Couleur $val incorrecte");
   return $val;
  }

 /**
  *  prend en compte le paramètre $name passé en mode GET
  *   qui doit représenter un entier sans signe
  *  @return : valeur retenue, convertie en int.
  *   - si le paramètre est absent ou vide, renvoie  $defaultValue
  *   - si le paramètre est incorrect, déclenche une exception ParmsException
  *
  */
  function checkUnsignedInt(string $name, int $defaultValue) : int {
   try {
     if(!isset($_GET[$name]) || $_GET[$name] == ""){
       $res = $defaultValue;
     }else {
       $res = $_GET[$name];
       if(!ctype_digit($res)) throw new ParmsException("$name incorrect");
     }
     return (int) $res;
   } catch(ParmsException  $e){
     require("views/pageErreur.html");
   }

 }

 ?>
