import pickle

def predict(row):
    filename = r'C:\Users\user\Documents\MainProject\smarthealth\linear_model.sav'
    model = pickle.load(open(filename, 'rb'))
    predicted_value = model.predict([row])
    return predicted_value[0]


