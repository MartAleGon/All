<!DOCTYPE html>
<html land="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- Latest compiled and minified CSS -->
<link rel="stylesheet"href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
<!-- jQuery library -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
<!-- Latest compiled JavaScript -->
<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>

<link rel="stylesheet" href="reveal.css"/>

for (var i=0; i<final_image.data.length; i+=4) {
  // make the vertical gradient red
  var v = Math.abs(vertical.data[i]);
  final_image.data[i] = v;
  // make the horizontal gradient green
  var h = Math.abs(horizontal.data[i]);
  final_image.data[i+1] = h;
  // and mix in some blue for aesthetics
  final_image.data[i+2] = (v+h)/4;
  final_image.data[i+3] = 255; // opaque alpha
}
