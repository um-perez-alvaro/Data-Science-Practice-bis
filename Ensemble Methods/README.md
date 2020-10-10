# Ensemble Methods and Random Forests

## Jupyter notebooks

- [Decision Trees]()
- [Random Forests]()
- [Gradient Tree Boosting]()

## Homework ()
- [1]()
- [2]()
- [3]()

## In-class project ()
- [Credit Card Fraud Detection]()

## Datasets

Filename | Description |  Source
--- | --- |  --- 
flights2015 | national flights that took place in the US territory in 2015 as well as information about the airlines and the airports |  [U.S. Department of Transportation’s (DOT) Bureau of Transportation Statistics](https://www.bts.gov/) <br> also [Kaggle](https://www.kaggle.com/c/flight-delays-spring-2018)


## Project Dataset

The **Data folder** contains the following data:

- Untagged_Transactions.csv: transaction data from on an online store
- Account_Info.csv: Anonomyzed account information
- Fraud_Transactions.csv: transactions identified as fraud


**Untagged_Transactions.csv** contains the following fields:

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
cvvVerifyResult	| M-- CVV2 Match <br> N-- CVV2 No Match <br> P--Not Processed <br> S--Issuer indicates that CVV2 data should be present on the card, but the merchant has indicated data is not present on the card <br> U--Issuer has not certified for CVV2 or Issuer has not provided Visa with the CVV2 encryption keys Empty--Transaction failed because wrong CVV2 number was entered or no CVV2 number was entered
paymentInstrumentID	|	ID of payment Instrument: e.g. credit card number (hashed or encrypted) e.g. paypal account Id
paymentBillingAddress	|	Street Address , hashed or encrypted
paymentBillingPostalCode	|	payment billing postal code
paymentBillingState	|	payment billing state
paymentBillingCountryCode	|	payment billing country code
paymentBillingName	|	Name, hashed or encrypted, needs to be consistent with other names
isProxyIP	|	Whether the IP address is a proxy or not
browserType	|	I -- IE <br> C -- Chrome <br> F -- Firefox <br> O -- Other
browserLanguage	|	Similar to country code
paymentInstrumentType	|	Type of payments: <br> C -- Credit Card <br> D -- Debit Card <br> P -- Paypal <br> K -- Check <br> H -- Cash <br> O -- Other
cardType	|	Type of cards <br> M -- Magnetic <br> C -- Chip
cardNumberInputMethod	|	Input method of payment instrument number: <br> K -- Keyed <br> S -- Swiped <br> C --- Chip <br> D -- Contactless
transactionDeviceType	|	P -- PC <br> M -- Mobile Devices <br> C -- Console (e.g. Xbox, DVD) <br> O -- Other
transactionDeviceId	|	Mac Address, or Hardware ID like serial number
transactionIPaddress	|	Full IP Address for IPv4: 000.000.000.000
ipState	|	State of IP address originated from 2 alphabet letters
ipPostcode	|	Postal Code of IP address originated from
ipCountryCode	|	Country code of IP address originated from
transactionDate	|	Date when transaction occured Typically in the time zone of the processor, Format: yyyymmdd, e.g., 20000101
transactionTime	|	Time when transaction occurred. Typically in the time zone of processing end. Format: hhmmss, eg. 153059
localHour	|	The hour in local time. Value of 0-23
transactionScenario	|	A -- Authorization <br> O -- Others
transactionType	|	Type of transaction: <br> P -- Purchase <br> R -- Refund <br> T -- Transfer <br> O -- Other
transactionMethod	|	I -- Internet (Online) Order <br> P -- Phone order <br> M -- Mail order <br> O -- Other

**Account_Info.csv** contains the following fields:

Columns	|	Description
--- | --- 
transactionDate	|	Date when transaction occured Typically in the time zone of the processor. Format: yyyymmdd, e.g., 20000101
transactionTime	|	Time when transaction occurred. Typically in the time zone of processing end. Format: hhmmss, eg. 153059
accountOwnerName	|	User name (hashed/encrypted)
accountAddress	|	User street address
accountPostalCode	|	User postal code
paymentInstrumentAgeInAccount	|	Age of payment instrument in the account
numPaymentRejects1dPerUser	|	Number of payment rejection in one day of this user
accountCity	|	User city
accountState	|	User state
accountCountry	|	User country (3-alpha)
accountOpenDate	|	Account open date. Format: yyyymmdd
accountAge	|	Age of user account in number of days
isUserRegistered	|	Whether the user is registered or not

**Fraud_Transactions.csv** contains the following fields:

Columns	|	Description
--- | --- 
transactionID	|	Unique transaction Id
accountID	|	Unique account Id
transactionAmount	|	Transaction amount in currency expressed in transactionCurrencyCode e.g., 12345.00
transactionCurrencyCode	|	Currency code of the transaction. 3 alphabet letters, e.g., USD
transactionDate	|	Date when transaction occured Typically in the time zone of the processor. Format: yyyymmdd, e.g., 20000101
transactionTime	|	Time when transaction occurred. Typically in the time zone of processing end. Format: hhmmss, eg. 153059
localHour	|	The hour in local time. Value of 0-23
transactionDeviceId	|	Mac Address, or Hardware ID like serial number
transactionIPaddress	|	Full IP Address for IPv4: 000.000.000.000
