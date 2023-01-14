# ✅ Teorema di Bayes


```{exercise}
:label: label-prob-bayes-theorem-01

Un esame del sangue rilieva correttamente il vampirisimo il 95% delle volte, $Pr(Positive|Vampire)$ = 0.95. Il test ha un tasso di falsi psitivi di $Pr(Positive | Mortal)$ = 0.01. Sappiamo anche che i vampiri sono rari -- circa lo 0.1% della popolazione, $Pr(Vampire)$ = 0.001. Si trovi la probabilità di essere un vampiro dato che il test ha dato un risultato positivo. (da Statistical rethinking)
```

````{solution} label-prob-bayes-theorem-01
:class: dropdown

Per calcolare $Pr(Vampire|Positive)$ applichiamo il teorema di Bayes: 
$Pr(Vampire | Positive) = \frac{Pr(Positive | Vampire) * Pr(Vampire)}{Pr(Positive)}$.

```{code-block} python
Pr_Positive_Vampire = 0.95
Pr_Positive_Mortal = 0.01
Pr_Vampire = 0.001
tmp = Pr_Positive_Vampire * Pr_Vampire
Pr_Positive = tmp + Pr_Positive_Mortal * (1 - Pr_Vampire)
Pr_Vampire_Positive = tmp / Pr_Positive
Pr_Vampire_Positive
```
La risposta è 0.08683729433272395.
````

+++

```{exercise}
:label: label-prob-combinatorics-02

Se estraiamo a caso da un mazzo di carte da poker 2 carte, quante combinazioni sono possibili?
```

````{solution} label-prob-combinatorics-02
:class: dropdown

```{code-block} python
from math import factorial

n = 52
k = 2
C = factorial(n) / (factorial(k) * factorial(n - k))
print(C)
```
La soluzione è 1326. Oppure

```{code-block} python
from math import comb

C = comb(n, k)
print(C)
```

````
