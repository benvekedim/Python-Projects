## Temel İstatistik İşlemleri
_________
 **Amaç** : Python ile kütüphane kullanmadan temel istatistik işlemleri yapacağım.
_________

*  **Ortalama** :
 
```math
{\mu}=\dfrac{1}{N}\sum ^{N}_{i=1}x_{i}
```
--------

*  **Standart Sapma**

```math
{\sigma}=\sqrt{\dfrac{\sum ^{N}_{i=1}\left| x_{i}-{\mu}\right| }{N}}
```
--------

* **Varyans**



```math
Var(x) = {\sigma}^2
```

----

* **Kovaryans Değeri**

```math
\dfrac{\sum ^{N}_{i=1}\left( x-\mu _{x}\right) \left( y-\mu _{y}\right) }{N}
```
----

* **Kovaryans Matrisi**

```math
\begin{bmatrix} Var(x) & Cov(x,y) \\ Cov(y,x) & Var(y) \end{bmatrix}
```