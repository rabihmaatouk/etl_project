import pandas as pd

# Create a DataFrame with client data
data = {
    'client_id': ['C001', 'C002'],
    'name': ['John Doe', 'Jane Smith'],
    'email': ['john.doe@example.com', 'jane.smith@example.com'],
    'date_of_birth': ['1985-05-12', '1990-08-23'],
    'country': ['USA', 'UK'],
    'account_balance': [10000.00, 15000.00]
}

clients_df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
clients_df.to_csv('clients.csv', index=False)

