<?php
//$db = new SQLite3('system/modules/test.db');

$dbh = new PDO('sqlite:~/home/pi/Project/moduels/test.db') or die("cannot open db");

$query = 'SELECT * FROM connected;';



foreach($dbh->query($query) as $row){
    echo '[';
    echo ' { "a":"' . $row[0] .'",';
    echo '"b":"' . $row[1] .'",';
    echo '"c":"' .$row[2] .'" } ';
    echo ']';
}

?>