# ✅ Distribuzione binomiale

```{exercise}
:label: label-binomial-01

Sia X una v.c. binomiale di parametri $n$ = 5 e $p$ = 0.5. Si trovino le probabilità indicate.

a. $P(X \leq 3$

b. $P(X \geq 3$

c. $P(X == 3$

d. $P(X == 0)$

e. $P(X == 5)$
```

````{solution} label-binomial-01
:class: dropdown

a. 0.8125 

b. 0.5000 

c. 0.3125 

d. 0.0313 

e. 0.0312

````

+++

```{exercise}
:label: label-binomial-02

Una moneta sbilanciata ha probabilità di testa uguale a 2/3. La moneta è lanciata 10 volte. 

a. Si trovi la probabilità di ottenere testa non più di 5 volte.

b. Si trovi la probabilità di ottenere testa più spesso che croce.
```

````{solution} label-binomial-02
:class: dropdown

```{code-block} python
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

st.binom.cdf(5, 10, 2/3)
```
0.21312808006909523


0.7868719199309048
````

+++

```{exercise}
:label: label-binomial-03

Uno psicologo ha messo a punto un intervento per fare in modo che almeno la metà dei suoi pazienti riescano ad eseguire un certo compito. In un campione casuale di 20 pazienti 14 riescono a completare il compito. Qual è la probabilità che 14 o più pazienti su 20 riescano a completare il compito se nella popolazione la proporzione di coloro che riesco a fare questo è solo pari a 0.5?
```

````{solution} label-binomial-03
:class: dropdown

0.0577
````
