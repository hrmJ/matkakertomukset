


### Yleisiä tilastoja

Kaiken kaikkiaan teksteistä voidaan antaa seuraavat yleiset tiedot:

* Tekstejä ylipäätään: 492
* Tekstejä, joissa ei käsitellä asumista  ollenkaan: 75
* Tekstejä, joissa 1 kpl asumista: 284
* Tekstejä, joissa 2 kpl asumista: 81
* Tekstejä, joissa 3 kpl asumista: 29
* Tekstejä, joissa enemmän kuin 3 kpl asumista: 23
* Asumista käsitteleviä kappaleita yhteensä: 643


### Tilastoja pääverbeistä


Katsotaan yleisesti jotakin, mitä pääverbeistä voisi saada irti.
Jos otetaan

* tekstistä riippumatta kaikki kappaleet, jossa käsitellään asumista, 
* näistä kappaleista jokainen virke erikseen
* virkkeestä irti se, mikä on virkkeen ROOT-elementti

saadaan tulokseksi, että 20 suosituinta verbiä ovat:


```
## Error in `colnames<-`(`*tmp*`, value = c("Lemma", "Frekvenssi")): 'names' attribute [2] must be the same length as the vector [1]
```



|           | hvtab[order(hvtab, decreasing = T)][1:20]|
|:----------|-----------------------------------------:|
|olla       |                                      1578|
|asua       |                                       239|
|saada      |                                       187|
|kannattaa  |                                       175|
|maksaa     |                                       114|
|suositella |                                       114|
|l�yt��     |                                        88|
|tulla      |                                        74|
|sijaita    |                                        71|
|l�yty�     |                                        68|
|k�yd�      |                                        66|
|ei         |                                        63|
|jakaa      |                                        53|
|hankkia    |                                        39|
|p��st�     |                                        38|
|hakea      |                                        33|
|tarjota    |                                        33|
|tehd�      |                                        33|
|ottaa      |                                        32|
|vuokrata   |                                        32|

Tämä ei tietysti vielä ole millään tavalla hyödyllistä, mutta antaa
jonkinlaista yleiskuvaa siitä, että samat verbit todella kiertävät teksteissä.

Periaatteessa pääverbejä voisi eritellä luokkiin, niin että luokkia olisivat 
esimerkiksi *staattiset verbit*, *evaluoivat verbit* yms., jolloin näistä voisi 
saada jotakin mielekkäämpää aikaan.


Pohditaan seuraavaksi sitä, mihin kohtaan kappaletta yleensä sijoittuvat 
ensimmäisessä persoonassa esiintyvät verbit, mihin kohtaan toisessa ja niin edelleen.



```
## `stat_bin()` using `bins = 30`. Pick better value with `binwidth`.
```

![plot of chunk 1partexts](figure/1partexts-1.png) 
