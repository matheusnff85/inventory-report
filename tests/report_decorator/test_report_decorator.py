from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.colored_report import ColoredReport

DICT = [
    {
        "id": "1",
        "nome_do_produto": "Titanium Dioxide",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2020-12-08",
        "data_de_validade": "2023-12-08",
        "numero_de_serie": "FR29 5791 5333 58XR G4PR IG28 D08",
        "instrucoes_de_armazenamento": "instrucao 10",
    },
    {
        "id": "2",
        "nome_do_produto": "eucalyptus globulus",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2020-09-06",
        "data_de_validade": "2024-05-21",
        "numero_de_serie": "GT74 LHWJ FCXL JNQT ZCXM 4761 GWSP",
        "instrucoes_de_armazenamento": "instrucao 9",
    },
    {
        "id": "3",
        "nome_do_produto": "Aspirin",
        "nome_da_empresa": "Galena Biopharma",
        "data_de_fabricacao": "2021-02-22",
        "data_de_validade": "2024-03-14",
        "numero_de_serie": "KZ63 800H NM4B ZOWB YYUI",
        "instrucoes_de_armazenamento": "instrucao 8",
    },
]


def test_decorar_relatorio():
    simples = ColoredReport(SimpleReport).generate(DICT)
    completo = ColoredReport(CompleteReport).generate(DICT)
    assert ("\033[31m" in simples) is True
    assert ("\033[32m" in simples) is True
    assert ("\033[36m" in simples) is True
    assert ("\033[31m" in completo) is True
    assert ("\033[32m" in completo) is True
    assert ("\033[36m" in completo) is True
