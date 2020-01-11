FED_TAX = .05
REG_TAX = .025
cost = float(input('Enter cost: '))
current_fed_tax = cost * FED_TAX
current_reg_tax = cost * REG_TAX
current_total_tax = current_fed_tax + current_reg_tax
total_pay = cost + current_total_tax
print('Cost:', format(cost, ',.2f'), 
      '\nFederal tax:', format(current_fed_tax, ',.2f'), 
      '\nRegional tax:', format(current_reg_tax, ',.2f'), 
      '\nTotal tax', format(current_total_tax, ',.2f'), 
      '\nTotal pay', format(total_pay, ',.2f'))
