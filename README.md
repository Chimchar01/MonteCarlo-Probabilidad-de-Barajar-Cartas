# MonteCarlo-Probabilidad-de-Barajar-Cartas
Este es un programa en python que calcula la probabilidad por medio de monte carlo de que al barajar un deck de cartas nos encontremos con al menos un As y un Rey del mismo palo consecutivos. 

¿Cómo se aplica Monte Carlo al problema?
Primero se va a obtener de forma analítica la probabilidad de que al barajar un deck de cartas nos encontremos con un As y un Rey consecutivos del mismo palo.

Luego esta probabilidad también puede ser obtenida por medio de Monte Carlo, para esto se crea un programa que baraja las cartas de forma aleatoria una n cantidad de veces. En cada corrida se revisa si se obtuvo alguna de las configuraciones deseadas. Y la probabilidad está dada por la razón de la cantidad de veces que se obtuvo una configuración deseada entre la n cantidad de veces que se corrió el programa.

Finalmente se compara la probabilidad analítica con la de Monte Carlo. Para esto el programa creado se corre cien veces para un diferente número de intentos en los que se baraja el deck (10, 100, 1000). El objetivo de hacer esto es obtener la desviación estándar de las probabilidades que se obtienen y luego se calcula la diferencia entre el promedio de probabilidades de Monte Carlo con respecto a la probabilidad analítica.




Parámetros a tener en cuenta:

  trials_list: Es una lista con los números de veces que se quiere que se barajen las cartas. Mientras mayor sea el número de trials, más preciso es el programa.
  runs: Es el número de veces que se va a correr el programa para cada trial. Mientras más alto sea este número mejores promedios de probabilidades se obtienen.
  realvalue: Es el valor de la probabilidad real que se obtiene de forma analítica.
  Run(game): Es una función que activa todas las demás funciones del programa. El parámetro game determina que probabilidad de configuración estamos buscando al barajar un deck de cartas. En el programa hay dos que serían, As_King (la probabilidad de que al barajar un deck de cartas nos encontremos con al menos un As y un Rey consecutivos de mismo palo), y King_King (probabilidad de que nos encontremos con al menos dos reys consecutivos). Recuerde cambiar el valor de realvalue según el juego que desee usar. El realvalue de As_King es 7.692308, y el realvalue de King_King es 21.737557.
  
  
Sugerencias:

Como sugerencia para un futuro proyecto, sería probar este programa para trials > 1000 y runs > 100. De esta forma probablemente se obtengan resultados más precisos. Además este
programa funciona como base para obtener las probabilidades de cualquier otra configuración que se pueda pensar en un deck de cartas.  
