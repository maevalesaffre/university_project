<?php

set_include_path('..'.PATH_SEPARATOR);
require_once('lib/common_service.php');
require_once('lib/initDataLayer.php');
$insee=$_GET["insee"];
try{
    if(!isset($insee) || $insee=="" ){
      throw new PDOException("Invalid insee");

    }else{
      $commune = $data->getDetails($insee); 
      produceResult($commune);
    }
  }
  catch (PDOException $e){
      produceError($e->getMessage());
  }
?>