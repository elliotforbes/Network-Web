<?php
//$db = new SQLite3('system/modules/test.db'); 
header("Access-Control-Allow-Origin: *");

try{
     $dbh = new PDO('sqlite:engine/modules/test.db') or die('cannot open db');
    $query = 'SELECT * FROM connected;';
    $results = $dbh->query($query);

    $outp = '[';
    foreach($results as $row){
        if ($outp != "[") {
            $outp .= ",";
        }
        $outp .= ' { "ID":"' . $row[0] .'",';
        $outp .= '"IP":"' . $row[1] .'",';
        $outp .= '"CONNECTED":"' . $row[2] .'",';
        $outp .= '"LEASE_TIME":"' .$row[3] .'" } ';
    }
    $outp .= ']';
    echo $outp;
} catch(Exception $e) {echo $e->getMessage(); }


?>