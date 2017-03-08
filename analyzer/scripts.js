var currentparagraph = undefined;

function PickTheme(el){
    var picker = document.getElementById("themepicker");
    if(currentparagraph !== undefined){
        var previous = document.getElementById(currentparagraph);
        var prevtheme = previous.getElementsByTagName("input")[0].value;
        if(prevtheme==""){
            document.getElementById(currentparagraph).className = "themeparagraph unanalyzed";
        }
        else{
            document.getElementById(currentparagraph).className = "themeparagraph analyzed";
        }
    }

    if(picker.style.display=="block" && el.id == currentparagraph){
        picker.style.display="none";
        var prevtheme = previous.getElementsByTagName("input")[0].value;
        if(prevtheme==""){
            el.className = "themeparagraph unanalyzed";
        }
        else{
            el.className = "themeparagraph analyzed";
        }
    }
    else{
        el.className = "themeparagraph current";
        picker.style.display="block";
        var pickedtheme = el.getElementsByTagName("input")[0].value;
        currentparagraph = el.id;

        var themelist = picker.getElementsByTagName("li");
        for(var i=0;i<themelist.length;i++){
            var li = themelist[i];
            li.className = "unpicked";
            if(themelist[i].textContent==pickedtheme){
                li.className = "picked";
            }
        }
    }
}

function PickMe(el){
    var thisp = document.getElementById(currentparagraph);
    thisp.getElementsByTagName("input")[0].value = el.textContent;
    var items = el.parentNode.children;
    for(var i=0;i<items.length;i++){
        items[i].className="unpicked";
    }
    el.className="picked";
    document.getElementById("themepicker").style.display="none";
    thisp.className = "themeparagraph analyzed";
}

