<?php

session_start();
if( $_SERVER['REQUEST_METHOD'] == "POST" ){
	$uname = @$_POST['uname'];
	$passwd = @$_POST['passwd'];
	if( strpos($uname, " ") ){
		echo "<center><h1>I hate Hackers <span style='font-size:100px;'>&#129324;</span></h1></center>";
		die();
	}
	$conn = mysqli_connect("localhost", "root", "root", "cyhub");
	$query = "SELECT * FROM cyhub WHERE username='$uname'";
	$res = mysqli_query($conn, $query);
	$rows = @mysqli_fetch_array($res);
	if($rows){
		if( $rows['role'] == "admin" ){
			$_SESSION['admin'] = 1;
		}else{
			$_SESSION['admin'] = 0;
		}
		$_SESSION['flag'] = 1;
	}else{
		echo "<center>Invalid Creds.</center>";
	}
}
?>
<!DOCTYPE html>
<html>
	<head>
		<title>Login</title>
	</head>
	<body style="background-color: black;color:green;">
		<center>
			<?php
				if(@$_SESSION['flag'] == 1){
					if(@$_SESSION['admin'] == 1){
						echo "Hi admin :) <a href=index.php>home</a>";
					}else{
						echo "you're not admin :( <a href=index.php>home</a>";
					}
				}
			?><br><br><br><br><br><br>
		<form method="POST">
			<input type="text" style="width: 300px" name="uname" placeholder="Username" autocomplete="off"><br>
			<input type="password" style="width: 300px" name="passwd" placeholder="Password" autocomplete="off"><br>
			<input type="submit" value="Login">
		</form>
		</center>
	</body>
</html>