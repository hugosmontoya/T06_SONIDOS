# 1. Concepto:

En el metro quiero traducir el caudal de personas a un sonido, cuantas más personas pasen más sonido habrá.
Quiero representar como el metro es una máquina que trafica personas y que el metro es una máquina que transporta un fluido, ese fluido son las personas. Y como a diferentes horas la máquina del metro tiene más o menos personas y por lo tanto cuantas más personas haya más ruido habrá. Quiero que a través del sonido las personas se sientan como si solo fuesen un fluido.

# 2. Banco de sonidos:
Obtenidos del freesound.org

-Nombre del sonido: (LICENCIA)
-Lavadora: washing_machine_valve_open_water_going_out_2.mp3 by Greg Baumont -- https://freesound.org/s/49100/ -- License: Attribution NonCommercial 4.0
-Agua sumergida: Underwater [Loop] AMB.wav by DCSFX -- https://freesound.org/s/366159/ -- License: Creative Commons 0
-Agua cayendo: Water Pour Small Pan by Rudmer_Rotteveel -- https://freesound.org/s/699581/ -- License: Creative Commons 0
-Tubería de agua: rain coming through a drain pipe.MP3 by marsal.oido -- https://freesound.org/s/415847/ -- License: Attribution 4.0
-Agua cae a concreto: Water drops into concrete washing basin low and rapid flow.wav by jb_stems -- https://freesound.org/s/410420/ -- License: Attribution NonCommercial 4.0

He escogido estos 5 sonidos para representar el flujo del metro como una máquina que mueve fluido que serían las personas.
El sonido de la máquina del metro que es lo que mueve a las personas, como si fuese un motor, por ello he escogido el sonido de la lavadora.
Luego el agua sumergida es como que se escucha porque siempre que el metro este funcionando habrán personas y por lo tanto fluido que cada vez suena más fuerte cuantas más personas hay.
El agua cayendo, quiere mostrar como las personas salen del metro, como caen desde el metro hasta que se ponen a caminar, el sonido del agua que cae al concreto fortalece esto.
El sonido de la tubería del agua quiere representar el sonido de como las personas caminan por los andenes una vez salen de su vagón.

# 3. Disparador visual:
La idea es un video en timelapse de grabado en un metro que a medida que las personas salen de su vagón harán el ruido del agua fluyendo, y cuantas más personas haya, (es decir más parte de la pantalla lo ocupen el movimiento de personas) más fuerte se hara ese sonido. A diferentes horas del día el metro tiene más flujo o menos pero mientras está abierto sigue funcionando por eso de fondo se oye el sonido de una máquina en funcionamiento.

# 4. Parámetros de sonido 
En cuanto a la detección no he querido que tampoco tenga un umbral demasiado bajo, ya que el vídeo no es de mucha calidad y no hace falta que se aprecien demasiados detalles, lo que hace que produzca el sonido es de un tamaño bastante grande, como se puede apreciar son masas de personas. Y cuanto más bajo es el umbral, el proyecto funciona peor y se traba.

El sonido del fondo está al máximo para que se pueda apreciar ese sonido de máquina que funciona constantemente.
El pasa-bajos y el reverb están a un nivel medio, para que se escuche mejor el sonido original que ese de agua, al cambiar el parámetro pasa-bajos y el reverb deja de sonar como el sonido original y parece más un sonido irreconocible.

# 5. Gráfica
Cabe destacar que estos parámetros de la gráfica se pueden modificar en el sistema, a gusto de quien lo use y los paramétros de los que se van a hablar a continuación son los usados para el vídeo.
En cuanto a la visualización he usado 4 líneas, que al detectar un cambio alguna de esas líneas produce un sonido de agua, la que está más a la derecha tiene combinada dos sonidos, que es por donde solo se ve prácticamente el metro, combina el sonido del desagüe con el de la cañería, los otros dos del medio y de la izquierda están situados por donde más personas hay caminando y producen sonidos de agua vertiéndose, de debajo del agua y gotas de agua, a más a la izquierda que es donde menos personas pasan se escuchan somo como si fueran algunas gotas de agua.

# 6. Reflexión 

Al traducir la imagen a sonido descubrí la importancia que tiene el audio en cuanto a lo visual y como cambiando el sonido que produce el movimiento en un video es como si estuvieses viendo otra imagen prácticamente diferente, un video de un metro donde el sonido es de agua y de una máquina, hace que lo que estamos viendo parezca una escena muy diferente. Resumidamente descubrí la importancia del sonido y me hizo pensar que incluso puede llegar a ser más importante que lo visual.

En este sistema queda fuera de la escucha son las personas que están en el andén pero están quietas, ya que el sistema solo detecta movimiento y también queda fuera el aspecto de la profundidad, un cambio que ocurre muy lejos de la cámara, hace el mismo efecto que uno que ocurre cerca.

Una mejora podría ser mejorar el aspecto del umbral ya que eso hace que el vídeo trabe si este es muy bajo, otra mejora sería que pueda detectar el tamaño del cambio y que haya una opción que por ejemplo, si el cambio de la pantalla es muy grande que pueda generar un sonido más fuerte que un cambio que ocurre muy pequeño en alguna parte de la pantalla.

