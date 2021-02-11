<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
        <title>Index</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="../bootstrap-4.4.1-dist/css/bootstrap.css" rel="stylesheet" type="text/css"/>
        <script src="../bootstrap-4.4.1-dist/js/bootstrap.js" type="text/javascript"></script>
        <link href="style.css" rel="stylesheet" type="text/css"/>
    </head>
    <body>
        <div class="container">
            <p>Ihre IP</p>
            <?php
                $ip = $_SERVER["REMOTE_ADDR"];  
                $host = gethostbyaddr($ip);

                echo "IP Adresse: $ip<br>";  
                echo "Hostname: $host";  
?>
        </div>
    </body>
</html>
