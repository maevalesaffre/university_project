<?php

require_once("lib/fonctionsLivre.php");

function testbookToHTML($fileName){
    $fd = fopen($fileName,'r');
    $page = libraryToHTML($fd);
    echo $page;
}
testbookToHTML('data/livres.txt');

?>