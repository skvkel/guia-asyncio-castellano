# Asyncio Learn

## Capítulo 1. Concurrencia con Asyncio
Una **corutina** es una función que puede ser suspendida y reanudada. Tienen
el control sobre cuando son suspendidas.
Puede ser suspendida por varias razones, como la ejecución de otra corrutina 
para esperar otra task o esperar por un recurso externo.

Muchas corrutinas pueden ser ejecutadas a la vez, por lo que permitimos la 
concurrencia.  

Una **subrutina** es una función que puede ser ejecutada, empezando desde un
punto y finalizada en otro punto. 
Por lo tanto, una corrutina puede ser ejecutada después de ser suspendida, y 
reanudada muchas veces antes de su finalización.

La diferencia entre multihebra y multitasking es que la multihebra es 
gestionada por el SO. Él es quien decide cuál hebra ejecutar y cuál detener.
En el multitasking, son "ellas mismas" quien toman estas decisiones.

### Corrutina vs rutina vs subrutina
Rutina --> programa  
Subrutina --> función del programa  
Corutina --> extensión de subrutina. Un tipo especial de subrutina 
> Una rutina tiene subrutinas (un programa tiene funciones)

Entonces, la gran diferencia es que la **subrutina se ejecuta de principio a 
fin y la corrutina se puede pausar durante su ejecución las veces que queramos**

Cuando una corrutina lanza otra corrutina, debe parar su ejecución y continuar 
con la nueva.

### Corrutina vs generador
Un generador es una función especial que puede pausar/suspender su ejecución, 
retornar un valor y recuperar su flujo al terminar la función llamada.
Una corutina puede suspenderse usando **await**. Será reanudada cuando la 
rutina haya sido completada.
> await (asyncio) --> misma función que *yield* en generador. Pausa su ejecución
> y cede el control.

### Corrutina vs thread
Una thread es una hebra de ejecución en el sistema operativo. Cada programa es
un proceso y tiene al menos una hebra (la hebra principal). Se pueden ejecutar
múltiples subprocesos (o hebras), que tendrán como padre la hebra principal.

El SO es quien controla la ejecución de dichas hebras. Una corrutina es mucho
más liviano que una hebra, ya que es definida como una función.  
IMPORTANTE: una 
hebra puede ejecutar múltiples corutinas.
> Las corutinas son más rápidas de crear, ejecutar y consumen menos memoria. 

Por lo tanto, una hebra es un "objeto independiente", mientras que las corrutinas
son "funciones" dentro de una misma hebra, que se van "turnando".

### ¿Qué es la programación asíncrona?
Asíncrono significa "no al mismo tiempo". Cuando programamos algo asíncrono, 
significa que es una acción requerida que se ejecutará más adelante.  

> Un **futuro** es un identificador de la llamada asíncrona con el fin de 
> comprobar el estado y tomar la devolución de datos.

> Una **task** se refiere al conjunto de una llamada asíncrona junto con su 
> futuro.

La programación asíncrona se utiliza para I/O no bloqueantes. Es decir, lecturas
y escrituras, por ejemplo, cuyo resultado es devuelto más adelante.  
En Python, la programación asíncrona se implementa, por ejemplo, con **asyncio**,
que nos brinda operaciones *async/await*. Se implementa usando corrutinas que corren
en un bucle de eventos, que corren sobre **una hebra**.

> async def --> Corutina
````python
async def my_coroutine():
    ...
````

> await --> suspenderá la llamada y planificará la corrutina para ejecutarse. La
> devolución no se producirá hasta que la corrutina termine. Es como ejecutar yield.
> Lo que devuelva la corrutina, se captura y si se ha programado para asignar 
> el retorno a una variable, dicha variable contendrá lo capturado por await

Es necesario definir un *event loop* para trabajar con corutinas en Python. Este
event loop se puede crear y ejecutar con **asyncio.run()**. Desde este event loop 
se llama a la corrutina "padre".
> asyncio.run() --> inicia el bucle de eventos. Toma una corrutina como argumento

### ¿Cuándo usar asyncio?
1. I/O no bloqueantes, como solicitudes HTTP, conexiones a base de datos, etc
2. Lectura y escritura de archivos 
3. La programación asíncrona es preferida o requerida.  

Las ventajas de asyncio frente a las hebras son:
- Menor sobrecarga: menos consumo de memoria y mejor y más rápido cambio de contexto.
- Escalabilidad: pueden manejar muchas más conexiones que las hebras
- Simplicidad en manejo de estados: es más sencillo manejar estados de corutinas.

