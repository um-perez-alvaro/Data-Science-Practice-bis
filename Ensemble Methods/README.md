The **Data folder** contains the following data:

- Untagged_Transactions.csv: transaction data from on an online store
- Account_Info.csv: Anonomyzed account information
- Fraud_Transactions.csv: transactions identified as fraud


**Untagged_Transactions.csv** contain the following fields:

Columns	|	Description
--- | --- 
transactionID |	Unique transaction Id
accountID	|	Unique account Id
transactionAmountUSD	|	Transaction amount in USD e.g., 12345.00
transactionAmount	|	Transaction amount in currency expressed in transactionCurrencyCode e.g., 12345.00
transactionCurrencyCode	|	Currency code of the transaction. 3 alphabet letters, e.g., USD
transactionCurrencyConversionRate	|	Conversion rate to US Dollars, e.g. 1.0000 for USD to USD
responseCode	|	response code from card issuer payment authorization
digitalItemCount	|	Number of digital items purchased. (e.g. music, ebook, software, etc, that can be directly downloaded online)
physicalItemCount |	Number of physical items purchased (that needs to be shipped)
purchaseProductType	|	Type of product purchased
shippingAddress	|	shipping street address
shippingPostalCode	|	shipping postal code
shippingCity	|	shipping city
shippingState	|	shipping state
shippingCountry	|	shipping country (3-alpha)
