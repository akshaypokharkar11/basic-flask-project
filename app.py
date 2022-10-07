from flask import Flask, request

from model.Expense import Expense, ExpenseSchema
from model.income import Income, IncomeSchema
from model.transaction_type import TransactionType

app = Flask(__name__)

transactions = [
    Income('Salary', 5000),
    Income('Dividends', 200),
    Expense('pizza', 50),
    Expense('Rock Concert', 100)
]


@app.route('/incomes')
def get_incomes():
    schema = IncomeSchema(many=True)
    incomes = schema.dump([income for income in transactions if income.type == TransactionType.INCOME])
    return incomes


@app.route('/incomes', methods=['POST'])
def add_income():
    income = IncomeSchema().load(request.get_json())
    transactions.append(income)
    return "", 201


@app.route('/expenses')
def get_expenses():
    schema = ExpenseSchema(many=True)
    expense = schema.dump([expense for expense in transactions if expense.type == TransactionType.EXPENSE])
    return expense


@app.route('/expenses', methods=['POST'])
def add_expense():
    expense = ExpenseSchema().load(request.get_json())
    transactions.append(expense)
    return "", 201


@app.route('/expenses', methods=['DELETE'])
def delete_expense():
    transactions.pop()
    return "", 204


if __name__ == '__main__':
    app.run()
