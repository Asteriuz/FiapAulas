-- rename in T_PRODUTO, qt_estoque to nr_estoque
-- rename in T_PRODUTO, vl_preco to vl_preco_venda

ALTER TABLE T_PRODUTO RENAME COLUMN qt_estoque TO nr_estoque;