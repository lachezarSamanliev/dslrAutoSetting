
<?php

session_start();
function put_image_and_info($name, $shutter, $aperture, $iso){
	$filepath = '../gallery/';
	$temp_name = $name;
	$temp_shutter = $shutter;
	$temp_aperture = $aperture;
	$temp_iso = $iso;
		$imgpath = $filepath . $temp_name;
		echo '<img src ="'.$imgpath,'" height="240" width="320"/>';
		echo ("Shutter: ". $temp_shutter. " " . "Aperture: ". $temp_aperture . " " . "ISO: ". $temp_iso);
		echo '<BR>';
}
$items = array(array(array(array(array()))));
$choice = $_SESSION["color"];
$count_lines = 0;
$init_color = 4;
$init_name_one = 5;
$init_shutter = 1;
$init_aperture = 2;
$init_iso = 3;
$fh = fopen('../gallery/colorsResults.txt','r');
while(!feof($fh)){
	$textperline = fgets($fh);
	$parts = explode(' ', $textperline);
	array_push($items, $parts[0], $parts[1], $parts[2], $parts[3], $parts[4]);
	$count_lines++;
}
fclose($fh);
for ($i = 0; $i < $count_lines; $i++){

	if (($items[$init_color] == "RED")  && ($choice == "red")){
		put_image_and_info($items[$init_name_one], $items[$init_shutter], $items[$init_aperture], $items[$init_iso]);
	}
	elseif(($items[$init_color] == "GREEN")  && ($choice == "green")){

		put_image_and_info($items[$init_name_one], $items[$init_shutter], $items[$init_aperture], $items[$init_iso]);
	}
	elseif(($items[$init_color] == "BLUE") && ($choice == "blue")){
		put_image_and_info($items[$init_name_one], $items[$init_shutter], $items[$init_aperture], $items[$init_iso]);
	}
	else{
	echo ("");
	}
	$init_color = $init_color + 5;
	$init_name_one = $init_name_one + 5;
	$init_shutter = $init_shutter + 5;
	$init_aperture = $init_aperture + 5;
	$init_iso = $init_iso + 5;
}
?>
