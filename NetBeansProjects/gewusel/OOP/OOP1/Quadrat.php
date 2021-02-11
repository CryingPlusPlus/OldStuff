<?php
require 'Rechteck.php';
class Quadrat extends Rechteck {
    private $seite;
    
    function __construct($seite) {
        $this->laenge = $seite;
        $this->breite = $seite;
        $this->necks = 4;
    }
    
    
}


?>