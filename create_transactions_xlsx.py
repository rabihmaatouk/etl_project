import pandas as pd

# Create a DataFrame with transaction data
data = {
    'transaction_id': ['T001', 'T002', 'T003'],
    'client_id': ['C001', 'C001', 'C002'],
    'transaction_type': ['buy', 'sell', 'buy'],
    'transaction_date': ['2023-10-01', '2023-10-05', '2023-10-10'],
    'amount': [200.00, -100.00, 150.00],
    'currency': ['USD', 'USD', 'GBP']
}

transactions_df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
transactions_df.to_excel('transactions.xlsx', index=False)
