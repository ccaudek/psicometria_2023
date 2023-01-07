# ✅ Distribuzione Normale

```{exercise}
:label: label-distributions-gauss-01

Lo Scholastic Aptitude Test (SAT) è un test attitudinale richiesto per
l'ammissione ai college degli Stati Uniti. I punteggi SAT si distribuiscono normalmente
con media 500 e deviazione standard 100. Supponiamo che un college ammetta soltanto
studenti che ottengono punteggi nel 15 percento superiore della
distribuzione. Qual è il punteggio minimo per potere essere ammessi?
```

````{solution} label-distributions-gauss-01
:class: dropdown

```{code-block} python
import scipy.stats as st

st.norm.ppf(0.85, 500, 100)
```
La soluzione è 603.643338949379.
````

+++

```{exercise}
:label: label-distributions-gauss-02

Lo Scholastic Aptitude Test (SAT) è un test attitudinale richiesto per
l'ammissione ai college degli Stati Uniti. I punteggi SAT si distribuiscono normalmente
con media 500 e deviazione standard 100. Supponiamo che John Doe ottenga un punteggio
pari a 628.  Se vengono presentate 900 domande di ammissione, ci possiamo aspettare
che il numero di studenti con un punteggio superiore a quello di John Doe sia
approssimativamente uguale a:
```

````{solution} label-distributions-gauss-02
:class: dropdown

```{code-block} python
import scipy.stats as st

(1 - st.norm.cdf(628, 500, 100)) * 900
```
La soluzione è 90.
````

+++

```{exercise}
:label: label-distributions-gauss-03

Lo Scholastic Aptitude Test (SAT) è un test attitudinale richiesto per
l'ammissione ai college degli Stati Uniti. I punteggi SAT si distribuiscono normalmente
con media 500 e deviazione standard 100. Supponiamo che ad un college facciano
domanda di ammissione 800 candidati.  Ci possiamo aspettare che il seguente
numero di candidati ottenga un punteggio compreso tra 550 e 600:
```

````{solution} label-distributions-gauss-04
:class: dropdown

```{code-block} python
import scipy.stats as st

(st.norm.cdf(600, 500, 100) - st.norm.cdf(550, 500, 100)) * 800
```

La soluzione è 120 (119.90).
````

+++

```{exercise}
:label: label-distributions-gauss-04

Viene creato un test per misurare il livello di motivazione degli studenti
delle scuole superiori. I punteggi del test seguono approssimativamente la distribuzione
normale con media 25 e deviazione standard 6. Maggiore il punteggio nel test,
maggiore il livello di motivazione dello studente. A Mario Rossi viene detto che
solo il 35% degli studenti che hanno completato il test mostra un livello di
motivazione superiore al suo.  Quale punteggio ha ottenuto Mario Rossi nel test?
```

````{solution} label-distributions-gauss-03
:class: dropdown

```{code-block} python
import scipy.stats as st

st.norm.ppf(0.65, 25, 6)
```

La soluzione è 27.311922798445405.
````
