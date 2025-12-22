# Step-Back Analysis

**Date**: 2025-12-22
**Request**: Standardiser la création de custom slash commands, créer un skill pour les futures instances, et aligner les commandes existantes.

## Problem Statement

Les slash commands créées (/start, /end) ne suivent pas le format standard de Claude Code, manquant le YAML frontmatter et les bonnes pratiques.

## Success Criteria

1. Un skill documenté pour créer des slash commands conformes
2. Un template réutilisable pour les futures commandes
3. Toutes les commandes existantes alignées avec le standard
4. Documentation pour les futures instances

## Domain Concepts

- **YAML Frontmatter**: Métadonnées en début de fichier (---)
- **allowed-tools**: Restriction des outils disponibles pour la commande
- **description**: Description courte pour la découverte
- **argument-hint**: Indication des arguments attendus
- **$ARGUMENTS / $1**: Variables pour capturer les arguments utilisateur

## Écart Observé

| Élément | Bon exemple (elevate.md) | Mes commandes (start.md) |
|---------|--------------------------|--------------------------|
| YAML frontmatter | ✅ Présent | ❌ Absent |
| allowed-tools | ✅ Défini | ❌ Absent |
| description | ✅ Courte, claire | ❌ Absent |
| argument-hint | ✅ Présent | ❌ Absent |
| Variables | ✅ $1, $ARGUMENTS | ❌ Mal utilisé |
| Structure | ✅ Purpose, Variables, Pipeline | ⚠️ Partielle |
