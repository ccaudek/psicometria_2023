#!/usr/bin/env python
# coding: utf-8

# # FAQ
# 
# ## ❓ Problemi con l'installazione dei pacchetti R su Windows?
# 
# Ottenere la configurazione necessaria per gli scopi di questo insegnamento su Windows potrebbe richiedere un po' più di fatica rispetto a Linux e Mac. Di conseguenza, se possibile, consigliamo di utilizzare Linux o MacOS. Inoltre, Stan, il linguaggio di programmazione probabilistico che useremo in questo insegnamento, richiede una toolchain del compilatore C++ che non è disponibile di default in Windows (colpa Microsoft). Per l'installazione di `cmdstan` sui vari sistemi operativi è possibile consultare la pagina web [CmdStan User's Guide](https://mc-stan.org/docs/2_28/cmdstan-guide/cmdstan-installation.html).
# 
# 
# ## Istallare `knitr`
# 
# Se avete installato RStudio e R, è probabile che sulla vostra macchina manchi `knitr`, il pacchetto responsabile del rendering dei notebook in pdf.
# 
# **Soluzione:**
# 
# ```{r eval=FALSE}
# install.packages("knitr")
# ```
# 
# Potete anche installare i pacchetti dal menu di RStudio `Tools->Install Packages`.
# 
# ## Se `knitr` è installato ma il pdf non si compila 
# 
# In questo caso è possibile che non sia installato LaTeX, che è il pacchetto che elabora il codice e produce il file in formato pdf.
# 
# **Soluzione:**
# 
# È sufficiente installare tinytex che fornisce l'insieme minimo di funzionalità LaTeX  indispensabili per potere usare il compilatore pdf:
# 
# ```{r eval=FALSE}
# install.packages("tinytex")
# tinytex::install_tinytex()
# ```
# 
# ## Installare `cmdstan`
# 
# Assicuratevi sempre di avere aggiornato il sistema operativo all'ultima versione disponibile. Assicuratevi inoltre di avere installato la versione più recente di $\textsf{R}$.
# 
