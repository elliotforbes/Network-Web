<?php
//$db = new SQLite3('system/modules/test.db');

try{
    $dbh = new PDO('sqlite:/system/test.db');
} catch (PDOException $e) {
    echo 'Connection failed: ' . $e->getMessage();
}
$query = 'SELECT * FROM connected;';



foreach($dbh->query($query) as $row){
    echo '[';
    echo ' { "a":"' . $row[0] .'",';
    echo '"b":"' . $row[1] .'",';
    echo '"c":"' .$row[2] .'" } ';
    echo ']';
}

?>