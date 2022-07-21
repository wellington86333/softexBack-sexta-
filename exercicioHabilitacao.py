#características do veículo e habilitação correspondente

quantidadeRodas = int (input("Digite a quantidade de rodas: "))
pesoBruto = int(input("Digite o peso em quilogramas: "))
quantidadeDePessoas = int(input("Digite a quantidade de pessoas no veículo: "))

if quantidadeRodas == 3:
    print("A categoria de habilitação para o veículo é A")

elif quantidadeRodas == 4 and quantidadeRodas == 8 and pesoBruto == 3500:
    print("A categoria de habilitação para o veículo é B")

elif quantidadeRodas >= 4 and pesoBruto and pesoBruto >= 3500 and 6000:
    print("A categoria de habilitação para o veículo é C")

elif quantidadeRodas >=4 and quantidadeDePessoas >8:
    print("A categoria de habilitação para o veículo é D") 

elif quantidadeRodas >= 4 and pesoBruto > 6000:
    print("A categoria de habilitação para o veículo é E")      

    