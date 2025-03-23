from flask import Flask, json
app = Flask(__name__)
@app.route("/diccionario/<path:diccio>")
def imprimir_diccionario(diccio):
    diccionario = json.loads(diccio)
    if isinstance(diccionario, dict):
        print(diccionario)
        return diccionario
    else:
        print("No es un diccionario")
        return "No es un diccionario"

@app.route("/diccionario/agregar/<path:diccio>/<clave>/<valor>")
#1. Función que reciba un diccionario y agregar una clave-valor, retornar el diccionario modificado (Debe agregarlo al final)
def agregar_elemento_diccionario(diccio,clave,valor):
    diccionario = json.loads(diccio)
    print(f"Agregar clave-valor diccionario \nParametros:\n\tDiccionario: {diccionario}\n\tClave: {clave}\n\tValor: {valor}")
    diccionario[clave] = valor
    return diccionario

@app.route("/diccionario/eliminar/<path:diccio>/<clave>")
#2. Función que reciba un diccionario y elimine una clave-valor, retornar el diccionario modificado
def eliminar_elemento_diccionario(diccio,clave):
    diccionario = json.loads(diccio)
    print(f"Eliminar clave-valor diccionario \nParametros:\n\tDiccionario: {diccionario}\n\tClave: {clave}")
    del diccionario[clave]
    return diccionario

@app.route("/diccionario/modificar/<path:diccio>/<clave>/<valor>")
#3. Función que reciba un diccionario y modifique el valor de una clave, retornar verdadero si pudo modificar y falso si no pudo
def modificar_elemento_diccionario(diccio,clave,valor):
    diccionario = json.loads(diccio)
    print(f"Modificar clave-valor diccionario \nParametros:\n\tDiccionario: {diccionario}\n\tClave: {clave}\n\tValor: {valor}")
    if clave in diccionario:
        diccionario[clave] = valor
        return diccionario
    return "Error: Clave no encontrada"

@app.route("/diccionario/combinar/<path:diccio_1>/<path:diccio_2>")
#4. Función que combine dos diccionarios, regresar el diccionario resultante
def combinar_diccionario(diccio_1, diccio_2):
    diccionario_1 = json.loads(diccio_1)
    diccionario_2 = json.loads(diccio_2)
    print(f"Combinar diccionario \nParametros:\n\tDiccionario 1: {diccionario_1}\n\tDiccionario 2: {diccionario_2}")
    diccionario_1.update(diccionario_2)
    return diccionario_1

@app.route("/conjunto/<path:conj>")
def imprimir_conjunto(conj):
    conjunto = set(json.loads(conj))
    if isinstance(conjunto, set):
        print(conjunto)

        return list(conjunto)
    else:
        print("No es un conjunto")
        return "No es un conjunto"

@app.route("/conjunto/agregar/<path:conj>/<elemento>")
#5. Función que agregue elementos a un conjunto, retornar verdadero si pudo agregar y falso si no pudo.
def agregar_elemento_conjunto(conj,elemento):
    conjunto = set(json.loads(conj))
    print(f"Agregar elemento conjunto \nParametros:\n\tConjunto: {conjunto}\n\tElemento: {elemento}")
    conjunto.add(elemento)
    return list(conjunto)

@app.route("/conjunto/eliminar/<path:conj>/<elemento>")
#6. Función que elimine un elemento de un conjunto, retornar verdadero si pudo eliminar y falso si no pudo
def eliminar_elemento_conjunto(conj, elemento):
    conjunto = set(json.loads(conj))
    print(f"Eliminar elemento conjunto \nParametros:\n\tConjunto: {conjunto}\n\tElemento: {elemento}")
    try:
        conjunto.remove(elemento)
        return list(conjunto)
    except KeyError:
        return "Error: No existe el elemento"

@app.route("/conjunto/combinar/<path:conj_1>/<path:conj_2>")
#7. Función que combine dos conjuntos, regresar el conjunto resultante
def combinar_conjunto(conj_1, conj_2):
    conjunto_1 = set(json.loads(conj_1))
    conjunto_2 = set(json.loads(conj_2))
    print(f"Combinar conjunto \nParametros:\n\tConjunto 1: {conjunto_1}\n\tConjunto 2: {conjunto_2}")
    return list(conjunto_1.union(conjunto_2))

@app.route("/conjunto/diferencia/<path:conj_1>/<path:conj_2>")
#8. Función que regrese la diferencia de dos conjuntos
def diferencia_conjunto(conj_1, conj_2):
    conjunto_1 = set(json.loads(conj_1))
    conjunto_2 = set(json.loads(conj_2))
    print(f"Diferencia conjunto \nParametros:\n\tConjunto 1: {conjunto_1}\n\tConjunto 2: {conjunto_2}")
    return list(conjunto_1.difference(conjunto_2))

@app.route("/tupla/<path:tup>")
def imprimir_tupla(tup):
    lista = json.loads(tup)
    tupla = tuple(lista)
    if isinstance(tupla, tuple):
        print(tupla)
        return f"Tupla: {tupla}"
    else:
        print("No es una tupla")
        return "No es una tupla"

@app.route("/tupla/agregar/<path:tup>/<elemento>")
#9. Función que agregue un elemento a una tupla y lo guarde los cambios en una tupla nueva, regresar la nueva tupla
def agregar_elemento_tupla(tup, elemento):
    lista = json.loads(tup)
    tupla = tuple(lista)
    print(f"Agregar elemento tupla \nParametros:\n\tTupla: {tupla}\n\tElemento: {elemento}")
    lista.append(elemento)
    nuevaTupla = tuple(lista)
    return f"Tupla: {nuevaTupla}"

@app.route("/tupla/eliminar/<path:tup>/<elemento>")
#10. Función que elimine un elemento a una tupla y lo guarde los cambios en una tupla nueva, regresar la nueva tupla
def eliminar_elemento_tupla(tup, elemento):
    lista = json.loads(tup)
    tupla = tuple(lista)
    print(f"Eliminar elemento tupla \nParametros:\n\tTupla: {tupla}\n\tElemento: {elemento}")
    nuevo = list(tupla)
    nuevo.remove(elemento)
    nuevaTupla = tuple(nuevo)
    return f"Tupla: {nuevaTupla}"

@app.route("/tupla/concatenar/<path:tup_1>/<path:tup_2>")
#11. Función que concatene dos tuplas en una nueva, regresar la nueva tupla
def concatenar_tupla(tup_1,tup_2):
    lista_1 = json.loads(tup_1)
    lista_2 = json.loads(tup_2)
    tupla_1 = tuple(lista_1)
    tupla_2 = tuple(lista_2)
    print(f"Concatenar tupla \nParametros:\n\tTupla 1: {tupla_1}\n\tTupla 2: {tupla_2}")
    nuevaTupla = tupla_1 + tupla_2
    return f"Tupla: {nuevaTupla}"

@app.route("/tupla/revertirorden/<path:tup>")
#12. Función que revertir el orden de una tupla y lo guarde los cambios en una tupla nueva, regresar la nueva tupla
def revertir_orden_tupla(tup):
    lista = json.loads(tup)
    tupla = tuple(lista)
    print(f"Revertir orden tupla \nParametros:\n\tTupla: {tupla}")
    nuevo = list(tupla)
    nuevo.reverse()
    nuevaTupla = tuple(nuevo)
    return f"Tupla: {nuevaTupla}"