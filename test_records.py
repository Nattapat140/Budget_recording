import unittest
from io import StringIO
from unittest.mock import patch
from expense_recorded import Record, Records, Categories

class TestRecords(unittest.TestCase):
    def setUp(self):
        """Set up a mock Records instance and other preparations."""
        self.records = Records()
        self.categories = Categories()
    
    @patch('builtins.open')
    def test_balance_file_not_found(self, mock_open):
        """Test behavior when Balance.txt is not found."""
        mock_open.side_effect = FileNotFoundError()
        with patch('sys.stderr', new_callable=StringIO) as mock_stderr:
            Records()
            self.assertIn('File not found TT', mock_stderr.getvalue())

    def test_is_category_valid(self):
        """Test category validation."""
        self.assertTrue(self.categories.is_category_valid('expense', self.categories._categories))
        self.assertFalse(self.categories.is_category_valid('invalid_category', self.categories._categories))

    def test_add_record(self):
        """Test adding a valid record."""
        record_input = ['expense snack 50']
        with patch('builtins.input', side_effect=record_input):
            self.records.add(record_input)
            self.assertIn('snack', self.records._records_book)

    def test_view_records(self):
        """Test viewing records."""
        self.records._records_book = 'expense snack 50,'
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.records.view
            self.assertIn("Here's your expense and income records:", mock_stdout.getvalue())

    def test_find_category(self):
        """Test finding records by category."""
        self.records._records_book = 'expense snack 50,income salary 1000,'
        subcategories = self.categories.find_subcategories('expense', self.categories._categories)
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.records.find(subcategories, True)
            self.assertIn("snack", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
