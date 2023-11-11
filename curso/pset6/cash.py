from cs50 import get_float

# Change for US locale
change = get_float("Quanto de dinheiro é devido? ")
print("You entered: ", change)

while change < 0:
    print("Insira um valor não negativo.")
    change = get_float("Enter the value that is not negative: ")

# Coins denominations in cents
denominations = [25, 10, 5, 1]

min_coins = 0
remainder = round(change * 100)

for coin in denominations:
    count = remainder // coin
    min_coins += count
    remainder %= coin

print(min_coins)