"""Accounting, funding, and economically meaningful sensitivity checks."""
import copy
import math
import unittest
from unittest.mock import patch
import proforma_lly as m


class ModelTests(unittest.TestCase):
    def test_opening_and_five_years_balance(self):
        self.assertAlmostEqual(m.assets(m.OPENING), 112476.)
        self.assertAlmostEqual(m.liabilities_equity(m.OPENING), 112476.)
        years = m.project()
        m.validate(years)
        self.assertEqual([y['year'] for y in years], list(range(2026,2031)))
        self.assertTrue(all(y['cash'] >= m.MIN_CASH for y in years))
        self.assertTrue(all(y['fcfe'] > 0 for y in years))
        # Independently assembled FY2026 net income, including non-deductible IPR&D.
        pretax = 86000*.84*(1-.20)-86000*.20-5000-42503*.035
        self.assertAlmostEqual(years[0]['net_income'], pretax-(pretax+5000)*.20)
        v = m.value_equity(years)
        self.assertAlmostEqual(v['equity']/m.SHARES, v['per_share'])

    def test_frozen_cash_refuses_value(self):
        years = m.project()
        years[0]['cash'] = m.OPENING['cash']
        with self.assertRaisesRegex(ValueError, 'FY2026 Assets - liabilities - equity'):
            m.value_equity(years)

    def test_rd_cost_flows_to_earnings_cash_and_value(self):
        base, more_rd = m.project(), m.project(rd_ratio=.21)
        m.validate(more_rd)
        self.assertAlmostEqual(base[0]['net_income']-more_rd[0]['net_income'], 688.)
        self.assertAlmostEqual(base[0]['cash']-more_rd[0]['cash'], 688.)
        self.assertLess(m.value_equity(more_rd)['per_share'], m.value_equity(base)['per_share'])

    def test_capex_changes_cash_and_ppe_without_instant_expense(self):
        base = m.project_year(m.OPENING,0)
        more = m.project_year(m.OPENING,0,capex_ratio=.14)
        self.assertAlmostEqual(more['ppe']-base['ppe'],860.)
        self.assertAlmostEqual(base['cash']-more['cash'],860.)
        self.assertAlmostEqual(base['net_income'],more['net_income'])

    def test_funding_shortfall_refuses_even_if_balanced(self):
        years = m.project(capex_ratio=1.)
        self.assertAlmostEqual(m.assets(years[0]),m.liabilities_equity(years[0]))
        self.assertEqual(years[0]['draw'],m.REVOLVER_LIMIT)
        with self.assertRaisesRegex(ValueError, 'Cash floor shortfall'):
            m.value_equity(years)

    def test_corrupted_cash_flow_link_refuses(self):
        years = m.project()
        years[2]['cfo'] += 100
        with self.assertRaisesRegex(ValueError,'FY2028 Cash flow statement gap'):
            m.value_equity(years)

    def test_nonfinite_values_and_bad_discount_rates_refuse(self):
        years = m.project()
        years[0]['cash'] = math.nan
        with self.assertRaisesRegex(ValueError,'non-finite'):
            m.value_equity(years)
        for r,g in ((.1,.1),(.09,.1),(math.nan,.025)):
            with self.assertRaises(ValueError):
                m.value_equity(m.project(),r,g)

    def test_negative_terminal_cash_flow_refuses(self):
        # Large opening liquidity allows the loss scenario to pass funding checks.
        opening = copy.deepcopy(m.OPENING)
        opening['cash'] += 1000000
        opening['equity'] += 1000000
        with patch.object(m,'OPENING',opening):
            years = m.project(rd_ratio=.70)
            m.validate(years)
            self.assertLess(years[-1]['fcfe'],0)
            with self.assertRaisesRegex(ValueError,'terminal FCFE'):
                m.value_equity(years)


if __name__ == '__main__':
    unittest.main(verbosity=2)
