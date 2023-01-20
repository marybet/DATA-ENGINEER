<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Data Engineering`**</h1>

<p align="center">
<img src="https://files.realpython.com/media/What-is-Data-Engineering_Watermarked.607e761a3c0e.jpg"  height=300>
</p>

¡Bienvenidos al primer proyecto individual de la etapa de labs! 
                                      ***Data Engineer***.  


<hr>  

## **Descripción del problema (Contexto y rol a desarrollar)**


## **TABLA DE CONTENIDO**
1-Introducción.
2-Objetivo de trabajo.
3-Principales tecnologías utilizadas.
4-Plan de Acción.
5-Conclusiones.
<br/>

## **Introducción**
Hola! 👋 mi nombre es Carmen Mariana Hernandez Betacourt y este repositorio contiene mi proyecto individual de Data Engineering de la carrera de Data Science en la academia Henry.
<br/>

## **Objetivo de trabajo**
Como parte del equipo de data de una empresa, el área de análisis de datos le solicita al área de Data Engineering (usted) ciertos requerimientos para el óptimo desarrollo de sus actividades. Usted deberá elaborar las *transformaciones* requeridas y disponibilizar los datos mediante la *elaboración y ejecución de una API*.

<br/>


**`Transformaciones`**:  El analista de datos requiere estas, ***y solo estas***, transformaciones para sus datos:


+ Generar campo **`id`**: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = **`as123`**)

+ Los valores nulos del campo rating deberán reemplazarse por el string “**`G`**” (corresponde al maturity rating: “general for all audiences”

+ De haber fechas, deberán tener el formato **`AAAA-mm-dd`**

+ Los campos de texto deberán estar en **minúsculas**, sin excepciones

+ El campo ***duration*** debe convertirse en dos campos: **`duration_int`** y **`duration_type`**. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)
<br/>


**`Desarrollo API`**:  Para disponibilizar los datos la empresa usa el framework ***FastAPI***. El analista de datos requiere consultar:

+ Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma

+ Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año

+ La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.

+ Película que más duró según año, plataforma y tipo de duración

+ Cantidad de series y películas por rating
<br/>


**`Deployment`**: La empresa suele usar [Deta](https://www.deta.sh/?ref=fastapi) (no necesita dockerizacion) para realizar el deploy de sus aplicaciones. Sin embargo, también puede usar [Railway](https://railway.app/) y [Render](https://render.com/docs/free#free-web-services) (necesitan dockerizacion).
<br/>

## **Principales tecnologías utilizadas.**

**FastAPI**
`Application Programming Interface`  es una interfaz que permite que dos aplicaciones se comuniquen entre sí, independientemente de la infraestructura subyacente. Son herramientas muy versátiles que permiten por ejemplo, crear pipelines facilitando mover y brindar acceso simple a los datos que se quieran disponibilizar a través de los diferentes endpoints, o puntos de salida de la API.

Hoy en día contamos con **FastAPI**, un web framework moderno y de alto rendimiento para construir APIs con Python.
<p align=center>
<img src = 'https://i.ibb.co/9t3dD7D/blog-zenvia-imagens-3.png' height=250><p>

<br/>
**Uvicorn**
Uvicorn es una implementación de servidor web ASGI para Python.

Hasta hace poco, Python carecía de una interfaz mínima de servidor/aplicación de bajo nivel para marcos asíncronos. La especificación ASGI llena este vacío y significa que ahora podemos comenzar a crear un conjunto común de herramientas utilizables en todos los marcos asíncronos.
https://www.uvicorn.org/

<br/>

**Deta**
Deta es una nube gratuita. Deta Micros (servidores) son un tiempo de ejecución de nube ligero pero escalable vinculado a un punto final HTTP. Actualmente se admiten Node.js y Python Micros.
<br/>



## `Disclaimer`
De parte del equipo de Henry se aclara y remarca que el fin de los proyectos propuestos es exclusivamente pedagógico, con el objetivo de realizar simular un entorno laboral, en el cual se trabajan diversas temáticas ajustadas a la realidad. No reflejan necesariamente la filosofía y valores de la organización. Además, Henry no alienta ni tampoco recomienda a los alumnos y/o cualquier persona leyendo los repositorios (y entregas de proyectos) que tomen acciones con base a los datos que pudieran o no haber recabado. Toda la información expuesta y resultados obtenidos en los proyectos nunca deben ser tomados en cuenta para la toma real de decisiones (especialmente en la temática de finanzas, salud, política, etc.).
