<?php
function trigger_color(){
	$result = exec('python3 /var/www/html/SP_photo/controller/take_photo_and_color.py 2>&1', $output);
	print_r($result);
}
trigger_color();
?>
