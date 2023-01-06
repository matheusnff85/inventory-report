from inventory_report.inventory.product import Product


def test_relatorio_produto():
    produto = Product(
        1,
        "Playstation 5",
        "Amazon",
        "16/11/2022",
        "16/11/2023",
        "123456789",
        "Armazenar em um local com sombra",
    )
    assert ("Playstation 5" in produto.__repr__()) is True
    assert ("Amazon" in produto.__repr__()) is True
    assert ("16/11/2022" in produto.__repr__()) is True
    assert ("16/11/2023" in produto.__repr__()) is True
    assert ("Armazenar em um local com sombra" in produto.__repr__()) is True
