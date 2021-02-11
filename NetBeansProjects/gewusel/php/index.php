<?php
//Session System
session_start();

function back2Login() {
    session_destroy();
    header("Location: login.php");
}

//Das login system

/* if ($username === 'olaf') {
  if ($pwd === 'olaf') {
  //gehen rein du darfst
  $_SESSION['user'] = true;
  echo 'hola';
  } else {
  back2Login();
  }
  } else {
  back2Login();
  } */
?>



<!DOCTYPE html>
<html>
    <head>
        <title>Obstladen</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="../bootstrap-4.4.1-dist/js/bootstrap.js" type="text/javascript"></script>
        <link href="../bootstrap-4.4.1-dist/css/bootstrap.css" rel="stylesheet" type="text/css"/>
    </head>
    <body>
        <div class="container">
            <nav class="navbar navbar-light navbar-expand-lg" style="background-color: #e3f2fd;">
                <a class="navbar-brand" href="#">Obstladen</a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>

                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav mr-auto">
                        <li class="nav-item active">
                            <a class="nav-link" href="index.php">Home <span class="sr-only">(current)</span></a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Ben Wernicke</a>
                        </li>
                        <li>
                            <form action="login.php" method="post" class="form-inline my-2 my-lg-0">
                                <div class="form-group">
                                    <input placeholder="Username" type="username" class="form-control" id="username" name="username">
                                </div>
                                <br>
                                <div class="form-group">
                                    <input placeholder="Passwort" type="password" class="form-control" id="pwd" name="pwd">
                                </div>
                                <button type="submit" class="btn btn-primary">Login</button>
                            </form>
                        </li>
                        <li>
                            <a class="nav-link" href="register.php">Register</a> 
                        </li>
                    </ul>


                </div>
            </nav>

            <?php
            $obst = array();
            $filename = 'obstladen.csv';
            $fh = fopen($filename, 'r');

            //file einlesen
            while (!feof($fh)) {

                $zeile = fgets($fh);

                $elemente = explode(';', $zeile);
                if (count($elemente) >= 2) {
                    array_push($obst, $elemente);
                }
            }
            // tabelle ausgeben
            echo '<div class="table-responsive">';
            echo '<table id="table" class="table table-hover table.table-responsive">';
            echo '<thead>';
            echo '<tr>';
            echo '<th scope="col">Sorte</th><th scope="col">Preis in €/kg</th>';
            echo '</tr>';
            echo '</thead>';
            echo '<tbody>';
            foreach ($obst as $key => $value) {
                echo '<tr>';
                echo '<td>' . $value[0] . '</td><td>' . $value[1] . '</td>';
                echo '</tr>';
            }
            echo '</tbody>';
            echo '</table>';
            echo '</div>';

            fclose($fh);
            ?>
        </div>    
    </body>
</html>
