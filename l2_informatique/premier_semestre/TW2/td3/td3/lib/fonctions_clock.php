<?php
/**
 * calcule les angles des aiguilles
 * @return : array
 *  avec les clés
 *  'seconds'
 *  'minutes'
 *  'hours'
 */
function angles(int $hours, int $minutes, int $seconds) : array {
  $time = $seconds + $minutes  ;
  return [
   'seconds' => 6 * $seconds,
   'minutes' => 6 * $minutes + 0.1 * $seconds,
   'hours' => 30 * $hours + 0.5 * $minutes + (0.5/60) * $seconds
  ];
 }
 ?>