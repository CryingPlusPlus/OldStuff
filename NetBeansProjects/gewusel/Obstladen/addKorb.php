<?php
session_start();
?>
<?php
foreach($_SESSION['obst'] as $key => $value){
    $_SESSION['obstkorb'][$value[0]] = $_POST[$value[0]];
}
 var_dump($_SESSION['obstkorb']);
?>