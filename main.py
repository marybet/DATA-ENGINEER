from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, StreamingResponse
from deta import Deta
import pandas as pd
from collections import Counter
import requests

df_plataformas= pd.read_csv(r"C:\Users\mariana\Downloads\PI01-Data-Engineering-main\Dataset")
app = FastAPI(title="Proyecto Data Engineer")
deta = Deta("906a13f2-8dd6-4ffa-b906-239cf92cde0a")  # configure your Deta project 
drive = deta.Drive("images") # access to your drive

@app.post("/")
async def root(file: UploadFile=File(...)):
        return{"file_name": file.filename}

#1. Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma
@app.get("/keyword_funcion/") 
def keyword_funcion(plataforma,keyword):
    cantidad_de_keyword=df_plataformas.loc[df_plataformas['title'].str.contains(keyword)]
    tabla_id = cantidad_de_keyword.groupby(['id']).size().reset_index(name='cantidad de id')
    lista=list(plataforma)
    if lista[0] == 'a':
        plataforma = 'amazon'
        cantidad_a = tabla_id['id'].str.startswith('a').sum()
        return f' la plataforma seleccionado fue : {str(plataforma)}, y la cantidad de veces que aparece la palabra sleccionada es :{int(cantidad_a)}'
    else:
        pass
    if lista[0] == 'd':
        plataforma = 'disney'
        cantidad_d = tabla_id['id'].str.startswith('d').sum()
        return f'la plataforma seleccionado fue : {str(plataforma)}, y la cantidad de veces que aparece la palabra sleccionada es : {int(cantidad_d)}'
    else:
        pass
    if lista[0] == 'h':
        plataforma = 'hulu'
        cantidad_h = tabla_id['id'].str.startswith('h').sum()
        return f'la plataforma seleccionado fue :{str(plataforma)}, y la cantidad de veces que aparece la palabra sleccionada es : {int(cantidad_h)}'
    else:
        pass

    if lista[0] == 'n':
        plataforma = 'netflix'
        cantidad_n = tabla_id['id'].str.startswith('n').sum()
        return f'la plataforma seleccionado fue : {str(plataforma)},  y la cantidad de veces que aparece la palabra sleccionada es :{int(cantidad_n)}'
    else:
        return print('por favor ingrese una plaforma como amazon, disney,hulu o netflix muchas gracias')



#2. Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año

@app.get("/get_score_count/")
async def get_score_count(plataforma:str, xx:int, anio:int):
    df_consul_2= df_plataformas[["plataforma","release_year","score","type"]]
    result = df_consul_2[(df_consul_2['plataforma']== plataforma)&(df_consul_2['release_year']== anio)&(df_consul_2['score']> xx)]
    return len(result)


#3. La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.

@app.get("/get_second_score/")
async def second_score_plataforma(plataforma):
  if (plataforma != '') and ((plataforma.lower() == 'disney') or (plataforma.lower() == 'hulu')\
    or (plataforma.lower() == 'amazon') or (plataforma.lower() == 'netflix')):
      local_data = df_plataformas[df_plataformas['id'].str.startswith('a', na=False)]
      local_data = local_data[local_data['score'] == local_data['score'].max()]
      if len(local_data) > 0:
        local_data = local_data.sort_values(by='title', ascending=True, na_position='first')
      
        score = local_data.iloc[1]['score']
        title = local_data.iloc[1]['title']

        respuesta = {"plataforma":plataforma,
                     "title": str(title),
                     "score": str(score)
                    }
        return respuesta
      return {"message":"No existen datos para esa plataforma"}
  return {"message":"Error, parametros incorrectos"}
   

#4. Película que más duró según año, plataforma y tipo de duración
@app.get("/mayor_duracion/")
async def get_longest(plataforma:str,duration_tipo:str,date:int):
    plataformas = {"netflix":"n","amazon":"a","hulu":"h","disney":"d"}
    df_temp = df_plataformas[(df_plataformas['id'].str[0] == plataformas[plataforma])&(df_plataformas['release_year']==date)&(df_plataformas['duration_type']==duration_tipo)&\
          (df_plataformas['type']=='movie')].sort_values(['duration_int'], ascending=False).reset_index(drop=True)[["title","duration_int","duration_type"]].iloc[0,:]
    return df_temp.to_dict()


#antidad de series y películas por rating
@app.get("/get_rating_count/") 
def get_rating_count(rating):
    
    cantidad_rating= df_plataformas[df_plataformas['rating']== rating]

    return  f'{rating,(len(cantidad_rating))}'


