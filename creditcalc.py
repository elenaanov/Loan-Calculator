from math import ceil, log
import argparse

parser = argparse.ArgumentParser(description="Credit Calculator Project")

parser.add_argument('--type', help="Type of Payment (Annuity or Differential")
parser.add_argument('--payment', help="Monthly payment", type=int)
parser.add_argument('--principal', help="Credit principal", type=int)
parser.add_argument('--periods', help="Count of months", type=int)
parser.add_argument('--interest', help="Credit interest (rate of interest)", type=float)

args = parser.parse_args()

if args.type not in ['annuity', 'diff']:
    print('Incorrect Parameters')
    exit(0)

if args.type == 'diff' and args.payment is not None:
    print('Incorrect Parameters')
    exit(0)

if args.interest is None:
    print('Incorrect Parameters')
    exit(0)

args_list = [args.type, args.payment, args.principal, args.periods, args.interest]
count = 0
for item in args_list:
    if count > 1:
        print('Incorrect Parameters')
        exit(0)
    elif item is None:
        count += 1


# Calculate number of monthly payments
if args.type == 'annuity' and args.periods is None:

    i = args.interest / (12 * 100)
    n = log((args.payment / (args.payment - i * args.principal)), 1 + i)
    n = ceil(n)

    if n == 1:
        print('It will take 1 month to repay the loan')
    elif n < 12:
        print(f'It will take {n} months to repay the loan')
    elif n == 12:
        print('It will take 1 year')
    elif n == 13:
        print('It will take 1 year and 1 month to repay this loan!')
    elif n < 24 and n % 12 != 1:
        print(f'It will take 1 year and {n % 12} months to repay this loan!')
    elif n % 12 == 0:
        print(f'It will take {int(n / 12)} years to repay this loan!')
    elif n % 12 == 1:
        print(f'It will take {n // 12} years and 1 month to repay this loan!')
    else:
        print(f'It will take {n // 12} years and {n % 12} months to repay this loan!')

    overpayment = args.payment * n - args.principal
    print(f'Overpayment = {overpayment}')


# Calculate annuity monthly payment amount
elif args.type == 'annuity' and args.payment is None:

    i = args.interest / (12 * 100)
    payment = ceil(args.principal * i * pow(1 + i, args.periods) / (pow(1 + i, args.periods) - 1))
    payment_last = args.principal - (args.periods - 1) * payment

    if payment_last == 0:
        print(f'Your annuity payment = {payment}')
#    else:
#        print(f'Your annuity payment = {payment} and the last payment = {payment_last}')

    overpayment = payment * args.periods + payment_last - args.principal
    print(f'Overpayment = {overpayment}')


# Calculate loan principal
elif args.type == 'annuity' and args.principal is None:

    i = args.interest / (12 * 100)
    principal = args.payment * (pow(1 + i, args.periods) - 1) / (i * pow(1 + i, args.periods))

    print(f'Your loan principal = {principal}!')

    overpayment = args.payment * args.periods - principal
    print(f'Overpayment = {overpayment}')


# Calculate monthly differentiated payment
elif args.type == 'diff' and args.payment is None:

    i = args.interest / (12 * 100)
    payment_total = 0

    for m in range(args.periods):
        payment = ceil(args.principal / args.periods + i * (args.principal - args.principal * m / args.periods))
        payment_total += payment
        print(f'Month {m + 1}: payment is {payment}')

    overpayment = payment_total - args.principal
    print(f'Overpayment = {overpayment}')
