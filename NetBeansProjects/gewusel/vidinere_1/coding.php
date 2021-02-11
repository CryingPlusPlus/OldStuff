<!DOCTYPE html>
<html>
    <head>
        <title>VigenereCode</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="../bootstrap-4.4.1-dist/css/bootstrap.css" rel="stylesheet" type="text/css"/>
        <script src="../bootstrap-4.4.1-dist/js/bootstrap.js" type="text/javascript"></script>
        <link href="style.css" rel="stylesheet" type="text/css"/>
    </head>
    <body>
        <div class="container">
            
            <nav class="navbar navbar-expand-lg navbar-nav navbar-toggler navbar-collapse" style="background-color: #94e4ff;">
                <a class="navbar-brand" href="index.php" style="color: #004861;">Vigenere Coder</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      
        <li class="nav-item">
        <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true"></a>
      </li>
        <li class="nav-item">
        <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true" style="color: #005f80;">Matthias</a>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true" style="color: #005f80;">Marit</a>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true" style="color: #005f80;">Ben</a>
      </li>
    </ul>
  </div>
</nav>
            <br>
            
            
            
            
            <form action="coding.php" method="post">
                    <div class="form-group">
                        <label for="exampleInputEmail1">Text</label>
                        <input type="text" class="form-control" id="text" aria-describedby="text" placeholder="Text" name="wort">
                    </div>
                    <div class="form-group">
                        <label for="exampleInputPassword1">Schlüssel</label>
                        <input type="text" class="form-control" id="exampleInputPassword1" placeholder="Schlüssel" name="key">
                    </div>
                    <button type="submit" class="btn btn-primary">Decode/Encode</button>
                </form>
        <?php
            //raster erstellen
            $a = array("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"," ");
            $kodierungsliste = array();
            $kodierungsliste[0] = $a;
            for($i = 1; $i<count($a); $i++) {
                $b = $kodierungsliste[$i-1];
                $g = array_shift($b);
                array_push($b, $kodierungsliste[$i-1][0]);
                array_push($kodierungsliste, $b);
                
                
            }
            //----------------------------------------------------------------------------------
            //String in nummern arrays
            function position($x, $a) { //$b = abc array, $x ist der string
                $end = array();
                $text = str_split(sonderzeichen($x));
                for ($i = 0; $i < count($text); $i++) {  
                    for ($j = 0; $j < count($a); $j++) {
                        if ($text[$i] == $a[$j]) {
                            array_push($end, $j);
                       
                        }
                    }
                }
                return $end;
            }
            
            function singlePosition($x, $a) { //$b = abc array, $x ist der string
                $text = str_split(sonderzeichen($x));
                $end = array();
                for ($i = 0; $i < count($text); $i++) {  
                    for ($j = 0; $j < count($a); $j++) {
                        if ($text[$i] == $a[$j]) {
                            array_push($end, $j);
                       
                        }
                    }
                }
                return $end[0];
            } 
            //-------------------------------------------------------------------------------------------------
            //sonderzeichen ersetzen
            function sonderzeichen($string){
                $search = array("Ä", "Ö", "Ü", "ä", "ö", "ü", "ß", "´");
                $replace = array("Ae", "Oe", "Ue", "ae", "oe", "ue", "ss", "");
            return str_replace($search, $replace, $string);
            }
            //key in richtige länge machen
            function schlussel($Bwort,$Bkey,$a){
                $key = position($Bkey, $a);
                $wort = position($Bwort, $a);
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
            //-----------------------------------------------------------------------------------------------    
            //kodieren
            function kodieren($Bwort, $Bkey, $a){
                $wort = position($Bwort, $a[0]);
                $key = schlussel($Bwort, $Bkey, $a[0]);
                $end = array();
                for($i = 0; $i<count($wort); $i++){
                    array_push($end, $a[$key[$i]][$wort[$i]]);
            
                }
                return implode($end);
        
            }
            //-----------------------------------------------------------------------------------------------------
            //entkodieren
            function entkodieren($Bwort, $Bkey, $a){
                $end = array();
                $letters = str_split(sonderzeichen($Bwort));
                $key = schlussel($Bwort, $Bkey, $a[0]);
                if(count($letters) == count($key)){
                    for($i=0;$i<count($letters);$i++){
                        $position = singlePosition($letters[$i], $a[$key[$i]]);
                        array_push($end, $a[0][$position]);
                    }
                
                    return implode($end);
                }
            }
        
            $wort = $_POST["wort"];
            $key = $_POST["key"];
            
            echo '<br>';
            if($key != NULL && $wort != NULL){
                echo '<p>Decoding</p>';
                echo '<div class="container-fluid output overflow-auto" style="background-color: #ffffff;">';
                    echo '<div>'.kodieren($wort, $key, $kodierungsliste).'</div>';
                echo '</div>';
                    echo '<br>';
                echo '<p>Encoding</p>';
                echo '<div class="container-fluid output overflow-auto" style="background-color: #ffffff;">';
                    echo '<div>'.entkodieren($wort, $key, $kodierungsliste).'</div>';
                echo '</div>';
            }
            echo '<br><br>'
        
    ?>
        </div>    
    </body>
</html>
