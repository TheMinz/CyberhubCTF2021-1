
<html>
	<head>
		<title>backup</title>
	</head>
	<body>
			<h1>
			Index of /
			</h1>
			<hr>
			<a href="../">../</a><br>
  				<a href="?file=c3JjCg==">src</a><br>
  				<a href="?file=ZmlsZTIK">file2</a><br>
				<a href="?file=dGllcgo=">tier</a>
			<hr>
	</body>


<?php
// CYBERHUB{4_Pi3ac3_0f_c4k3_wo0Ow}
$file = $_GET["file"];
if(!empty($file)){
	$file = base64_decode($file);
	if(!preg_match("", $file)){
		echo "<pre>";
		echo file_get_contents($file);
		echo "</pre>";
	}
}else{
		echo "0_0";
	}
?>


</html>
