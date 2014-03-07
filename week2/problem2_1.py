# Paste your code into this box
sumpaid = 0

for month in xrange(12):
	minmonthlypay = balance * monthlyPaymentRate
	balance = (balance - minmonthlypay) + annualInterestRate / 12 * (balance - minmonthlypay)
	sumpaid += minmonthlypay
	print "Month: %d" %(month+1)
	print "Minimum monthly payment: %.2f" %minmonthlypay
	print "Remaining balance: %.2f" %balance

print "Total paid: %.2f" %sumpaid
print "Remaining balance: %.2f" %balance
