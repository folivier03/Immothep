from typing import Optional
from fastapi import FastAPI
import pandas as pd
import uvicorn
import pickle




app = FastAPI()

with open ('src/model_rfg_apartment_pickle', 'rb') as f:
    rf_model_appart = pickle.load(f)
with open ('src/model_rfg_house_pickle', 'rb') as f:
    rf_model_hous = pickle.load(f)

@app.get("/")
def read_root():
    return {"hello": "world"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/api/estimate/")
def estimate(surafce_reelle, nb_piece, surface_terrain, code_postal, type_local):
    req = {'Code postal':[code_postal],'Surface reelle bati':[surafce_reelle],'Nombre pieces principales':[nb_piece], 'Surface terrain':[surface_terrain], 'type_local':[type_local]}
    df = pd.DataFrame(req, columns = ['Code postal','Surface reelle bati','Nombre pieces principales','Surface terrain'])
    print("Given Parameters for Estimation value:\n", df.to_string(index= False)) 
    print(type_local)
    if int(type_local) == 1:
        
        return(dict(estimation = str(dict(enumerate(rf_model_appart.predict(df).round(2)))[0]) + ' €'))
    else:
        return(dict(estimation = str(dict(enumerate(rf_model_hous.predict(df).round(2)))[0]) + ' €')) 
        

# estimate(80, 4,80,75000,1)
# estimate(80, 4,80,75000,2)

 

