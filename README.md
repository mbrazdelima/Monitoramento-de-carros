# Monitoramento de carros

### Introdução
Em empresas florestais, é muito comum que equipes de campo visitem vários plantios diariamente. Algumas equipes ficam responsáveis por monitorar pragas e doenças, outras por fazer a mensuração das florestas e por aí vai. Sendo assim, muitas empresas adotam sistemas para rastrear seus carros. Muitas informações são geradas e podem ser utilizadas para checar a utilização dos carros.

Esse projeto consiste na plicação de uma análise de dados sobre a utilização de carros de uma empresa. A solução foi criada para processar dados brutos e gerar produtos de fácil interpretação para tomada de decisão. 
A base de dados contêm valores diários do horário de começo e término da jornada de trabalho. O horário de início da jornada representa o exato momento que o colaborador ligou o carro pela primeira vez naquele dia. Já o horário de término, representa o último horário do dia em que o carro foi desligado.

### Tratamento dos dados
Tive bastante dificuldade para trabalhar com dados no formato datatime nas colunas que continham os horários. Para contornar o problema, fiz algumas manipulações. Ao importar a base, transformei as colunas de horas em formato 00:00 em string. Separei os valores de horas e minutos em duas novas colunas. A partir daí, converti a coluna de minutos em horas, somei esse valor com a coluna de horas e armazenei o resultado em uma nova coluna. Dessa forma, uma hora que estava representada por 07:30, foi transformada em 7,5. Essa transformação foi feita para as colunas de hora de início e hora final. Os dias que não continham informação, foram excluídos da base.

### Vizualização de dados
Em um primeiro momento, foi desenvolvido um gráfico que apresentava os dados diários de cada mês (IMAGEM ....). POsteriormente, foi desenvolvido 
um gráfico que traria os dados agrupados por mês (IMAGEM ....) . O segundo, traz informações mais gerais, já o primeiro, é possível maior detalhamento
dos dados.

![gráfico](https://user-images.githubusercontent.com/51482960/81885833-9614a580-9571-11ea-979a-1e85c8602f99.png)

### Tabela de índices
Após a vizualização, é gerado uma tabela de índices. A tabela visa ajudar a interpretrar o gráfico através de números.
Os índices são calculados para cada mês. São eles: 

![tabela](https://user-images.githubusercontent.com/51482960/81886344-d6285800-9572-11ea-81ad-743079408154.png)

