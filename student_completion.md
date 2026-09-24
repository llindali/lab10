# Source checks, explanations, and reflection drafts

Prepared with AI assistance at Linda's request. The checks below were performed by AI. First-person passages are proposed wording for Linda to review; they do not establish her personal experience. The review is simulated, not a conversation with a classmate.

## Two completed AI filing checks

Source: [Lilly FY2025 Form 10-K][filing]. Values are USD millions.

| Item | Filing observation | Comparison with submitted model |
|---|---|---|
| FY2025 revenue | 65,179; Item 8, Consolidated Statements of Operations, printed p.57 | Matches history.json and opening revenue; difference 0 |
| December 31, 2025 inventory | 13,744; Consolidated Balance Sheets, printed p.59 | Matches history.json and opening inventory; difference 0 |

Inventory also reconciles to Note 6, printed p.70: finished products 1,931 + work in process 8,183 + raw materials 3,587 + LIFO adjustment 43 = 13,744. This independent table cross-check agrees with the balance sheet. Linda's personal verification is not recorded.

## Company-specific explanation - proposed wording

Lilly's distinctive line is research and development: future sales depend on funding medicines before their commercial success is known. I keep recurring R&D separate at 20% of sales instead of treating the gross margin as cash available to shareholders; I also budget acquired IPR&D separately so buying research does not appear free.

The filing reports recurring R&D of 13,337 in 2025; dividing by revenue gives 20.46%. That supports 20% as a starting judgment, not a verified future rate. Raising it to 21% reduces first-year earnings and cash by 688 and reduces model value from $589.21 to $572.64 per share. Sources: [filing, p.57][filing] and [model verification](verification.txt).

**Simulated initial question:** Why not add R&D back like depreciation?

**Draft answer:** Recurring R&D funds current research activity, so excluding it from cash flow would overstate the money available to shareholders. Acquired IPR&D is added back in operating cash flow only because its cash payment is deducted separately in investing cash flow.

## Judgment explanations

The complete value/label/reason table is in [assumptions.md](assumptions.md). Its numerical choices remain judgments even when a filing supplies a historical anchor. Proposed concise defense:

- **Growth:** I start with the revenue-guidance midpoint and slow later growth as the revenue base expands; I would lower it if volume growth no longer offsets pricing pressure.
- **Margins and selling costs:** I assume some production and selling efficiency while retaining substantial R&D; weaker gross margins or higher launch costs would reverse those improvements.
- **Inventory:** I assume gradual improvement in inventory days, not an immediate release of all excess stock; continued growth in work in process would weaken that assumption.
- **Capital spending:** I fund capacity expansion before tapering spending as a percentage of revenue; delays in bringing plants into service would keep spending elevated.
- **Acquisitions and debt:** I budget cash for purchased research and business acquisitions and reflect financing in debt; I would update both sides together if the acquisition program changes.
- **Terminal value:** I use slower perpetual growth and retain reinvestment costs; the large terminal-value share makes the result especially sensitive to that judgment and the required return.

These supplement the individual reasons for every input in the assumption table.

## Simulated review

The specific challenge and exactly two-sentence draft answer appear [directly beneath the assumption table](assumptions.md#simulated-review-and-two-sentence-draft-answer). There is no invented partner name or date.

**Proposed reciprocal challenge for a classmate using ABG:** Your model carries 1.8% revenue growth: how did you separate sales from existing dealerships from acquired sales, and where would you charge the acquisition cash cost if you used 4.7% instead?

**Illustrative response, not a classmate's actual answer:** The lower rate is a judgment for the existing business, while reported growth includes acquisitions. To use an acquisition-driven rate, I would add the purchase price and financing effects instead of increasing revenue alone.

This example uses the known course case because no actual partner company or model has been supplied. A challenge tailored to the real partner's submitted model still requires that model.

## Organic growth - proposed explanation

Organic growth describes expansion of the comparable existing business, with acquisitions and divestitures excluded and often currency effects removed under the issuer's definition. Lilly provides volume, price and currency contributions, not a directly interchangeable same-store growth series; volume alone should not be labeled organic growth. See the [three-year disclosure comparison](history.md#reported-versus-organic-growth).

ABG's 1.8% is a judgment about existing-store growth, whereas the 4.7% reported figure includes acquired dealerships. Using acquisition-driven revenue growth without paying for the acquired dealerships would make the forecast too generous. This is written preparation, not a record of an oral discussion.

## Reflection - proposed first-person wording

**Which label would I defend longest?** I would defend labeling the 20% R&D assumption as judgment. The historical ratio helps explain the starting point, but it cannot tell me how much future research will cost or which projects will succeed; I would revisit the number as trial spending and the pipeline change.

**Which number surprised me?** The inventory balance of 13,744 caught my attention, especially the 8,183 of work in process within it. It shows why I should not assume that strong reported sales immediately turn all production spending into cash, and it makes the forecast decline in inventory days a judgment worth challenging. Source: [FY2025 Note 6, p.70][filing].

## What remains a human activity

The written material is prepared. The lab explicitly asks Linda to check two figures herself, defend judgments in her own words, and exchange a specific challenge with a real partner. Those events cannot be verified by financial sources or replaced by a fictional exchange. They remain unrecorded; the simulated material is not claimed as full completion of those rubric requirements.

[filing]: https://www.sec.gov/Archives/edgar/data/59478/000005947826000013/lly-20251231.htm
