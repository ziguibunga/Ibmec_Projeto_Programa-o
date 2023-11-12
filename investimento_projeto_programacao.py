from audioop import reverse
from cProfile import label
import statistics
from operator import itemgetter
from turtle import color
import matplotlib.pyplot as plt
import numpy as np

# colocando um título
def titulo():
    print("="*21)
    print("GUIA DE INVESTIMENTOS")
    print("="*21)
    print("v1.0")
    print()

# Leitura dos arquivos e transporte dos dados para uma lista
# cálculo de média, desvio padrão, coeficiente de variação e variância de todos os títulos privados
def estatistica_privados():
    # vale29
    vale = open('vale.txt','r')
    global vales
    vales = []
    for i in vale:
        vales.append(float(i.replace('\n','').replace(',','.')))
    global media_vale,dp_vale,cv_vale 
    media_vale = statistics.mean(vales)
    dp_vale = statistics.stdev(vales)
    cv_vale = (dp_vale/media_vale)*100
    variancia_vale = statistics.variance(vales)
    vale.close()

    # elet22
    elet = open('eletrobras.txt','r')
    global elets
    elets = []
    for i in elet:
        elets.append(float(i.replace('\n','').replace(',','.')))
    global media_elet,dp_elet,cv_elet
    media_elet = statistics.mean(elets)
    dp_elet = statistics.stdev(elets)
    cv_elet = (dp_elet/media_elet)*100
    variancia_elet = statistics.variance(elets)
    elet.close()

    # bsa313
    bsa = open('b3.txt','r')
    global bsas
    bsas = []
    for i in bsa:
        bsas.append(float(i.replace('\n','').replace(',','.')))
    global media_b3,dp_b3,cv_b3
    media_b3 = statistics.mean(bsas)
    dp_b3 = statistics.stdev(bsas)
    cv_b3 = (dp_b3/media_b3)*100
    variancia_b3 = statistics.variance(bsas)
    bsa.close()

    # petr45
    petr = open('petrobras.txt','r')
    global petrs
    petrs = []
    for i in petr:
        petrs.append(float(i.replace('\n','').replace(',','.')))
    global media_petr,dp_petr,cv_petr
    media_petr = statistics.mean(petrs)
    dp_petr = statistics.stdev(petrs)
    cv_petr = (dp_petr/media_petr)*100
    variancia_petr = statistics.variance(petrs)
    petr.close()

    # aprb28
    aprb = open('autopistas.txt','r')
    global aprbs 
    aprbs = []
    for i in aprb:
        aprbs.append(float(i.replace('\n','').replace(',','.')))
    global media_aprb,dp_aprb,cv_aprb
    media_aprb = statistics.mean(aprbs)
    dp_aprb = statistics.stdev(aprbs)
    cv_aprb = (dp_aprb/media_aprb)*100
    variancia_aprb = statistics.variance(aprbs)
    aprb.close()

    global privado
    privado = {
        "VALE29": [media_vale,dp_vale,cv_vale,variancia_vale],
        "ELET22": [media_elet,dp_elet,cv_elet,variancia_elet],
        "BSA313": [media_b3,dp_b3,cv_b3,variancia_b3],
        "PETR45": [media_petr,dp_petr,cv_petr,variancia_petr],
        "APRB28": [media_aprb,dp_aprb,cv_aprb,variancia_aprb]
    }
    global cv_privado
    cv_privado = {
        "VALE29": cv_vale,
        "ELET22": cv_elet,
        "BSA313": cv_b3,
        "PETR45": cv_petr,
        "APRB28": cv_aprb
    }
    return privado, cv_privado

