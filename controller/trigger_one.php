<?php
function trigger_one(){
	$result = exec('sudo python3 /var/www/html/SP_photo/controller/taking_photo.py 2>&1', $output);
	print_r($result);
}
trigger_one();
?>
