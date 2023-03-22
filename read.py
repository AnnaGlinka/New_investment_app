from get_currency import RealCurrency

with open('add_files_for_testing/currency_list_for_testing.txt') as list:
    currency = list.readlines()
    currency_list = eval(currency[0]) 

with open('add_files_for_testing/exchange_rates_for_testing.txt') as exchange:
    exchange = exchange.readlines()
    exchange_rates = eval(exchange[0])

with open('add_files_for_testing/merged_data_for_testing.txt') as merged:
    merged = merged.readlines()
    merged_currency = eval(merged[0])


rc = RealCurrency()
print(len(rc.merge_data(exchange_rates, currency_list)))
print("*****************************")

print(len(merged_currency))
