library(RSQLite)
con <- dbConnect(RSQLite::SQLite(), "~/data/matkakertomukset.db")
paragraphs <- dbGetQuery(con, "SELECT textid, parsed, theme, content, uncertain, theme, analyzedby FROM paragraphs WHERE theme !='' AND content !=''")
#paragraphs <- dbGetQuery(con, "SELECT content FROM paragraphs WHERE content !=''")
dbDisconnect(con)
saveRDS(paragraphs, "paragraphs.RDS")

require(stringr)
nwords <- function(string, pseudo=F){
  ifelse( pseudo, 
          pattern <- "\\S+", 
          pattern <- "[[:alpha:]]+" 
        )
  str_count(string, pattern)
}

