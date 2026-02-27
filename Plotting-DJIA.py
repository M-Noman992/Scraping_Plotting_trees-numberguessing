import matplotlib.pyplot as plt

opening_prices = [34000, 33508, 33000, 32500, 34000, 34500, 35000, 35500, 34000, 33000, 32000, 31000]
closing_prices = [34500, 33000, 32500, 34000, 33500, 35000, 35500, 36000, 35000, 34000, 33000, 32000]
date_range = ['2022-01', '2022-02', '2022-03', '2022-04', '2022-05', '2022-06', '2022-07', '2022-08', '2022-09', '2022-10', '2022-11', '2022-12']

plt.figure(figsize=(10, 5))

plt.plot(date_range, opening_prices, label='Opening Prices', color='orange')
plt.plot(date_range, closing_prices, label='Closing Prices', color='blue')

plt.title("DJIA Opening and Closing Prices")
plt.xlabel("Date")
plt.ylabel("Price")

plt.xticks(rotation=40)
plt.legend()
plt.grid(True)

plt.show()