### Resumen capítulo 1
1. Una corutina es una función que puede ser pausada y reanudada varias veces hasta
que finaliza. Se define como ``async def my_async_function()``
2. Se utiliza ``asyncio.run(my_async_routine())`` para lanzar el bucle de eventos.
3. Asyncio se utiliza para I/O no bloqueantes, con grandes necesidades de una
rápida construcción y lanzamiento (mejores que con hebras).

## Capítulo 2. Corrutinas y tasks 
Para lanzar una corrutina y esperar su resultado, debemos utilizar la
sentencia ``await``. Por ejemplo, ``await my_coro()``
````python
python3 example_await.py
````
En este ejemplo, se planifica *my_first_coroutine*. Se suspende su ejecución
para lanzar *my_second_coroutine* y continua cuando ha terminado. 

### ¿Cómo crear y correr Tasks?
Las tasks son un wrapper para ejecutar corrutinas de manera independiente. Una 
task provee de un identificador de una rutina planificada con el fin de 
interactuar con ella (un **futuro**). 
> La diferencia entre llamar a una corrutina y crear una task es que la task no
> hay que esperarla (no hay que poner await my_coroutine()). Sin embargo, si no 
> se esperan con await, al terminar la ejecución se pausará la posible ejecución
> sin devolver nada.

````python
python example_tasks.py
````

En este ejemplo, creamos dos task que se planifican en el event loop. Es necesario
poner un await dentro de las tasks para que se puedan ir turnando los print, 
ya que sin los await la primera task se ejecutaría hasta terminar y luego 
continuaría la otra task. Si las lanzamos sin crear una task (con un await),
deberíamos hacer un ``await my_task()`` y 
deberíamos esperar (pase lo que pase en el interior de la corrutina) su 
finalización. 

Cuando usamos await en una coroutine, como await my_task(), estás diciendo:
"Ejecuta esta coroutine hasta que se pause (por una operación de 
entrada/salida o await interno), luego continúa con la corroutine actual 
(la que está esperando)".

Con las funciones *get_name()* y *result()* podemos obtener el 
nombre y el return de la task planificada.

### ¿Cuándo se ejecuta una task tras crearla?
Aun ejecutando ``asyncio.create_task()``, puede que no se ejecute inmediatamente.
Se ejecutará cuando el event loop tenga la oportunidad de hacerlo. Es decir, 
cuando se suspenda la corrutina que se ejecuta actualmente en el event loop y le 
toque ejecutarse a esa task. 

### ¿Cómo utilizar Gather para esperar todas las task creadas?
asyncio.gather es una manera de esperar una lista de tasks. Imaginemos
que tenemos que procesar 100 ficheros. Debemos crear entonces 100 tasks
para procesarlos todos de manera concurrente. Pero sería muy sucio hacer
un await por cada una de las tasks. Para ello utilizamos asyncio.gather
y esperamos una lista de tasks.
````python
python example_gather.py
````

### Captura de excepciones en corrutinas
Podemos capturar la excepción lanzada por la corrutina utilizando
``task.exception()``

### Cancelación de task
Podemos cancelar una task mediante ``task.cancel()``. Nos devolverá
True si se ha cancelado correctamente y False en caso contrario.
IMPORTANTE: si la tarea ha acabado y llamamos a task.cancel() nos devolverá
False.   
Si se ha recibido correctamente, la siguiente ejecución de esa
corrutina devolverá un CancelledError.

### Callback de correcta finalización.
Podemos asignar un manejador que se ejecute cuando la Task acaba
correctamente. Para ello usamos ``task.add_done_callback(function_to_call())``
La función a llamar debe tener como primer parámetro la Task.

## Capítulo 3. Colecciones de Tasks
### Función asyncio.gather()

La función ``asyncio.gather()`` se utiliza para esperar **corrutinas, Futuros 
o task** a la misma vez. Es decir, algo como hacer un "await" de todas de una sola vez.
Por ejemplo:
> asyncio.gather(coroutine1())

Si pasamos una lista de Tasks, deberemos de hacer un desempaquetado utilizando
"*".
> coros = [coro1(), coro2()]
> 
> asyncio.gather(*coros)

**IMPORTANTE**: si se proveen corrutinas, se encapsularán como Tasks (como si
hubésemos llamado a create_task).

**IMPORTANTE**: La llamada asyncio.gather devuelve un Future:
````python
python example_2_gather.py
````
Si queremos recoger lo retornado por cada una de las Tasks, tendremos que 
asignar a una variable el await del asyncio.gather()

