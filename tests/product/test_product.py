from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "God of War",
        "Sony",
        "16/11/2022",
        "16/11/2025",
        "GOWRAG2K22",
        "instrução 1",
    )
    assert product.id == 1
    assert product.nome_do_produto == "God of War"
    assert product.nome_da_empresa == "Sony"
    assert product.data_de_fabricacao == "16/11/2022"
    assert product.data_de_validade == "16/11/2025"
    assert product.numero_de_serie == "GOWRAG2K22"
    assert product.instrucoes_de_armazenamento == "instrução 1"
