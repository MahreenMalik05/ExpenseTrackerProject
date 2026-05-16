import unittest
def calculate_total(expenses):
    """Return the sum of all expense amounts."""
    total = 0
    for expense in expenses:
        total += expense['amount']
    return total

def category_summary(expenses):
    """Return a dict mapping category -> total amount."""
    summary = {}
    for expense in expenses:
        cat = expense['category']
        summary[cat] = summary.get(cat, 0) + expense['amount']
    return summary

def delete_expense(expenses, index):
    """
    Remove expense at 1-based index.
    Returns the removed item, or None if index is invalid.
    """
    if 1 <= index <= len(expenses):
        return expenses.pop(index - 1)
    return None

def add_expense(expenses, category, amount, date):
    """
    Add a new expense dict to the list.
    Returns False (and does not add) if amount is negative or category is empty.
    """
    if not category or amount < 0:
        return False
    expenses.append({"category": category, "amount": amount, "date": date})
    return True

class TestAddExpense(unittest.TestCase):

    def setUp(self):
        self.expenses = []

    # TC-01
    def test_add_valid_expense(self):
        """TC-01: Adding a valid expense should succeed and increase list size."""
        result = add_expense(self.expenses, "Food", 500.0, "15-05-2026")
        self.assertTrue(result)
        self.assertEqual(len(self.expenses), 1)

    # TC-02
    def test_add_expense_correct_values(self):
        """TC-02: Stored values must exactly match the input."""
        add_expense(self.expenses, "Transport", 200.0, "10-05-2026")
        e = self.expenses[0]
        self.assertEqual(e['category'], "Transport")
        self.assertEqual(e['amount'],   200.0)
        self.assertEqual(e['date'],     "10-05-2026")

    # TC-03
    def test_add_negative_amount_rejected(self):
        """TC-03: Negative amounts must be rejected (returns False, list unchanged)."""
        result = add_expense(self.expenses, "Food", -100.0, "10-05-2026")
        self.assertFalse(result)
        self.assertEqual(len(self.expenses), 0)

    # TC-04
    def test_add_empty_category_rejected(self):
        """TC-04: Empty category string must be rejected."""
        result = add_expense(self.expenses, "", 300.0, "10-05-2026")
        self.assertFalse(result)

    # TC-05
    def test_add_zero_amount_accepted(self):
        """TC-05: Zero amount is a valid edge-case and should be accepted."""
        result = add_expense(self.expenses, "Miscellaneous", 0.0, "01-01-2026")
        self.assertTrue(result)


class TestViewExpenses(unittest.TestCase):

    # TC-06
    def test_empty_list(self):
        """TC-06: An empty expense list should have length 0."""
        expenses = []
        self.assertEqual(len(expenses), 0)

    # TC-07
    def test_multiple_expenses_stored(self):
        """TC-07: Multiple expenses should all be retrievable."""
        expenses = []
        add_expense(expenses, "Food",      500, "01-05-2026")
        add_expense(expenses, "Transport", 200, "02-05-2026")
        add_expense(expenses, "Utility",   300, "03-05-2026")
        self.assertEqual(len(expenses), 3)


class TestCalculateTotal(unittest.TestCase):

    # TC-08
    def test_total_correct(self):
        """TC-08: Total should equal the sum of all amounts."""
        expenses = [
            {"category": "Food",      "amount": 500, "date": "01-05-2026"},
            {"category": "Transport", "amount": 300, "date": "02-05-2026"},
        ]
        self.assertEqual(calculate_total(expenses), 800)

    # TC-09
    def test_total_empty_list(self):
        """TC-09: Total of an empty list must be 0."""
        self.assertEqual(calculate_total([]), 0)

    # TC-10
    def test_total_single_expense(self):
        """TC-10: Total with one expense equals that expense's amount."""
        expenses = [{"category": "Food", "amount": 150, "date": "05-05-2026"}]
        self.assertEqual(calculate_total(expenses), 150)


class TestCategorySummary(unittest.TestCase):

    # TC-11
    def test_summary_groups_correctly(self):
        """TC-11: Expenses with the same category should be summed together."""
        expenses = [
            {"category": "Food", "amount": 200, "date": "01-05-2026"},
            {"category": "Food", "amount": 300, "date": "02-05-2026"},
        ]
        summary = category_summary(expenses)
        self.assertEqual(summary["Food"], 500)

    # TC-12
    def test_summary_multiple_categories(self):
        """TC-12: Different categories must be tracked separately."""
        expenses = [
            {"category": "Food",      "amount": 400, "date": "01-05-2026"},
            {"category": "Transport", "amount": 100, "date": "02-05-2026"},
        ]
        summary = category_summary(expenses)
        self.assertEqual(summary["Food"],      400)
        self.assertEqual(summary["Transport"], 100)

    # TC-13
    def test_summary_empty_list(self):
        """TC-13: Summary of empty list should be an empty dict."""
        self.assertEqual(category_summary([]), {})


class TestDeleteExpense(unittest.TestCase):

    def setUp(self):
        self.expenses = [
            {"category": "Food",      "amount": 100, "date": "01-05-2026"},
            {"category": "Transport", "amount": 200, "date": "02-05-2026"},
            {"category": "Utility",   "amount": 300, "date": "03-05-2026"},
        ]

    # TC-14
    def test_delete_valid_index(self):
        """TC-14: Deleting at a valid index should reduce list length by 1."""
        delete_expense(self.expenses, 2)
        self.assertEqual(len(self.expenses), 2)

    # TC-15
    def test_delete_correct_item_removed(self):
        """TC-15: The correct item (by 1-based index) should be removed."""
        removed = delete_expense(self.expenses, 1)
        self.assertEqual(removed['category'], "Food")

    # TC-16
    def test_delete_invalid_index_returns_none(self):
        """TC-16: An out-of-range index must return None and not change the list."""
        result = delete_expense(self.expenses, 99)
        self.assertIsNone(result)
        self.assertEqual(len(self.expenses), 3)

    # TC-17
    def test_delete_zero_index_invalid(self):
        """TC-17: Index 0 is invalid (1-based) and must be rejected."""
        result = delete_expense(self.expenses, 0)
        self.assertIsNone(result)

    # TC-18
    def test_delete_last_item(self):
        """TC-18: Deleting the last item should leave the list one shorter."""
        delete_expense(self.expenses, 3)
        self.assertEqual(len(self.expenses), 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
