
<?php
/*
Sachen löschen 
DELETE FROM bw_produkte WHERE bild='obstimg/apfel.jpg'
 * 
 Sachen einfügen
 INSERT INaaaTO `bw_produkte` (`produktname`, `preis`, `bild`) VALUES ('Aepfel', '3€', 'obstimg/apfel.jpg');
  */

session_start();
$inactive = 3600;

if (isset($_SESSION['start_time'])) {
    if (time() - $_SESSION['start_time'] > $inactive) {
        var_dump($_SESSION);
        header("Location: logout.php");
    }
}
?>
<!DOCTYPE html>
<html>
    <head>
        <title>Opas Obstladen</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="../bootstrap-4.4.1-dist/css/bootstrap.css" rel="stylesheet" type="text/css"/>
        <script src="../bootstrap-4.4.1-dist/js/bootstrap.js" type="text/javascript"></script>
        <link href="style.css" rel="stylesheet" type="text/css"/>
        <link href="https://fonts.googleapis.com/css?family=Rochester&display=swap" rel="stylesheet">
    </head>
    <body>
        <div class="container">


            <nav  class="navbar navbar-expand-lg navbar-light navbarstyle" style="background-color: rgba(0,0,0,0);">
                <img src="opa.png" width="30" height="30" alt="">
                <a style="color: #28a745; font-family: 'Rochester', cursive;" class="navbar-brand" href="#">Opas Obstladen</a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>

                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav mr-auto">
                        <li class="nav-item active">
                            <a class="nav-link" href="index.php">Home <span class="sr-only">(current)</span></a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Obstkorb</a>
                        </li>
                    </ul>
                    <?php
                    if (isset($_SESSION['auth']) == true) {
                        echo '<a class="mr-sm-2 nav-link disabled" href="#">Einen schönen Einkauf  ' . $_SESSION['username'] . '</a>';
                        echo '<a class="btn btn-outline-success my-2 my-sm-0" type="link" href="logout.php">Logout</a>';
                    } else {
                        echo '<form class="form-inline my-2 my-lg-0" action="login.php" method="post">';
                        echo '<input class="hide " name = "username">';
                        echo '<input class="hide " name="pwd">';
                        echo '<button class="btn btn-outline-success my-2 my-sm-0"  type="submit">Login</button>';
                        echo '</form>';
                    }
                    ?>
                </div>
            </nav>

            <br>
            <?php
            //MYSQL
            //verbindung mit der Datenbank
            $host = '127.0.0.1';
            $user = 'infsalzig';
            $password = 'salzstangerl';
            $database = 'SALZ_Default';
            $mysqli = new mysqli($host, $user, $password, $database);

            if ($mysqli->connect_error) {
                die('Connect Error');
            }
            $obst = array();
            $sql = 'SELECT * FROM bw_produkte';
            $result = $mysqli->query($sql);
            while ($obj = $result->fetch_object()) {
                //echo $obj->produktname.'<br>';
                array_push($obst, [$obj->produktname, $obj->preis, $obj->bild]);
            }
            //die();
            //Verbindung schließen
            $mysqli->close();
            ?>

            <div class="auswahl">

                <?php
                /*$filename = 'obst';
                $fh = fopen($filename, 'r');

//file einlesen
                while (!feof($fh)) {

                    $zeile = fgets($fh);

                    $elemente = explode(';', $zeile);
                    if (count($elemente) >= 2) {
                        array_push($obst, $elemente);
                    }
                }
                fclose($fh);*/
                $_SESSION['obst'] = $obst;
                $rochester = 'Rochester';
                echo '<div class="row">';
                foreach ($obst as $key => $value) {


                    echo '<div class="col-sm-3 kartencol">
                    <div class="card karte">';
                    echo '<img class="card-img-top karteimg" src="' . $value[2] . '" alt="Card image cap">';
                    echo '<div class="card-body">
                            <h6 class="card-title">' . $value[0] . ' Preis: '.$value[1].'</h6>
                            <button href="#" class="btn btn-outline-success" type="submit" style="font-size: 75%; font-family: ' . $rochester . ', cursive;">In den Obstkorb</button>
                            
                            
                        </div>
                    </div>
                </div>
                <br>';
                }
                echo '</div>';
                ?>
            </div>
        </div>
    </body>
</html>
