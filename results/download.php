<?php

header("Access-Control-Allow-Origin: *");

try{
    $dbh = new PDO('sqlite:../system/main.db') or die('cannot open db');
    $query = 'SELECT * FROM download;';
    $results = $dbh->query($query);
    
    $outp = '[';
    foreach($results as $row){
        if($outp != "["){
            $outp .= ",";
        }
        $outp .= ' { "DOWNLOAD":"' .$row[1] .'",';
        $outp .= '"UPLOAD":"' .$row[2] .'" }';
    }
    $outp .= ']';
    echo $outp;
} catch(Exception $e){
    echo $e->getMessage();   
}