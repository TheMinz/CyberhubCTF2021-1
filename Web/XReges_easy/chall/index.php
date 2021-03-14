<?php
	include('box.php');
  $reg="/[4-7][s-z]{4}_.*$_SERVER[REMOTE_ADDR].*\tc\ty\tb\te\tr\th\tu\tb/";
  if(preg_match($reg,$_GET['key'])){
  	done();
  }
  else echo("<h2>Try Again</h2>");

  highlight_file( __FILE__ );
?>