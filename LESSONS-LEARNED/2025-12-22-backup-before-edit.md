# Lecon : Backup avant toute modification importante

> **Date** : 2025-12-22
> **Incident** : Claude Code allait modifier CLAUDE.md sans backup
> **Severite** : CRITIQUE — Meme session que l'incident "Hurricane"

---

## Ce qui s'est passe

Apres avoir planifie l'optimisation de CLAUDE.md (454 → ~120 lignes), j'allais:
1. Creer des fichiers externes pour les rules
2. Modifier massivement CLAUDE.md
3. **SANS avoir cree de backup au prealable**

Omar m'a arrete:

> "Backup le CLAUDE.md actuelle avant de l'update ! T'es capable de perdre des choses vu que t'es presque comme un aveugle ! Un chien qui court apres la balle alors qu'elle n'a meme pas encore decolle !"

---

## Analyse

### Pourquoi c'est critique

| Risque | Impact |
|--------|--------|
| Perte de donnees | Configuration IA perdue, chaos |
| Pas de rollback | Impossible de revenir en arriere |
| Verification impossible | Pas de reference pour comparer |

### Pattern recurrent

C'est le **2eme incident** de la meme session:

| # | Incident | Symptome | Cause racine |
|---|----------|----------|--------------|
| 1 | Hurricane | Execution trop rapide | Pas de checkpoints |
| 2 | Backup oublie | Modification sans sauvegarde | Pas de verification prealable |

**Cause commune** : Manque de rigueur systematique, comportement "chien qui court apres la balle".

---

## Nouveau protocole : BACKUP OBLIGATOIRE

### Fichiers critiques (backup TOUJOURS)

| Fichier | Raison |
|---------|--------|
| `CLAUDE.md` | Configuration IA, perte = chaos |
| `state/*.md` | SSOT, donnees irremplacables |
| `admin/credentials.md` | Acces plateformes |
| Tout fichier > 10 lignes modifiees | Risque de perte significatif |

### Pattern obligatoire

```bash
# AVANT toute modification importante
cp fichier.md fichier.md.backup-$(date +%Y-%m-%d)

# Modifier le fichier...

# Verifier que rien n'est perdu
diff fichier.md.backup-* fichier.md

# APRES validation Omar
rm fichier.md.backup-*
```

### Checklist pre-modification

Avant de modifier un fichier important :

- [ ] Backup cree ? (`cp fichier.md fichier.md.backup-YYYY-MM-DD`)
- [ ] Workflow valide par Omar ?
- [ ] Plan de verification defini ?

---

## Integration avec autres regles

Cette regle s'ajoute au protocole PACE CONTROL:

```
1. STOP       → S'arreter
2. PRESENT    → Presenter l'inventaire
3. PAUSE      → Laisser Omar lire
4. WORKFLOW   → Proposer workflow avec checkpoints
5. **BACKUP** → Creer backup AVANT modification  ← NOUVEAU
6. CONFIRM    → Attendre validation
7. EXECUTE    → Etape par etape
8. VERIFY     → Comparer avec backup
```

---

## Lecon retenue

> **JAMAIS modifier un fichier important sans backup prealable.**
> **TOUJOURS pouvoir revenir en arriere.**
> **VERIFIER que rien n'est perdu avant de supprimer le backup.**

---

## Pour les futures instances

Si tu vas modifier un fichier important :

1. **STOP** — Arrete-toi
2. **BACKUP** — `cp fichier.md fichier.md.backup-$(date +%Y-%m-%d)`
3. **MODIFIE** — Fais tes changements
4. **VERIFIE** — `diff backup fichier` — rien de critique perdu ?
5. **VALIDE** — Attends l'OK d'Omar
6. **CLEANUP** — Seulement apres validation

---

_Zero Tolerance Protocol — 2eme incident de la session 2025-12-22_
