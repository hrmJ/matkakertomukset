


About the data
==============

* Paragraphs discussing *accommodation*

This theme was one of the topics suggested in the writing instructions for
the report. The part of the report that concerns accommodation is as follows:

    Asuminen: Oliko asunto valmiina saavuttuasi paikalle? Vuokrataso? Onko sinulla
    suosituksia asunnon hankinnassa tai muita neuvoja asumisen suhteen?


General statistical information about the data
==================================

* Total amount of texts: 492
* Texts where accommodation as a topic not discussed: 75
* Texts with 1 paragraphs about accommodation: 284
* Texts with 2 paragraphs about accommodation: 81
* Texts with 3 paragraphs about accommodation: 29
* Texts with more than 3 paragraphs about accommodation: 23
* Total number of paragraphs about accommodation: 643


Introducing the topic
=====================

First, let us take a look at how the topic (accommodation) is introduced to the
reader. 

Contrary to what at least used to be the case in English [cf. e.g. @dangelo86],
Finnish writing guides do not usually advice the writer to use special *topic
sentences*: sentences that summarize the contents of a paragraph and are most often
located at the beginning of it.

BTW, from [@smith2008braddock]:

    The third of Bain’s six rules called for a statement of topic in the initial
    sentence of the paragraph. Later scholars noted that the topic sentence could
    appear in another part of the paragraph or even be implied (Rogers, 1965).
    Furthermore, in his notable study, Braddock (1974) found that only 13% of the
    expository paragraphs in his study began with a topic sentence. Braddock’s
    study has been widely cited to support the view that reading and writing
    instruction needs to be modified to account for this fact.


However, even when there is no topic sentence *per se*, the reader must at some
point begin to have an idea about what the paragraph he is reading is about. 
When talking about accommodation, the most obvious way to indicate the topic
is, arguably, to use a word derived from the verb *asua*. Thus, we used the
asua-derivatives as *topic indicators* -- clues that indicate the reader
that the topic of the paragraph is accommodation. The data included
the following asua-derivatives:


     asunto,      asua,      asua#kokemus,      asua#ratkaisu,      opiskelija-asuntola,      asun#tola,      Kotmerckx-asuntolasta,      asunto#etsintä,      opiskelija-asunto,      asua#järjestely,      rivi#talo#asunto,      asunto#palvelu,      asunto#politiikka,      asun#tola#paikka,      asuin#paikka,      opiskelija-asunto#säätiö,      asunto#ilmoitus,      opiskelija-asunto#tila,      asunto#loka,      asunto#asia,      asunto#tarjoaja,      asua#vaihto#ehto,      asukas,      kimppa#kämppä#asua,      asua#asia,      asunto#tila,      asunto#kanava,      asua#mahdollisuus,      solu#asunto,      asunto#tarjous,      opiskelija-asuntola#huone,      asunto#saanti,      asunto#haku,      asunto#toimisto,      perhe#asunto,      asunto#mahdollisuus,      asun#tola#majoitus,      vuokra-asunto,      asunto#tarjonta,      asua#tilanne 


Interestingly enough, our data shows that out of the total 415
texts that discuss accommodation 338
(81,45 %)
use one of the aforementioned words in the **first sentence of the first paragraph that discusses 
accommodation.**


Let us now look at what these occurrences reveal about the paragraphs studied and the
writing strategies used by the authors.

Introducing strategies indicated by dependency roles
---------------------------------------------------

One way to get an idea about what kind of a strategy a writer is using to 
introduce the topic of accommodation is to look at the *dependency role*
given to the indicator word by the parser. The distribution of different dependency roles
of the topic indicators is given in table 1:[^distexpl]


|Dependency role | Frequency|
|:---------------|---------:|
|dobj            |       116|
|nmod            |        71|
|root            |        65|
|nsubj           |        41|
|nmod:gobj       |        40|
|nmod:poss       |        34|
|nsubj:cop       |        22|
|xcomp           |         9|
|conj            |         6|

Table 1: Dependency roles of topic indicators 
![plot of chunk accommodationwordstats](figure/accommodationwordstats-1.png)

[^distexpl]: The data in the table covers  the cases where the indicator
word is used in the first paragraph (in any sentence)


### Object

According to table 1 the most common dependency role is
the direct object. If we take a closer look at the cases which use a topic
indicator as the object of the first sentence, we can see that the majority of
them (75,86 %) use the word *asunto* ('apartment').
Further, if we look at the head verbs of these cases, the most frequent ones are 
the following:


----------------------------------------------------
  hankkia   etsiä   saada   löytää   hakea   hommata
--------- ------- ------- -------- ------- ---------
       20      13      12       11       7         3
----------------------------------------------------

Table 2: Head verbs of the topic indicator 'asunto' as object 

This statistical information gives us a clear pattern of one popular strategy for 
starting a paragraph about accommodation. This strategy is exemplified by sentences
@ee_yliopistonkautta and @ee_yksityisilta:

(@ee_yliopistonkautta) Asunnon hankin yliopiston kautta.
(@ee_yksityisilta) Hankin asunnon yksityisiltä markkinoilta.

Example @ee_yliopistonkautta presents a variant with the topic indicator as the
first word; example @ee_yksityisilta uses the canonical verb-initial order.
Of all the 116 sentences where the topic indicator is a direct object, 
40 (34,48 %) are cases where 
the topic indicator is the first word like in example @ee_yliopistonkautta. 

### Root

As demonstrated in table 1, direct objects are by far the most common
dependency role of topic indicators. The second dependency role with a
frequency well above all others is *root* -- that is, cases, where the topic is indicated
by the main verb of the sentence.



If we take a closer look at these cases, we can see, first of all, that
besides the most obvious option (the verb *asua*) the verbs that were
used included *majoittua* ( occurences)
*majoittaa* ( occurences)
*vuokrata* ( occurences)
and *alivuokrata* ( occurences).

Further, the data reveals that of the 59
cases with *asua*, 45 start with the verb.
The vast majority of these cases resemble example @ee_ulkopuolella in that they represent
the structure *asua* + time span + place of accommodation (the order of the
temporal and spatial arguments varies somewhat):

(@ee_ulkopuolella) Asuin koko lukuvuoden kampuksen ulkopuolella Brookfield Hallissa.

If the sentence does not begin with the verb, it is often the case that the adverbial of space
is the first constituent; another alternative is that the sentence begins with the pronoun *itse*
as in the following example:

(@ee_omassahuoneessa) Itse asuin yliopiston kampuksen asuntolassa omassa huoneessa.

The functions of these sentences are quite simple to describe: "During my stay at X I chose this kind of accommodation. 
Here's how it turned out to be: (positive / negative experiences)".

### Nsubj

Let us now look at the total 41 cases which used a nominative subject to introduce the
topic. The most common subject was, unsurprisingly, *asunto* (21 occurences). Others included 
*asuminen* (7 occurences), asuntola (4 occurences) and some unique cases such as 
*vuokrasopimus*.

Here are some examples of *asuminen*:

(@ee_asuminentapahtui) Asuminen tapahtui kampuksella asuntoloissa kahden henkilön huoneissa.
(@ee_asuminenjarjestyy) Asuminen järjestyy varsin kivuttomasti ja suhteellisen edullisesti kampuksella sijaitsevasta asuntolasta.

The examples with *asunto* represent a somewhat more heterogenous group.
If we look at the head verbs of these cases, we get the following table:


|Var1      | Freq|
|:---------|----:|
|olla      |   15|
|järjestyä |    2|
|sijaita   |    2|
|kannattaa |    1|
|kuulua    |    1|

Table 2: Head verbs of the topic indicator 'asunto' as subject 

The *olla*-cases can be grouped into a) possessive sentences like examples @ee_oliasunto and @ee_irlantiin:

