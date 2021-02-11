<?php
require 'Polygon.php';

class Rechteck  extends Polygon {
    private $laenge;
    private $breite;
    
    
    function __construct($laenge, $breite) {
        $this->laenge = $laenge;
        $this->breite = $breite;
        $this->necks = 4;
    }
    function __toString() {
        return Rechteck::class;
    }

    public function getFlaeche(){
        return $this->laenge * $this->breite;
    }

    public function getUmfang() {
        return 2 * ($this->laenge + $this->breite);
    }

}
?>