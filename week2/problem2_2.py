# Paste your code into this box
originalbalance = balance 
for minPay in xrange(10,originalbalance,10):
	balance = originalbalance
	for month in range(12):
		balance = (balance - minPay) + annualInterestRate / 12 * (balance - minPay)
	if balance <= 0 : break
	minPay += 10
	
print "Lowest Payment: %d" %minPay
