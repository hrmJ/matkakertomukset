<?php
require("dbutils.php");
require("htmlutils.php");
#$result = $con->select("textmeta",Array("id","vaihtoaika"),Array(),"","ORDER BY id")->fetchAll();
#var_dump($result);


class Text{

    public function __construct ($con, $id, $themefieldname='theme') {
        $this->id = $id;
        $chapters = $con->select("chapters",Array("id","header","text_id"),Array(Array("text_id","=",$this->id)),"","ORDER BY id")->fetchAll();
        $chapter_ids = Array();
        $this->chapters = Array();
        foreach($chapters as $chapter){
            $chapter_ids[] = $chapter["id"];
            $this->chapters[$chapter["id"]] = $chapter["header"];
        }
        $paragraphs = $con->select("paragraphs",Array("chapter_id","id","content",$themefieldname,"parsed","uncertain"),Array(Array("chapter_id",">=", min($chapter_ids)),Array("chapter_id","<=",max($chapter_ids))),"","ORDER BY chapter_id, id")->fetchAll();
        $this->paragraphs = Array();
        foreach($paragraphs as $paragraph){
            if(array_key_exists($paragraph["chapter_id"],$this->paragraphs))
                $this->paragraphs[$paragraph["chapter_id"]][] = Array("uncertain"=>$paragraph["uncertain"],"id"=>$paragraph["id"],"content"=>$paragraph["content"],"theme"=>$paragraph[$themefieldname]);
            else
                $this->paragraphs[$paragraph["chapter_id"]] = Array(Array("uncertain"=>$paragraph["uncertain"], "id"=>$paragraph["id"],"content"=>$paragraph["content"],"theme"=>$paragraph[$themefieldname]));
            #Mark each paragraph locked
            $con->update("paragraphs", Array("locked"=>1),Array(Array("id","=",intval($paragraph["id"]))));
        }
    }

    public function output(){
        $url = "index.php";
        $form = new DomEl('form','');
        $form->AddAttribute('action',$url);
        $form->AddAttribute('method','POST');
        $section = new DomEl('section','', $form);
        $section->AddAttribute('class','cont');

        foreach($this->chapters as $id => $header){
            if($header != "unnamed")
                $headerel = new DomEl('h3',$header,$section);
            foreach($this->paragraphs[$id] as $paragraph){
                if(!empty($paragraph["content"])){
                    $status = " unanalyzed";
                    if(!empty($paragraph["theme"]) AND $paragraph["theme"]!="notanalyzed")
                        $status = " analyzed";
                    $p = new DomEl('p',$paragraph["content"],$section);
                    $p->AddAttribute('id','p_' . $paragraph["id"]);
                    $p->AddAttribute('class',"themeparagraph$status");
                    $p->AddAttribute('onClick','PickTheme(this);');

                    $input = new DomEl('input',"",$p);
                    $input->AddAttribute("type","text");
                    $input->AddAttribute("value",$paragraph["theme"]);
                    $input->AddAttribute("name","theme_" . $paragraph["id"] );

                    $input = new DomEl('input',"",$p);
                    $input->AddAttribute("type","text");
                    $input->AddAttribute("value",$paragraph["uncertain"]);
                    $input->AddAttribute("name","uncertain_" . $paragraph["id"] );

                }
            }
        }

        $input = new DomEl('input',"",$section);
        $input->AddAttribute("type","text");
        $input->AddAttribute("value",$this->id);
        $input->AddAttribute("name","textid");
        $input->AddAttribute("class","hidden");
        echo $section->Show();
    }
}




function SaveData($con, $themefieldname="theme"){
    foreach($_POST as $key => $item){
        $pos = strpos($key, "theme_");
        if($pos !== false){
            $id = substr($key,6);
            #Huom: anna mahdollisuus jättää joku kappale täysin analysoimatta
            if($item=="")
                $item = "notanalyzed";
            $con->update("paragraphs", Array($themefieldname=>$item,"analyzedby"=>$_POST["performer"]),Array(Array("id","=",intval($id))));
        }
        $pos = strpos($key, "uncertain_");
        if($pos !== false){
            $id = substr($key,10);
            $con->update("paragraphs", Array("uncertain"=>$item,"analyzedby"=>$_POST["performer"]),Array(Array("id","=",intval($id))));
        }
    }
    $con->update("textmeta", Array("analyzed"=>"yes","analyzedby"=>$_POST["performer"]),Array(Array("id","=",intval($_POST["textid"]))));
}

