price_of_location_per_night = 5500
nights = 3

price_per_pizza = 240000
pizza_num = 4

price_per_soda = 35000
soda_num = 4


price_of_location = price_of_location_per_night * nights
price_of_pizza = price_per_pizza * pizza_num
price_of_soda = price_per_soda * soda_num

all_prices = price_of_location + price_of_pizza + price_of_soda

print(all_prices)