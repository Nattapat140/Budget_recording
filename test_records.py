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
    @patch('builtins.input', side_effect=['100', 'a', 'food food 50', 'e'])
    def test_balance_file_not_found(self, mock_input, mock_open):
        """Test behavior when Balance.txt is not found."""
        mock_open.side_effect = FileNotFoundError()
        with patch('sys.stderr', new_callable=StringIO) as mock_stderr:
            Records()
            self.assertIn('File not found TT', mock_stderr.getvalue())

    @patch('builtins.input', side_effect=['a', 'food food 50', 'e'])
    def test_is_category_valid(self, mock_input):
        """Test category validation."""
        self.assertTrue(self.categories.is_category_valid('expense', self.categories._categories))
        self.assertFalse(self.categories.is_category_valid('invalid_category', self.categories._categories))

    @patch('builtins.input', side_effect=['a', 'food food 50', 'e'])
    def test_add_record(self, mock_input):
        """Test adding a valid record."""
        record_input = ['expense snack 50']
        self.records.add(record_input)
        self.assertIn('snack', self.records._records_book)

    @patch('builtins.input', side_effect=['e'])
    def test_view_records(self, mock_input):
        """Test viewing records."""
        self.records._records_book = 'expense snack 50,'
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.records.view()
            self.assertIn("Here's your expense and income records:", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['a', 'food food 50', 'e'])
    def test_find_category(self, mock_input, mock_stdout):
        """Test finding records by category."""
        self.records._records_book = 'expense food 50,income salary 1000,'
        subcategories = self.categories.find_subcategories('expense', self.categories._categories)
        self.records.find(subcategories, True)
        self.assertIn("food", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