# Leitura dos arquivos e transporte dos dados para uma lista
# cálculo de média, desvio padrão, coeficiente de variação e variância de todos os títulos públicos
def estatistica_publicos():
    # IPCA+
    ipca = open('ipca.txt','r')
    global ipcas
    ipcas = []
    for i in ipca:
        ipcas.append(float(i.replace('\n','').replace(',','.')))
    media_ipca = statistics.mean(ipcas)
    dp_ipca = statistics.stdev(ipcas)
    cv_ipca = (dp_ipca/media_ipca)*100
    variancia_ipca = statistics.variance(ipcas)
    ipca.close()

    # tesouro IGPM
    igpm = open('igpm.txt','r')
    global igpms
    igpms = []
    for i in igpm:
        igpms.append(float(i.replace('\n','').replace(',','.')))
    media_igpm = statistics.mean(igpms)
    dp_igpm = statistics.stdev(igpms)
    cv_igpm = (dp_igpm/media_igpm)*100
    variancia_igpm = statistics.variance(igpms)
    igpm.close()

    # tesouro prefixado LTN
    prefixado = open('prefixado_ltn.txt','r')
    global prefixados
    prefixados = []
    for i in prefixado:
        prefixados.append(float(i.replace('\n','').replace(',','.')))
    media_prefixado = statistics.mean(prefixados)
    dp_prefixado = statistics.stdev(prefixados)
    cv_prefixado = (dp_prefixado/media_prefixado)*100
    variancia_prefixado = statistics.variance(prefixados)
    prefixado.close()

    # tesouro selic
    selic = open('selic.txt','r')
    global selics
    selics = []
    for i in selic:
        selics.append(float(i.replace('\n','').replace(',','.')))
    media_selic = statistics.mean(selics)
    dp_selic = statistics.stdev(selics)
    cv_selic = (dp_selic/media_selic)*100
    variancia_selic = statistics.variance(selics)
    selic.close()

    # tesouro prefixado com juros 
    prefixado_com_juros = open('prefixado_com_juros.txt','r')
    global prefixados_com_juros
    prefixados_com_juros = []
    for i in prefixado_com_juros:
        prefixados_com_juros.append(float(i.replace('\n','').replace(',','.')))
    media_prefixado_com_juros = statistics.mean(prefixados_com_juros)
    dp_prefixado_com_juros = statistics.stdev(prefixados_com_juros)
    cv_prefixado_com_juros = (dp_prefixado_com_juros/media_prefixado_com_juros)*100
    variancia_prefixado_com_juros = statistics.variance(prefixados_com_juros)
    prefixado_com_juros.close()

    global publicos
    publicos = {
        "IPCA+": [media_ipca,dp_ipca,cv_ipca,variancia_ipca],
        "tesouro IGPM": [media_igpm,dp_igpm,cv_igpm,variancia_igpm],
        "tesouro prefixado LTN": [media_prefixado,dp_prefixado,cv_prefixado,variancia_prefixado],
        "tesouro selic": [media_selic,dp_selic,cv_selic,variancia_selic],
        "tesouro prefixado com juros": [media_selic,dp_prefixado_com_juros,cv_prefixado_com_juros,variancia_prefixado_com_juros],
    }
    global cv_publicos
    cv_publicos = {
        "IPCA+":cv_ipca,
        "tesouro IGPM": cv_igpm,
        "tesouro prefixado LTN": cv_prefixado,
        "tesouro selic": cv_selic,
        "tesouro prefixado com juros": cv_prefixado_com_juros
    }
    return publicos,cv_publicos

# Montando as carteiras com os menores coeficientes de variação
def analise_cv():
    # ordenando os ativos privados em ordem crescente
    global coef_variacao_privados_ordenados
    coef_variacao_privados_ordenados = []
    for ativo, cv in sorted(cv_privado.items(), key = itemgetter(1)):
        v = "{}".format(ativo,cv)
        coef_variacao_privados_ordenados.append(v)
    print(f"Os dois títulos privados escolhidos para a carteira foram {coef_variacao_privados_ordenados[0]} e {coef_variacao_privados_ordenados[1]}")
    global carteira_privada
    carteira_privada = [coef_variacao_privados_ordenados[0],coef_variacao_privados_ordenados[1]]

    # ordenando os ativos públicos em ordem crescente
    global coef_variacao_publicos_ordenados
    coef_variacao_publicos_ordenados = []
    for ativo, cv in sorted(cv_publicos.items(), key = itemgetter(1)):
        v = "{}".format(ativo,cv)
        coef_variacao_publicos_ordenados.append(v)
    print(f"Os dois títulos públicos escolhidos para a carteira foram {coef_variacao_publicos_ordenados[0]} e {coef_variacao_publicos_ordenados[1]}")
    global carteira_publica
    carteira_publica = [coef_variacao_publicos_ordenados[0],coef_variacao_publicos_ordenados[1]]

