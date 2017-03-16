<?php

session_start();
require("utils.php");
$oldcon = new DbCon("sqlite:dbfolder/matkakertomukset_old.db");
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

</section>


<?php

if(isset($_POST["saveannotationsbutton"]))
    $textid = $_POST["textid"];
else{
    $textid=FetchTextIdForTest($con,"K");
}

$thistext = new Text($con, $textid);
$thistext->output();

?>


</form>

<div id="themepicker">

<form name="themesetter" method="POST" action="ktesti.php">
<?php FetchThemes($con);?>
<input type="submit" value="Tallenna" class="hidden" name="newthemebutton" id="newthemebutton">
</form>

</div>

<form name="textidsaver" method="POST" action="ktesti.php" class="hidden">
    <input type="text"  value="<?php echo $textid;?>" name="textid">
    <input type="submit" value="Tallenna" name="fetchtextbutton" id="fetchtextbutton">
</form>


</body>

</html>

