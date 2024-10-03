

<h1>Sistema de Controle de Estoque</h1>

<h2>Descrição</h2>
<p>Este projeto foi desenvolvido como parte de uma disciplina de "Programação com Python". O projeto consiste em um sistema de controle de estoque para uma loja de produtos eletrônicos, desenvolvido em Python. Ele permite o cadastro, atualização e consulta de produtos no estoque, além de gerar relatórios detalhados sobre a quantidade e valor dos itens. O sistema também calcula o lucro presumido com base no custo e no preço de venda dos produtos.</p>

<h2>Funcionalidades</h2>
<ul>
    <li><strong>Cadastro de Produtos</strong>: Adiciona novos produtos ao estoque, com descrição, código, quantidade, custo e preço de venda.</li>
    <li><strong>Inserção Inicial de Estoque</strong>: O sistema processa uma string fornecida com dados iniciais e carrega os produtos no estoque.</li>
    <li><strong>Listagem de Produtos</strong>: Exibe uma lista completa dos produtos cadastrados, com todos os seus atributos.</li>
    <li><strong>Ordenação de Produtos por Quantidade</strong>: Permite ordenar os produtos por quantidade em ordem crescente ou decrescente.</li>
    <li><strong>Busca de Produtos</strong>: Busca produtos por descrição ou código, com parâmetros obrigatoriamente passados por palavra-chave.</li>
    <li><strong>Remoção de Produtos</strong>: Remove um produto do estoque com base no código fornecido.</li>
    <li><strong>Consulta de Produtos Esgotados</strong>: Lista produtos cuja quantidade no estoque é zero.</li>
    <li><strong>Filtro de Produtos com Baixa Quantidade</strong>: Filtra produtos com quantidade abaixo de um limite mínimo, gerando um relatório.</li>
    <li><strong>Atualização de Estoque</strong>: Atualiza a quantidade de um produto específico, permitindo aumento ou redução.</li>
    <li><strong>Atualização de Preços</strong>: Permite alterar o preço de venda de um produto.</li>
    <li><strong>Validação de Atualizações</strong>: Verifica se as atualizações de quantidade e preço são válidas, evitando estoque negativo ou preços de venda inferiores ao custo.</li>
    <li><strong>Cálculo do Valor Total do Estoque</strong>: Calcula o valor total dos produtos no estoque.</li>
    <li><strong>Cálculo do Lucro Presumido</strong>: Calcula o lucro baseado na diferença entre custo e preço de venda de cada produto.</li>
    <li><strong>Relatório Geral do Estoque</strong>: Gera um relatório detalhado no terminal, formatado de forma organizada, com o valor total e o lucro do estoque.</li>
</ul>

<h2>Estrutura do Sistema</h2>
<p>O sistema é baseado no processamento de uma string inicial de estoque, que é convertida em uma lista de dicionários, onde cada dicionário representa um produto. As operações são realizadas por meio de um menu interativo, onde o usuário pode escolher a funcionalidade desejada.</p>
