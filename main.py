from FileManager import getContentFromFile, separateContent  # Importar funciones del módulo FileManager
from Utils import formatDerivations  # Importar función del módulo Utils
from AnalizadorSintactico import AnalizadorSintactico  # Importar clase del módulo AnalizadorSintactico

if __name__ == '__main__':  # Comienzo del programa principal
    content = getContentFromFile('Archivos/slr-4.yalp')  # Obtener contenido del archivo y guardarlo en la variable content

    tokens, derivations, comments = separateContent(content)  # Separar el contenido en tokens, derivaciones y comentarios

    formattedDerivations = formatDerivations(derivations)  # Formatear las derivaciones

    analizadorSintactico = AnalizadorSintactico(tokens, formattedDerivations)  # Crear una instancia de la clase AnalizadorSintactico

    analizadorSintactico.analizar()  # Realizar análisis sintáctico

    analizadorSintactico.printISet()  # Imprimir información del análisis sintáctico

    analizadorSintactico.graphAutomatonLR0()  # Generar gráfico del autómata LR0

