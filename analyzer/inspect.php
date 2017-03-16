<?php

session_start();
require("utils.php");
$con = new DbCon();


?>

<html lang="fi">
<head>
<meta http-equiv="Content-Type" content="text/html" charset="UTF-8">
<link rel="stylesheet" href="styles.css?id=aslkddhddj">
<script src="scripts.js"></script>
<title>Framework for annotations</title>
</head>

<body>



<section id="controls">

<form name="inspectform" method="GEST" action="inspect.php">

<span>
    Analysoija:
    <select name="performer" id="performer">
    <option> J
    <option> K
    </select>
</span>


<span>
    <input type="submit" value="Hae" name="inspsub" id="inspsub">
</span>

</form>

</section>


<?php



if(isset($_GET["inspsub"])){
    $ids=FetchTexts($con, $_GET["performer"]);
    foreach($ids as $textid){
        echo "<hr>";
        $thistext = new Text($con, $textid);
        $thistext->output();
    
    }
}


?>



<div id="themepicker">

<form name="themesetter" method="POST" action="index.php">
<?php FetchThemes($con);?>
<input type="submit" value="Tallenna" class="hidden" name="newthemebutton" id="newthemebutton">
</form>

</div>



</body>

</html>

