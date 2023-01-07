#!/usr/bin/env python
# coding: utf-8

# # Calendario
# 
# Viene qui fornito un calendario delle attività didattiche: l'elenco dei materiali da studiare ogni settimana, le scadenze per la consegna degli esercizi WarmUp, e le scadenze dei report in itinere. I compiti WarmUp assegnati vanno svolti **prima** di venire a lezione. 
# 
# **Nota:** DSpP = *Data Science per Psicologi* (la dispensa che useremo in questo insegnamento).
# 
# **Il presente calendario non è definitivo e potrà subire delle variazioni che saranno comunicate mediante l'aggiornamento di questa pagina web.**
# 
# \
# 
# <!-- ------------------------------------------------------ -->
# 
# ### `r meeting_headers[1]`
# 
# **Presentazione dell'insegnamento**
# 
# La prima settimana di lezioni include un unico incontro. In tale incontro verrà presentato il calendario didattico e verranno descritte le attività che si svolgeranno durante il semestre. Nell'ottica dell'_insegnamento capovolto_, questa prima settimana darà il tempo agli studenti di leggere il materiale didattico e di svolgere gli esercizi WarmUp relativi agli argomenti trattati nella seconda settimana di lezione, ovvero la statistica descrittiva e l'analisi esplorativa dei dati.
# 
# *Incontri di lezione ed esercitazioni pratiche #* 1
# 
# *Letture da fare questa settimana sugli argomenti che verranno trattati la settimana successiva:*  
# 
#  - DSpP capitoli 1, 2, 3, 4, 5.
#  - DSpP appendice: linguaggio $\textsf{R}$. In parallelo, suggerisco anche di consultare il testo [R for Data Science](https://r4ds.had.co.nz/index.html) (consiglio i capitoli 1, 2, 3, 9, 10, 15, 18, 20, 21).
# 
# *Compiti*: 
# 
# - Installare $\textsf{R}$ e RStudio sul proprio computer (per un tutorial, si veda il capitolo [Getting Started with R and RStudio](https://moderndive.netlify.app/1-getting-started.html) di _ModernDive_).
# - Iscriversi alla pagina Moodle dell'insegnamento.
# - Iscriversi ad un gruppo Moodle. 
# - Replicare sul proprio computer il seguente [demo](http://htmlpreview.github.io/?https://github.com/ccaudek/ds4psy_R_demos/blob/main/demos_ch03/demo03_01.html).
# - Svolgere gli esercizi 3.2.2, 3.2.3, 3.2.4, 3.3.1, 3.3.2, 3.5.3, 3.5.4, 3.6.2, 3.8.1, 5.2.1, 5.3.2, 5.4.1, 5.5.1, 5.6.1 di [R for Data Science](https://r4ds.had.co.nz/index.html) (le soluzioni sono fornite nel sito [R for Data Science: Exercise Solutions](https://jrnold.github.io/r4ds-exercise-solutions/)).
# 
# - Esercizi Warm Up [1](https://e-l.unifi.it/mod/quiz/view.php?id=823251), [2](https://e-l.unifi.it/mod/quiz/view.php?id=823252), [3](https://e-l.unifi.it/mod/quiz/view.php?id=823254), [4](https://e-l.unifi.it/mod/quiz/view.php?id=823255).
# 
# *Risorse aggiuntive*
# 
# - Vari tutorial sull'uso di $\textsf{R}$ sono forniti nella pagina [RStudio Educational](https://education.rstudio.com/learn/beginner/).
# 
# <!-- ------------------------------------------------------ -->
# 
# ### `r meeting_headers[2]`
# 
# **Statistica descrittiva e analisi esplorativa dei dati**
# 
# La statistica descrittiva è estremamente semplice e molti di voi conoscono già quasi tutti i concetti che discuteremo (media, mediana, varianza, ...). Le (poche) formule che sono presenti nella dispensa **vanno memorizzate** e le (poche) dimostrazioni algebriche discusse **vanno capite** (questo è un utile esercizio propedeutico alle dimostrazioni più complesse che incontreremo in seguito): se vogliamo capire i concetti statistici dobbiamo capire le dimostrazioni, non c'è altra strada. Una volta capiti i concetti teorici della statistica descrittiva, si pone poi un secondo problema importante: quello di sapere eseguire in pratica l'analisi dei dati. Non basta avere capito la formula della deviazione standard, ad esempio: se avete un file di dati, dovete sapere come applicare questa conoscenza utilizzando un software. È chiaro che, nel caso di dati psicologici reali, siamo sempre di fronte ad un enorme numero di osservazioni. Dunque, nessuna manipolazione di questi dati può essere fatta con metodi "carta e penna". Pertanto è necessario sapere usare un software (nel nostro caso, $\textsf{R}$) per svolgere quella che si chiama l'analisi esplorativa dei dati. Lo studio delle procedure dell'analisi esplorativa dei dati mediante software è un progetto a lungo termine: il software cambia continuamente e i problemi di analisi dei dati che ci poniamo sono sempre diversi, variano da progetto a progetto. Il nostro obiettivo qui è quello di imparare le tecniche di base: importare i dati in $\textsf{R}$, calcolare le statistiche descrittive, svolgere semplici manipolazioni di dati (per esempio, la creazione di nuove variabili), visualizzare le distribuzioni e le relazioni tra variabili. Impareremo anche ad usare $\textsf{R}$ markdown per creare un report che contiene sia testo sia il codice $\textsf{R}$.
# 
# *Incontri di lezione ed esercitazioni pratiche #* 2, 3, 4
# 
# *Letture per la settimana successiva:*  
# 
# - DSpP capitoli 6, 7, 8, 9.
# - [R for Data Science](https://r4ds.had.co.nz/r-markdown.html) capitoli 7, 8, 16, 27, 29, 30.
# 
# *Compiti*: 
# 
# - Esercizi WarmUp 
# - Replicare sul proprio computer il seguente [demo](http://htmlpreview.github.io/?https://github.com/ccaudek/ds4psy_R_demos/blob/main/demos_ch07/demo07_01.html).
# 
# *Risorse aggiuntive*
# 
# - [Introduction to Modern Statistics](https://openintro-ims.netlify.app) capitoli 4, 5.
# 
# <!-- ------------------------------------------------------ -->
# 
# ### `r meeting_headers[3]`
# 
# **Elementi di teoria delle probabilità**
# 
# La teoria delle probabilità è senza dubbio un argomento complesso, che richiede uno studio molto lungo e l'introduzione di tanti concetti. I problemi della teoria delle probabilità, ad esempio quelli che richiedono il calcolo combinatorio, sono tra i problemi più complessi che si possono immaginare. I matematici più geniali della storia dell'umanità hanno compiuto numerosi errori nel tentativo di risolvere problemi di questo tipo. Il nostro obiettivo qui non è quello di sviluppare una conoscenza più o meno approfondita dei temi del calcolo delle probabilità, ma solo quello di capire i concetti necessari all'analisi dei dati psicologici. Quindi, gli esercizi di calcolo delle probabilità che incontreremo saranno (relativamente) semplici, dato che avranno quale unico obiettivo quello di chiarire il significato delle nozioni di base della teoria delle probabilità. Tali concetti (ad esempio, la densità di probabilità, il valore atteso, la probabilità congiunta, condizionata, marginale, ecc.) ci forniscono il linguaggio nei termini del quale si articola la discussione dell'inferenza statistica. Ma quanta matematica / teoria delle probabilità dobbiamo conoscere per il nostro scopo, ovvero l'analisi dei dati psicologici? Una possibile risposta è stata fornita da Andrew Gelman: _"If you wanted to do foundational research in statistics in the mid-twentieth century, you had to be a bit of a mathematician, whether you wanted to or not ... if you want to do statistical research at the turn of the twenty-first century, you have to be a computer programmer."_ In altre parole, non è necessaria una conoscenza molto approfondita dell'analisi matematica e della teoria delle probabilità; molto più utili sono invece le competenze computazionali e algoritimiche. Dunque, selezioneremo dalla teoria delle probabilità solo quegli strumenti che risultano utili (e necessari) ai nostri scopi, senza troppi approfondimenti. Invece, utilizzeremo da subito un approccio algoritmico, perché questo sarà il metodo che verrà impiegato nella trattazione degli argomenti successivi.
# 
# *Incontri di lezione ed esercitazioni pratiche #* 5, 6, 7
# 
# *Letture per la settimana successiva:*  
# 
#  - DSpP capitoli 10, 11, 12, 13
# 
# *Compiti*: 
# 
# - **Relazione in itinere 1:** 
#   - leggere l'articolo di riferimento;
#   - importare i dati degli autori in $\textsf{R}$;
#   - creare un un file RMarkdown che include alcune statistiche descrittive sui dati forniti dagli autori dell'articolo scelto.
# 
# 
# *Risorse aggiuntive*
# 
# - Espresso in forma sintetica, tutto ciò che c'è da sapere sugli argomenti discussi questa settimana è presentato in questa [pagina web](https://ermongroup.github.io/cs228-notes/preliminaries/probabilityreview/).
# - I materiali di [ Introduction to Probability and Statistics](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/readings/) sono fatti benissimo (qualche anno fa, questo è stato giudicato come il migliore insegnamento undergraduate del MIT!). La trattazione degli argomenti di teoria delle probabilità è molto simile a quella della dispensa. Noi approfondiremo un po' di più i temi dell'inferenza bayesiana -- invece trascureremo quasi del tutto l'approccio frequentista (che reputo obsoleto).
# 
# <!-- ------------------------------------------------------ -->
# 
# ### `r meeting_headers[4]`
# 
# **Distribuzioni di densità e modellizzazione bayesiana**
# 
# Questa settimana introdurremo le distribuzioni di densità di probabilità. Tra esse, la più importante è certamente la gaussiana. Ma non c'è molto da capire sulla gaussiana: c'è una formula che definisce una famiglia di curve che hanno alcune proprietà. Impareremo ad usare $\textsf{R}$ per disegnare una tale curva e per calcolare alcune caratteristiche di essa, come ad esempio l'area sottesa alla curva in un intervallo. Non c'è niente di particolarmente difficile in tutto questo.  Nell'appendice della dispensa è fornita una breve discussione della relazione tra distribuzione gaussiana e il metodo dei minimi quadrati. Quella discussione illustra l'eleganza della teoria della probabilità e suggerisce come, dietro la semplicità apparente della trattazione nella dispensa, c'è in realtà molto di più di quello che appare a primo sguardo. Ma questi temi non fanno parte del programma d'esame: li presento solo come una curiosità.  Un maggiore sforzo andrà invece diretto alla distribuzione Beta (e alle funzioni beta e gamma). Non perché la distribuzione Beta sia molto importante (la gaussiana lo è enormemente di più), ma perché questa distribuzione ci consentirà di capire come ottenere _per via analitica_ la distribuzione a posteriori quando i dati sono costituiti da una proporzione. La distribuzione Beta ci consentirà anche, in una particolare circostanza, di risolvere in forma analitica (e sarà l'unico caso di questo tipo che discuteremo) l'integrale che si trova a denominatore nel rapporto di Bayes. Per ottenere questi risultati è però necessario conoscere nei dettagli le proprietà della distribuzione Beta. Per cui ad essa dovrà essere rivolta un'attenzione particolare. Questa settimana verrà anche introdotta la funzione di verosimiglianza. Questo concetto non presenta alcuna difficoltà. Il modo più semplice per capire cosa significa "verosimiglianza" è quello di fare una simulazione. Dunque a questo punto del semestre gli studenti dovranno avere capito e dovranno sapere usare il ciclo `for` e l'aritmetica vettorializzata in $\textsf{R}$. 
# 
# *Incontri di lezione ed esercitazioni pratiche #* 8, 9, 10
# 
# *Letture per la settimana successiva:*  
# 
#  - DSpP capitoli 14, 15, 16, 17
# 
# *Compiti*: 
# 
# - Installazione di `cmdstanr`.
# 
# *Risorse aggiuntive*
# 
# - Shiny app per la [distribuzione beta](https://github.com/ccaudek/ds4psy_R_demos/blob/main/demos_ch13/beta_distr.R).
# - Le video-registrazioni di Richard McElreath basate sul suo famoso libro [Statistical rethinking](https://github.com/rmcelreath/stat_rethinking_2022) forniscono sicuramente la migliore introduzione alla statistica bayesiana. Il libro (ora nella seconda edizione) ha avuto uno straordinario successo. Non l'ho adottato perché è ad un livello troppo avanzato per un primo insegnamento di statistica per psicologi. Tuttavia, la parte iniziale del libro copre gli stessi argomenti che discutiamo anche noi: fortemente consigliata! 
# 
# <!-- ------------------------------------------------------ -->
# 
# ### `r meeting_headers[5]`
# 
# **Distribuzioni a priori coniugate; l'influenza della distribuzione a priori**
# 
# L'inferenza bayesiana richiede la soluzione di un'equazione che, a denominatore, contiene un integrale che, in generale, non è risolvibile per via analitica. Un caso a parte è quello nel quale la verosimiglianza viene combinata con una distribuzione a priori tale per cui la distribuzione a posteriori è della stessa famiglia della distribuzione a priori. Esamineremo qui il caso più semplice, ovvero lo schema beta-binomiale. Ci porremo anche il problema di capire qual è l'effetto della distribuzione a priori sulla distribuzione a posteriori. Dato che la distribuzione a priori è arbitraria, l'influenza della distribuzione a priori sulla distribuzione a posteriori rappresenta l'aspetto più controverso della stastistica bayesiana. Ma le cose stanno veramente così? L'arbitrarietà della distribuzione a priori rappresenta il limite maggiore della statistica bayesiana? Oppure può essere interpretato come uno dei punti di forza più grandi di questo approccio?
# 
# *Incontri di lezione ed esercitazioni pratiche #* 11, 12, 13
# 
# *Letture per la settimana successiva:*  
# 
#  - DSpP capitoli 18, 19, 20
# 
# *Compiti*: 
# 
# *Risorse aggiuntive*
# 
# - [Bayes Rules!](https://www.bayesrulesbook.com/chapter-3.html) capitolo 3.
# 
# <!-- ------------------------------------------------------ -->
# 
# ### `r meeting_headers[6]`
# 
# **Stima della distribuzione a posteriori**
# 
# In generale, la distribuzione a posteriori non può essere determinata per via analitica, ma solo per via numerica. Questa settimana ci porremo la seguente domanda: come è possibile approssimare numericamente la forma di una distribuzione _che non conosciamo_? Questo sembra magico: è possibile descrivere in maniera numerica, con un livello arbitrario di precisione, la forma di una distribuzione sconosciuta. Esamineremo nei dettagli due metodi che rendono "meno magica" la soluzione a questo problema: i metodi basati su griglia e i metodi di campionamento Monte Carlo basati su Catena di Markov. Ci concentreremo in particolare sul primo algoritmo che è stato usato per risolvere questo problema, ovvero l'_algoritmo di Metropolis_.
# 
# *Incontri di lezione ed esercitazioni pratiche #* 14, 15, 16
# 
# *Letture per la settimana successiva:*  
# 
#  - DSpP capitoli 
# 
# *Compiti*: 
# 
# - **Relazione in itinere 2:** completare le analisi descrittivie e replicare le analisi frequentiste svolte dagli autori;
# 
# 
# <!-- ------------------------------------------------------ -->
# 
# ### `r meeting_headers[7]`
# 
# *Incontri di lezione ed esercitazioni pratiche #* 17
# 
# - **Primo parziale**
# 
# *Letture per la settimana successiva:*  
# 
#  - DSpP capitoli 21, 22, 23
# 
# <!-- ------------------------------------------------------ -->
# 
# ### `r meeting_headers[8]`
# 
# **Introduzione al linguaggio Stan; inferenza su una proporzione**
# 
# Gli algoritmi MCMC forniscono una risposta ai problemi dell'inferenza bayesiana. Sono state proposte varie implementazioni di algoritmi che consentono di ottenere una sequenza di osservazioni che approssima da la distribuzione di probabilità a posteriori. Tali algoritmi sono più efficienti dell'algoritmo di Metropolis che abbiamo discusso. Tuttavia, quello dei campionatori è un aspetto estremamente tecnico che non verrà qui affrontato. Invece, ci porremo il problema di imparare ad usare un linguaggio probabilistico che consente di fare utilizzare uno di questi campionatori sul nostro computer. Il linguaggio probabilistico che verrà qui presentato si chiama Stan. Quale campionatore, Stan utilizza il formalismo di Hamilton, ovvero il più efficiente dei campionatori che sono stati finora proposti.
# 
# *Incontri di lezione ed esercitazioni pratiche #* 18, 19, 20
# 
# *Letture per la settimana successiva:*  
# 
#  - DSpP capitoli 24, 25, 26
# 
# *Compiti*: 
# 
# <!-- ------------------------------------------------------ -->
# 
# ### `r meeting_headers[9]`
# 
# **Il modello statistico lineare (I)**
# 
# Il modello statistico lineare costituisce il fondamento di analisi statiche più complesse e, nella sua forme di base, consente di affrontare molti problemi statistici. Qui ci focalizzeremo sul confronto tra due gruppi indipendenti e sul caso del confronto tra più di due gruppi. Questo è il caso di una variabile dipendente continua e di una variabile indipendente qualitativa con due o più modalità. Il caso di una variabile dipendente continua e di una sola variabile indipendente continua costituisce il modello lineare classico. La presenza di due o più predittori continui definisce il modello di regressione multipla, mentre il caso di due o più variabili dipendenti continue definisce il caso della regressione multivariata. Nella presente trattazione faremo solo qualche accenno alla regressione multipla e non considereremo la regressione multivariata, mentre esamineremo tutti gli altri casi elencati sopra.
# 
# *Incontri di lezione ed esercitazioni pratiche #* 21, 22, 23
# 
# *Letture per la settimana successiva:*  
# 
#  - DSpP capitoli 27, 28, 29, 30
# 
# *Compiti*: 
# 
# 
# <!-- ------------------------------------------------------ -->
# 
# ### `r meeting_headers[10]`
# 
# **Il modello statistico lineare (II)**
# 
# Questa settimana presenteremo un'estensione al modello lineare che impiega una o più variabili indipendenti qualitative, con due o più modalità.  Il caso di una o più variabili indipendenti qualitative con più di due modalità definisce il cosiddetto modello ANOVA. Un'altra estensione del modello lineare classico, estremamente popolare in psicologia, è il modello gerarchico.
# 
# *Incontri di lezione ed esercitazioni pratiche #* 24, 25, 26
# 
# *Letture per la settimana successiva:*  
# 
#  - DSpP capitoli 31, 32, 33, 34
# 
# *Compiti*: 
# 
# - **Relazione in itinere 3:** impostare l'analisi bayesiana usando i dati forniti dagli autori;
# 
# *Risorse aggiuntive*
# 
# - Interessante discussione su [come NON fare una ricerca psicologica](https://statmodeling.stat.columbia.edu/2021/06/16/wow-just-wow-if-you-think-psychological-science-as-bad-in-the-2010-2015-era-you-cant-imagine-how-bad-it-was-back-in-1999/).
# 
# <!-- ------------------------------------------------------ -->
# 
# ### `r meeting_headers[11]`
# 
# **Il confronto tra modelli e selezione di variabili**
# 
# Gli ultimi argomenti che affronteremo sono quelli del contronto tra modelli e della selezione di variabili. Questi argomenti stanno al centro del dibattito contemporaneo. Sono argomenti molto complessi. La soluzione di questi problemi tramite software è semplice. Meno semplice è l'interpretazione dei risultati ottenuti. Lo scopo della discussione di questa settimana è di fornire un'introduzione a tali argomenti in maniera tale da consentire un'interpretazione dei risultati ottenuti tramite software. Di particolare importanza è il concetto di divergenza di Kullback–Leibler. 
# 
# *Incontri di lezione ed esercitazioni pratiche #* 27, 28, 29
# 
# *Compiti*: 
# 
# - Consegna del progetto di gruppo
# 
# <!-- ------------------------------------------------------ -->
# 
# ### `r meeting_headers[12]`
# 
# *Incontri di lezione ed esercitazioni pratiche #* 30, 31, 32
# 
# - **Secondo parziale**
# - **Presentazione dei progetti dei gruppi**
# 
# <!-- ------------------------------------------------------ -->
# 
