<?php

if (isset($_POST['submit'])) {
$name = $_POST['name'];
$subject = $_POST['subject'];
$mailFrom = $_POST['mail'];	
$message = $_POST['message'];

$mailTo = "admin@monsite.fr";
$headers = "From: ".$mailFrom;
$txt = "Vous avez reçu un email de ".$name.":\n\n".$message;

if (($name != '') && ($subject != '') && ($mailFrom != '') && ($message != '')){
	if (strstr($mailFrom, "@") !== FALSE) {
		if (strstr($mailFrom, ".") !== FALSE) {
			mail($mailTo, $subject, $txt, $headers);
			header("Location: ../contact-success.html");
		}
		else{
		header("Location: ../contact-fail.html");
		}
	}
	else{
	header("Location: ../contact-fail.html");
	}
}
else{
	header("Location: ../contact-fail.html");
}
}
