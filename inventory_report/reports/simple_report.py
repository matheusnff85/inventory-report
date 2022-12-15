from datetime import datetime
from collections import Counter


class SimpleReport:
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
        return (
            f"Data de fabricação mais antiga: {oldest_product}\n"
            f"Data de validade mais próxima: {closest_validity}\n"
            f"Empresa com mais produtos: {company}"
        )
