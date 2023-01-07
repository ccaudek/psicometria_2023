# ✅ Calcolo combinatorio

Del calcolo combinatorio qui considereremo solo le permutazioni e le combinazioni. Una combinazione riguarda la selezione di un certo numero di elementi da un elenco e l'ordine non ha importanza. Una permutazione riguarda la selezione di un certo numero di elementi da un insieme e l'ordine è importante.

```{exercise}
:label: label-prob-combinatorics-01

Quante permutazioni si possono ottenere dall'insieme $\{1, 2, 3\}$?
```

````{solution} label-prob-combinatorics-01
:class: dropdown

```{code-block} python
from math import factorial

n = 3
perm = factorial(n)
print(perm)
```
La soluzione è 6.
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
