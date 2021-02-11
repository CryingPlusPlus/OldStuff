<?php
    $logins = array();
            $filename = 'logins.csv';
            $fh = fopen($filename, 'r');

            //file einlesen
            while (!feof($fh)) {

                $zeile = fgets($fh);
                $elemente = explode(';', $zeile);
                if (count($elemente) >= 2) {
                    array_push($logins, $elemente);
                }
            }
            fclose($fh);
?>