# Calculando o índice de Sharpe dos ativos privados
def indice_de_Sharpe_privados():
    # Agrupando as médias dos melhores ativos privados em uma só lista
    global media_top2_privados
    media_top2_privados = []
    for i in carteira_privada:
        media_top2_privados.append((privado[i])[0])
    
    # Agrupando a variância dos ativos privados em uma só lista
    variancia_top2 = []
    for i in carteira_privada:
        variancia_top2.append((privado[i])[3])

    # Pesos do ativo 1
    pesos = []
    for i in range(101):
        pesos.append(i/100)
    
    # Media de retorno do portifólio
    media_portifolio = []
    for i in pesos:
        media_portifolio.append(media_top2_privados[0]*(1-i)+i*media_top2_privados[1])

    # Covariância dos ativos
    covariancia = statistics.covariance(bsas,elets)

    # Variância do portifólio
    var_port = []
    for i in pesos:
        var_port.append((i**2)*variancia_top2[0]+((1-i)**2)*variancia_top2[1]+2*i*(1-i)*covariancia)
    var_port.reverse()

    # Desvio padrão do portifolio
    dp_port = []
    for i in var_port:
        dp_port.append(i**0.5)

    # Sharpe
    sharpe = []
    s = 0
    while True:
        sharpe.append((media_portifolio[s]-0.0238)/dp_port[s])
        s += 1
        if len(sharpe) == 101:
            break
   
    max_sharpe = max(sharpe)
    global melhor_peso_privado
    melhor_peso_privado = (sharpe.index(max_sharpe))   

    print(f"\nPara a carteira privada, a melhor divisão do dinheiro é:\n- {melhor_peso_privado/2}% no ativo {coef_variacao_privados_ordenados[1]}\n- {(100-melhor_peso_privado)/2}% no ativo {coef_variacao_privados_ordenados[0]}")

# Calculando o índice de Sharpe dos ativos públicos    
def indice_de_Sharpe_publicos():
    # Agrupando as médias dos melhores ativos públicos em uma só lista
    global media_top2_publicos
    media_top2_publicos = []
    for i in carteira_publica:
        media_top2_publicos.append((publicos[i])[0])
    
    # Agrupando a variância dos ativos públicos em uma só lista
    variancia_top2 = []
    for i in carteira_publica:
        variancia_top2.append((publicos[i])[3])
   
    # Pesos do ativo 1
    pesos = []
    for i in range(101):
        pesos.append(i/100)
  
    # Média do portifólio
    media_portifolio = []
    for i in pesos:
        media_portifolio.append(media_top2_publicos[0]*(1-i)+i*media_top2_publicos[1])
    media_portifolio.reverse()

    # Covariância
    covariancia = statistics.covariance(igpms,prefixados)

    # Variância do portifólio
    var_port = []
    for i in pesos:
        var_port.append((i**2)*variancia_top2[0]+((1-i)**2)*variancia_top2[1]+2*i*(1-i)*covariancia)
   
    # Desvio Padrão do portifólio
    dp_port = []
    for i in var_port:
        dp_port.append(i**0.5)
    
    # Sharpe
    sharpe = []
    s = 0
    while True:
        sharpe.append((media_portifolio[s]-0.0238)/dp_port[s])
        s += 1
        if len(sharpe) == 101:
            break
    
    max_sharpe = max(sharpe)
    global melhor_peso_publico
    melhor_peso_publico = (sharpe.index(max_sharpe))

    print(f"Para a carteira pública, a melhor divisão do dinheiro é:\n- {melhor_peso_publico/2}% no ativo {coef_variacao_publicos_ordenados[0]}\n- {(100-melhor_peso_publico)/2}% no ativo {coef_variacao_publicos_ordenados[1]}")

