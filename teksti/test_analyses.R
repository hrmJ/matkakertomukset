# Load the relevant model into R’s working memory:
source("r/DBDA2E-utilities.R") 
source("r/kruschke_anova.R") 
# Generate the MCMC chain:
ss <- headverbs[,c("sentence_number","pers")]
mcmcCoda = genMCMC(datFrm=ss, yName="sentence_number", xName="pers", numSavedSteps=11000, thinSteps=10)
mustacheplot <- plotMCMC(mcmcCoda,ss,"sentence_number","pers")
