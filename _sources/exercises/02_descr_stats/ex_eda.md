# ✅ EDA

```{exercise}
:label: my-exercise

Recall that $n!$ is read as "$n$ factorial" and defined as
$n! = n \times (n - 1) \times \cdots \times 2 \times 1$.

There are functions to compute this in various modules, but let's
write our own version as an exercise.

In particular, write a function `factorial` such that `factorial(n)` returns $n!$
for any positive integer $n$.
```

````{solution} my-exercise
:class: dropdown
:label: my-solution

Here's one solution.

```{code-block} python
def factorial(n):
    k = 1
    for i in range(n):
        k = k * (i + 1)
    return k

factorial(4)
```
````

+++

```{admonition} Question
A categorical variable is:

- a) a variable with **only two** different possible values
- b) a variable with continuous numerical values
- c) a variable with a finite set of possible values

_Select a single answer_
```

+++

```{admonition} Question
In the notebook "First look at our dataset", we used pandas and specifically
`adult_census = pd.read_csv("../datasets/adult-census.csv")` to:

- a) load a comma-separated values file
- b) load a dataset already included in the pandas package
- c) load a file only containing the survey features
- d) load a file only containing the target of our classification problem:
  whether or not a person has a low or high income salary
- e) load a file containing both the features and the target for our classification
  problem

_Select all answers that apply_
```

+++

```{admonition} Question

In the previous notebook, we used:

- a) pandas to manipulate data
- b) pandas and seaborn to visually inspect the dataset
- c) numpy and scipy to perform numerical inspection (for instance using
  `scipy.optimize.minimize`)
- d) scikit-learn to fit some machine learning models

_Select all answers that apply_
```

+++

```{admonition} Question
How is a tabular dataset organized?

- a) a column represents a sample and a row represents a feature
- b) a column represents a feature and a row represents a sample
- c) the target variable is represented by a row
- d) the target variable is represented by a column

_Select all answers that apply_
```
