from inventory_report.reports.simple_report import SimpleReport
from datetime import datetime
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, product_list: list):
        oldest_product = min(
            [item["data_de_fabricacao"] for item in product_list]
        )
        closest_validity = min(
            [
                item["data_de_validade"]
                for item in product_list
                if item["data_de_validade"]
                > datetime.now().strftime("%Y-%m-%d")
            ]
        )
        company, _ = Counter(
            item["nome_da_empresa"] for item in product_list
        ).most_common()[0]
        company_item = {}
        for item in product_list:
            if item["nome_da_empresa"] in company_item:
                company_item[item["nome_da_empresa"]] += 1
            else:
                company_item[item["nome_da_empresa"]] = 1

        company_list_item = ""
        for key, value in company_item.items():
            company_list_item += f"- {key}: {value}\n"

        return (
            f"Data de fabricação mais antiga: {oldest_product}\n"
            f"Data de validade mais próxima: {closest_validity}\n"
            f"Empresa com mais produtos: {company}\n"
            f"Produtos estocados por empresa:\n"
            f"{company_list_item}"
        )
