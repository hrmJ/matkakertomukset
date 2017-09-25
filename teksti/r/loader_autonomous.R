library(jsonlite)
library(pander)
library(stringr)

srurce("utilities.R")
source("functions.R")

#Lataa data

headverbs <- as.data.frame(fromJSON("../../data/headverbs.json"))
genstats <- as.data.frame(fromJSON("../../data/genstats.json"))
fsstats1 <- as.data.frame(fromJSON("../../data/firstsentence.json"))

panderOptions('table.alignment.default', function(df) ifelse(sapply(df, is.numeric), 'right', 'left'))
panderOptions('table.split.table',400)
#..pandoc("analysis.md",config="r/conf.txt")

#...Note: Taking only the first indicator into account:

fsstats1$asuminen_expressed <- gsub(";.*","",fsstats1$asuminen_expressed)
fsstats1$indicatorword <- gsub(";.*","",fsstats1$indicatorword)
fsstats1$head_of_indicator <- gsub(";.*","",fsstats1$head_of_indicator)
fsstats1$head_of_indicator_loc <- gsub(";.*","",fsstats1$head_of_indicator_loc)
fsstats1$indicatorloc <- gsub(";.*","",fsstats1$indicatorloc)
fsstats1$indicatorword_case <- gsub(".*Case=(\\w+).*","\\1",fsstats1$indicatorword_feat)


fsstats1$indicator_ratio  <- round(fsstats1$indicatorwords / fsstats1$words_total * 100,0)

fsstats1$headverb_person_simple <- "--"
fsstats1$headverb_person_simple[grepl("1",fsstats1$headverb_person)] <- "1p"
fsstats1$headverb_person_simple[grepl("3",fsstats1$headverb_person)] <- "3p"
fsstats1$headverb_person_simple[which(fsstats1$headverb_person=="")] <- "--"
fsstats1$indicatorword_length <-  str_length(fsstats1$indicatorword_token) 

write.csv(fsstats1,"updated_data.csv")

withindicator <- subset(fsstats1,asuminen_expressed!="None")
withindicator$indicator.deprel <- factor(withindicator$asuminen_expressed,levels=unique(names(sort(table(withindicator$asuminen_expressed),d=T))))

deprels <- list(dobj = list(df=subset(withindicator,asuminen_expressed=="dobj")),
                root   = list(df=subset(withindicator,asuminen_expressed=="root")),
                nsubj  = list(df=subset(withindicator,asuminen_expressed=="nsubj")),
                nmposs = list(df=subset(withindicator,asuminen_expressed=="nmod:poss")),
                nscop  = list(df=subset(withindicator,asuminen_expressed=="nsubj:cop")),
                xcomp  = list(df=subset(withindicator,asuminen_expressed=="xcomp")),
                nmod   = list(df=subset(withindicator,asuminen_expressed=="nmod")),
                gobj   = list(df=subset(withindicator,asuminen_expressed=="nmod:gobj")),
                props  = round(100*prop.table(sort(table(withindicator$indicator.deprel),d=T)))
                )
for(deprel in names(deprels)){
    if(deprel != "props"){
        deprels[[deprel]] <- VerbInfo(deprels[[deprel]])
        deprels[[deprel]]$indicatorprops <- round(100*prop.table(table(deprels[[deprel]]$df$indicatorword)))
    }
}


