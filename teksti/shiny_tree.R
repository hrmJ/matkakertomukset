#
library(yaml)
l <- yaml.load_file("tree1.yaml")
library(data.tree)
jl <- as.Node(l)
#Plotting
library(igraph)
library(ape)
jl$Revert()
jlp <- as.phylo(jl)

library(igraph)
G <- graph.tree(n=13,children=2)

# let's print it using a tree-specific layout 
# (N.B. you must specify the root node)
co <- layout.reingold.tilford(G, params=list(root=1)) 
plot(G, layout=co)



acme <- Node$new("Acme Inc.")
  accounting <- acme$AddChild("Accounting")
    software <- accounting$AddChild("New Software")
    standards <- accounting$AddChild("New Accounting Standards")
  research <- acme$AddChild("Research")
    newProductLine <- research$AddChild("New Product Line")
    newLabs <- research$AddChild("New Labs")
  it <- acme$AddChild("IT")
    outsource <- it$AddChild("Outsource")
    agile <- it$AddChild("Go agile")
    goToR <- it$AddChild("Switch to R")

print(acme)



ti <- Node$new("Topic indicators")
    do <- ti$AddChild("dobj")
        va <- do$AddChild("Verb=hankkia/etsiä/etc")
            fp <- va$AddChild("First person")
                fp$AddChild("Asumisen järjestin itselleni jo Suomesta käsin. ")
                fp$AddChild("Asunnon hankin yksityiseltä vuokranantajalta, ja se oli valmiina saapuessani. ")
            va$AddChild("third person / passive")
        do$AddChild("other")
    do <- ti$AddChild("nmod")
        fp <- do$AddChild("First person")
            fp$AddChild("Kuljin rautatieasemalta metrolla yliopiston asuntolalle, missä... ")
        ot <- do$AddChild("Other")
        lc <- ot$AddChild("Locative cases")
            ela <- lc$AddChild("Elative")
                ela$AddChild("Asunnosta muodostui kriittisin osa koko vaihtoa. ")
            ila <- lc$AddChild("Illative")
                ila$AddChild("Suurin osa Pietarin vaihtareista majoittuu samaan asuntolaan, ")
            ine <- lc$AddChild("Inessive")
                ine$AddChild("Meidän lisäksi samassa asunnossa asui italialainen tyttö, jonka kanssa jaoimme vessan, suihkun ja jääkaapin. ")
        ot <- do$AddChild("Asunnon suhteen / kanssa")
            ot$AddChild("Minulla kävi tuuri asunnon kanssa, sillä eräs tuttuni omistaa asunnon Berliinissä. ")
    do <- ti$AddChild("")


print(ti)

collapsibleTree(ti, fontSize=20, height=900, width=1200, linkLength=200)
collapsibleTreeNetwork(ti, fontSize=20, height=900, width=1200, linkLength=200)

simpleNetwork(tiNetwork[-3], fontSize = 15)

tiNetwork <- ToDataFrameNetwork(ti, "name")
acmeNetwork <- ToDataFrameNetwork(acme, "name")

        other:

            Rekistöröityminen paikalliseksi asukkaaksi sujui helposti,  


  accounting <- acme$AddChild("Accounting")
    software <- accounting$AddChild("New Software")
    standards <- accounting$AddChild("New Accounting Standards")
  research <- acme$AddChild("Research")
    newProductLine <- research$AddChild("New Product Line")
    newLabs <- research$AddChild("New Labs")
  it <- acme$AddChild("IT")
    outsource <- it$AddChild("Outsource")
    agile <- it$AddChild("Go agile")
    goToR <- it$AddChild("Switch to R")
