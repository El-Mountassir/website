# Step-Back Analysis

**Date**: 2025-12-24
**Request**: Analyser le concept "agent harness" généré par ChatGPT et voir comment l'adapter au modèle El-Mountassir (1 humain + flotte d'agents IA)

## Problem Statement

Comment formaliser le rôle d'Omar dans "The Collective" en utilisant la terminologie et les patterns établis du domaine multi-agent, afin que ce rôle soit clair pour les agents actuels, les futurs agents, et aligné avec les best practices de l'industrie ?

## Success Criteria

1. **Terminologie précise** : Un terme/concept qui capture exactement le rôle d'Omar (pas trop large, pas trop étroit)
2. **Alignement industrie** : Le terme doit être reconnu/reconnaissable dans le jargon agent/LLM
3. **Actionnable** : Le concept doit informer des décisions pratiques (permissions, workflows, escalations)
4. **Cohérent avec l'existant** : Doit s'intégrer avec notre CLAUDE.md, GOVERNANCE.md, partnership.md
5. **Différenciation claire** : Distinguer ce qui est "Omar uniquement" vs "socio-technique" (outils + règles + Omar)

## Domain Concepts

| Concept | Définition (à valider) |
|---------|------------------------|
| **Agent Harness** | Couche logicielle autour du modèle : boucle d'exécution, outils, contexte, permissions, observabilité |
| **Human-in-the-Loop (HITL)** | Pattern où un humain intervient dans la boucle d'exécution de l'agent |
| **Supervisory Control** | Contrôle humain qui définit objectifs et valide sorties sans micro-manager l'exécution |
| **Control Plane** | Dans les systèmes distribués : la couche qui gère/orchestre vs la couche qui exécute (data plane) |
| **Socio-Technical System** | Système où humains + technologie + règles forment un tout interdépendant |

## Questions Clés à Résoudre

1. **Omar = harness, ou Omar = composant du harness ?**
   - ChatGPT propose : Omar EST le harness (la couche de supervision)
   - Alternative : Le harness est socio-technique (Omar + outils + règles), Omar en est le "cerveau"

2. **Quel terme adopter ?**
   - Human Control Plane (technique, systèmes distribués)
   - Agent Supervisor (simple, clair)
   - Operator/Orchestrator (devops-like)
   - Autre ?

3. **Comment cela change nos pratiques ?**
   - Quelles responsabilités sont explicitement "Omar only" ?
   - Quels garde-fous formalisent ce rôle ?

## Source Material (ChatGPT Input)

```
agent harness = l'infrastructure d'orchestration autour du modèle
(boucle de contrôle, appels d'outils, gestion d'état/contexte, garde-fous, observabilité)

Variante 1: Omar = couche de supervision et gouvernance autour de la flotte
Variante 2: Omar = orchestrateur/superviseur (HITL) : intention, objectifs, budgets, permissions, validation
Variante 3: Le harness est socio-technique : outils + règles + CI/évals + décisions Omar
```

## Hypothèse Initiale

La **Variante 3** semble la plus précise : le "harness" n'est pas QUE Omar, mais Omar + l'écosystème (CLAUDE.md, rules, workflows, permissions). Omar est le **décisionnaire final** au sein de ce harness socio-technique.

Terme proposé à valider : **Human Control Plane** (Omar) au sein d'un **Socio-Technical Harness** (le système complet).

---

_Next: Phase 1 - Source Triangulation_
