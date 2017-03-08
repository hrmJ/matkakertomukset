
<html lang="fi">
<head>
<meta http-equiv="Content-Type" content="text/html" charset="UTF-8">
<link rel="stylesheet" href="styles.css">
<script src="scripts.js"></script>
<title>Framework for annotations</title>
</head>

<body>

<form name="performer" method="POST" action="index.php?id=49">

<section id="controls">

<span>
    Yhteensä tehty x / y
</span>

<?php

session_start();
$jselected = "";
$kselected = "";

#Valitse analysoijan nimi per sessio
if (isset( $_POST['performer']))
    $_SESSION['performer'] = $_POST["performer"];
else
    $_SESSION['performer'] = "J";

if($_SESSION['performer']=="J")
    $jselected = "selected";
else
    $kselected = "selected";


?>

<span>
    Analysoija:
    <select name="performer" id="performer">
    <option <?php echo $jselected;?>> J
    <option <?php echo $kselected;?>> K
    </select>
</span>

<span>
    Seuraava teksti
</span>

<span>
    <input type="submit" value="Tallenna" name="saveannotationsbutton" id="saveannotationsbutton">
</span>

</section>


<?php


require("utils.php");

$con = new DbCon();
$thistext = new Text($con,$_GET["id"]);
$thistext->output();

var_dump($_POST);
?>

</form>

</body>

</html>
