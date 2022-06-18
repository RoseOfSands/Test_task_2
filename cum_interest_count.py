from load_file import load_file


class payment:
    def __init__(self, loan: float, payment: float, months: float, rate: float) -> None:
        self.loan = loan
        self.payment = payment
        self.rate = rate
        self.rate_m = self.rate / (12 * 100)
        self.months = months

    def cum_interest(self) -> float:
        """count cumulative interest"""
        cum_inter = 0
        for i in range(int(self.months)):
            interest_paid = self.loan * self.rate_m
            princ_repayment = self.payment - interest_paid
            cum_inter = cum_inter + interest_paid
            self.loan = self.loan - princ_repayment
        return cum_inter


example_data = load_file('/home/natalia/Рабочий стол/new/test_task/data.json')
if 'years' in example_data:
    example_data['months'] = example_data['years'] * 12
loan_example = payment(example_data['loan'], example_data['payment'], example_data['months'],
                       example_data['rate'])
print(loan_example.cum_interest())