function FetchThemes($con){
    $themes = $con->select("themes",Array("theme"),Array(),"DISTINCT","")->fetchAll();
    $ul = new DomEl('ul',"");
    $ul->AddAttribute("id","themelist");

    $li = new DomEl('li',"",$ul);
    $input = new DomEl('input',"",$li);
    $input->AddAttribute("name","newtheme");
    $input->AddAttribute("placeholder","lisää uusi kategoria");
    $input->AddAttribute("id","newthemeinput");

    $sub = new DomEl('a',"Vahvista lisäys",$li);
    $sub->AddAttribute("href","javascript:void(0)");
    $sub->AddAttribute("OnClick","AddTheme();");

    foreach($themes as $theme){
        $input = new DomEl('li',$theme[0],$ul);
        $input->AddAttribute("OnClick","PickMe(this)");
    }

    echo $ul->Show();
}

function FetchTextIdForTest($con, $bywho, $themefieldname){
    $chapter_id = $con->select("paragraphs",Array("chapter_id"),Array(Array("analyzedby","=",$bywho),Array("content","!=",""),Array($themefieldname,"=","")),"","ORDER BY id DESC LIMIT 1")->fetch();
    $chapter_id = $chapter_id[0];
    $text_id = $con->select("chapters",Array("text_id"),Array(Array("id","=",$chapter_id)),"","LIMIT 1")->fetch();
    return $text_id[0];
}


function FetchTextId($con){
    $chapter_id = $con->select("paragraphs",Array("chapter_id"),Array(Array("locked","=",0),Array("content","!=",""),Array("theme","=","")),"","ORDER BY RANDOM() LIMIT 1")->fetch();
    $chapter_id = $chapter_id[0];
    $text_id = $con->select("chapters",Array("text_id"),Array(Array("id","=",$chapter_id)),"","LIMIT 1")->fetch();
    return $text_id[0];
}

function ReleaseLocks($con){
    if(isset($_POST["fetchtextbutton"])){
        $chapter_ids = Array();
        $chapters = $con->select("chapters",Array("id"),Array(Array("text_id","=",$_POST["textid"])),"","")->fetchAll();
        foreach($chapters as $chapter){
            $chapter_ids[] = $chapter["id"];
        }
        $paragraphs = $con->update("paragraphs",Array("locked"=>0),Array(Array("chapter_id",">=", min($chapter_ids)),Array("chapter_id","<=",max($chapter_ids))));
    }
}


function PrintTestStatus($con,$performer, $max){
    $ready = $con->select("textmeta",Array("id"),Array(Array("analyzed","=","yes"),Array("analyzedby","=",$performer)))->fetchAll();
    echo "Testiaineistosta valmis: " . intval(sizeof($ready)) .  " / " . $max ;
}

function PrintStatus($con){
    $ready = $con->select("textmeta",Array("id"),Array(Array("analyzed","=","yes")))->fetchAll();
    $all = $con->select("textmeta",Array("id"),Array())->fetchAll();
    echo "Käsittelemättä noin: " . intval(sizeof($all) - sizeof($ready)) . " / " . sizeof($all);
}

#var_dump($thistext->chapters);
#
#

function FetchTextsForTest($con,$bywhom,$count=""){

    $chapter_ids = $con->select("paragraphs",Array("chapter_id"),Array(Array("analyzedby","=",$bywhom),Array("theme","=","")),"DISTINCT","")->fetchAll();
    $textids = Array();
    if($count=="")
        $count = sizeof($chapter_ids);
    foreach($chapter_ids as $cid){
        $text_id = $con->select("chapters",Array("text_id"),Array(Array("id","=",$cid[0])),"","LIMIT 1")->fetch();
        $thisid = $text_id[0];
        if(in_array($thisid,$textids)===false){
            $textids[] = $thisid;
        }
    }
    return $textids;
}

function FetchTexts($con,$bywhom,$count=""){

    $chapter_ids = $con->select("paragraphs",Array("chapter_id"),Array(Array("analyzedby","=",$bywhom)),"DISTINCT","")->fetchAll();
    $textids = Array();
    if($count=="")
        $count = sizeof($chapter_ids);
    foreach($chapter_ids as $cid){
        $text_id = $con->select("chapters",Array("text_id"),Array(Array("id","=",$cid[0])),"","LIMIT 1")->fetch();
        $thisid = $text_id[0];
        if(in_array($thisid,$textids)===false){
            $textids[] = $thisid;
        }
    }
    return $textids;
}


?>
