def formatDerivations(derivations):
    formattedDerivationsArray = []  # Lista para almacenar las derivaciones formateadas

    for derivation in derivations:  # Iterar a través de cada derivación en la lista 'derivations'
        derivationRoot = derivation.split(':')[0]  # Obtener la parte izquierda de la derivación (antes de ':')
        derivationBody = derivation.split(':')[1]  # Obtener la parte derecha de la derivación (después de ':')
        derivationBody = derivationBody.split('|')  # Dividir la parte derecha en subderivaciones separadas por '|'

        for subderivation in derivationBody:  # Iterar a través de cada subderivación en la lista 'derivationBody'
            if ";" not in subderivation:  # Si no hay un punto y coma al final de la subderivación
                subderivation += ';'  # Agregar un punto y coma al final de la subderivación
            formattedDerivation = derivationRoot + ':' + subderivation  # Construir la derivación formateada
            formattedDerivationsArray.append(formattedDerivation)  # Agregar la derivación formateada a la lista 'formattedDerivationsArray'

    return formattedDerivationsArray  # Devolver la lista 'formattedDerivationsArray'
