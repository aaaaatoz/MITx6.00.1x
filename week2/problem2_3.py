def getbalance(theBalance,payment):
	for month in range(12):
		theBalance = (theBalance - payment) + annualInterestRate / 12 * (theBalance - payment)
	return theBalance

monthlyRate = annualInterestRate/12
lower = balance/12.0
upper = (balance * ((1+monthlyRate)**12)) /12.0

while abs(upper-lower) >= 0.01:
	minPayment = (lower + upper)/2
	leftBalance = getbalance(balance,minPayment)
	if leftBalance > 0:				# still money to pay
		lower = minPayment
	else:
		upper = minPayment

print "Lowest Payment: %.2f" %minPayment
