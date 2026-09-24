# Lab 10 - Eli Lilly (LLY) pro-forma

**Student author and submitter: Linda Li.** This is Linda's individual lab, prepared with AI assistance.

**Review partner: Annika Rao** ([rao229@purdue.edu](mailto:rao229@purdue.edu)). Annika is the review partner, not the author or submitter of this lab.

**Question: What are five years of Eli Lilly's statements worth, built from assumptions I can defend?**

The proposed FY2026-2030 base case produces **$589.21 per diluted share**, with all five years balancing and cash above the $5,000 million floor. This is an annual course scenario, not an investment recommendation. Linda has confirmed her personal filing checks and verification with her real partner. The [completion record](student_completion.md) includes that confirmation, the AI-assisted review account, and separately labeled reflection drafts and practice material.

## Run and review

Python 3, standard library only. Run from this repository:

```sh
python proforma_lly.py
python -m unittest -v
```

| File | Purpose |
|---|---|
| [history.md](history.md) | Three years of filing-sourced history, ratios, growth disclosures, provider capex comparison, and opening balance sheet |
| [history.json](history.json) | Machine-readable historical inputs and source URLs |
| [assumptions.md](assumptions.md) | Three-column value / label / reason table, plus space for the real partner review |
| [proforma_lly.py](proforma_lly.py) | Personalized three-statement engine, check block and FCFE valuation |
| [output.txt](output.txt) | Full saved income statements, balance sheets, cash flows, checks and valuation |
| [test_proforma.py](test_proforma.py) | Eight tests covering accounting, sensitivity, funding failure and valuation refusal |
| [verification.txt](verification.txt) | Test results, deliberate failure messages, and R&D sensitivity |
| [student_completion.md](student_completion.md) | Personally confirmed checks, partner-review confirmation, proposed explanations and reflections |

## Reopen and rerun: Lab 09 prerequisite

The existing Lab 09 `proforma.py` was rerun before this build. It reproduced ABG's **$291.75 per share**, and all four of its known-answer/failure tests passed. This lab saves Lilly's engine as a new Python file. It does not overwrite the ABG model. The source model is in the existing course workspace's `lab9` folder; its method was adapted here.

## Define and represent

Company: **Eli Lilly and Company, NYSE: LLY**. The company-specific line is **recurring research and development**: the model expenses it separately at 20% of revenue and carries its cost into net income, operating cash flow and equity. It also separately budgets acquired IPR&D and rebates. Lilly has no modeled dealer floor-plan borrowing; ordinary debt funds the acquisition budget and suppliers/rebate accruals affect working capital.

The [history grid](history.md) traces FY2023, FY2024 and FY2025 revenue, gross profit, SG&A, income, inventory, PP&E and equity to the three 10-Ks. It adds the inputs needed for inventory days, depreciation, tax, growth and capital-spending ratios. All proposed judgment reasons appear in [assumptions.md](assumptions.md). Their student-authored status remains pending Linda's review and wording.

## Implement: how the statements connect

The engine computes earnings, then noncash assets/liabilities, then operating, investing and financing cash flows. Ending cash is opening cash plus the three cash-flow totals. It is never chosen to force the balance sheet to balance.

Reported gross margin, SG&A and R&D already contain depreciation/amortization. The model does not subtract D&A a second time in the income statement. It adds D&A back once in operating cash flow and reduces PP&E/intangibles in their roll-forwards. Capital spending increases PP&E and reduces investing cash flow. Acquired IPR&D reduces earnings, is added back in CFO, then paid in CFI, so it consumes cash once. Capitalized business acquisitions are a separate asset addition and cash use.

Receivables, inventory, prepaids, payables and rebate liabilities determine working capital. Their net change affects CFO. Taxes are paid as expensed, with no modeled deduction for acquired IPR&D. Net ordinary borrowing increases cash and debt; dividends and buybacks reduce cash and equity. A hypothetical revolver draws only when needed for the cash floor. Funding beyond its limit stops valuation.

## Validate: five-year results

USD millions, except per-share value.

| Line | 2026E | 2027E | 2028E | 2029E | 2030E |
|---|---:|---:|---:|---:|---:|
| Revenue | 86,000.00 | 107,500.00 | 129,000.00 | 148,350.00 | 163,185.00 |
| Recurring R&D | 17,200.00 | 21,500.00 | 25,800.00 | 29,670.00 | 32,637.00 |
| Net income | 26,283.52 | 36,122.62 | 45,311.72 | 53,443.88 | 58,807.03 |
| FCFE | 17,950.90 | 23,327.30 | 32,122.60 | 40,714.90 | 47,960.71 |
| Ending cash | 14,718.90 | 31,221.20 | 56,177.54 | 89,367.89 | 129,427.80 |
| Revolver draw | 0 | 0 | 0 | 0 | 0 |
| Assets - liabilities - equity | 0 | 0 | 0 | 0 | 0 |

