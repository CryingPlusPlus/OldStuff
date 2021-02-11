<?php
    session_start();
    $_SESSION['auth'] = false;
    unset($_SESSION);
    session_destroy();
    header('Location: ../index.php');
?>