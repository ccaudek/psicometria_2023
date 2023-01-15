# ✅ EDA

```{exercise}
:label: ex-eda-pensuins-1

Si importi il file `penguins.csv` e si verifichi la presenza di dati mancanti. Se ci sono dei dati mancanti li si escluda. Si trovi la proporzione di osservazioni che sono state raccolte sull'isola Dream.
```

````{solution} ex-eda-pensuins-1
:class: dropdown
:label: sol-eda-pensuins-1

```{code-block} python
import numpy as np 
import pandas as pd

df = pd.read_csv('data/penguins.csv')
df.dropna(inplace=True)
df.shape

df.value_counts('island', normalize=True)
```

il 36.9% delle osservazioni è relativa all'isola Dream.
````

+++

```{exercise}
:label: ex-eda-pensuins-2

Per i dati dell'esercizio {ref}`ex-eda-pensuins-1`, si trovino la media e la deviazione standard, quale statistica descrittiva, della variabile `body_mass_g`. Si verifichi il risultato applicando la formula della deviazione standard.
```

````{solution} ex-eda-pensuins-2
:class: dropdown
:label: sol-eda-pensuins-2

```{code-block} python
import numpy as np 
import pandas as pd

df = pd.read_csv('data/penguins.csv')
df.dropna(inplace=True)

df['body_mass_g'].mean()
df['body_mass_g'].std(ddof=0)

y = df['body_mass_g']

def mystd(x):
    vx = np.sum((x - np.mean(x))**2) / len(x)
    std = np.sqrt(vx)
    return std

mystd(y)
```
La media è 4207.057057057057; la deviazione standard è 804.0058601595629.
````

+++

```{exercise}
:label: ex-eda-penguins-3

Si ripeta l'esercizio {ref}`ex-eda-pensuins-2` usando solo i dati dell'isola Biscoe.
```

````{solution} ex-eda-penguins-3
:class: dropdown
:label: sol-eda-penguins-3

```{code-block} python
import numpy as np 
import pandas as pd

df = pd.read_csv('data/penguins.csv')
df.dropna(inplace=True)

df[df['island'] == 'Biscoe']['body_mass_g'].mean()
df[df['island'] == 'Biscoe']['body_mass_g'].std(ddof=0)
```
La media è 4719.171779141105; la deviazione standard è 788.4303859944841.
````

+++

```{exercise}
:label: ex-eda-penguins-4

Per i dati dell'esercizio {ref}`ex-eda-penguins-3`, si costruisca un istogramma per verificare il tipo di distribuzione dei dati. Si verifichi se, per questi dati, è plausibile la regola $s ≈ 1.4281 MAD$. 
```

````{solution} ex-eda-penguins-4
:class: dropdown
:label: sol-eda-penguins-4

```{code-block} python
import numpy as np 
import pandas as pd

df = pd.read_csv('data/penguins.csv')
df.dropna(inplace=True)

df[df['island'] == 'Biscoe']['body_mass_g'].plot.hist()

y = df[df['island'] == 'Biscoe']['body_mass_g']
y

mad = np.median(np.abs(y - np.median(y)))
mad

1.4826 * mad
```

Anche se i dati mostrano una leggera asimmetria negativa, la regola $s ≈ 1.4281 MAD$ descrive in maniera approssimativa quello che succede nel campione. Questo ci offre un modo per interpretare la deviazione standard.
````

+++

```{exercise}
:label: ex-eda-penguins-5

Per dati che si distribuiscono in maniera approssimativamente Normale, ci possiamo aspettare che il 95% dei dati sia compreso nell'intervallo $\bar{y} \pm 2 s$. Si verifichi questa affermazione usando i dati dei pinguini maschi che sono stati osservati sull'isola Dream prima del 2009.
```

````{solution} ex-eda-penguins-5
:class: dropdown
:label: sol-eda-penguins-5

```{code-block} python
import numpy as np 
import pandas as pd

df = pd.read_csv('data/penguins.csv')
df.dropna(inplace=True)

eval_string = "island == 'Dream' & sex == 'male' & year < 2009"
y = df.query(eval_string)['flipper_length_mm']
y.hist()
y.quantile(0.975) - y.quantile(0.025)
4 * y.std(ddof=0)
```

