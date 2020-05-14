# Monitoramento de carros

O projeto visa gerar informação diante de uma base de dados com horário de começo e término de jornada de trablhado de carros de uma empresa. 
Imagine que uma empresa monitora todos os carros que são disponibilizados aos funcionários. Uma das informações geradas é uma base dados que
contêm o primeiro horário que o carro foi ligado e o último horário que o carro foi desligado.
A proposta desse projeto é gerar informação de valor diante dessa base de dados. Os produtos gerados foram dois, um gráfico 
para vizualizar os dados e uma tabela de índices.

### Tratamento de dados
A base de dados contém as colunas "Mês", "Dia", "Hora Início" e "Hora Final".
A hora estava no formato 00:00. Para conseguir trablhar como esse tipo de dado, pode-se utilizar o module "datetime". Porém, tive bastante dificuldade em 
trabalhar com ele e tive que que fazer por outro caminho. Transformei as colunas de horas em string, extrair horas e minutos, transformei minutos em horas e somei
os dados. Dessa forma, uma hora que estava representada por 07:30 na base de dados, foi transformada em 7,5h. Essa transformação foi feita
para a hora de início e hora final. 
Os dias que não continham dados, foram excluídos da base.

### Vizualização de dados
Em um primeiro momento, foi desenvolvido um gráfico que apresentava os dados diários de cada mês (IMAGEM ....). POsteriormente, foi desenvolvido 
um gráfico que traria os dados agrupados por mês (IMAGEM ....) . O segundo, traz informações mais gerais, já o primeiro, é possível maior detalhamento
dos dados.

![gráfico](https://user-images.githubusercontent.com/51482960/81885833-9614a580-9571-11ea-979a-1e85c8602f99.png)

### Tabela de índices
Após a vizualização, é gerado uma tabela de índices. A tabela visa ajudar a interpretrar o gráfico através de números.
Os índices são calculados para cada mês. São eles: 
