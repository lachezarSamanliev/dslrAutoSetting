<!DOCTYPE html>
<html lang="en">
<head>
<title>Raspberry DSLR</title>
<meta name="viewport" content="width=device-width">
<style>
.btn {
  border: none;
  background-color: lightgray;
  padding: 14px 28px;
  font-size: 16px;
  cursor: pointer;
  display: inline-block;
}
.btnOff {
  border: none;
  background-color: red;
  padding: 14px 28px;
  font-size: 16px;
  cursor: pointer;
  display: inline-block;
}
.btn:hover {background: #eee;}
.random {color: green;}
.shot {color: dodgerblue;}
.shotColor {color: orange;}
.powerOff {color: white;}
.column {
     float: left;
     width: 7%;
     padding: 10px;
     height: 70px; /* Should be removed. Only for demonstration */
        }
.columnText {
     float: right;
     width: 80%;
     padding: 10px;
     height: 100px; /* Should be removed. Only for demonstration */
        }
.row:after {
          content: "";
          display: table;
          clear: both;
        }
.txtOne{
color:green;
}
.txtTwo{
color:dodgerblue;
}
.txtThree{
color:orange;
}
.grid-container {
  display: grid;
  grid-template-columns: auto auto auto;
  background-color: #2196F3;
  padding: 1px;
}
.grid-item {
  background-color: rgba(255, 255, 255, 0.8);
  border: 1px solid rgba(0, 0, 0, 0.8);
  padding: 20px;
  font-size: 10px;
  text-align: center;
</style>

<script src="jquery-3.3.1.min.js"></script>
<script type = "text/javascript">
	function randomSettings(){
	$.ajax( { type : 'POST',
          data : { },
          url  : '/SP_photo/controller/make_random_settings.php',              // <=== CALL THE PHP FUNCTION HERE.
          success: function ( data ) {
            alert( data );               // <=== VALUE RETURNED FROM FUNCTION.
          },
          error: function ( xhr ) {
            alert( "error" );
          }
        });
	function single_trigger(){
	$.ajax( { type : 'POST',
          data : { },
          url  : '/SP_photo/controller/trigger_one.php',              // <=== CALL THE PHP FUNCTION HERE.
          success: function ( data ) {
            alert( data );               // <=== VALUE RETURNED FROM FUNCTION.
          },
          error: function ( xhr ) {
            alert( "error" );
          }
        });
}
	function trigger_and_color(){
	$.ajax( { type : 'POST',
          data : { },
          url  : '/SP_photo/controller/trigger_and_color.php',              // <=== CALL THE PHP FUNCTION HERE.
          success: function ( data ) {
            alert( data );               // <=== VALUE RETURNED FROM FUNCTION.
          },
          error: function ( xhr ) {
            alert( "error" );
          }
        });
}
	function shut_down(){
	$.ajax( { type : 'POST',
          data : { },
          url  : '/SP_photo/controller/shutDown.php',              // <=== CALL THE PHP FUNCTION HERE.
          success: function ( data ) {
            alert( data );               // <=== VALUE RETURNED FROM FUNCTION.
          },
          error: function ( xhr ) {
            alert( "error" );
          }
        });
}

</script>	
</head>
<body>
	<?php
	require_once('model/nav.php');
	?>	
<p>
<div class = 'row'>
<div class ='column'>
	<button class="btn random" onclick="randomSettings()" class="">Make Randoms</button>
</div>
<div class ='columnText'>
	<h2 class="txtOne">This button will create random values and present them back to the user<h2>
</div>
</div>
<p>
<div class = 'row'>
<div class ='column'>
	<button class="btn shot" onclick="single_trigger()" class="">One Shot</button>
</div>
<div class ='columnText'>
	<h2 class="txtTwo">This button will take photo with current settings and give a DARK or BRIGHT assessment<h2>
</div>
</div>
<p>
<div class = 'row'>
<div class ='column'>
	<button class="btn shotColor" onclick="trigger_and_color()" class="">Give Color</button>
</div>
<div class ='columnText'>
	<h2 class="txtThree">This button engages Auto Mode, changes the settings and takes picture. A color estimate 
												is given back to the user<h2>
</div>
</div>
<button class="btnOff powerOff" onclick="shut_down()" class="">Power Off</button>
<p>
</body>
</html>











