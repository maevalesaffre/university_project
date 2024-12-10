<?php /*
   Licence Informatique Université de Lille 2020
   
*/?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Horloge</title>
        <meta charset="UTF-8" />
        <link rel="stylesheet" href="" />
        <!--<script src="clock.js"></script>-->
        <style>
            body{
                background-color  : tan;
            }
            #clockSVG{
                width : 300px;
                height : 300px;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Horloge</h1>
        </header>
        <?php
          require(__DIR__.'/clockComponent.php')   ; 
        ?>
    </body>
    
</html>