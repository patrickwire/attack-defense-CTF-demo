<?php

/*
CREATE TABLE "support"."support" (
	 "id" text,
	 "Name" TEXT,
	 "Message" TEXT
);
*/
//ini_set("display_errors", "1");
error_reporting(E_NONE);

function generateRandomString($length = 10) {
    $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $charactersLength = strlen($characters);
    $randomString = '';
    for ($i = 0; $i < $length; $i++) {
        $randomString .= $characters[rand(0, $charactersLength - 1)];
    }
    return $randomString;
}



$mysqli = new mysqli("localhost", "root", "demo", "support");
if ($mysqli->connect_errno) {
    echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
}

if(isset($_POST['text'])){
	
	$id=generateRandomString();

    /* Prepared statement, stage 1: prepare */
    if (!($stmt = $mysqli->prepare("INSERT INTO support(id,Name, Message) VALUES (?,?,?)"))) {
        echo "Prepare failed: (" . $mysqli->errno . ") " . $mysqli->error;
    }


    if (!$stmt->bind_param("sss",$id, $_POST['name'],$_POST['text'])) {
        echo "Binding parameters failed: (" . $stmt->errno . ") " . $stmt->error;
    }

    if (!$stmt->execute()) {
        echo "Execute failed: (" . $stmt->errno . ") " . $stmt->error;
    }
    echo "you can access your customer request via this ID: ".$id;
	die();
}

if($_GET['ultrasceretpass']=='mannheimmorgenspatzenessenlangsammeralsdiemannheimeradler'){
    echo '<h1 style="color:#ea0a8e">Trololol Web Support System</h1><h3>welcome support person</h3>';
    echo 'this are the open customer requests, please read them an than put them in ht e waste bin like always ;)<br>your secret token for today is wackelpudding<br>';
    $res = $mysqli->query("SELECT * FROM support");
	while ($row = $res->fetch_assoc()) {
			echo "<br><br><br>".$row['Name'].'<br>----------------<br>'.$row['Message'];
		}
    echo 'bye bye';
	die();
}

if(isset($_POST['id'])){
    echo '<h1 style="color:#ea0a8e">Trololol Web Support System</h1>';
    echo 'this is your feedback from lasttime	<br>';
    $res = $mysqli->query("SELECT * FROM support WHERE id='".$_POST['id']."'");
	while ($row = $res->fetch_assoc()) {
			echo "<br><br><br>".$row['Name'].'<br>----------------<br>'.$row['Message'];
		}
		die();
}

?>
<h1 style="color:#ea0a8e">Trololol Web Support System</h1>
<h3>We care for our customers, so please send us your feedback</h3>
<form action="?" method="post">
   Name<br> <input name="name"><br>
    <textarea name="text"></textarea><br>
    <input type="submit" value="Send your feedback">
</form>

<h3>Want to access an old request?</h3>
<form action="?" method="post">
    ID<br> <input name="id"><br>
    <input type="submit" value="access your feedback">
</form>
