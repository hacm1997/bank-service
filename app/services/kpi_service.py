class KPIService:
    @staticmethod
    def calculate_balance(transactions):
        ingresos = sum(txn["amount"] for txn in transactions if txn["type"] == "INFLOW")
        egresos = sum(txn["amount"] for txn in transactions if txn["type"] == "OUTFLOW")
        return {"balance": ingresos - egresos, "ingresos": ingresos, "egresos": egresos}
