import csv, datetime, io, re

from  decimal import Decimal
from datetime import datetime
from transactions.models import Update, Transaction

class TransactionsService():
    CREDIT_CARD = "1"

    def save_transactions(self, file, email):
        credit = {"counter": 0, "amount": 0}
        debit = {"counter": 0, "amount": 0}
        month_transactions_amount = {}
        transactions_months = {}
        #update = create_update_record = self.__create_update(file, email)
        data_set = file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for transaction in csv.reader(io_string, delimiter=',', quotechar='|'):
            #self.__create_transaction(transaction, update)
            self.__get_transactions_dates(transactions_months, transaction[1])
            if (transaction[2] == self.CREDIT_CARD):
                credit["counter"] = credit["counter"] + 1
                credit['amount'] = self.__get_amount(credit['amount'], transaction[3])
            else:
                debit["counter"] = debit["counter"] + 1
                debit['amount'] = self.__get_amount(debit['amount'], transaction[3])

        #update.update(transactions_amount = credit_counter + debit_counter)

        return {
            "balance": credit["amount"] + debit["amount"],
            "credit_average": credit["amount"] / credit["counter"],
            "debit_average": debit["amount"] / debit["counter"],
            "transactions_months": transactions_months
        }

    def __get_transactions_dates(self, dates, date):
        dt = datetime.strptime(date, "%m-%d-%Y")
        month = dt.strftime("%B")
        if (dates.get(month) is None):
            dates[month] = 1
        else:
            dates[month] = dates[month] + 1


    def __get_amount(self, amount, transaction):
        if (re.search(r"\+", transaction) is None):
            return Decimal(amount) - Decimal(transaction.split("-")[1])
        else:
            return Decimal(amount) + Decimal(transaction.split("+")[1])

    def __create_update(self, file, email):
        name = file.name.split('.')[0]
        return Update(name = name, email = email).save()

    def __create_transaction(self, transaction, update):
        Transaction(
            transaction_id = transaction[0],
            transaction_date = transaction[1],
            transaction = transaction[2],
            is_credit_card = transaction[3],
            update = update,
        ).save()
