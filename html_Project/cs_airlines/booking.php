<?php
require_once 'credentials.php'; 
$connecionstr="host=".DB_SERVER." port=5432 dbname=".DB_BASE." user=".DB_USER." password=".DB_PASS." options='--client_encoding=UTF8'"; 
$dbconn = pg_connect($connecionstr);
if (!$dbconn) {
	die("Connection failed: " . pg_connect_error());
}
if (isset($_POST['button']) && $_POST['button']==='Αποθήκευση') {
$sql = "INSERT INTO bookings(mail, password, firstname, lastname, address, country, zip, phone, card_num, type_card) VALUES 
('".$_POST['mail']."','".$_POST['password']."','".$_POST['firstname']."','".$_POST['lastname']."','".$_POST['address']."','".$_POST['country']."','".$_POST['zip']."','".$_POST['phone']."','".$_POST['card_num']."','".$_POST['type_card']."') ";
}
else {
	$sql = "SELECT * FROM bookings WHERE mail='".$_GET['mail']."' AND password='".$_GET['password']."';";
}
echo $sql;
$result = pg_query($dbconn, $sql);
if ($result) {
	echo "Πραγματοποιήθηκε αποθήκευση δεδομένων";
} 
else {
	echo "Η αποθήκευση των δεδομένων δεν πραγματοποιήθηκε<br>";
	die('Query failed: ' . pg_last_error());
}
 echo "<table style='width:1800;border:2px solid black;font-size:17;padding:10px'>";
 echo "<tr><th>email</th><th>password</th><th>Όνομα</th><th>Επώνυμο</th><th>Διεύθυνση</th><th>Χώρα</th><th>Ταχυδρομικός Κώδικας</th><th>Τηλέφωνο</th><th>Αριθμός πιστωτικής κάρτας</th><th>Τύπος πιστωτικής κάρτας</th></tr>";
 while($row = pg_fetch_array($result)) {
echo "<tr><td style='text-align:center'>".$row['mail']."</td>"."<td style='text-align:center'>".$row['password']."</td>"."<td style='text-align:center'>".$row['firstname']."</td>"."<td style='text-align:center'>".$row['lastname']."</td>"."<td style='text-align:center'>".$row['address']."</td>"."<td style='text-align:center'>".$row['country']."<td style='text-align:center'>".$row['zip']."</td>"."<td style='text-align:center'>".$row['phone']."</td>"."<td style='text-align:center'>".$row['card_num']."</td>"."<td style='text-align:center'>".$row['type_card']."</td></tr>";
 }
echo "</table>";
pg_close($dbconn);
?>