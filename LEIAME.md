# by: @cucah (Discord)

# REGRAS

1: Não diga que o código é seu, dê os devidos créditos 

2: Você pode melhorar e utilizar o código de forma livre

# INFO

1: Esse código facilita achar o valor correto do "width" para seu planeta feito no Spaceflight Simulator utilizando alguns cálculos matemáticos.
se você gosta de fazer Planet Edit, provavelmente você vai adorar esse simples código.

**COMO DEVO USAR?**

você vai por os valores que é pedido durante o uso do sistema, coloque o Radius (Raio) de seu objeto, logo em seguida a altura drsejada das nuvens (StartHeight), após isso lhe mostrará o valor final para se utilizar no "width", copie e cole no seu código e salve.

exemplo:

    },
    "CLOUDS": {
      "texture": "TEXTURE",
      "startHeight": -1000.0, < Altura desejada
      "width": 537555.7, < Valor do width apresentado
      "height": 100000.0,
      "alpha": 1,
      "velocity": 1.0


os ciclos funcionam removendo a atmosfera original do objeto e substituindo por outra textura, criando um arco que gira envolta do objeto dando a sensação de atmosfera mais realista ao SFS.

entretanto, existe um bug no SFS que exatamente no ângulo de 270° do objeto, caso o WIDTH não esteja na largura correta ocorre uma quebra de textura, formando uma linha e quebrando a continuidade da mesma, esse código corrige isso te mostrando o valor correto para funcionar sem problemas.
