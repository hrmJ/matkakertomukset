ClassifyWords <- function(mydf,path,sourcecol,targetcol){
    types <- setNames(lapply(paste(path,list.files(path),sep=""),function(x) return (unname(as.vector(readLines(x))))),gsub(".txt","",list.files(path)))
    types.df <- data.frame(token=c(),type=c())
    for(type in names(types)){
        types.df <- rbind(types.df, data.frame(token=types[[type]],type=type))
    }
    types.df$token <- as.character(types.df$token)
    mydf[[targetcol]] <- sapply(mydf[[sourcecol]],function(x,vt){
                                 classified <- vt$type[which(vt$token==x)]
                                 if(x %in% vt$token){
                                     return(as.character(classified[1]))
                                 }
                                 return("other")
                                    }
                                 ,vt=types.df)
    return(mydf)
}


ClassifyVerbs <- function(mydf){
    path="../data/verbs_fi/"
    verbtypes <- setNames(lapply(paste(path,list.files(path),sep=""),function(x) return (unname(as.vector(read.table(x))))),gsub(".txt","",list.files(path)))
    vtypes.df <- data.frame(lemma=c(),verbtype=c())
    for(type in names(verbtypes)){
        vtypes.df <- rbind(vtypes.df, data.frame(lemma=verbtypes[[type]],verbtype=type))
    }
    vtypes.df$verbtype <- as.character(vtypes.df$verbtype)
    mydf$verbtype <- sapply(mydf$headverb_lemma,function(x,vt) return(ifelse(x %in% vt$lemma,vt$verbtype[which(vt$lemma==x)],"other")),vt=vtypes.df)
    return(mydf)
}


VerbInfo <- function(mylist){
    mylist$df <- ClassifyVerbs(mylist$df)
    mylist$df$headverb_person[grepl("(olin|pääsin|aloin) ",mylist$df$sentence, ignore.case=T) & mylist$df$headverb_person=="--"] <- "Sing.1"

    mylist$df$headverb_person  <- gsub("(Plur|Sing)\\.","",mylist$df$headverb_person)
    mylist$df$headverb_person[mylist$df$headverb_person==""] <- "--"
    mylist$df$verbtype[grepl("(etsimään|etsiä|etsimisessä|etsin)",mylist$df$sentence)] <- "searching"
    mylist$df$verbtype[mylist$df$verbtype=="coming"] <- "other"
    mylist$df$verbtype[mylist$df$verbtype=="searching"] <- "aquiring"

    mylist$verbs <- list(count=sort(table(mylist$df$verbtype)))
    mylist$verbs$prop <- round(prop.table(mylist$verbs$count)*100,0)
    mylist$pers.bytype <- list(count=xtabs(~verbtype + headverb_person, data=mylist$df))
    mylist$pers.bytype$prop  <- round(prop.table(mylist$pers.bytype$count,1)*100,0)
    mylist$pers <- list(count=xtabs(~headverb_person, data=mylist$df))
    mylist$pers$prop  <- round(prop.table(mylist$pers$count)*100,0)
    return(mylist)
}