Nel caso presente, la "regola empirica" è valida.
````

+++

```{exercise}
:label: ex-eda-penguins-6

Si considerino le osservazioni relative all'isola Biscoe e alla specie Adelie. Esaminiamo la variabile `flipper_length_mm`. Per questa variabile, si trovino gli eventuali valori *outlier* costruendo un boxplot. Dopo avere eliminato gli *outlier*, si calcoli la media.
```

````{solution} ex-eda-penguins-6
:class: dropdown
:label: sol-eda-penguins-6

```{code-block} python
import numpy as np 
import pandas as pd

df = pd.read_csv('data/penguins.csv')
df.dropna(inplace=True)

eval_string = "island == 'Biscoe' & species == 'Adelie'"
y = df.query(eval_string)['flipper_length_mm']
y.hist()
newdf = pd.DataFrame(y)
_ = newdf.boxplot(column=['flipper_length_mm'])  
q1 = y.quantile(0.25)
q3 = y.quantile(0.75)
IQR = q3 - q1
outliers = newdf[((newdf < (q1 - 1.5*IQR)) | (newdf > (q3 + 1.5*IQR)))]
outliers.dropna(subset=['flipper_length_mm'])
newdf2 = newdf[newdf['flipper_length_mm'] > 172]
newdf2['flipper_length_mm'].mean()
```
````

+++

```{exercise}
:label: ex-eda-penguins-7

Per i dati dell'esercizio {ref}`ex-eda-pensuins-1`, dopo avere eliminato i dati mancanti, si costruisca un violin plot che include uno strip plot della variabile `flipper_length_mm` in funzione di `species`.

```

````{solution} ex-eda-penguins-7
:class: dropdown
:label: sol-eda-penguins-7

```{code-block} python
import numpy as np 
import pandas as pd
import seaborn as sns

df = pd.read_csv('data/penguins.csv')
df.dropna(inplace=True)

ax = sns.violinplot(
    data=df,
    x = 'species',
    y = 'flipper_length_mm',
    color = '.8'
)

ax = sns.stripplot(
    data = df,
    x = 'species',
    y = 'flipper_length_mm',
    palette = 'colorblind'
)
```
````

+++

```{exercise}
:label: ex-eda-penguins-8

Per i dati dell'esercizio {ref}`ex-eda-pensuins-1`, dopo avere eliminato i dati mancanti, si consideriano solo i dati dei pinguini femmina che non si trovano sull'isola Biscoe. Si trovi la deviazione standard, quale statistica inferenziale, per le variabili `bill_length_mm`	 e `bill_depth_mm`, separatamente per ciascuna specie.
```

````{solution} ex-eda-penguins-8
:class: dropdown
:label: sol-eda-penguins-8

```{code-block} python
import numpy as np 
import pandas as pd

df = pd.read_csv('data/penguins.csv')
df.dropna(inplace=True)

eval_string = "island != 'Biscoe' & sex == 'female'"
newdf = df.query(eval_string)
newdf.groupby("species")[["bill_length_mm", "bill_depth_mm"]].std(ddof=1)
```
````

+++

```{exercise}
:label: ex-eda-penguins-9

Per i dati dell'esercizio {ref}`ex-eda-pensuins-1`, dopo avere eliminato i dati mancanti, si consideriano solo le osservazioni raccolte nel 2009. Si trovi il numero di osservazioni e la media per le variabili 'bill_length_mm' e 'bill_depth_mm', separatamente per ciascuna specie e ciascun genere.
```

````{solution} ex-eda-penguins-9
:class: dropdown
:label: sol-eda-penguins-9

```{code-block} python
import numpy as np 
import pandas as pd

df = pd.read_csv('data/penguins.csv')
df.dropna(inplace=True)

newdf = df[df['year'] == 2008]
summary_stats = (newdf.loc[:, ['species', 'sex', 'bill_length_mm', 'bill_depth_mm']]
                         .groupby(['species', 'sex'])
                         .aggregate(['mean', 'count']))
summary_stats.round(2)
```
````
