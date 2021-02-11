<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
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
                    <div class="form-group overflow-auto">
                        <label for="exampleInputEmail1">Text</label>
                        <input type="text" class="form-control" id="text" aria-describedby="text" placeholder="Text" name="wort">
                    </div>
                    <div class="form-group overflow-auto">
                        <label for="exampleInputPassword1">Schlüssel</label>
                        <input type="text" class="form-control" id="exampleInputPassword1" placeholder="Schlüssel" name="key">
                    </div>
                    <button type="submit" class="btn btn-primary">Decode/Encode</button>
                </form>
            
            

        </div>
    </body>
</html>
