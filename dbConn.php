<?php
//$db = new SQLite3('system/modules/test.db'); 
header("Access-Control-Allow-Origin: *");

try{
    $db = new SQLite3('test.db');
} catch(Exception $e) {echo $e->getMessage(); }

$query = 'SELECT * FROM connected;';

$results = $db->query('SELECT * FROM connect;');

$outp = '[';
foreach($dbh->query($query) as $row){
    if ($outp != "[") {$outp .= ",";}
    $outp .= ' { "ID":"' . $row[0] .'",';
    $outp .= '"IP":"' . $row[1] .'",';
    $outp .= '"CONNECTED":"' . $row[2] .'",';
    $outp .= '"LEASE_TIME":"' .$row[3] .'" } ';
    
}
$outp .= ']';

echo($outp);
?>