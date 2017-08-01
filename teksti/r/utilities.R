
fn <- function(n,numbers=2){
    numstring <- formatC(round(n,numbers),numbers,format="f")
    return(gsub('\\.',',',numstring))
}

#Referencing tables

if(!exists("tabRef")){
    tabRef <- local({
        tag <- numeric()
        created <- logical()
        used <- logical()
        function(label, caption, prefix = options("tabcap.prefix"), sep = options("tabcap.sep"), prefix.highlight = options("tabcap.prefix.highlight")) {
            i <- which(names(tag) == label)
            if (length(i) == 0 & !missing(caption)) {
                i <- length(tag) + 1
                tag <<- c(tag, i)
                names(tag)[length(tag)] <<- label
                used <<- c(used, FALSE)
                names(used)[length(used)] <<- label
                created <<- c(created, FALSE)
                names(created)[length(created)] <<- label
            }
            if (!missing(caption)) {
                created[label] <<- TRUE
                paste0(prefix.highlight, prefix, " ", i, sep, prefix.highlight, 
                    " ", caption)
            } else {
                #In-text cross-references:
                used[label] <<- TRUE
                paste(tag[label])
            }
        }
    })
}

options(tabcap.prefix = "Table", tabcap.sep = ":", tabcap.prefix.highlight = "")


GetFractionForAnalysis <- function(deprole, d){

}

