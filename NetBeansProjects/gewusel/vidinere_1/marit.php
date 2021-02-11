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
            $text = array();
            for($i = 0; $i<strlen($x); $i++){
                array_push($text, $x[$i]);
                
            }
            for ($i = 0; $i < sizeof($text); $i++) {
               
                for ($j = 0; $j < sizeof($a); $j++) {
                    if ($text[$i] == $a[$j]) {
                        array_push($end, $j);
                       
                    }
                }
            }
            return $end;
        }
        function sonderzeichen($string){
            $search = array("Ä", "Ö", "Ü", "ä", "ö", "ü", "ß", "´");
            $replace = array("Ae", "Oe", "Ue", "ae", "oe", "ue", "ss", "");
            return str_replace($search, $replace, $string);
        }
        
        var_dump(sonderzeichen("Hallo Üüüü äää ö"));
           
        
        ?>
    </body>
</html>
