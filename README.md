# Projeto: Sistema de Controle de Estoque

Você foi contratado para desenvolver um sistema em Python para gerenciar o controle de estoque de uma loja de produtos eletrônicos. O sistema deve permitir o cadastro de produtos, a atualização de suas quantidades e preços, a consulta do estoque disponível e a geração de relatórios sobre o estoque e seus valores. O sistema também deve calcular o lucro presumido com base no custo e preço de venda dos produtos. O aluno irá inserir o estoque inicial como uma string, que será processada pelo sistema para carregar os dados de produtos.

# Detalhes do sistema:

O estoque inicial será fornecido como uma única string, onde cada produto estará separado por "#", e as informações de cada produto estarão separadas por ";". A string deverá ser convertida na estrutura de dados que você achar mais adequada dentro do programa. O sistema deve permitir o cadastro de novos produtos, bem como a atualização das quantidades e preços de produtos já cadastrados. Além disso, o sistema deve gerar relatórios com informações sobre produtos em falta, produtos abaixo de um determinado limite de quantidade, e calcular o lucro presumido com base no custo e preço dos itens.

# Sinal amarelo 🟡:

Neste trabalho, os alunos têm permissão para usar ferramentas baseadas em IA somente nas tarefas 15 e 16, apenas para auxiliar na formatação textual desses itens, porém com a exigência de compreensão plena das técnicas utilizadas para tal. Todas as fontes, incluindo ferramentas de IA, devem ser devidamente citadas. O uso de IA de forma inconsistente com os parâmetros acima será considerado má conduta acadêmica e estará sujeito à aplicação do código disciplinar. Observe que os resultados da IA ​​podem ser tendenciosos e imprecisos. É responsabilidade do aluno garantir que as informações usadas da IA ​​sejam precisas. Aprender como usar ferramentas baseadas em IA de maneira cuidadosa e estratégica contribui para o desenvolvimento das habilidades, refinamento de seu trabalho e prepara o aluno para sua futura carreira.

# Requisitos:

1. Cadastro de produtos: Implemente uma função que permita o cadastro de novos produtos. Cada produto deve conter os seguintes atributos: descrição, código, quantidade em estoque, custo do item e preço de venda por item. O código deve ser um identificador único do produto.

2. Inserção inicial de estoque: O aluno deve copiar e colar o seguinte bloco de código como string no início do programa para definir o estoque inicial. O sistema deve processar essa string e converter os dados em uma lista de dicionários:

estoque_inicial = "Notebook Dell;201;15;3200.00;4500.00#Notebook Lenovo;202;10;2800.00;4200.00#Mouse Logitech;203;50;70.00;150.00#Mouse Razer;204;40;120.00;250.00#Monitor Samsung;205;10;800.00;1200.00#Monitor LG;206;8;750.00;1150.00#Teclado Mecânico Corsair;207;30;180.00;300.00#Teclado Mecânico Razer;208;25;200.00;350.00#Impressora HP;209;5;400.00;650.00#Impressora Epson;210;3;450.00;700.00#Monitor Dell;211;12;850.00;1250.00#Monitor AOC;212;7;700.00;1100.00"

Cada produto é descrito por sua descrição (e.g., "Notebook Dell"), código (e.g., 201), quantidade (e.g., 15 unidades), custo do item (e.g., 3200.00) e preço de venda (e.g., 4500.00), nesta respectiva ordem. O sistema deve carregar esses dados como o estoque inicial.

3. Listagem de produtos: Desenvolva uma função que exiba uma lista de todos os produtos cadastrados, incluindo a descrição, código, quantidade, custo e preço de venda de cada item.

4. Ordenação de produtos por quantidade: Desenvolva uma função que permita ao usuário ordenar os produtos pela quantidade disponível no estoque, exibindo a lista em ordem crescente ou decrescente.

5. Menu interativo: Implemente um menu interativo que permita ao usuário escolher qual operação deseja realizar (adicionar, atualizar, listar, buscar, etc.).

6. Busca de produtos: Implemente uma função para buscar produtos no estoque com base na descrição ou código do produto, esta função deve receber parâmetros passados obrigatoriamente por palavra-chave. Caso o produto não seja encontrado, exiba uma mensagem apropriada e caso mais de um produto seja encontrado as informações de todos devem ser exibidas.

7. Remoção de produtos: Adicione uma função que permita a remoção de um produto do sistema com base no código do produto.

8. Consulta de produtos esgotados: Crie uma funcionalidade que exiba todos os produtos com quantidade igual a zero (esgotados).

9. Filtro de produtos com baixa quantidade: Adicione uma função que permita filtrar os produtos com quantidade abaixo de um limite mínimo especificado pelo usuário ou uma quantidade padrão caso o usuário não o forneça e gere um relatório com esses produtos.

10. Atualização de estoque: Crie uma função para atualizar a quantidade de um produto específico no estoque. A atualização pode incluir tanto a entrada (aumento) de quantidade quanto a saída (diminuição) da quantidade de produtos.

11. Atualização de preços: Implemente uma função que permita alterar o preço de venda de um produto específico.

12. Validação de atualizações: Implemente uma função que valida as alterações de quantidade e preço, ou altere as funções de atualização, para garantir que o estoque não fique negativo após uma atualização e que o novo preço de venda não seja menor que o custo do item.

13. Calcular valor total do estoque: Crie uma função que calcule o valor total do estoque, multiplicando a quantidade de cada produto pelo seu preço de venda.

14. Cálculo do lucro presumido: Crie uma função que calcule o lucro presumido do estoque, considerando a diferença entre o preço de venda e o custo de cada item multiplicado pela quantidade disponível. Exiba o lucro total do estoque no terminal.

15. Documentação de Código: Adicione comentários adequados ao seu código. Além de implementar DocStrings em ao menos 60% das funções criadas.

16. Relatório geral do estoque: Desenvolva uma função que exiba um relatório geral no terminal, incluindo a descrição, código, quantidade, custo, preço de venda, e o valor total por item (quantidade * preço). O relatório deve usar os métodos .ljust(), .rjust(), método .format() ou métodos semelhantes para formatar a saída de forma organizada. Ao final do relatório, exiba o custo total e o faturamento total do estoque.


### Observações
A entrega do seu AT poderá ser feita através de uma ou todas as técnicas descritas abaixo: 

Envio de um arquivo PDF no Moodle contendo todo o texto de seu código e prints que demonstram o funcionamento adequado de cada requisito em sua máquina.
Envio de arquivo ZIP no moodle contendo todos os arquivos de código necessários à sua solução dentro da estrutura de pastas adequada quando necessário.
Através do software disponibilizado pelo professor durante a aula e envio no Moodle do nome cadastrado no software, data e horário de submissão através do software EntregaTPDacio, sendo este meio de envio condicionado à validação pelo professor.
Não é permitida a utilização de bibliotecas de terceiros, apenas bibliotecas nativas do Python.

Lembro que a entrega de AT está sujeita à arguição e o professor irá selecionar alunos para realização de uma breve arguição segundo critérios do professor e por sorteio aleatório, portanto garanta que você tenha pleno domínio de todos os detalhes de sua implementação. 
