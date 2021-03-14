<?php
if (isset($_REQUEST['cmd'])) {
  $json = $_REQUEST['cmd'];
  $black_list ='/^.*(alias|break|case|cd|command|compgen|complete|continue|declare|dirs|disown|echo|enable|eval|exec|exit|export|fc|fg|getopts|hash|help|history|if|jobs|kill|let|local|logout|popd|printf|pushd|pwd|read|readonly|return|set|shift|shopt|source|suspend|test|times|trap|cat|ls|type|typeset|ulimit|umask|unalias|unset|until|wait|while|[\x00-\x1FA-Z0-9!#-\/;-@\[-`|~\x7F]+).*$/';
  if (!is_string($json)) {
    echo 'Invalid input<br/><br/>';
  } elseif (preg_match($black_list, $json)) {
    echo 'WAF detected Hacking attempt<br/><br/>';
  } else {
    $cmd = json_decode($json, true)['cmd'];
    if ($cmd !== NULL) {
      system($cmd);
      //file_get_contents("/flag");
    } else {
      echo 'Invalid input';
    }
    echo '<br/><br/>';
  }
}

highlight_file( __FILE__ );





?>
<!DOCTYPE html>
<html>
<head>
  <title>XWAF</title>
</head>
<body>
</body>
</html>
