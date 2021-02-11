<?php
//object importieren´
    require 'Quadrat.php';

//Objekt anlegen
    $rec = new Quadrat(4);
    $A = $rec->getFlaeche();
    echo $A;

?>