<?php
session_start();
$flag = "CYBERHUB{50m3_ppl_H4te_SQLi_wbu_my_Fr!nD}";
?>
<!DOCTYPE html>
<html>
	<head>
		<title>Home</title>
	</head>
	<body style="background-color: black;color:green;">
		<center>
		<h2><a href="login.php">login</a></h2>
		<?php
			if(@$_SESSION['flag'] == 1 ){
				if( @$_SESSION['admin'] == 1 ){
					echo "<center><h1><font color='green'>".$flag."</font></h1></center>";
				}else{
					echo "<center><h1>Welcome User.</h1></center>";
				}
			}
		?>
		</center>
	</body>
</html>