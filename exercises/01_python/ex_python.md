# ✅ Python

```{exercise}
:label: label-python-01

Date le seguenti variabili, 
`thing = "light"` e `speed = 299792458`, si usi la formattazione f-string per stampare `The speed of light is 2.997925e+08 m/s.`.
```

````{solution} label-python-01
:class: dropdown

```{code-block} python
thing = "light"
speed = 299792458  # m/s
print(f"The speed of {thing} is {speed:2e} m/s.")
```
````

+++

```{exercise}
:label: label-python-02

Si definisca la variabile `language`. Si scriva uno script che usa `if/elif/else` e ritorna 

- `Mi piacciono i serpenti!` se `language` è `python`;
- `Sei un pirata?` se `language` è `R`;
- `Che cosa significa [valore della variabile <language>]?` se `language` è qualsiasi altra cosa.

```

````{solution} label-python-02
:class: dropdown

```{code-block} python
language = "python"
if language.lower() == "python":
    print("Mi piacciono i serpenti!")
elif language.lower() == "r":
    print("Sei un pirata?")
else:
    print(f"Che cosa significa {language}?")
```
````

+++

```{exercise}
:label: label-python-03

Si crei una funzione che accetta due numeri e ritorna True se la somma dei due numeri è maggiore di 0 o False se la somma è minore o uguale a 0.


```

````{solution} label-python-03
:class: dropdown

```{code-block} python
def mysum(a, b):
    return True if a+b > 0 else False

mysum(2, -3)
```
````

+++

```{exercise}
:label: label-python-04

Si usi una list comprehension per sommare 10 a ciascun elemento della seguente lista: [1, 2, 3, 4, 5].
```

````{solution} label-python-04
:class: dropdown

```{code-block} python
mylist = [1, 2, 3, 4, 5]
[element +10 for element in mylist]
```
````

+++

```{exercise}
:label: label-python-05

Si usi una list comprehension sulla seguente lista ['giovanna', 'Maria', 'luca', 'Fabio', 'valentina'], in maniera tale da selezionare solo i nomi la cui prima lettera è maiuscola. Si usi la funzione `str.isupper()`.
```

````{solution} label-python-05
:class: dropdown

```{code-block} python
names = ['giovanna', 'Maria', 'luca', 'Fabio', 'valentina']
[_ for _ in names if _[0].isupper()]
```
````

+++

```{exercise}
:label: label-python-06

Si crei un dizionario `d` costituito da 10 elementi nel quale la chiave ha la forma 'key-0', 'key-1', ecc. e i corrispondenti valori vadano da 0 a 9. Da questo dizionario si recuperi il valore associato a `key-5`.
```

````{solution} label-python-06
:class: dropdown

```{code-block} python
keys = [f"key-{k}" for k in range(10)]
vals = range(10)
d = {k:v for k, v in zip(keys, vals)}
d['key-5']
```
````

+++

```{exercise}
:label: label-python-07

Si scriva un ciclo for che, per i numeri da 1 a 5, stampi "Il quadrato di 1 è 1.", "Il quadrato di 2 è 4.", ecc.
```

````{solution} label-python-07
:class: dropdown

```{code-block} python
numbers = [1, 2, 3, 4, 5]
for i in numbers:
    square = i**2
    print(f"Il quadrato di {i} è {square}.")
```
````

+++

```{exercise}
:label: label-python-08

Anziché usare un ciclo for, si innalzino al quadrato gli elementi della lista dell'esercizio {ref}`label-python-07` usando una list comprehension.
```

````{solution} label-python-08
:class: dropdown

```{code-block} python
numbers = [1, 2, 3, 4, 5]
[_ **2 for _ in numbers]
```
````

+++

```{exercise}
:label: label-python-09

Usando `if/else` in un ciclo `for`, per ciascun elemento di una lista di numeri da 0 a 10, si stampi un messaggio che specifica se il numero è pari o dispari. (suggerimento: si usi l'operatore `%`)
```

````{solution} label-python-09
:class: dropdown

```{code-block} python
for i in range(1, 11):
    if i % 2 == 0:
        print('Numero pari:', i)
    else:
        print('Numero dispari:', i)
```
````

