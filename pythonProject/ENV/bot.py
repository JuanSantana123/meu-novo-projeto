# Import for integration with BotCity Maestro SDK
"""chrome_options.add_experimental_option("detach", True)"""
from botcity.web import WebBot, Browser, By
# imports
import logging
import traceback
from botcity.plugins.excel import BotExcelPlugin
#import for your application
from ENV import Env
from get_value import GetValue





# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    try:
        # Runner passes the server url, the id of the task being executed,
        # the access token and the parameters that this task receives (when applicable).
        maestro = BotMaestroSDK.from_sys_args()
        ## Fetch the BotExecution with details from the task, including parameters
        execution = maestro.get_execution()
        print(f"Task ID is: {execution.task_id}")
        print(f"Task Parameters are: {execution.parameters}")
        #-------------------------------------- CONFIGURAÇÕES --------------------------------------------
        download_folder = r'C:\Users\Juan\Downloads'+ '\\'  #todo: CAMINHO PARA BAIXAR TODOS OS ARQUIVO -- NÃO MEXER



        #criar funcao para o log
        # Configurações de log
        logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.WARNING, format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')

        logging.warning('INFO - robo está começando')
        # Implement here your logic...




        bot = WebBot()



    # Uncomment to set the WebDriver path
        bot.driver_path = r"C:\Users\Juan\OneDrive\Documentos\BotCity\Drivers\chromedriver.exe"

    # Opens the BotCity website.
        bot.browse("https://www.rpachallenge.com/")
        bot.wait(10000)



        #estrutura de pastas
        path_env = Env(r"C:\Users\Juan\OneDrive\Documentos" + "\\") # todo: Preencher com o cminho onde fica todos os robôs.
        arquivo_config = path_env.arquivo_config()
        arquivo_env = path_env.arquivo_env()
        ambiente = path_env.ambiente(arquivo_config)

        print(f'Caminho do arquivo Config:{arquivo_env}'
              f'Caminho do arquivo ENV:{arquivo_env}'
              f'Ambiente selecionado:{ambiente}')
        #--------------------------------------------------------------------------------------
        # Buscar outros diretórios em que o robo irá trabalhar
        nome_aba = 'BDs' #todo: Preencher com o diretório que está no arquivo env.xlsx
        env_reader = GetValue(nome_aba,arquivo_env) #todo: Preencher com a variável do nome da aba e o caminho do arquivo env.xlsx
        chave = 'connection_db' #todo: Preencher o nome da chave
        conexao_bd  = env_reader.ReadValue(ambiente, chave) #todo: Preencher com a variável ambiente e chave

    #------------------------------------------------------------------------------------
        #Todo: Criar sua lógica para o robô


    except Exception as e:
        print(f'Ocorreu um erro ao executar a tarefa. Erro:{e}. Favor verificar')

        logging.warning(f"WARNING - Ocorreu um erro: {e}")

        logging.warning(traceback.format_exc())
    finally:
            print("Robô Finalizado.")

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )
class ExcelReader:
    # Classe com a lógica de ler um arquivo excel
    def __init__(self, caminho_arquivo, nome_aba):
        bot_excel = BotExcelPlugin()
        bot_excel.read(caminho_arquivo)
        self.caminho_arquivo = caminho_arquivo
        self.nome_aba = nome_aba

        self.df = bot_excel.as_dataframe(nome_aba)
        self.df.columns = self.df.iloc[0]
        self.df = self.df.iloc[1:].reset_index(drop=True)

    def imprimir_linhas(self):
        cont = 0
        for indice, linha in self.df.iterrows():
            primeira_linha = self.df.iloc[cont]
            valor1 = primeira_linha['First Name']
            valor2 = primeira_linha['Last Name ']
            valor3 = primeira_linha['Company Name']
            valor4 = primeira_linha['Role in Company']
            valor5 = primeira_linha['Address']
            valor6 = primeira_linha['Email']
            valor7 = primeira_linha['Phone Number']
            cont += 1

            # Imprimindo os valores das variáveis
            logging.warning(f'printing:{valor1}')
            print(f"Valor 1: {valor1}")
            logging.info(f'printing:{valor2}')
            print(f"Valor 2: {valor2}")
            print(f"Valor 3: {valor3}")
            print(f"Valor 4: {valor4}")
            print(f"Valor 5: {valor5}")
            print(f"Valor 6: {valor6}")
            print(f"Valor 7: {valor7}")
            print('----------------------------------')

if __name__ == '__main__':
    main()
