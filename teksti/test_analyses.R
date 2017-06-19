# Load the relevant model into R’s working memory:
source("r/DBDA2E-utilities.R") 
source("r/kruschke_anova.R") 
# Generate the MCMC chain:
ss <- headverbs[headverbs$number_of_paragraphs>1,c("paragraph_number","number_of_paragraphs","pers")]
ss$paragraph_number <- ss$paragraph_number/ss$number_of_paragraphs
yName="paragraph_number";xName="pers"
#ss$sentence_number <- headverbs$sentence_number/headverbs$number_of_sentences
mcmcCoda = genMCMC(datFrm=ss, yName=yName, xName=xName, numSavedSteps=11000, thinSteps=10)
plotMCMC(mcmcCoda,ss,yName,xName)


