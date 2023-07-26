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
#BotMaestroSDK.RAISE_NOT_CONNECTED = False

#IMPORTS
from botcity.plugins.excel import BotExcelPlugin

# Implement here your logic...

#exclusivo para buscar valores do arquivo ENV.xlsx (arquivo Excel). Busca valor com base em um ambiente e chave.

try:

    class GetValue:
        def __init__(self,nome_aba, caminho_arquivo):
            bot_excel = BotExcelPlugin()
            self.nome_aba = nome_aba
            self.caminho_arquivo = bot_excel.read(caminho_arquivo)

            self.df = bot_excel.as_dataframe(nome_aba)


            self.df.columns = self.df.iloc[0]
            self.df = self.df.iloc[1:].reset_index(drop=False)
            self.df.reset_index(drop=True, inplace=True)


        def ReadValue(self,ambiente, chave):
            valor = self.df.loc[(self.df['Ambiente'] == ambiente) & (self.df['Chave'] == chave), 'Valor'].iloc[0]
            return valor


except Exception as e:
    print(e)
finally:


    print("Robô Finalizado de busca de valor do excel finalizou")


