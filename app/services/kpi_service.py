class KPIService:
    @staticmethod
    def calculate_balance(transactions):
        revenues = sum(txn["amount"] for txn in transactions if txn["type"] == "INFLOW")
        expenses = sum(txn["amount"] for txn in transactions if txn["type"] == "OUTFLOW")
        return {"balance": revenues - expenses, "revenues": revenues, "expenses": expenses}
