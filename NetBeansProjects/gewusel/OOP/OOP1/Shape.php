<?php

abstract class Shape {
    //Eigenschaften
    public $color;
    
    
    //Methdoen
    public function test(){
        $this->color = 12;
        echo $this->color;
        
    }
    abstract public function getFlaeche();
    abstract public function getUmfang();
}


?>