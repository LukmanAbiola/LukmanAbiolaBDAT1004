#!/usr/bin/env python
# coding: utf-8

# In[7]:


def curconv(currency):
    rates = {
        'AUD': 1.0345157,
        'CHF': 1.0237414,
        'CNY': 0.1550176,
        'DKK': 0.1651442,
        'EUR': 1.2296544,
        'GBP': 1.5550989,
        'HKD': 0.1270207,
        'INR': 0.0177643,
        'JPY': 0.01241401,
        'MXN': 0.0751848,
        'MYR': 0.3145411,
        'NOK': 0.1677063,
        'NZD': 0.8003591,
        'PHP': 0.0233234,
        'SEK': 0.148269,
        'SGD': 0.788871,
        'THB': 0.0313789
    }

    if currency in rates:
        return rates[currency]
    else:
        return None

currency_code = 'EUR'
rate = curconv(currency_code)
if rate is not None:
    print(f"The currency rate for {currency_code} is {0.01241401}.")
else:
    print(f"Currency code {currency_code} is not found.")


# In[3]:


## B


# In[ ]:





# In[5]:


def curconv(currency, amount):
    rates = {
        'AUD': 1.0345157,
        'CHF': 1.0237414,
        'CNY': 0.1550176,
        'DKK': 0.1651442,
        'EUR': 1.2296544,
        'GBP': 1.5550989,
        'HKD': 0.1270207,
        'INR': 0.0177643,
        'JPY': 0.01241401,
        'MXN': 0.0751848,
        'MYR': 0.3145411,
        'NOK': 0.1677063,
        'NZD': 0.8003591,
        'PHP': 0.0233234,
        'SEK': 0.148269,
        'SGD': 0.788871,
        'THB': 0.0313789
    }

    if currency in rates:
        usd_amount = amount * rates[currency]
        return usd_amount
    else:
        return None

# Example usage
currency_code = 'EUR'
amount = 50
converted_amount = curconv(currency_code, amount)
if converted_amount is not None:
    print(f"The amount {amount} {currency_code} is equivalent to {converted_amount} USD.")
else:
    print(f"Currency code {currency_code} is not found.")


# In[ ]:




