
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
