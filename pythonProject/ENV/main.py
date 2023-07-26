"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""
# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

#import for your application
from ENV import Env
from get_value import GetValue




def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")


    # Carregando variáveis de configuração de ambiente ------------------------------------------------------


    # -------------------------------- Configurar variaveis  OBS: NÃO MEXER ---------------------------------

    with open(file_config,"r", encoding='utf-8') as txt:
        for linha in txt:
            ambiente = linha.strip()

    ambiente = ambiente.split(":")
    ambiente = ambiente[1].strip()

    mapeamento_ambiente = {
        '1': 'PRODUÇÃO',
        '2': 'HOMOLOGAÇÃO',
        '3': 'DESENVOLVIMENTO'
    }
    AMBIENTE = mapeamento_ambiente.get(ambiente, 'AMBIENTE INVÁLIDO')
    print(f'Ambiente selecionado: {AMBIENTE}')
    # --------------------------------------------------------------------------------------------------------------


    #Configurar pasta padrão

    nome_aba = 'Diretorios'
    excel_reader = GetValue(nome_aba, file_env)
    chave_desejada = 'path_raiz'
    path_raiz = excel_reader.ReadValue(AMBIENTE,chave_desejada)
    print(f'Caminho da pasta principal em que o robô irá realizar suas execuções: {path_raiz}')

    # Buscar outros diretórios em que o robo irá trabalhar
    help_folder = path_raiz+'Auxiliar'
    input_folder = path_raiz+'Entrada'
    log_folder = path_raiz+'Log'
    processing_folder = path_raiz+'Processamento'
    parameterization_folder = path_raiz+'Parametrização'
    output_folder = path_raiz+'Saída'
    #------------------------------------------------------------------------------------------------------------

    """
    nome_aba = 'BDs'   #indicar nome da aba do excel
    excel_reader = GetValue(nome_aba,file_env)
    #ambiente_desejado = AMBIENTE   #irá carregar os valores: PRODUÇÃO, HOMOLOGAÇÃO OU DESENVOLVIMENTO
    chave_desejada = 'connection_db'  #Chave do valor que está buscando
    conexao_bd  = excel_reader.ReadValue(AMBIENTE,   chave_desejada)   # passar valor para sua variável
    print(f'String da conexão de bancod de dados: {conexao_bd}')
    """

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )


if __name__ == '__main__':
    main()
