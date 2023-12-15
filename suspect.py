import os
import pandas as pd
import numpy as np
import json
import pprint
from keras.models import load_model
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the Model
model = load_model('revision_1_nn_model.h5')

# Label
labels = ["Tick fever", "Distemper", "Parvovirus",
       "Hepatitis", "Tetanus", "Chronic kidney Disease", "Diabetes",
       "Gastrointestinal Disease", "Allergies", "Gingitivis", "Cancers",
       "Skin Rashes"]
# membaca data description.json
with open('Description.json') as f:
    global_data = json.load(f)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.form.get("gejala")
    
    # Jika data tidak ada
    if not data:
        return jsonify({"message": "Maaf, tidak ada data gejala yang diberikan."})
    
    try:
        gejala = np.array(eval(data))
        if not isinstance(gejala, np.ndarray):
            raise ValueError
    except (ValueError, SyntaxError):
        return jsonify({"message": "Maaf, format data gejala tidak valid."})
    
    # Jika input kurang dari 3 gejala
    if len(gejala) < 3:
        return jsonify({"message": "Maaf, setidaknya Anda perlu memasukkan 3 gejala."})
    
    # Menampilkan gejala yang dipilih
    selected_gejala = [i+1 for i, value in enumerate(gejala) if value == 1]
    gejala_message = f"Gejala yang dipilih: {list(selected_gejala)}"

    # Konversi data menjadi format yang dapat digunakan oleh model
    df = pd.DataFrame([gejala], columns=["gejala_" + str(i+1) for i in range(len(gejala))])
    df = df.astype(int)

    # akan Prediksi jika gejala lebih dari atau sama dengan 3
    predicted_label = None
    if len(selected_gejala) >= 3:
        # Prediksi
        prediction = model.predict(df)
        # Menentukan label berdasarkan nilai prediksi tertinggi
        max_index = np.argmax(prediction)
        predicted_label = labels[max_index]

        # mencari description dan treatment hasil dari predicted_label
        for item in global_data['deskripsi_gejala']:
            if item["name"] == predicted_label:
                output = {
                    "description": item["description"],
                    "treatment": item["treatment"],
                }
        return jsonify({"message": "Prediksi berhasil.", "gejala": gejala_message, "Prediction": predicted_label,"test": output})
    
        # for item in global_data['deskripsi_gejala']:
        #     output = {
        #         "Name:", item["name"],
        #         "Description:", item["description"],
        #         "Treatment:", item["treatment"]
        #     }
        
        # return jsonify({"message": "Prediksi berhasil.", "gejala": gejala_message, "Prediction": predicted_label})
    else:
        return jsonify({"gejala": gejala_message, "Prediction": "No Prediction"})
    
@app.errorhandler(404)
def invalid_route(e):
    return jsonify({'errorcode' : 404, 'message' : 'Route not Found'})
    
if __name__ == '__main__':
    # Menentukan port berdasarkan variabel lingkungan PORT atau menggunakan port default 8080

    app.run(host='0.0.0.0', port=port)


