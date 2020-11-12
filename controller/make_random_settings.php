<?php
function setting_one()
{
	$result = exec('sudo python3 /var/www/html/SP_photo/controller/make_all_randoms.py 2>&1', $output);
	print_r($result);
}
setting_one();
?>