### Función asyncio.wait()
La finalidad de wait es la misma que gather, pero con mayor granularidad:
- Nos devuelve dos cosas: las tareas completadas y las pendientes
- Podemos definir cuándo nos devuelve el control con **return_when**: ALL_COMPLETED,
FIRST_COMPLETED, FIRST_EXCEPTION
- Podemos especificar un timeout. Si el timeout se alcanza, se devuelve la 
ejecución y las que estaban pending continúan ejecutándose

En el siguiente ejemplo, podemos ver cuáles son las tareas que han terminado 
cuando se ha alcanzado el timeout y cuales no:
````python
python example_wait.py
````
### Función await_for
Es igual que **await**, pero se puede indicar un timeout. Si se llama sin
timeout, es lo mismo que await. Si se llama con timeout, devolverá TimeOutError
si se alcanza el timeout.  
En el siguiente ejemplo, veremos cómo se levanta un TimeoutError al expirar el
timeout configurado:
````python
python example_wait_for.py
````

## Función as_completed
Esta función nos retorna un iterable de awaitables. Sin embargo, los iterables
deben ser **esperados**. Si no, nos retorna un RuntimeWarning. Ponemos 
configurar un **timeout**, que nos devolverá un TimeOutError si todas las task
no han terminado en ese tiempo.
````python
python example_as_completed.py
````

## Función to_thread()
Es un método difícil de entender, pero realmente útil. Imaginemos que hay
un procedimiento I/O que debemos ejecutar fuera del bucle de eventos, sin ceder
el control a otro. La única manera es ejecutarlo fuera del bucle de eventos.
Para ello, podríamos ejecutarlo en un proceso o una hebra. Esta función está
diseñada para ejecutar esa función en una hebra. Esto nos permite poder ejecutar
de forma **paralela una hebra y una o varias corrutinas**. 
Utilizamos corrutinas porque son mucho más livianas que las hebras (lanzar 1000
hebras es muchísimo más costoso y puede agotar los recursos del equipo), pero
si necesitamos lanzar una hebra dentro de un bucle de eventos, tenemos esta 
función.

Podríamos pensar que podemos hacer una función asíncrona colocando un await a
la lectura del fichero, pero si queremos usar una libreria para ello (en el 
core no se encuentra) deberíamos hacerlo así.

En el siguiente ejemplo, tendremos 3 endpoints. En uno de ellos, se ejecutan 
cosas I/O simuladas con un sleep y devuelve la respuesta. En otro, se ejecuta
la lectura de un fichero (CPU/bound) por lo que si lo ejecutamos en otra hebra,
el servidor podrá seguir recibiendo peticiones sin bloquear el bucle de eventos.
En el último, es un mix de ambos. La petición hace cosas I/O y tareas intensivas
de CPU. Estas tareas se lanzan en una hebra nueva con to_thread y el resto de 
tareas I/O se ejecutan en el bucle de eventos.
````python
python example_to_thread.py
````

En este otro ejemplo, el bucle de eventos estará en contínua ejecución, mientras
que la tarea larga se ejecuta en una hebra separada:
````python
python example_to_thread_2.py
````

## Iteradores, generadores y context managers
### Iteradores asíncronos
Un iterador asíncrono es un objeto que implementa los métodos **aiter y anext**.
Es lo mismo que un iterador síncrono, pero con soporte para asincronía. Es decir,
podemos utilizar iteradores en bucles de eventos sin bloquearlo.
- __ **aiter** __ retorna la instancia en sí misma 
- __ **anext** __ retorna el siguiente elemento.

En el siguiente ejemplo podemos ver cómo __ **anext** __ nos devuelve el siguiente
elemento y que se define como async. En la lógica durante el retorno, podemos
incluir un await para alguna tarea pesada (un sleep)
````python
python example_iterator.py
````

### Generadores asíncronos
Los generadores asíncronos son exactamente lo mismo que los síncronos, pero 
con soporte de **await**. Es decir, podemos utilizar los iteradores en bucles
de eventos sin bloquearlo. Para ello, se utiliza el ``async for``
Debemos implementar __ **anext** __  
En el siguiente ejemplo, podemos comprobar que se utiliza un generador
asíncrono:

````python
python example_generator.py
````
Este ejemplo no tiene mucho sentido, ya que el iterador va a esperar a que 
termine el primero para devolver la llamada por lo que bloqueará el bucle de 
eventos pero nos sirve como ejemplo.

