library(RSQLite)
con <- dbConnect(RSQLite::SQLite(), "~/data/matkakertomukset.db")
paragraphs <- dbGetQuery(con, "SELECT parsed, theme_j, theme_k, content, uncertain, theme FROM paragraphs WHERE theme_j!='' AND theme_k!='' AND content !=''")
dbDisconnect(con)
saveRDS(paragraphs, "paragraphs.RDS")
