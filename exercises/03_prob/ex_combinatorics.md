# ✅ Calcolo combinatorio


```{exercise}
:label: label-combinatorics-01

Vengono lanciati 5 dadi bilanciati a 6 facce. Qual è la probabilità che la somma dei dadi sia uguale a 19?
```

````{solution} label-combinatorics-01
:class: dropdown

```{code-block} python
import numpy as np
import pandas as pd
import itertools as it
import math

die_rolls = list(it.product(range(1, 7), repeat=5))
results = np.arange(5, 31)
prob_distr = pd.DataFrame()
freq = sum(sum(rol) == results for rol in die_rolls)
prob_distr['py'] = freq / sum(freq)
prob_distr['y'] = results
prob_distr[prob_distr['y'] == 19]
```
La soluzione è 0.094522.

Oppure, in maniera più semplice:

```
die_rolls = list(it.product(range(1, 7), repeat=5))
n1 = sum(sum(rol) == 19 for rol in die_rolls)
n = len(die_rolls)
n1 / n
```

````

+++
```{exercise}
:label: label-combinatorics-02

Vengono lanciati 5 dadi bilanciati a 6 facce. Qual è la probabilità che la somma dei dadi sia minore o uguale a 19?
```

````{solution} label-combinatorics-02
:class: dropdown

```{code-block} python
import numpy as np
import pandas as pd
import itertools as it
import math

die_rolls = list(it.product(range(1, 7), repeat=5))
results = np.arange(5, 31)

prob_distr = pd.DataFrame()
freq = sum(sum(rol)==results for rol in die_rolls)

prob_distr['py'] = freq / sum(freq)
prob_distr['y'] = results

prob_distr.query('y <= 19')['py'].sum()
```
La soluzione è 0.6948302469135803.

Oppure, in maniera più semplice

```
die_rolls = list(it.product(range(1, 7), repeat=5))
n1 = sum(sum(rol) <= 19 for rol in die_rolls)
n = len(die_rolls)
n1 / n
```

````

+++
```{exercise}
:label: label-combinatorics-03

Vengono lanciati 5 dadi bilanciati a 6 facce. Qual è la probabilità che la somma dei dadi sia maggiore di 25?
```

````{solution} label-combinatorics-03
:class: dropdown

```{code-block} python
import numpy as np
import pandas as pd
import itertools as it
import math

die_rolls = list(it.product(range(1, 7), repeat=5))
results = np.arange(5, 31)

prob_distr = pd.DataFrame()
freq = sum(sum(rol) == results for rol in die_rolls)

prob_distr['py'] = freq / sum(freq)
prob_distr['y'] = results

prob_distr.query('y > 25')['py'].sum()
```
La soluzione è 0.016203703703703703.

Oppure, in maniera più semplice

```
die_rolls = list(it.product(range(1, 7), repeat=5))
n1 = sum(sum(rol) > 25 for rol in die_rolls)
n = len(die_rolls)
n1 / n
```

````

+++

```{exercise}
:label: label-combinatorics-04

Se estraiamo a caso da un mazzo di carte da poker 2 carte, quante combinazioni sono possibili?
```

````{solution} label-combinatorics-04
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

+++

```{exercise}
:label: label-combinatorics-05

Supponiamo di lanciare 3 dadi equilibrati a 4 facce marcate con 1, 2, 3, 4. Sia $X$ la somma dei valori ottenuti dal lancio dei tre dadi. Si trovi la probabilità $P(X) > 8$.
```

````{solution} label-combinatorics-05
:class: dropdown

```{code-block} python
r = range(1, 5)
sample = [(i, j, k) for i in r for j in r for k in r]
sample
len(sample)
z = [sum(point) for point in sample]
z
r = range(1, 5)
sample = [(i, j, k) for i in r for j in r for k in r]

for i in range(3, 13):
    event = [roll for roll in sample if sum(roll) == i]
    print(f"z = {i} : {len(event)} / {len(sample)}")
px = []

for i in range(3, 13):
    event = [roll for roll in sample if sum(roll) == i]
    px.append(len(event) / len(sample))

px
list(zip(list(range(3, 13)), px))
0.15625 + 0.09375 + 0.046875 + 0.015625
```
La soluzione è 0.3125. Oppure

```{code-block} python
import empiricaldist

d1 = empiricaldist.Pmf.from_seq([1,2,3,4])
d2 = d1.add_dist(d1)
d3 = d2.add_dist(d1)

d3[9] + d3[10] + d3[11] + d3[12] 
```

````

