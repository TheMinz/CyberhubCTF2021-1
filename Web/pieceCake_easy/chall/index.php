
<!DOCTYPE html>
<html>
<head>
	<title>pieceCake</title>

</head>
<body>
<!--?what-->


<?php

include('cake.php');
if(isset($_GET['what'])){

	 highlight_file( __FILE__ ); 
}
if(!isset($_COOKIE['whoami'])) {SetCookie("whoami","0","/"); }

if(!is_numeric($_COOKIE['whoami'])){
	$_COOKIE['whoami'] = 0;
} 


if($_COOKIE['whoami'] != 296 && $_COOKIE['whoami'] != 297) {
	if(strlen($_COOKIE['whoami']) === 3){
		if ($_COOKIE['whoami'] > 296 ) {
			# code...
			pieceCake();
		}
 		
 	}
}


?>

</body>
</html>