# Platform Operations Rules — Villa Thaifa

> **CRITICAL**: Ces règles s'appliquent à TOUTE opération sur HotelRunner, Booking.com, ou autre plateforme.
> Zero tolerance — Une erreur peut affecter des réservations clients.

---

## ⚠️ Confidence-Based Action Rule

> **Si confiance < 90% → STOP EVERYTHING et DEMANDE à Omar.**

### Contextes concernés

| Contexte              | Exemples                         |
| --------------------- | -------------------------------- |
| Platform operations   | HotelRunner, Booking.com clicks  |
| Room/pricing changes  | Room selection, rate adjustments |
| Client-facing actions | Reservations, cancellations      |
| Irreversible actions  | Submissions, confirmations       |

### Pattern

```
1. PAUSE before clicking/submitting
2. VERIFY against documentation (state/current/rooms.md, etc.)
3. If unsure → STOP → ASK → Wait for confirmation
4. NEVER guess or assume on platform operations
```

**Background**: Ajouté 2025-12-22 après near-miss Chambre 11.

---

## ⚠️ Date/Detail Verification Rule

> **TOUJOURS répéter les détails clés à Omar AVANT d'exécuter.**

| Détail             | Action                                       |
| ------------------ | -------------------------------------------- |
| **Dates**          | Répéter "Du X au Y" et attendre confirmation |
| **Numéro chambre** | Confirmer "Chambre X" explicitement          |
| **Nom invité**     | Épeler le nom                                |
| **Prix**           | Annoncer le total avant soumission           |

### Pattern réservations

```
1. PARSE the request carefully
2. REPEAT BACK: "Je vais créer: Chambre X, du DD au DD/MM, nom: Y, prix: Z"
3. WAIT for "oui" or correction
4. THEN execute
```

**Background**: Ajouté 2025-12-22 après erreur date ("25 au 27" au lieu de "24 au 27").

---

## ⚠️ Use Exact System Values

> **JAMAIS calculer/approximer — utiliser la valeur EXACTE de la plateforme.**

| ❌ Faux              | ✅ Correct                        |
| -------------------- | --------------------------------- |
| "4500 DH (3 × 1500)" | "4.512,21 MAD" (from HotelRunner) |
| "~280€"              | "280,00 €" (exact)                |

**Règle**: Toujours copier le total final de HotelRunner/Booking.com. Les systèmes peuvent ajouter frais, taxes, ou arrondis.

---

## ⛔ State File Protection

> **FULL STOP requis avant toute modification destructive des fichiers state.**

| Type d'action                    | Confirmation requise |
| -------------------------------- | -------------------- |
| Écraser données existantes       | ✅ MUST ASK          |
| Remplacer valeurs (pas ajouter)  | ✅ MUST ASK          |
| Supprimer/retirer informations   | ✅ MUST ASK          |
| Changer compteurs/métriques      | ✅ MUST ASK          |
| Ajouter NOUVELLES données à côté | ❌ OK to proceed     |

### Pattern pour updates state

```
1. READ current state carefully
2. IDENTIFY what exists vs what's new
3. ADD new data WITHOUT removing existing
4. If modification needed → STOP → ASK OMAR
```

### Exemple (rooms.md)

- ❌ BAD: "Room types: 9" → "Room types: 8" (destroyed data)
- ✅ GOOD: Add "Room types (Booking.com): 8" alongside existing

> **Rationale**: State files = SSOT. Différentes plateformes peuvent avoir différentes données.

---

## Checklist pré-exécution

Avant toute action plateforme:

- [ ] Confiance > 90% ?
- [ ] Détails répétés à Omar ?
- [ ] Valeurs exactes (pas calculées) ?
- [ ] State files non modifiés destructivement ?

Si une réponse est NON → **STOP** et ajuste.

---

_Platform Operations Rules v1.0.0 — Zero Tolerance_
