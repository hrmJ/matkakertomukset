<?php

session_start();
require("utils.php");
$con = new DbCon();
ReleaseLocks($con);


?>

<html lang="fi">
<head>
<meta http-equiv="Content-Type" content="text/html" charset="UTF-8">
<link rel="stylesheet" href="styles.css?id=aslkddhddj">
<script src="scripts.js"></script>
<title>Framework for annotations</title>
</head>

<body>

<form name="performer" method="POST" action="index.php">


<section id="controls">


<span>
<?php
if(isset($_POST["saveannotationsbutton"]))
    SaveData($con);
PrintStatus($con);
?>
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

#Lataa tekstin id
if(isset($_GET["id"]))
    $textid = $_GET["id"];
elseif(isset($_POST["saveannotationsbutton"]))
    $textid = $_POST["textid"];
else
    $textid = FetchTextId($con);

$res = $con->select("textmeta",Array("ispractice"),Array(Array("id","=",$textid)),"","")->fetch();
$ispractice = $res[0];
if($ispractice=='on')
    $ispractice = " checked='checked' ";
else
    $ispractice = "";

?>

<span>
    Analysoija:
    <select name="performer" id="performer">
    <option <?php echo $jselected;?>> J
    <option <?php echo $kselected;?>> K
    </select>
</span>

<span>
    <a href="javascript:void(0)" onClick="NewText();">Lataa uusi teksti</a>
</span>

<span>
    <input type="submit" value="Tallenna" name="saveannotationsbutton" id="saveannotationsbutton">
</span>

<span> Tekstin tunnistenumero: <?php echo $textid; ?> </span>
<span> <a href='javascript:void(0)' onClick="LoadById();">Lataa teksti tunnisteen perusteella: </a><input type="text" name="loadtextbyid" id="loadtextbyid" value="" placeholder=""></input> </span>
<span> <input id="ispractice" name="ispractice" type="checkbox" <?php echo $ispractice;?>>aiheena HARJOITTELU eikä vaihtoopiskelu</input></span>
   
</section>


<?php


$thistext = new Text($con, $textid);
$thistext->output();

?>


</form>

<div id="themepicker">
    <input id="uncertain" onChange="MarkCertainty(this, '<?php echo $_SESSION['performer'] ?>');"type="checkbox">Olen epävarma</input>
    <ul id="themelist">
        <li OnClick="PickMe(this);">Etukäteisjärjestelyt</li>
        <li OnClick="PickMe(this);">Asuminen</li>
        <li OnClick="PickMe(this);">Hinnat</li>
        <li OnClick="PickMe(this);">Merkityksellisyys</li>
    </ul>
</div>

<form name="textidsaver" method="POST" action="index.php" class="hidden">
    <input type="text"  value="<?php echo $textid;?>" name="textid">
    <input type="submit" value="Tallenna" name="fetchtextbutton" id="fetchtextbutton">
</form>


</body>

</html>

