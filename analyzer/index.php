<?php

session_start();
require("utils.php");
$con = new DbCon();

?>

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

if(isset($_POST["saveannotationsbutton"]))
    SaveData($con);

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


$thistext = new Text($con,$_GET["id"]);
$thistext->output();

?>

</form>

<div id="themepicker">

<ul>
    <li OnClick="PickMe(this);">etukäteisjärjestelyt</li>
    <li OnClick="PickMe(this);">kielikurssi</li>
    <li OnClick="PickMe(this);">kohdemaahan saapuminen</li>
    <li OnClick="PickMe(this);">asuminen</li>
    <li OnClick="PickMe(this);">opiskelu</li>
    <li OnClick="PickMe(this);">muuta mainitsemisen arvoista</li>
    <li OnClick="PickMe(this);">paluu tampereelle</li>
    <li OnClick="PickMe(this);">merkityksellisyys</li>
    <li OnClick="PickMe(this);">kritiikkiä tai kiitoksia</li>
    <li OnClick="PickMe(this);">muu</li>
</ul>


</div>

</body>

</html>