The full check block also verifies income, cash flows, PP&E, intangibles, debt, revolver, equity, working capital and FCFE. Each displayed gap is zero; calculation tolerance is $0.01 million. No base-case year draws the revolver because available cash and financing cover investment and distributions. Every base-case year has positive FCFE.

All eight tests pass. Freezing FY2026 cash at its opening value causes a **-$7,450.90 million** balance-sheet gap and valuation refuses. A 100%-of-revenue capex stress exhausts the revolver and breaches the cash floor even though accounting still balances; valuation refuses that case too. Increasing R&D from 20% to 21% of sales reduces FY2026 net income and cash by **$688 million**, demonstrating that the company-specific line affects the statements. See [verification.txt](verification.txt).

## Value and compare with the market

FCFE is CFO + CFI + net borrowing, before shareholder distributions. Discount it at 10% for years 1-5. Terminal value is `2030 FCFE * 1.025 / (0.10 - 0.025)`, discounted five years. Add $2,268 million of opening cash above the floor once. Debt is already reflected in levered cash flows; do not subtract it again. Do not add ending accumulated cash because those forecast cash flows have already been valued.

| Component | USD millions |
|---|---:|
| Present value of explicit FCFE | 117,320.59 |
| Present value of terminal cash flows | 406,990.98 |
| Opening excess cash | 2,268.00 |
| Total modeled equity value | 526,579.57 |
| Fixed diluted share proxy, millions | 893.7 |
| Value per share, USD | 589.21 |

**The model says $589.21 per share; the market observation is $1,188.87 on September 24, 2026, using the same 893.7 million diluted-share proxy for the equity comparison; what growth, research productivity and reinvestment would reconcile this gap?** The price comes from the dated Close column on [ChartExchange](https://chartexchange.com/symbol/nyse-lly/historical/); the share proxy comes from [Lilly's Q2 2026 10-Q](https://www.sec.gov/Archives/edgar/data/59478/000005947826000081/lly-20260630.htm), p.5. Price times this proxy is $1,062,493.12 million; it is not a claim about the exchange's reported basic market cap.

**Timing limitation:** the course engine discounts five full annual forecasts to December 31, 2025, using information obtained in September 2026. The market observation is September 24, 2026. This is a transparent comparison of an annual teaching scenario with today's price, not a valuation rolled forward to today's date or a historical backtest. No buy/sell recommendation or reliable current-date discount is inferred.

Terminal value supplies **77.29%** of total value. The growth slowdown, perpetual reinvestment, discount rate and future research productivity deserve scrutiny. The acquisition allocation, amortization, debt refinancing, noncontrolling-interest treatment and fixed share count are explicitly simplified; see the assumption table. Later actual transactions could require a different capital structure. The model's large accumulated cash balance is not added again to value.

If a later scenario produces negative FCFE, retain it in the statements and print that label. The lab's positive-only valuation convention assigns zero to such explicit years, which is more optimistic than deducting funding deficits in an ordinary DCF. A nonpositive terminal FCFE makes the model refuse: a growing negative cash flow cannot support a defensible positive going-concern perpetuity without a separate recovery case.

## Evolve, learn and reflect

The [growth discussion](history.md#reported-versus-organic-growth) explains organic growth, Lilly's volume/price/FX disclosures, and ABG's 1.8% versus 4.7%. No separate consistent Lilly organic-growth series was identified, so none is invented.

The inventory challenge and two-sentence answer appear directly below the assumption table, with Linda's confirmation that she verified the review with her real partner. The account retains AI-assisted wording rather than claiming to be a verbatim transcript. A proposed reciprocal ABG challenge and reflection drafts remain separately labeled in [student_completion.md](student_completion.md); no actual partner company has been supplied.

## Rubric coverage and checkout

| Criterion, 5 points each | Evidence and remaining work |
|---|---|
| History and sources | Three-year grid, sources and ratios complete; Linda confirmed two personal filing checks. FY2025 parent-only equity is not separately disaggregated; consolidated equity is verified. |
| Assumptions and labels | All forecast inputs labeled with proposed reasons; Linda's own wording pending. |
| Statements and checks | Five balanced years, full cash flows, per-share value and deliberate refusal tests complete. |
| Personalization | R&D, acquired IPR&D and rebate financing modeled; R&D sensitivity verified. Linda's explanation to a partner pending. |
| Partner review | Inventory challenge and two-sentence account confirmed by Linda after partner verification; reciprocal ABG challenge remains illustrative until the actual partner model is identified. |

No full-score claim is made while student activities are pending. Submit individual GitHub links to this README, history, assumptions, Python model, and supporting output/tests as needed. AI assisted with research, implementation, verification and draft explanations.

Course references: [Lab 10 instructions](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-05/lab-10-proforma-your-company.md), [Week 5 overview](https://github.com/CinderZhang/FIN43900-Fall2026/tree/main/lessons/week-05), and [Part 1 tutorial](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-05/pro-forma-abg-tutorial.md).
