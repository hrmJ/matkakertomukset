
<html lang="fi">
<head>
 <link rel="stylesheet" href="../font-awesome-4.6.3/css/font-awesome.min.css">
<link href="https://fonts.googleapis.com/css?family=Nothing+You+Could+Do|Quicksand" rel="stylesheet">
<meta http-equiv="Content-Type" content="text/html" charset="UTF-8">
<link rel="stylesheet" href="tyylit2.css">
<title>Majakkamessu</title>
</head>

<body>

<?php
require("utils.php");

$con = new DbCon();
$thistext = new Text($con,49);
$thistext->output();

?>

</body>

</html>
