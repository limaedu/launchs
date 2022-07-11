import requests
import xlsxwriter


def answer_questions():
    #--Criando as instâncias da planilha--#
    workbook = xlsxwriter.Workbook("respostas.xlsx")
    worksheet = workbook.add_worksheet()
    #----------------------------------#

    #--Definindo os parâmetros para as requisições--#
    url = "https://api.spacexdata.com/v3/launches"
    params = {"start": "2019-01-01","end": "2021-12-31"}
    headers = {'Content-Type': 'application/json'}

    response = requests.request("GET", url, 
                               headers = headers)
    json_response = response.json()

    response_filtered = requests.request("GET", url, 
                        headers = headers,params = params)
    json_response_filtered = response_filtered.json()
    #------------------------------------------------#

    years = {}
    sites = {}

    for flight in json_response:
        #Criando um dicionário com todos os anos de lançamento
        if flight["launch_year"] in years.keys(): 
            years[flight["launch_year"]] +=1
        else:
            years[flight["launch_year"]] = 1

        #Criando um dicionário com todos os 'site_id' 
        if flight["launch_site"]["site_id"] in sites.keys():
            sites[flight["launch_site"]["site_id"]] +=1
        else:
            sites[flight["launch_site"]["site_id"]] = 1


    #--Respostas--#
    #Qual o ano onde houve mais lançamentos?
    year_most_launches = max(years, key=years.get)

    #Qual o launch_site onde mais houve lançamentos?
    site_most_launches = max(sites, key = sites.get)

    #Qual foi o total de lançamentos entre os anos de 2019 – 2021?
    total_launches = len(json_response_filtered) #Poderíamos também fazer years["2020"] + years["2021"]
    #---------------#

    #--Exportando para o arquivo xlsx--#
    worksheet.write("A1","Qual o ano onde houve mais lançamentos?")
    worksheet.write("A2",year_most_launches)
    worksheet.write("B1","Qual o launch_site onde mais houve lançamentos?")
    worksheet.write("B2",site_most_launches)
    worksheet.write("C1","Qual foi o total de lançamentos entre os anos de 2019 – 2021?")
    worksheet.write("C2",total_launches)
    worksheet.set_column(0,3,55)

    workbook.close()
    #----------------------------------#

if __name__ == "__main__":
    answer_questions()