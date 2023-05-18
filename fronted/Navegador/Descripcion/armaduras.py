from dash import html
import dash_bootstrap_components as dbc

armaduras = dbc.Container(
    [
        html.Label('El método de la rigidez es una técnica ampliamente utilizada en ingeniería estructural para el análisis de estructuras. En particular, el método de la rigidez para armaduras es una técnica de análisis que se utiliza específicamente para el cálculo de desplazamientos y reacciones en estructuras reticuladas o armaduras.'),
        html.Label('Este método se basa en la idea de que cada elemento de la armadura tiene una matriz de rigidez asociada, que describe la relación entre las cargas aplicadas y los desplazamientos resultantes en el elemento. Al ensamblar todas las matrices de rigidez de los elementos, se obtiene la matriz de rigidez global de la armadura.'),
        html.Label('Aplicando las condiciones de contorno, como restricciones en los nodos, se puede resolver el sistema de ecuaciones para obtener los desplazamientos desconocidos en la armadura. Con los desplazamientos conocidos, es posible calcular las fuerzas en los elementos y las reacciones en los nodos.'),
        html.Label('El método de la rigidez para armaduras es particularmente útil para el análisis de estructuras con geometrías complejas, ya que permite descomponer la estructura en elementos más simples y resolverlos individualmente. Además, es una técnica muy eficiente para el análisis de grandes estructuras, ya que reduce significativamente el número de ecuaciones que se deben resolver en comparación con otros métodos de análisis, como el método de los elementos finitos.'),
        html.Label('En resumen, el método de la rigidez para armaduras es una técnica valiosa para el análisis de estructuras reticuladas y armaduras, ya que proporciona una forma eficiente y precisa de calcular las fuerzas en los elementos y las reacciones en los nodos.')
    ]

)

Informacion_importante = dbc.Container(
    [
        html.H1('Información a tener en cuenta:'),  #Se agrega la información que el usuario debe tener presente para el uso de la app
        html.Label('*La aplicación calcula fuerzas, desplazamientos y cargas de armaduras compuestas por 3 nodos y 2 elementos'),
        html.Label('*Los nodos se deben ingresar en orden ascendente'),
        html.Label('*Antes de ingresar los datos de área, módulo de elasticidad y cargas, el usuario debe verificar que el sistema de unidades esté unificado en todos los datos solicitados, evitando así, errores en los calculos.')
    ]

)

