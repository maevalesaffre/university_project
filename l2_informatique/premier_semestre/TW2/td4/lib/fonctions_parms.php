<?php
 /**
  *  prend en compte le paramètre $name passé en mode GET
  *   qui doit représenter une couleur CSS
  *  @return : valeur retenue
  *   - si le paramètre est absent ou vide, renvoie  $defaultValue
  *   - si le paramètre est incorrect, déclenche une exception ParmsException
  *
  */
 function checkColor(string $name, string $defaultValue) : string {
    if( !isset($_GET[$name]) || $_GET[$name]=='' ){
      return $defaultValue;
    } elseif ( !ctype_digit($_GET[$name]) ) {
      throw new ParmsException('mon khey y a pas d\'entier là! Il faut un entier');
      return null;
    } else {
      return $_GET[$name];
    }
  }
  
 /**
  *  prend en compte le paramètre $name passé en mode GET
  *   qui doit représenter un entier sans signe
  *  @return : valeur retenue, convertie en int.
  *   - si le paramètre est absent ou vide, renvoie  $defaultValue
  *   - si le paramètre est incorrect, déclenche une exception ParmsException
  *
  */
 function checkUnsignedInt(string $name, ?int $defaultValue=NULL, bool $mandatory=TRUE) : ?int{
    if((!isset($_GET[$name]) || $_GET[$name]=='')&&($defaultValue==NULL)&&($mandatory)){
      throw new ParmsException('il faut un entier et un nom');
    } elseif ((!isset($_GET[$name]) || $_GET[$name]=='')&&($defaultValue==NULL)&&(!$mandatory)) {
      return NULL;
    } else {
      return $_GET[$name];
    }
  }
     
 ?>