# Ce que Python m’a appris sur les objets, l’identité et la mutabilité

En travaillant sur un projet récemment, j’ai pris un moment pour approfondir certains concepts clés en Python :

-  `id()` et `type()`
-  Objets **mutables** vs **immutables**
-  Comportement des **arguments de fonction** et effets de bord

Quelques découvertes intéressantes

---

## Les listes sont mutables

Si deux variables font référence à la même liste, modifier l’une modifie aussi l’autre :

```python
a = [1, 2]
b = a
b.append(3)
print(a)  # Résultat : [1, 2, 3]
```

## Les entiers sont immuables

Par exemple, avec un entier on retrouve : 

```python
x=10
y = x
y += 5
print(x) -> 10
print(y) -> 15
