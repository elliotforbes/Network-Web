<?php

header("Access-Control-Allow-Origin: *");

try{
    $dbh = new PDO('sqlite:../system/main.db') or die('cannot open db');
    $query = 'SELECT * FROM throughputResults;';
    
    $results = $dbh->query($query);
    
    $outp = '[';
    foreach($results as $row){
        if ($outp != "[") {
            $outp .= ",";
        }
        $outp .= ' { "ID":"' . $row[0] .'",';
        $outp .= '"RESULT":"' . $row[1] .'",';
        $outp .= '"CREATED":"' . $row[2] .'" }';
    }
    $outp .= ']';
    echo $outp;
    
} catch (Exception $e){
    echo $e->getMessage();   
}

?>