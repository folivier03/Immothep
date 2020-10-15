from .notebook import predict

class Estimate:

    def __init__(self,metre_carre_bati, nb_piece, terrain, code_postal ):
        self.metre_carre_bati = metre_carre_bati
        self.nb_piece = nb_piece
        self.terrain= terrain
        self.code_postal =code_postal

    
    
    def predict(self, metre_carre_bati, nb_piece, terrain, code_postal):
        return predic()

        
               req = {'Code postal':[code_postal],'Surface reelle bati':[mate_carre_bati],'Nombre pieces principales':[nb_piece]}
        df = pd.DataFrame(req, columns = ['Code postal','Surface reelle bati','Nombre pieces principales'])
        print("Given Parameters for Estimation value:\n", df.to_string(index= False)) 
        return (dict(estimation = str(dict(enumerate(rf.predict(df).round(2)))[0]) + ' €')) 
