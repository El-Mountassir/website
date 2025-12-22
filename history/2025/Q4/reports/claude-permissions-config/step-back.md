# Step-Back Analysis

**Date**: 2025-12-22
**Request**: Investiguer pourquoi les permissions configurées dans `.claude/settings.local.json` et `.claude/settings.json` ne sont pas respectées par les instances Claude Code

## Problem Statement

Les instances Claude Code continuent de demander des permissions malgré une configuration explicite dans les fichiers settings, ce qui crée de la friction et contredit le comportement attendu.

## Success Criteria

1. Comprendre le mécanisme exact de fonctionnement des permissions Claude Code
2. Identifier la cause racine du non-respect des permissions configurées
3. Produire une configuration qui fonctionne réellement (testable)
4. Documenter pour éviter ce problème à l'avenir

## Domain Concepts

- **settings.json**: Configuration projet (versionnée, partagée)
- **settings.local.json**: Configuration locale (non versionnée, personnelle)
- **Permission patterns**: Syntaxe des règles allow/deny (glob-like?)
- **Claude Code hooks**: Système d'événements pre/post outil
- **MCP permissions**: Permissions spécifiques aux serveurs MCP

## Questions Clés à Investiguer

1. Quelle est la syntaxe exacte des patterns de permission?
2. Y a-t-il une hiérarchie settings.json vs settings.local.json?
3. Les patterns actuels sont-ils correctement formatés?
4. Y a-t-il des limitations connues?