(@ee_oliasunto) Minulla oli valmiiksi asunto, kun saavuin Prahaan.
(@ee_irlantiin) Minulla ei ollut asuntoa lähtiessäni Irlantiin.

and b) sentences like examples @ee_asuntovalmiina and @ee_asunnotvaihtareille:

(@ee_asuntovalmiina) Asuntoni oli valmiina heti saavuttuani paikalle.
(@ee_asunnotvaihtareille) Asunnot olivat vaihtareille valmiina, mutta saimme muuttaa niihin sisään vasta juuri ennen lukukauden alkua ja jouduimme lähtemää n niistä heti seuraavana päivänä lukukauden päättymisestä."

Other cases include the following:

(@ee_toas) Asunto järjestyi paikallisen Toas:in, Studentwerkin kautta.

Nmod:

[44] "Olimme jo Suomessa päättäneet olevamme hieman liian mukavuudenhaluisia ja suoraan sanottuna vanhoja jenkkien opiskelija-asuntoloihin."

Attempts at grouping the various ways of indicating the topic
------------------------------------------------------------

[check out this online whiteboard](https://app.ziteboard.com/?code=d977eb10-376e-4c84-a17a-ad7fac399ef0)


DOBJ
=====



------------------------------ ------------------------------ ------------------------------ ------------------------------
Aloin etsimään asuntoa heti    Itse löysin asunnon jo ennen   Ensimmäiseksi neljäksi yöksi   Otin itse asunnon             
harjoittelupaikan              vaihtoon lähtöä yliopiston     olin hankkinut huoneen         paikalliselta ” TOAS:lta ”,   
varmistuttua, joka ei          sivujen vuokrailmoituksista,   Airbnb:stä, mutta pysyvän      Seezeitilta.                  
Hollannissa niin helppoa       ja päätin luottaa siihen että  asunnon hommasin vasta                                       
ulkomaalaiselle ole.           perille päästyäni kaikki on    saavuttuani paikan päälle.                                   
                               niin kuin pitää.                                                                            

Emme olleet hankkineet asuntoa Asuntoni hommasin etukäteen,   Alkuperäisenä ajatuksenani oli Asunnon hankin yksityiseltä   
etukäteen, vain luotimme       mutta käsittääkseni suurin osa hankkia asunto vasta           vuokranantajalta, ja se oli   
siihen, että löytäisimme       löysi asunnon helposti paikan  kohteeseen saavuttuani, mutta  valmiina saapuessani.         
kimppakämpän sopuhintaan.      päältä Santiagon vaihtareiden  Facebook-ryhmien keskusteluita                               
                               Facebook-ryhmästä, joka on     seuratessani ja                                              
                               täynnä kämppäilmoituksia.      tarkastellessani joitain                                     
                                                              asuntoja välittäviä                                          
                                                              palveluita, alkoi jo elokuun                                 
                                                              aikana tuntumaan siltä, että                                 
                                                              hyvät asuntovaihtoehdot käyvät                               
                                                              nopeasti vähiin Lissabonin                                   
                                                              keskustan alueella.                                          

Saavuttuamme asuntolaamme,     Asuntoa minulla ei ollut       Itse olin varannut hostellin   Itse en saanut asuntoa        
Avant-Garden:iin, huomasimme   valmiina Sevillaan             neljäksi yöksi( 18 e /yö) ,    Studierendenwerkiltä, joten   
nopeasti mihin paholaisen      saapuessani.                   sillä tarkoituksena oli löytää jouduin etsimään sitä         
loukkuun olimme päätyneet.                                    asunto näiden päivien aikana.  yksityisiltä markkinoilta, ja 
                                                                                             eniten tuli etsittyä asuntoa  
                                                                                             wg-gesucht –sivustolta.       

Yliopistoon hakiessa voi       Asuntoa minulla ei ollut       Vietin ensimmäisen viikon      Yliopiston kautta on          
samalla hakea myös asuntoa     valmiiksi, mutta kämppäkaverit hostellissa( PILOT Hostel,     mahdollista saada asunto.     
paikalliselta                  olivat.                        voin suositella) , josta käsin                               
opiskelija-asuntosäätiöltä                                    yritin löytää asunnon                                        
SSHN:lta.                                                     itselleni.                                                   

Aloin etsiä asuntoa heti       Asunnon hankin vasta           Yritin ennen lähtöäni katsoa   Asunnon sain                  
saavuttuani                    saavuttuani paikan päälle.     netistä asuntoasiat kuntoon,   Hafenstraße-taloista          
pisocompartido.com-sivuston                                   mutta mielestäni nettisivut    paikalliselta                 
                                                              oli melko sekavia.             opiskelija-asuntojärjestöltä. 

Asuntoa minulla ei vielä ennen Asunnon olin katsonut jo       Asunnon sain tutun tutun       Aloitin asunnonhaun heti      
Brysseliin saapumista ollut,   etukäteen ja asuin kahden muun kautta, kuulin että eräällä    kesäkuun alussa sen jälkeen,  
mutta olin sopinut muutamia    vaihtaritytön kanssa Sevillan  omanikäiselläni                kun olin saanut vahvistuksen  
näyttöjä jo etukäteen.         keskustassa.                   varsovalaisella                vaihtopaikastani.             
                                                              feministi-kasvissyöjä-tyypillä                               
                                                              oli kaksiossaan juuri toinen                                 
                                                              huone vapaana.                                               

Yritin etsiä asuntoa jo        Varasin itselleni asunnon      Asunnon olin hommannut jo      Olin ottanut asuntoni         
Suomesta käsin, mutta se       Roommates Sevilla –nimisen     etukateen Suomesta kasin eraan paikallisen                   
osoittautui vaikeaksi.         välitysfirman kautta netistä   valitysfirman kautta.          opiskelija-asuntosäätiön ”    
                               jo ennen vaihtoon lähtöäni.                                   Studentenwerkin ” kautta.     

Haimme alun perin asuntoa      Majoituksen suhteen päätin,    Asunnon löysin Krakovassa      Saavuin Belgradiin hyvissä    
yliopiston asuntotoimiston     että hankin pysyvän asunnon    ollessani facebookin           ajoin ennen harjoittelun      
kautta, mutta heillä ei ollut  vasta paikan päällä.           Łódź-ryhmän avulla, jossa      alkua, jotta ehdin löytää     
tarjota meille sopivaa                                        ihmiset etsivät                asunnon.                      
asuntoa, koska emme halunneet                                 vuokra-asuntoja/ kämppiksiä.                                 
soluun.                                                                                                                    

Aloitin asunnonetsinnän noin   Asunto jokaisen on hankittava  Etsin asuntoa laittamalla      Asunnon sain jo ennen joulua, 
kaksi kuukautta ennen vaihdon  itse.                          hakuilmoituksen Pariisin       kun slovenialainen tyttö      
alkua.                                                        suomalaisten Facebook-ryhmään  ilmoitti Facebookin Erasmus   
                                                              sekä Pariisin                  Ljubljana -ryhmässä lähtevänsä
                                                              Suomi-instituutin              kevääksi vaihtoon ja          
                                                              asuntofoorumille.              vuokraavansa huoneensa täksi  
                                                                                             ajaksi.                       

Asunnon hankin yliopiston      Itse hankin asunnon jo         Asumisen järjestin itselleni   Asunnon olin hankkinut jo     
kautta.                        Suomesta käsin, asuin College  jo Suomesta käsin.             aiemmin Facebookin avulla     
                               Courtissa joka sijaitsee aivan                                yksityiseltä vuokranantajalta,
                               kampuksen kyljessä.                                           mutta tarpeellista se ei ole. 

Sain häneltä avaimet           Asuntoa minun ei tarvinnut     Hain suosiolla asuntoa CROUSin Hain jo syksyllä              
asuntolaani, johon olin        hankkia.                       opiskelija-asuntolasta, koska  asuntolapaikkaa ja sainkin    
hakenut kätevästi samalla                                     minua varoitettiin, että       paikan vaihtareille           
hakulomakkeella kuin itse                                     asunnon löytäminen omin päin   osoitetusta asuntolasta.      
yliopistoonkin ja hän ohjasi                                  on hankalaa ja hintataso                                     
minut oikeaan paikkaan.                                       kallis.                                                      

Kuulin vasta vähän ennen       Olin löytänyt asunnon          Koen olevani onnekas että sain Asunnon sain paikallisen      
lähtöä, että asunto olisi      ensimmäiseksi kuukaudeksi      asuntolapaikan juuri Résidence Toasin Apartiksen kautta.     
hommattava itse.               Airbnb:n kautta ennen Italiaan d'Amboisesta.                                                
                               saapumista.                                                                                 

Parkwood sisältää pääosin      Asunnon olin hankkinut jo      Hain yliopiston                Asuntoni sain vuokrattua      
rivitaloasuntoja ja muutaman   ennen Roomaan saapumista, mikä asuntolapaikkaa ja onnistuin   Apartiksen( paikallinen TOAS) 
kerrostalon.                   hieman hirvitti, mutta kaikki  saamaan 9 neliön suuruisen     kautta.                       
                               meni lopulta hyvin.            huoneen.                                                     

Hankin asunnon yksityisiltä    Oman asuntoni hankin           Jälkiviisaana sanoisin, että   Kuten mainittua, asunnon      
markkinoilta.                  wggesucht.de –sivustolta, ja   asunto kannattaa hankkia       hankin itse.                  
                               samaa voin suositella          ennen.                                                       
                               jokaiselle Wieniin lähtevälle.                                                              

Asuminen Kentissä on           Itse hankin asunnon jo         Asunnon hankin paikalliselta   Aloin jo loppukeväästä        
järjestetty niin että          etukäteen, ja paikallinen      opiskelija-asuntosäätiöltä(    katsella asuntomahdollisuuksia
paikalliset ekavuotiset ja     kaverini kävi sitä katsomassa  CROUS) yliopiston              Prahasta.                     
vaihtarit asuvat kampuksen     ja hakemassa avaimen jo        ilmoittautumisen yhteydessä.                                 
opiskelijakylässä tai          etukäteen.                                                                                  
collegeissa ja vanhemmat                                                                                                   
opiskelijat muuttavat                                                                                                      
lähemmäksi n. 5 kilometrin                                                                                                 
päässä sijaitsevaa Canterburyn                                                                                             
kylää.                                                                                                                     

Saapuessani ensimmäinen        Asumisen hoidin vaihtareille   Asunnon sain tosiaan kaksi     Päätimme vaihtoon             
tehtävä oli löytää oma         tarkoitetun OeAD-järjestön     viikkoa ennen opintojeni alkua lähtiessämme, ettemme halua   
asuntolani.                    kautta.                        koska minulla kävi hyvä tuuri, asuntolamajoitusta, vaan      
                                                              mutta jälkikateen mietittynä,  hoidamme itsenäisesti         
                                                              asunnon löytäminen ei pitäisi  välittäjäfirman kautta        
                                                              olla niin vaikeata, kunhan     itsellemme asunnon.           
                                                              vain osaa käyttää olemassa                                   
                                                              olevia verkostoja.                                           

Sain siis asuntolapaikan       Minua varten oli varattu       Pariisi saattaa olla monelle   Ennen Prahaan lähtöä etsimme  
automaattisesti, koska olin    asunto valmiiksi.              ulkomaalaiselle opiskelijalle  ystäväni kanssa netistä       
vaihdossa vain yhden                                          vaikea kaupunki, sillä         vuokra-asuntoja.              
lukukauden.                                                   ensimmäiseksi jokaisen                                       
                                                              tarvitsee löytää asunto.                                     

Vaihtoon haettaessa hain myös  Asuntoa oli hyvin vaikea saada Kv. koordinaattori Maggy oli   Istanbulin teknillinen        
asuntolapaikkaa, ja sain       vapailta markkinoilta etänä,   suuri apu asuntoa etsittäessä. yliopisto ei pysty tarjoamaan 
valita itse mieluisimman       sillä kukaan ei halunnut                                      asuntoa vaihto-opiskelijoille,
asuntolan( tästä myöhemmin     vuokrata minulle huonetta                                     eikä Istanbulissa ole         
lisää) .                       ainoastaan neljäksi                                           yksittäistä organisaatiota,   
                               kuukaudeksi tapaamatta                                        joka välittäisi asuntoja      
                               kasvotusten.                                                  vaihtareille.                 

Hain asuntoa yliopistolta,     Hain myös heti                 Asunnon varasin paikallista    Saavuin Istanbuliin muutamaa  
mutta koska huomasin           hyväksymiskirjeen saatuani     vuokramarkkinaa hoitavan       viikkoa ennen opiskeluiden    
tarjouskirjeen vasta niin      asuntoa Carletonin             Kopparstaden-palvelun kautta.  alkua, koska halusin löytää   
myöhään, myöhästyin yliopiston kampukselta, mutta jäin                                       asunnon hyvissä ajoin.        
asuntolahakemusten             odotuslistalle.                                                                             
deadlinesta.                                                                                                               

Asunnon hankin vasta paikan    Bishop ’ sin sivujen kautta    Tukholmaan lähtiessä kannattaa Ennen lähtöä rekisteröidyin   
päältä.                        löysin asunto- ja              pyrkiä hankkimaan asunto       www.erasmusu.com -sivulle,    
                               kämppisilmoituksia, ja päädyin mahdollisimman ajoissa, sillä  jolla voi etsiä asuntoja      
                               kolmanneksi asukkaaksi kahden  kaupungin asuntotilanne on     kaikkialta maailmasta.        
                               toisen vuoden opiskelijan      todella huono.                                               
                               kanssa.                                                                                     

Asun kaksiossa avopuolisoni    Päädyin hakemaan asuntoa       Yliopisto takaa asunnot        Saavuin Istanbuliin sateisena 
kanssa, joten minun ei         paikallisen koordinaattorin    kaikille                       keskiviikkoiltana muutama     
tarvinnut miettiä asumista     suosittelemana kampuksen       vaihto-opiskelijoille.         päivä ennen orientaatioviikon 
Suomessa.                      asuntoloista.                                                 alkua etsiäkseni asunnon ja   
                                                                                             asettautuakseni kaupunkiin.   

Asuntomme oli täysin           Asuntolaa ei tarvinnut         Asuntoa hain myös jo keväällä  Aluksi majoituin hostelliin ja
kalustettu ja vuokra piti      erikseen hakea etukäteen, vaan Uppsalasta tulleiden ohjeiden  etsin samalla asuntoa.        
sisällään wifin, sähkön ja     kaikille vaihto-oppilaille oli mukaisesti.                                                  
veden.                         varattu paikka yliopiston                                                                   
                               asuntolasta kahden hengen                                                                   
                               huoneesta.                                                                                  

Aloin katsella                 Asuntoa voi hakea BNU          Kyselimme vaihtoyliopistosta   Yliopisto tarjosi             
asuntoilmoituksia Suomessa     nettijärjestelmän kautta,      asumismahdollisuuksia, mutta   majoitusvaihtoehdoiksi        
vähän ennen lähtöäni, mutten   johon saa ohjeet               yliopisto ei voinut tarjota    asuntolaa, perhemajoitusta    
varannut vielä mitään.         hyväksymispaketin kanssa.      minkäänlaisia asuntoja         sekä apua oman vuokra-asunnon 
                                                              pariskunnille.                 etsimisessä.                  

Asunnon olin tosin etsinyt jo  CUHKin hakuvaiheessa tulee     Asunnon löysin sattuman kautta Asuntola oli tarkoitettu      
Suomesta käsin, mikä onnistui  laittaa järjestykseen          Facebookista.                  nimenomaan                    
kohdallani erityisen hyvin,    asumisvaihtoehdot, jotka ovat                                 vaihto-opiskelijoille, joten  
koska poikaystäväni asui       international house, collegen                                 siellä asui ihmisiä useista   
Barcelonassa, joten hän pystyi asuntola tai collegen asuntola                                eri maista.                   
käymään tarkistamassa asunnon. johon kuuluu "communal                                                                      
                               dinner"tiistaista torstaihin.                                                               

Etsin asunnon vasta paikan     Varasimme halvan hotellin      Asuntoa hain                   Asunnon sain järjestettyä     
päällä, sillä minulla oli      yliopiston läheltä vajaaksi    Studentendorfilta, joka        Austinista jo paria kuukautta 
kaupungissa kavereita, joiden  viikoksi ja toisena päivänä    tarjoaa Humboldtin             ennen vaihdon alkamista, ja   
luona sain viettää ensimmäiset aloimme etsimään vuokrattavaa  opiskelijoille soluasuntoja    sen hankkiminen oli myös hyvin
pari viikkoa.                  asuntoa yleisiltä              sekä yksiöitä.                 helppoa ainakin omalla        
                               markkinoilta.                                                 kohdallani.                   

Hankin asunnon ennen kuin      Opiskelijoille asuminen oli    Asunnon sain kätevästi         Totesin itse, että alle 500$  
saavuin kaupunkiin.            organisoitu dormiin nimeltä    yliopiston kautta              ei asuntoa oikein saa, ellei  
                               Gonzaga hall. Sijainniltaan    opiskelija-asuntolasta.        halua asua kamalassa luukussa 
                               asuntola oli kampuksen                                        tai kaukana kampuksesta.      
                               sisäreunalla ja hyvällä                                                                     
                               sijainnilla monellakin tapaa.                                                               

Asuntoa hankkiessa kannattaa   Sain alivuokrattua asuntoni,   Alivuokrasimme puolisoni       Asunto oli onneksi hoidettu   
miettiä, haluaako asunnon      mutta Kyprokselta en hankkinut kanssa asuntomme Berliinissä   ISEP:n puolesta, kuten myös   
läheltä yliopistoa vai läheltä asuntoa ennen sinne            oleskelun ajaksi.              ruokailu.                     
keskustaa.                     saapumistani.                                                                               

Olin etsinyt asunnon etukäteen Rupesin hyvissä ajoin          Yliopisto lähetti minulle      Asuminen vaihtareille oli     
Facebookin avulla.             kyselemään asuntoa             hyvissä ajoin                  järjestetty kampukselle.      
                               asunnonvälittäjä Wendyltä.     asuntotarjouksen.                                            

Olin katsonut Couch Surfing    Löysin asunnon SiO:n eli Oslon Ennen vaihtoon lähtöä koitimme Sama nainen auttoi minua      
palvelut Renting rooms in      opiskelijasäätiön kautta.      saada yksityisiltä             muutenkin kertomalla          
Madrid( tai jokin vastaavan                                   markkinoilta asuntoa, koska    kontaktin, jonka avulla voisin
niminen) -palstalta sopivan                                   aluksi haimme kyllä            etsiä asuntoa.                
asunnon etukäteen ja jutellut                                 opiskelija-asuntoa, mutta                                    
omistajan kanssa netissä.                                     sieltä meille tarjottiin                                     
                                                              ainoastaan omia huoneita,                                    
                                                              kaksioita ei vaihtareille                                    
                                                              tarjota.                                                     
------------------------------ ------------------------------ ------------------------------ ------------------------------






Kappaleen rajan käsittely
=========================

- Tsekkaa edellinen kappale, ja miten siinä johdateltu tulevaan aiheenvaihdokseen?
- Parempi: tsekataan tarpeen tullen -- tsekataan tietyiltä ryhmiltä







Literature
==========



