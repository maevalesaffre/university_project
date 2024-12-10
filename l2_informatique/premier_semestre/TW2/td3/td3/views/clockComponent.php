<?php
/**
 * Requiert une variable PHP $angles : tableau associatif comportant les clés :
 * 'hours' : angle de l'aiguille des heures
 * 'minutes' : angle de l'aiguille des minutes
 * 'seconds' : angle de l'aiguille des secondes
 *
 *
 */
  ?>
  <svg xmlns:xlink="http://www.w3.org/1999/xlink"
  xmlns:svg="http://www.w3.org/2000/svg"
  xmlns="http://www.w3.org/2000/svg"
  viewBox="-105 -105 210 210"
  id = "clockSVG">
   <!--
    (cc) bruno.bogaert@univ-lille.fr
    Licence Creative Commons  https://creativecommons.org/licenses/by-sa/3.0/deed.fr

    Version complétée et modifiée
    Original : https://fr.wikipedia.org/wiki/Fichier:Clock_11-37.svg
   -->
 <style>
    #base{
      fill : <?= $bg ?>; /* couleur du fond : bg */
    }
    #hourMarker, #minMarker, #centerMarker{
      stroke : <?= $markers ?>; /*couleur des marqueurs : markers */
      fill : <?= $markers ?>;   /*couleur des marqueurs : markers */
    }
    .hand{
      stroke : <?= $hands ?>;  /* couleur des aiguilles h et mn : hands */
    }
    .hand.seconds{
      stroke: #EB5E28; /* couleur aiguille des secondes */
    }
  </style>
  <defs>
    <circle cx="0" cy="87" r="2.2"  id="minMarker"/>
	  <line x1="0" y1="95" x2="0" y2="78" stroke-width="3.8" id="hourMarker"/>
  </defs>

  <circle id='base' cx="0" cy="0" r="105"/>

  <g id="markerSet">
    <use xlink:href="#hourMarker"/>
    <use xlink:href="#minMarker" transform="rotate( 6)"/>
    <use xlink:href="#minMarker" transform="rotate(12)"/>
    <use xlink:href="#minMarker" transform="rotate(18)"/>
    <use xlink:href="#minMarker" transform="rotate(24)"/>
  </g>

  <use xlink:href="#markerSet" transform="rotate( 30)"/>
  <use xlink:href="#markerSet" transform="rotate( 60)"/>
  <use xlink:href="#markerSet" transform="rotate( 90)"/>
  <use xlink:href="#markerSet" transform="rotate(120)"/>
  <use xlink:href="#markerSet" transform="rotate(150)"/>
  <use xlink:href="#markerSet" transform="rotate(180)"/>
  <use xlink:href="#markerSet" transform="rotate(210)"/>
  <use xlink:href="#markerSet" transform="rotate(240)"/>
  <use xlink:href="#markerSet" transform="rotate(270)"/>
  <use xlink:href="#markerSet" transform="rotate(300)"/>
  <use xlink:href="#markerSet" transform="rotate(330)"/>


  <line x1="0" y1="-95" x2="0" y2="0" stroke-width="2.8" transform="rotate(<?=$angles['minutes'] ?>)"  class ="hand minutes" />
  <line x1="0" y1="-62" x2="0" y2="0" stroke-width="5"   transform="rotate(<?=$angles['hours'] ?>)" class ="hand hours" />
  <line x1="0" y1="-100" x2="0" y2="20" stroke-width="1.2"  transform="rotate(<?=$angles['seconds'] ?>)"  class ="hand seconds" />
  <circle cx="0" cy="0" r="7" id="centerMarker"/>
</svg>
