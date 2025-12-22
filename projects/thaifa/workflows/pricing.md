# Workflow : Mise à Jour Tarifs

> Process pour modifier les prix sur HotelRunner/Booking.com.

---

## Prérequis

- [ ] Lire `state/current/rooms.md` (tarifs actuels)
- [ ] Lire `state/planned/pricing.md` (changements prévus)
- [ ] Validation Omar sur les nouveaux tarifs

---

## Étapes

### 1. BASELINE — Capturer état actuel

```bash
cp state/current/rooms.md state/baseline/rooms-YYYY-MM-DD.md
```

### 2. PLAN — Documenter les changements

```
Mettre à jour state/planned/pricing.md :
- Ancien tarif
- Nouveau tarif
- Raison du changement
- Date d'effet
```

### 3. CONFIRM — Validation Omar

```
Présenter tableau comparatif :
| Chambre | Ancien | Nouveau | Delta |
Attendre validation explicite
```

### 4. EXECUTE — Appliquer sur HotelRunner

```
1. Ouvrir app.hotelrunner.com
2. Navigation : Rates → Room Rates
3. Modifier les tarifs
4. Vérifier propagation vers OTAs
```

### 5. VERIFY — Confirmer sur Booking.com

```
1. Ouvrir admin.booking.com
2. Vérifier que les tarifs sont synchronisés
3. Screenshot de confirmation
```

### 6. UPDATE STATE

```
1. Mettre à jour state/current/rooms.md
2. Log dans state/execution/YYYY-MM-DD/pricing.md
3. Ajouter entrée dans state/historical/changelog-pricing.md
```

---

## Points d'attention

| Risque | Mitigation |
|--------|------------|
| Désync HotelRunner/Booking | Vérifier propagation après 15 min |
| Erreur de saisie | Double-check avant validation |
| Promotions en conflit | Vérifier `state/current/promotions.md` |

---

_Workflow v1.0.0_
