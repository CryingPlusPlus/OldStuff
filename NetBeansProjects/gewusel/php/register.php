<?php
    session_start();
?>

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
    require 'functions.php';
    
    foreach ($logins as $value) {
        echo $value[0];
        echo $value[1]; 
    
}
?>

