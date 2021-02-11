<?php
session_start();
$_SESSION['auth'] = false;
?>
<!DOCTYPE html>
<html>
    <head>
        <title>Obstladen</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="../jquery-3.3.1.js" type="text/javascript"></script>
        <link href="../bootstrap-4.4.1-dist/css/bootstrap.css" rel="stylesheet" type="text/css"/>
        <script src="../bootstrap-4.4.1-dist/js/bootstrap.js" type="text/javascript"></script>
        <link href="style.css" rel="stylesheet" type="text/css"/>
    </head>
    <body>
        <div class="container">
            <br>
            <div class="login_style">
                <h3 style="color: #005cbf;">Obstladen - Login</h3>
                <br>
                <form action="login.php" method="post">
                    <div class="form-group">
                        <input placeholder="Username" type="username" class="form-control" id="username" name="username">
                    </div>
                    <div class="form-group">
                        <input placeholder="Passwort" type="password" class="form-control" id="pwd" name="pwd">
                    </div>
                    <button type="submit" class="btn btn-primary">Login</button>
                    <button type="button" href="register.php" class="btn btn-primary">Register</button>
                </form>
                
            </div>  
        </div>
    </body>
</html>
<?php
$username = $_POST['username'];
$password = $_POST['pwd'];

if ($username === 'horst') {
    if ($password === 'horst') {
        $_SESSION['auth'] = true;
        header("Location: backend/index.php");
    }
}else{
    if ($username === 'olaf') {
        
        if ($password === 'olaf'){
            header('Location: index.php');
            
        }
    }
    
}
?>