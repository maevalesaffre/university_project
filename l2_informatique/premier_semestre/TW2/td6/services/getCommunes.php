<?php

set_include_path('..'.PATH_SEPARATOR);
require_once('lib/common_service.php');
require_once('lib/initDataLayer.php');
$territoire=$_GET["territoire"];
try{
    if (!isset($territoire)|| $territoire==''){
        $territoires = $data->getTerritoires();
        $u = $territoires['result'][1];
        produceResult($data->getCommunes($u));
    }else{
        $communes = $data->getCommunes($territoire);
        produceResult($communes);
    }
  }
catch (PDOException $e){
    produceError($e->getMessage());
  }

?>