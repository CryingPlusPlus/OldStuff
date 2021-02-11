<?php
require 'Shape.php';

abstract class Polygon extends Shape{
    private $necks;
    
    //Getter
    public function getNecks(){ 
        return $this->necks;
    }


    
    //Setter
    public function setNecks($necks){
        if($necks < 0){
            $this->necks = 3;
        }else{
            $this->necks = $necks;
        }
    }
    
}


?>
