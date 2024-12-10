<?php

  require("lib/ParmsException.class.php");

  require("lib/fonctions_parms.php");
  require("lib/fonctions_clock.php");

/**
 * IMPORTANT :
 * Ce script n'est qu'une ébauche.
 *
 * En l'état actuel son fonctionnement n'est pas satisfaisant
 *
 *
 * Utiliser directement les variable du tableau $_GET peut être dangereux
 *
 * Ce script est à modifier et compléter au cours de l'exercice
 *
 */


  try{
   // hours doit être un entier sans signe
   $hours = checkUnsignedInt('hours', 0);

   // minutes doit être un entier sans signe
   $minutes = checkUnsignedInt('minutes', 0);

   // seconds doit être un entier sans signe
   $seconds = checkUnsignedInt('seconds', 0);

   // Couleur des aiguilles minutes et secondes
   $hands = checkColor('hands', '#252422');

   // Couleur du background de l'horloge
   $bg = checkColor('bg', 'transparent');

   // Couleur
   $markers = checkColor('markers', 'grey');

   // calcul des angles des aiguilles
   $angles = angles($hours, $minutes, $seconds);

   // inclusion de la page template :
   require('views/page.php');

  }
  catch (ParmsException $e){

  }




?>
