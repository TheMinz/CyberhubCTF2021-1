<?php
			if(isset($_POST["message"])){
				try{
          if (preg_match("/system|echo|phpinfo|print|exec|shell_exec/i", $_POST["message"])) {
               echo "<script>alert('Hack Detected !! XD')</script>";
          }else{
            $headers = "From: webmaster@example.com" . "\r\n" .
            "CC: admin@example.com";
            eval('mail("webmaster@hashable.local","Website Message","'.$_POST["message"].'",$headers);');
            print 'Message successfully sent!';
          }
				}catch(Error $e){
					print 'Error in: '.$e->getFile().'<br/>';
					print 'Message: '.$e->getMessage().'<br/>';
				}	
      }
?>

