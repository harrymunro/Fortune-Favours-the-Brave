from numpy import random
import matplotlib.pyplot as plt

__version__ = "1.0"

print """
\n--------------------------
\nFortune Favours the Brave
\n--------------------------
"""
# Pause for 3 seconds

# Ask for players name
name = raw_input("\nWhat is your name? ")

# Speel about dead family and inheritance of $10,000

# Variables
# Age of death distribution needs to be improved
death = random.normal(75, 10)
if death <= 18:
	death = 19

stock_price = 10
historical_stock_price = []
stock = 0
cash = 10000
debt = 0
portfolio = []
net_worth = 10000
historical_net_worth = []
interest_rate = 0.01
historical_interest_rate = []
historical_interest_rate = []

# Set up initial figures
#plt.figure()
#plt.subplot(211)
#plt.plot(net_worth)
#plt.subplot(212)
#plt.plot(historical_stock_price)

fig = plt.figure()
ax1 = fig.add_subplot(311, title = 'Your Net Worth')
ax2 = fig.add_subplot(312, title = 'Stock Price')
ax3 = fig.add_subplot(313, title = 'Interest Rate')

ax1.plot(historical_net_worth)
ax2.plot(historical_stock_price)
ax3.plot(interest_rate)

plt.tight_layout()
plt.show(block = False)


age = 18

year = 2016

# Functions for yield
def stock_yield(x):
	y = random.normal(0.1, 0.2)
	if y < -1:
		y = -1
	return x * (1 + y)
	
def interest_change(x):
	y = random.normal(0, 0.01)
	return x + y		

# The game itself
for n in range(int(death - age)):
	print "\n\nThe year is %d and you are %d years old." % (year, age)
	
	exit = False
	while exit == False:
		print "\n\n\n--- %s's Total Portfolio ---" % name
		print "\nAvailable cash: $%d" % cash
		print "Current investment value: $%d" % (stock * stock_price)
		print "Current stock price: $%d" % stock_price
		print "Current debt: $%d" % debt
		print "\nTotal net worth: $%d" % (cash + (stock * stock_price) - debt)
		choice = raw_input("\nWhat do you want to do? \n\nBuy stocks: b\nSell stocks: s\nBorrow money: d\nRepay debt: r\nWait a year: w\n\nType your choice: ")
		
		# Buy choice
		if choice == 'b':
			if cash == 0:
				print "\nYou don't have any cash!"
			
			else:
				print "\nYou can purchase up to %d units of stock" % (cash / stock_price)
				buy = int(raw_input("\nHow many stock units do you want to buy? "))
				if buy < 0:
					print "\nYou can't buy a negative amount!"
					raw_input("\nPress enter to continue")
				elif buy > (cash / stock_price):
					print "\nYou don't have that much money!"
					raw_input("\nPress enter to continue")
				elif type(buy) != int:
					print "\nThat's not a number!"
					raw_input("\nPress enter to continue")
				else:
					cash = cash - (stock_price * buy)
					stock = stock + buy
					print "\nYou buy %d units of stock for $%d." % (buy, stock_price * buy)
					raw_input("\nPress enter to continue")
					
		# Sell choice
		elif choice == 's':
			if stock == 0:
				print "\nYou don't have any stocks to sell."
				raw_input("\nPress enter to continue")
			else:
				print "\nYou can sell up to %d units of stock" % stock
				sell = int(raw_input("\nHow many stock units do you want to sell? "))
				if sell < 0:
					print "\nYou can't sell a negative amount!"
					raw_input("\nPress enter to continue")
				elif sell > stock:
					print "\nYou don't own that much stock!"
					raw_input("\nPress enter to continue")
				elif type(sell) != int:
					print "\nThat's not a number!"
					raw_input("\nPress enter to continue")
				else:
					cash = cash + (sell * stock_price)
					stock = stock - sell
					print "\nYou sell %d units of stock for $%d." % (sell, stock_price * sell)
					raw_input("\nPress enter to continue")
		
		# Borrow money choice			
		elif choice == 'd':
			amount_available  = net_worth * 4
			if amount_available < 0:
				print "\nGot rejected by the bank because I have a negative net worth"
				raw_input("\nPress enter to continue")
			else:
				print "\nThe bank has said that you can borrow up to $%d" % amount_available
				borrow = int(raw_input("\nHow much do you want to borrow? $"))
				if borrow < 0:
					print "\nYou can't borrow a negative amount!"
					raw_input("Press enter to continue")
				elif borrow > borrow:
					print "\nThat's more than you are allowed to borrow!"
					raw_input("Press enter to continue")
				elif type(borrow) != int:
					print "\nThat's not a number!"
					raw_input("\nPress enter to continue")
				else:
					debt = debt + borrow
					cash = cash + borrow
					print "\nYou borrow $%d and now have $%d in cash" % (borrow, cash)
					raw_input("\nPress enter to continue")
		
		# Repay debt choice
		elif choice == 'r':
			if cash == 0:
				print "\nYou don't have any cash to repay debts with!"
				raw_input("\nPress enter to continue")
			elif debt == 0:
				print "\nYou don't have any debt to repay!"
				raw_input("\nPress enter to continue")
			else:
				print "\nYou have $%d in cash available to repay $%d of debt." % (cash, debt)
				repay = int(raw_input("\nHow much do you want to repay? $"))
				if repay < 0:
					print "\nYou can't repay a negative amount!"
					raw_input("\nPress enter to continue")
				elif repay > cash:
					print "\nYou don't have that much cash!"
					raw_input("\nPress enter to continue")
				elif repay > debt:
					print "\nThat's more than you owe!"
					raw_input("\nPress enter to continue")
				elif type(repay) != int:
					print "\nThat's not a number!"
					raw_input("\nPress enter to continue")
				else:
					debt = debt - repay
					cash = cash - repay
					print "\nYou repay $%d and now have $%d remaining debt." % (repay, debt)
					raw_input("\nPress enter to continue")
						
		# Wait choice
		elif choice == 'w':
			exit = True
			
		else:
			print "\nThat's not a valid command!"
			raw_input("\nPress enter to continue")
	
	# change stock price					
	stock_price = stock_yield(stock_price)
	
	# increase cash by interest rate
	cash = cash * (1 + interest_rate)
	
	# increase debt by interest rate + 2%
	debt = debt * (1 + (interest_rate + 0.02))
	
	# recalculate net worth
	net_worth = cash + (stock * stock_price) - debt
	
	# change interest rate
	interest_rate = interest_change(interest_rate)
	if interest_rate < 0:
		interest_rate = 0
	
	# advance year and age
	year = year + 1
	age = age + 1
	
	# Plotting
	portfolio.append(stock_price * stock + cash)
	historical_net_worth.append(stock_price * stock + cash - debt)
	historical_stock_price.append(stock_price)
	historical_interest_rate.append(interest_rate)
	
	ax1.plot(historical_net_worth)
	ax2.plot(historical_stock_price)
	ax3.plot(historical_interest_rate)
	

	plt.draw()

	
print "\n\n%s, you have snuffed it at %d years old!" % (name, age)
print "You leave behind $%d after debt." % (net_worth)
print "\nRest in peace."

myfile = open("Fortune_HS.txt", "ab")
write_string = "%s, died age %d with a fortune of $%d" % (name, age, net_worth)
myfile.write(write_string + '\n')
myfile.close()

print "\nHigh scores:\n"
f = open("Fortune_HS.txt", "r")
file_contents = f.read()
print (file_contents)
f.close

raw_input("\nPress enter to exit")
	
# You leave behind x after debt, unfortunately you don't have any children so the government takes all your money
	