+++

```{exercise}
:label: label-python-10

Si crei una list comprehension che seleziona i numeri pari da una lista di interi da 0 a 10.
```

````{solution} label-python-10
:class: dropdown

```{code-block} python
import numpy as np

numbers = np.arange(11)
even = [_ for _ in numbers if _ % 2 == 1]
even
```
````

+++

```{exercise}
:label: label-python-10

Usando la funzione `enumerate()` si stampino gli indici degli elementi della lista [4, 2, 5, 7, 8].
```

````{solution} label-python-10
:class: dropdown

```{code-block} python
numbers = [4, 2, 5, 7, 8]
for i, v in enumerate(numbers):
    print('numbers[',i,'] =', v)
```
````

+++

```{exercise}
:label: label-python-11

Per la lista [1.23, 10, 'Maria', 20, 'Giovanni'], si stampino l'elemento 1 e l'elemento 4.
```

````{solution} label-python-11
:class: dropdown

```{code-block} python
my_list = [1.23, 10, 'Maria', 20, 'Giovanni']
print(my_list[1])  
print(my_list[4])  
```
````


+++

```{exercise}
:label: label-python-12

Per la lista [1.23, 10, 'Maria', 20, 'Giovanni'], si stampino il penultimo e il quartultimo elemento.
```

````{solution} label-python-12
:class: dropdown

```{code-block} python
my_list = [1.23, 10, 'Maria', 20, 'Giovanni']
print(my_list[-2])  
print(my_list[-4])  
```
````

+++

```{exercise}
:label: label-python-13

Per la lista [1.23, 10, 'Maria', 20, 'Giovanni'], si estraggano mediante *list slicing* il terzo, quarto e quinto elemento.
```

````{solution} label-python-13
:class: dropdown

```{code-block} python
my_list = [1.23, 10, 'Maria', 20, 'Giovanni']
print(my_list[2:5]) 
```
````

+++

```{exercise}
:label: label-python-14

Per la lista [1.23, 10, 'Maria', 20, 'Giovanni'], usando il ciclo `for` e la keyword `in`, si stampino gli elementi della lista.
```

````{solution} label-python-14
:class: dropdown

```{code-block} python
for item in my_list:
    print(item)
```
````

+++

```{exercise}
:label: label-python-15

Per la lista [1.23, 10, 'Maria', 20, 'Giovanni'], usando il ciclo `for` e utilizzando l'indice degli elementi, si stampino gli elementi della lista.
```

````{solution} label-python-15
:class: dropdown

```{code-block} python
my_list = [1.23, 10, 'Maria', 20, 'Giovanni']

for i in range(0, len(my_list)):
    print(my_list[i])
```
````

+++

```{exercise}
:label: label-python-16

Si concatenino le liste [1, 2, 3, 4] e [5, 6, 7, 8].
```

````{solution} label-python-16
:class: dropdown

```{code-block} python
my_list1 = [1, 2, 3, 4]
my_list2 = [5, 6, 7, 8]

my_list3 = my_list1 + my_list2
print(my_list3)
# oppure
my_list1.extend(my_list2)
print(my_list1)
```
````

+++

```{exercise}
:label: label-python-17

Si crei la lista [1, 2, 3]. Si faccia una copia della lista usando l'operatore `=`. Si modifichi il primo elemento della lista originaria ponendolo uguale a 99. Si stampino i valori della seconda lista.
```

````{solution} label-python-17
:class: dropdown

```{code-block} python
my_list1 = [1, 2, 3]

new_list = my_list1
print(new_list)

my_list1[0] = 99

print(my_list1)
print(new_list)
```
````

+++

```{exercise}
:label: label-python-18

Si crei la lista [1, 2, 3]. Si faccia una copia della lista usando il metodo `copy()`. Si modifichi il primo elemento della lista originaria ponendolo uguale a 99. Si stampino i valori della seconda lista.
```

````{solution} label-python-18
:class: dropdown

```{code-block} python
my_list1 = [1, 2, 3]

new_list = my_list1.copy()
print(new_list)

my_list1[0] = 99

print(my_list1)
print(new_list)
```
````