try:
    class Env:
        def __init__(self, path_robo):
            self.path_robo = path_robo

        def imprimir_path_robo(self):
            print(self.path_robo)

        def arquivo_config(self):  # Definindo 'teste' como valor padrão
            config = self.path_robo + 'config.txt'
            return config

        def arquivo_env(self):
            env = self.path_robo+'ENV.xlsx'
            return env
        def ambiente(self, config):
            with open(config,"r", encoding='utf-8') as txt:
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
            return AMBIENTE

# __________________________________
    # Criando uma instância da classe Env
    path_env = Env(r"C:\Users\Juan\OneDrive\Documentos" + "\\")   # PREENCHER COM O CAMINHO RAIZ DO ROBO

    # Chamando o método arquivo_completo sem passar um parâmetro
    arquivo_config = path_env.arquivo_config()
    print("Valor retornado:", arquivo_config)
    #
    arquivo_env = path_env.arquivo_env()
    print(f'Valor retornado:{arquivo_env}')

    #ambiente
    ambiente = path_env.ambiente(arquivo_config)
    print(f'Ambiente selecionaddo:{ambiente}')

except Exception as e:
    print(e)
finally:
    print("Robô Finalizado")









