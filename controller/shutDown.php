<?php

function bb(){
$c = exec('sudo shutdown -h now', $output);
echo $c;
print_r($output);
}
bb();
?>
