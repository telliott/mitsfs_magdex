#!/usr/bin/python3

def head(): 
	return """
<html>
<head>

	<link rel="stylesheet" href="/css/mitsfs.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.3/jquery.min.js"></script>
	<script>
		$(document).ready(function() {
			$("#nav-placeholder").load("/header.html")
		})
		$(document).ready(function() {
			$("#footer-placeholder").load("/footer.html")
		})
	</script>
	<style>td {padding: 15px;} th {padding: 15px;}</style>
</head>
<body>
  <div id="nav-placeholder"></div>   

<div class="main">
"""


def foot():
	return """</div>

<div id="footer-placeholder"></div>
  </body>
</html>
"""

