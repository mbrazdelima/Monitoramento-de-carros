# Monitoramento de carros

### Introdução
Em empresas florestais, é muito comum que equipes de campo visitem vários plantios diariamente. Algumas equipes ficam responsáveis por monitorar pragas e doenças, outras por fazer a mensuração das florestas e por aí vai. Sendo assim, muitas empresas adotam sistemas para rastrear seus carros. Muitas informações são geradas e essas podem ser utilizadas para averiguar a correta utilização dos carros.
Diante disso, esse código foi criado para analisar dados de monitoramento de carros de empresas. Como produto, o código gera um gráfico e uma tabela de fácil interpretação para auxilar a análise de um gestor.

### Base de dados
A base de dados contêm valores diários do horário de começo e de término da jornada de trabalho. O horário de início da jornada representa o exato momento em que o colaborador liga o carro pela primeira vez no dia. Já o horário de término, representa o exata hora em que o carro foi desligado pela última vez no dia.

![baseDados](https://user-images.githubusercontent.com/51482960/81893231-89994880-9583-11ea-818f-ff9b1b7afd80.png)

Figura 1. Base de dados


### Tratamento dos dados
Tive bastante dificuldade para trabalhar com dados no formato "datatime" nas colunas que continham os horários. Para contornar o problema, fiz algumas manipulações. Ao importar a base, transformei as colunas de horas, em formato 00:00, para string. Separei os valores de horas e minutos em duas novas colunas. A partir daí, converti a coluna de minutos em horas, somei esse valor com a coluna de horas e armazenei o resultado em uma nova coluna. Dessa forma, uma hora que estava representada por 07:30, foi transformada em 7,5. Essa transformação foi feita para as colunas "Início" e "Final". 

Os dias que não continham informações, foram excluídos da base. Também foram excluídos os dias que representavam pequenos deslocamentos, intervalo entre o horário inicial e final menor que 4h.  


### Vizualização
Para facilitar a interpretação dos dados, foi desenvolvido um gráfico. Esse gráfico plota todos os valores diários de cada mês. Pontos verdes representam o horário de início, pontos vermelhos representam o horário final e duas linhas pretas representam os hórarios de início e fim do expediente, 8h e 17h respectivamente.

![gráfico](https://user-images.githubusercontent.com/51482960/81885833-9614a580-9571-11ea-979a-1e85c8602f99.png)

Figura 2. Gráfico de agrupamento mensal dos dados

Diante desse gráfico, é possível perceber facilmente desvios de conduta. É esperado que haja uma grande sobreposição de pontos bem próximos as linhas, demonstrando que os funcionários então comprindo devidamente o horário de trabalho. Entretanto, no mês de Outubro, é notável que os pontos verdes se encontram aglomerados acima da linha das 8h e os pontos vermelhos se encontram abaixo da linhas das 17h. Isso demostra claramente um começo tardio do expediente, assim como um término antecipado da jornada de trabalho.

### Tabela de índices
Além do gráfico, é gerado uma tabela de índices para auxiliar na interpretação. Os índices são calculados para cada mês.
Segue abaixo a lista de índices: 
- Porcentagem de dias iniciados após as 8h
- Porcentagem de dias com término do expediente antes das 17h
- Horário de início médio
- Horário de término médio
- Tempo de jornada médio

Além desses, novos índices podem ser adicionados, modificados ou excluídos facilmente.

![tabela](https://user-images.githubusercontent.com/51482960/82608201-9a077f80-9b90-11ea-9140-c233e454df52.png)

Figura 3. Tabela de índices

Com o auxílio da tabela, é possível comprovar os desvios do mês de Outubro. O expediente começou depois das 8h e terminou antes das 17h todos os dias. Na média, o trabalho começou 09:18 e finalizou 15:30. Além disso, é possível notar que a média da jornada de trabalho diária foi de 6h e 12min. 

### Conclusão
Esse projeto visa transformar dados brutos em informação de fácil interpretação. Com o gráfico e a tabela, o gestor consegue fazer uma análise rápida e precisa para tomar suas decisões.
Essa ferramenta também pode ser utilizada dentro de uma empresa em diferentes outros cenários, desde que esteja trabalhando com dados relacionados a horários. Ao invés de monitorar carros, pode ser utilizada para monitorar o funcionamento de máquinas, por exemplo.
Utilize-a você de acordo com a sua necessidade!
