class Estilos():

    def estilo_botao_navegacao(self):
        return """
                QPushButton
                {
                    color: white; 
                    font-size: 14px;
                    font-weight: bold; 
                    margin-top: 8px; 		
                    margin-bottom: 8px; 
                    padding: 10px;
                    text-align: left;
                    border-radius: 10px;
                }

                QPushButton:hover
                {
                    transition: all 1s ease-out;
                    background-color: #646464;
                }
                
                QPushButton:pressed
                {
                    background-color: #434343;
                }
               """

    def estilo_botao_navegacao_clicado(self):
        return """
                QPushButton
                {
                    color: white; 
                    font-size: 14px;
                    font-weight: bold; 
                    margin-top: 8px; 		
                    margin-bottom: 8px; 
                    padding: 10px;
                    text-align: left;
                    border-radius: 10px;
                    background-color: #646464;
                }

                QPushButton:hover
                {
                    transition: all 1s ease-out;
                    background-color: #646464;
                }

                QPushButton:pressed
                {
                    background-color: #434343;
                }
               """