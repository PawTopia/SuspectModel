# SuspectModel

## How to install .venv
```
#install .venv
python3 -m venv .venv
# Menginstal dependencies
RUN pip install --no-cache-dir -r requirements.txt
```

## URL
- https://suspectmodel-4losygvtsa-as.a.run.app

## Content type 
x-www-urlencoded

# Method
  - POST
    - Key : gejala
    - Value : 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0
    - Output
    - ```json
      {
       "data": {
          "description": "Skin rashes can occur in dogs and cats due to various causes, including allergies, infections, or parasites. Symptoms may include redness, itching, and changes in skin texture.",
          "treatment": "Treatment involves identifying and addressing the underlying cause, along with medications to alleviate symptoms."
        },
       "gejala": "Gejala yang dipilih: [1, 50, 80]",
       "message": "Prediksi berhasil.",
       "prediction": "Skin Rashes"
      }
      ```
# Try the request using Curl
If you want to try this API you can send request via Curl or thirparty like Postman
## Curl
  ### Window
  - You can adjust the value
    > for value always boolean 1 or 0 👀
    ```
    curl --location --request POST 'https://suspectmodel-4losygvtsa-as.a.run.app/predict' ^
    --data-urlencode 'gejala=1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0'
    ```
    If you using Linux or OSX change `^` to `\`

