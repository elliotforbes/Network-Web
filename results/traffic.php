<?php

header("Access-Control-Allow-Origin: *");

try{
    
    $dbh = new PDO('sqlite:../system/main.db') or die('cannot open db');
    $query = 'SELECT * FROM traffic;';
    $results = $dbh->query($query);
    
    $outp = '[';
    foreach($results as $row){
        if ($outp != "["){
            $outp .= ",";   
        }
        $outp .= ' { "ID": "' . $row[0] .'",';
        $outp .= '"HTTPCount": "' .$row[1] .'",';
        $outp .= '"FTPCount": "' .$row[2] .'",';
        $outp .= '"SSHCount": "' .$row[3] .'",';
        $outp .= '"SSDPCount": "' .$row[4] .'",';
        $outp .= '"SMTPCount": "' .$row[5] .'",';
        $outp .= '"DHCPCount": "' .$row[6] .'",';
        $outp .= '"POPCount": "' .$row[7] .'",';
        $outp .= '"MISCCount": "' .$row[8] .'" }';
    }
    $outp .= ']';
    echo $outp;
} catch(Exception $e){
    echo $e->getMessage();   
}

?>