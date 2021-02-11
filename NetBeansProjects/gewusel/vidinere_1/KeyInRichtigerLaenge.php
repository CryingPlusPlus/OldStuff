<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        <?php
        
        
        function pwToNmb($x) { //$b = abc array, $x ist der string
            $a= array("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z");
            $end = array();
            $text = str_split($x);
            for ($i = 0; $i < sizeof($text); $i++) {
               
                for ($j = 0; $j < sizeof($a); $j++) {
                    if ($text[$i] == $a[$j]) {
                        array_push($end, $j);
                       
                    }
                }
            }
            return $end;
        }
        function schlussel($Bwort,$Bkey){
            $key = pwToNmb($Bkey);
            $wort = pwToNmb($Bwort);
            if(count($key) < count($wort)){
                $length = count($wort) - count($key);
                for($i = 0; $i < $length; $i++){
                    array_push($key, $key[$i]);
                    
                }
                
            }else if(count($key)>count($wort)){
                $length = count($key)-count($wort) ; 
                for($i = 0; $i < $length; $i++){
                    array_pop($key);
                    
                }
                
            }
            return $key;
        }
           
        var_dump(schlussel("semmel", "auto"));
        ?>
    </body>
</html>