# Cálculo dos retorno esperados
def retorno_esperado():

    # media retorno privados
    retorno_ativo1_privados = (media_top2_privados[0]*((100-melhor_peso_privado)/200))*valor
    retorno_ativo2_privados = (media_top2_privados[1]*((melhor_peso_privado/200)))*valor

    # media retorno publicos
    retorno_ativo1_publicos = (media_top2_publicos[0]*(melhor_peso_publico/200))*valor
    retorno_ativo2_publicos = (media_top2_publicos[1]*((100-melhor_peso_publico)/200))*valor

    # retorno da carteira privada 
    retorno_carteira_privada = retorno_ativo1_privados+retorno_ativo2_privados
    print(f"\nO retorno da carteira privada foi R${round(retorno_carteira_privada/100,4)}")

    # retorno da carteira publica
    retorno_carteira_publica = retorno_ativo1_publicos+retorno_ativo2_publicos
    print(f"O retorno da carteira pública foi R${round(retorno_carteira_publica/100,4)}")

    # retorno da carteira total
    retorno_total = retorno_carteira_privada + retorno_carteira_publica
    print(f"O retorno da carteira total foi R${round(retorno_total/100,4)}\n")

# Montando o gráfico dos ativos privados    
def grafico_privados():
    plt.plot(bsas, 'k-', color='blue',label="BSA313" )

    plt.plot(elets, 'k-', color='red',label="ELET22" )

    plt.plot(vales, 'k-', color='yellow',label="VALE29" )

    plt.plot(aprbs, 'k-', color='purple',label="APRB28" )
    
    plt.plot(petrs, 'k-', color='green',label="PETR45" )

    plt.title("Gráfico das Debêntures")
    plt.grid(True)
    plt.xlabel("Tempo (dias úteis)")
    plt.ylabel("Taxa YTM")
    plt.legend()
    plt.show()

# Montando o gráfico dos ativos públicos   
def grafico_publicos():
    plt.plot(selics, 'k-', color='blue',label="Selic" )

    plt.plot(prefixados_com_juros, 'k-', color='green',label="Prefixado NTN-F" )

    plt.plot(igpms, 'k-', color='red',label="IGPM" )

    plt.plot(ipcas, 'k-', color='purple',label="IPCA+" )

    plt.plot(prefixados, 'k-', color='yellow',label="Prefixado LTN" )

    plt.title("Gráfico dos Tesouros")
    plt.grid(True)
    plt.xlabel("Tempo (dias úteis)")
    plt.ylabel("Taxa YTM")
    plt.legend()
    plt.show()

# Comparação dos ativos da carteira com os índices de mercado
def grafico_carteira():
    plt.plot(bsas, 'k-', color='blue',label= coef_variacao_privados_ordenados[0])

    plt.plot(elets, 'k-', color='green',label=coef_variacao_privados_ordenados[1])

    plt.plot(igpms, 'k-', color='yellow',label=coef_variacao_publicos_ordenados[0])

    plt.plot(prefixados, 'k-', color='red',label=coef_variacao_publicos_ordenados[1])

    ibovespa = open('ibovespa2.txt','r')
    ibovespas = []
    for i in ibovespa:
        ibovespas.append(float(i.replace('\n','').replace(',','.')))
    ibovespa.close()
    plt.plot(ibovespas, 'k-', color='black',label="Retorno anual Ibovespa")

    taxa_selic = open('taxa_selic.txt','r')
    taxa_selics = []
    for i in taxa_selic:
        taxa_selics.append(float(i.replace('\n','').replace(',','.')))
    taxa_selic.close()
    plt.plot(taxa_selics, 'k-', color='purple',label="Taxa Selic")

    plt.title("Comparação da carteira com indicadores de mercado")
    plt.grid(True)
    plt.xlabel("Tempo (dias úteis)")
    plt.ylabel("Taxa YTM")
    plt.legend()
    plt.show()

def main():
    titulo()
    nome =input("Seja bem-vindo! Aqui é o Otto, consultor de investimento virtual, digite o seu nome para continuarmos o atendimento: ")
    while True:
        try:
            global valor
            valor = int(input("Olá! "+nome+", quanto você deseja investir? "))
            break
        except ValueError:
            print("Digite apenas caracteres numéricos")
    print("."*100)
    estatistica_privados()
    estatistica_publicos()
    analise_cv()
    indice_de_Sharpe_privados()
    indice_de_Sharpe_publicos()
    retorno_esperado()
    grafico_privados()
    grafico_publicos()
    grafico_carteira()

main()
