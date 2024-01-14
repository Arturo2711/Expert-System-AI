def calculaCalorias(objetivo, caloriasQuemadas):
    if objetivo == "subirPeso":
        superAvit = caloriasQuemadas*0.1
        calorias = caloriasQuemadas+superAvit
    else:
        deficit = caloriasQuemadas*0.1
        calorias = caloriasQuemadas-deficit
    return calorias


def caloriasQuemadas(Kg, FA):
    return Kg*FA*22


'''   

def macronutrientes(Kg, calorias):
    factorCarbos = ((calorias - 9 * Kg) / (4 * Kg)) - 1.6
    carbohidratos = factorCarbos*Kg
    grasas = Kg
    proteina = 1.6*Kg
    return {'p': proteina, 'c': carbohidratos, 'g': grasas}


def macrosDesayuno(diccionarioMacros,calorias):
    return {'p': diccionarioMacros['p'] * 0.3, 'c': diccionarioMacros['c'] * 0.3, 'g': diccionarioMacros['g'] * 0.3,'k':calorias*0.3}

def macrosComida(diccionarioMacros,calorias):
    return {'p': diccionarioMacros['p'] * 0.4, 'c': diccionarioMacros['c'] * 0.4, 'g': diccionarioMacros['g'] * 0.4,'k':calorias*0.4}

def macrosColacion(diccionarioMacros,calorias):
    return {'p': diccionarioMacros['p'] * 0.1, 'c': diccionarioMacros['c'] * 0.1, 'g': diccionarioMacros['g'] * 0.1,'k':calorias*0.1}

def macrosCena(diccionarioMacros,calorias):
    return {'p': diccionarioMacros['p'] * 0.2, 'c': diccionarioMacros['c'] * 0.2, 'g': diccionarioMacros['g'] * 0.2,'k':calorias*0.2}


'''
