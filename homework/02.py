prices=[25,15,32,8,45,13,67,23]

max_price=max(prices)
min_price=min(prices)
total_price=sum(prices)
count_over_20=len([i for i in prices if i>20])

print("Most expensive:",max_price)
print("Cheapest:",min_price)
print("Total:",total_price)
print("Quantity of products at price>20:",count_over_20)