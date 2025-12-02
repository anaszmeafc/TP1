## Partie 3 : Collaboration, branches et merge requests

### Mission 1 : Créer une branche

```
git checkout -b nouvelle-branche
```

Crée un `.gitignore` :

```
code/__pycache__/
```

Push :

```
git push --set-upstream origin nouvelle-branche
```

### Merge Requests

Va dans l’onglet **Pull Requests** de GitHub → crée une PR → compare → merge.

---

## Rebase

GitHub permet le rebase via l’interface lorsque ta branche est en retard sur `main`.

---

## Cherry-pick (facultatif)

Récupère le SHA d’un commit dans l’onglet **Commits**, puis :

```
git checkout branche-a-rebase
git cherry-pick <SHA>
```

---

## Conclusion