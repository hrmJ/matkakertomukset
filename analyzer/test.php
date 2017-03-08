<?php
require("dbutils.php");
require("htmlutils.php");
#$result = $con->select("textmeta",Array("id","vaihtoaika"),Array(),"","ORDER BY id")->fetchAll();
#var_dump($result);


class Text{

    public function __construct ($con, $id) {
        $this->id = $id;
        $chapters = $con->select("chapters",Array("id","header","text_id"),Array(Array("text_id","=",$this->id)),"","ORDER BY id")->fetchAll();
        $chapter_ids = Array();
        $this->chapters = Array();
        foreach($chapters as $chapter){
            $chapter_ids[] = $chapter["id"];
            $this->chapters[$chapter["id"]] = $chapter["header"];
        }
        $paragraphs = $con->select("paragraphs",Array("chapter_id","id","content","theme","parsed"),Array(Array("chapter_id",">=", min($chapter_ids)),Array("chapter_id","<=",max($chapter_ids))),"","ORDER BY chapter_id, id")->fetchAll();
        $this->paragraphs = Array();
        foreach($paragraphs as $paragraph){
            if(array_key_exists($paragraph["chapter_id"],$this->paragraphs))
                $this->paragraphs[$paragraph["chapter_id"]][] = Array("id"=>$paragraph["id"],"content"=>$paragraph["content"],"theme"=>$paragraph["theme"]);
            else
                $this->paragraphs[$paragraph["chapter_id"]] = Array(Array("id"=>$paragraph["id"],"content"=>$paragraph["content"]));
        }
    }

    public function output(){
        $url = "index.php";
        $form = new DomEl('form','');
        $form->AddAttribute('action',$url);
        $form->AddAttribute('method','POST');
        $section = new DomEl('section','', $form);

        foreach($this->chapters as $id => $header){
            $header = new DomEl('h3',$header,$section);
            foreach($this->paragraphs[$id] as $paragraph){
                if(!empty($paragraph["content"])){
                    $p = new DomEl('p',$paragraph["content"],$section);
                    $p->AddAttribute('id','p_' . $paragraph["id"]);
                    $p->AddAttribute('class','themeparagraph');
                    $p->AddAttribute('onClick','PickTheme(this);');

                    $input = new DomEl('input',"",$p);
                    $input->AddAttribute("type","text");
                    $input->AddAttribute("value",$paragraph["theme"]);
                    $input->AddAttribute("name","theme_" . $paragraph["id"] );
                }
            }
        }
        echo $section->Show();
    }
}



$con = new DbCon();
$thistext = new Text($con,49);
$thistext->output();
#var_dump($thistext->chapters);

?>
