<div class="head info">
  <div class="containerOne">
    <p class="lead">Raspberry DSLR controller</p>
    <hr class="my-4" style="background-color: white">
  </div>
</div>
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
}
.topnav {
  overflow: hidden;
  background-color: #cccccc;
}
.topnav a {
  float: left;
  color: #333333;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}
.topnav a:hover {
  background-color: #ddd;
  color: black;
}
.topnav a.active {
  background-color: #4CAF50;
  color: white;
}
</style>
</head>
<body>
<div class='topnav'>
<a class='active' href='index.php'>Camera</a>
<a href='../../gallery/index_two.html'>Gallery</a>
<a href='redGallery.php'>Red Photos</a>
<a href='greenGallery.php'>Green Photos</a>
<a href='blueGallery.php'>Blue Photos</a>
<?php
$battery_value = exec('python3 /var/www/html/SP_photo/controller/battery.py', $ouput);
echo "<li style='float: right' class='nav-item active'><a class='nav-link'> Battery Level is: $battery_value </a></li>";
?>
</div>
</body>
</html>
