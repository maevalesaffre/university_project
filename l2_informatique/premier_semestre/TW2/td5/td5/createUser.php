<?php
spl_autoload_register(function ($className) {
     include ("lib/{$className}.class.php");
 });

try {
  require('lib/initDataLayer.php');
  require('lib/fonctions_parms.php');

   $login = checkString("login", NULL, true);
   $password = checkString("password", NULL, true);
   $nom = checkString("nom", NULL, true);
   $prenom = checkString("prenom", NULL, true);

   $res = $data->createUser($login, $password, $nom, $prenom);
   if ($res){
     require('views/pageCreateOK.php');
     exit();
   } else {
     $erreurCreation = true;
     require('views/pageRegister.php');
     exit();
   }
 } catch (ParmsException $e) {
   echo $e;
 }

?>