### Context Manager asíncronos
Un Context Manager asíncrono es lo mismo que uno síncrono, pero con soporte
para usar await. Es decir, podemos utilizar un context manager dentro de un 
bucle de eventos sin bloquearlo.

Debemos implementar:
- __ **aenter** __ : lo que se hace cuando entra al context manager 
- __ **aexit** __ : lo que se hace al salir del context manager

En el siguiente ejemplo, usamos un context manager asíncrono para establecer
una conexión con la base de datos de manera que podamos esperar mientras se
establece la conexión. Si no fuese asíncrono, deberíamos esperar ociosos 
mientras se establece la conexión.
````python
python example_context_manager.py
````

# Capítulo 5. Colas y primitivas de sincronización
Este capítulo es realmente importante debido a la necesidad de la sincronización
mientras se utilizan las técnicas de concurrencia usando la memoria compartida.  

**Corutina-segura**: es una corrutina que cuando se ejecute concurrentemente 
se asegura que estará libre de errores. Se refiere a que el código está **libre 
de condiciones de carrera**.

Las condiciones de carrera ocurren cuando el comportamiento de un software 
depende del orden o el tiempo en que se ejecutan múltiples hilos o procesos 
que acceden y manipulan recursos compartidos. Si los hilos no se sincronizan 
correctamente, esto puede llevar a resultados inesperados o incorrectos, ya que
las operaciones no son atómicas y pueden interrumpirse mutuamente.  
Pueden producir inconsistencias de datos, bloqueos (deadlocks), y otros 
errores difíciles de rastrear.

## Compartir datos entre corrutinas mediante colas
Las colas se pueden usar para compartir datos entre corrutinas de manera segura.
Para asincronía, podemos utilizar:
- cola FIFO ``asyncio.Queue`` (se recupera en el orden que fueron añadidos, o el que lleva más tiempo en la cola)
- cola LIFO ``asyncio.LifoQueue`` (se recupera el último añadido, o el más reciente)
- cola con prioridad ``asyncio.PriorityQueue``

Si al hacer queue.put no hay espacio suficiente, (hemos instanciado con el parámetro maxsize)
entonces se bloqueará hasta que haya espacio suficiente. Los métodos put y get
son corrutinas por lo que **deben ser esperados** (await).
````python
pyhton example_queue.py
````

### Protección de sección crítica
Proteger una sección crítica para evitar condiciones de carrera (race condition)
es extremadamente importante. Para ello, podemos utilizar diversas herramientas
como las descritas a continuación.

## Asyncio Lock
Es igual que el Lock síncrono (acquire y release), a diferencia que acquire es 
una corrutina (debemos esperarla). Espera hasta que el lock se libere, haciendo 
posible que otras corrutinas se ejecuten sin bloquear la hebra principal. 
Para utilizar el context manager with lock, debemos especificar async.
``async with lock:``
````python
python example_lock.py
````

## Asyncio Semaphore
Los semáforos asíncronos son exactamente lo mismo que los semáforos síncronos, a diferencia
que tienen soporte para asyncio. Son un Lock, pero para poder adquirir una cantidad 
concreta de ellos. Es decir, es como poner un número máximo de Locks que se pueden
adquirir hasta pausar la ejecución.

Un ejemplo de uso real es, por ejemplo, para limitar la cantidad de conexiones 
simultáneas en base de datos. Si nuestra base de datos tiene un límite máximo de 
10 conexiones simultáneas, utilizaremos un semáforo para limitarlas. Lanzaremos
un bucle de eventos con 100 corrutinas y compartiremos en todas ellas el mismo
semáforo. 

## Asyncio Event
Es una forma de compartir un bool entre corrutinas. Es un wrapper de una variable
booleana. Puede ser True (set) o False (not set).
La corrutina puede actuar bloqueándose hasta que el estado no sea el esperado.

````python
event.set() --> Establece a True el evento
event.clear() --> Establece a False el evento
````
La diferencia entre Lock y Event es que con Lock solamente puede adquirirse por 
una y no por varias. Es decir, protege sección crítica de varias corrutinas. Un
Event es una herramienta de sincronización. Una vez que se establece en True, 
deja continuar a **todas las corrutinas** que pudiesen estar esperando. 

Un ejemplo de uso real es que ese Event fuese la creación de una tabla en 
base de datos. Hasta que no fuese creada, no se establecería el Event a True 
con set() y no continuarían las demás corrutinas que habrían hecho un wait() de
ese evento para hacer lo necesario en la tabla. 


