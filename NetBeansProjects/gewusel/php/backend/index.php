<?php
    session_start();
    if($_SESSION['auth'] != true){
        $_SESSION['auth'] = false;
        
    }
?>

<!DOCTYPE html>
<html>
    <head>
        <title>Obstladen</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="../bootstrap-4.4.1-dist/js/bootstrap.js" type="text/javascript"></script>
        <link href="../bootstrap-4.4.1-dist/css/bootstrap.css" rel="stylesheet" type="text/css"/>
        <script src="../../jquery.js" type="text/javascript"></script>
    </head>
    <body>
        <script type="text/javascript">
            
        </script>
        <a id="logginout" href="logout.php">Logout</a>
        <?php 
            var_dump($_SESSION);
            if($_SESSION['auth'] == true){
                
                echo 'hola gehimer';
            }
        ?>
    </body>
</html>
