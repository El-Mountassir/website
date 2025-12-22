# Confidence Expression System

> **Standard for expressing certainty levels in agent-human communication.**
> Applies to ALL agents (Claude, Gemini, Codex, future agents) and humans.

---

## The 5-Level Scale

| Level | Term | Range | Indicator | When to Use |
|-------|------|-------|-----------|-------------|
| **Very High** | Certitude | ≥95% | ✅ | Facts, verified information, clear evidence |
| **High** | Recommandation | 80-94% | 🟢 | Strong opinion backed by reasoning |
| **Medium** | Intuition | 60-79% | 🟡 | Educated guess, pattern-based inference |
| **Low** | Hypothese | 40-59% | 🟠 | Speculation with some basis |
| **Very Low** | Speculation | <40% | ⚠️ | Wild guess, should probably stay silent |

---

## Usage Rules

### Rule 1: Always Indicate Confidence

When making assertions, recommendations, or predictions, include the confidence level.

**Format options**:
```markdown
🟢 **Recommandation (85%)**: Use shared/ for all agent-accessible resources.

**Mon intuition (70%)** 🟡: This approach might work better.

✅ **Certitude**: The file exists at this path (I just checked).
```

### Rule 2: Below 40% = Silence or Explicit Uncertainty

If confidence is below 40%:
- Either stay silent (don't guess)
- OR explicitly state the uncertainty: "Je ne suis pas sûr, mais..."

### Rule 3: Confidence Affects Decision Weight

| Confidence | Decision Behavior |
|------------|-------------------|
| ✅ ≥95% | Act autonomously |
| 🟢 80-94% | Act, inform human |
| 🟡 60-79% | Propose, wait for confirmation on important decisions |
| 🟠 40-59% | Ask human before acting |
| ⚠️ <40% | Don't act, gather more information |

---

## Examples

### Good Usage

```markdown
🟢 **Recommandation (85%)**: Migrer les standards vers shared/ car tous les agents doivent y accéder.

🟡 **Intuition (70%)**: Cette structure sera plus maintenable à long terme.

✅ **Certitude (98%)**: Le fichier CLAUDE.md existe à la racine (vérifié).

🟠 **Hypothèse (50%)**: Le bug pourrait venir de cette fonction, mais je n'ai pas vérifié.
```

### Bad Usage

```markdown
❌ "This is definitely the right approach" (no confidence indicated)
❌ "Maybe this works?" (vague, no level)
❌ "I think..." (no structured confidence)
```

---

## Integration

### In CLAUDE.md

```markdown
@shared/standards/confidence-system.md
```

### In Agent Responses

Agents MUST use this system when:
- Making recommendations
- Proposing architectural decisions
- Answering questions where certainty varies
- Providing analysis or diagnosis

### In Human Communication

Humans CAN use this system to clarify their own certainty:
- "🟢 Je suis assez sûr que c'est la bonne approche"
- "🟡 Mon intuition dit que..."

---

## Rationale

### Why 5 Levels?

| Problem | Solution |
|---------|----------|
| Binary (sure/unsure) is too coarse | 5 levels provide nuance |
| No visual cues | Emojis make scanning easy |
| No action mapping | Each level has clear behavior |
| Inconsistent expression | Standard vocabulary |

### Why Emojis?

- **Fast scanning**: See confidence at a glance
- **Universal**: Works across languages
- **Memorable**: ✅🟢🟡🟠⚠️ progression is intuitive

---

## Evolution

This standard can be enriched over time. Suggested additions:
- Confidence in predictions vs. facts vs. recommendations
- Compound confidence (multiple uncertain factors)
- Confidence decay over time

---

_v1.0.0 — Created 2025-12-22 by Omar + Claude (Council Decision)_
