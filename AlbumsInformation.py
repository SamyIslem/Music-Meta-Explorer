import requests

# Informations d'identification


CLIENT_ID = "d32faf33304d41febd864d985130a98e"
CLEINT_SECRET = "ee133668d90445168e7c2565b7e507d3"

# Url pour demander un token

TOKEN_URL = "https://accounts.spotify.com/api/token"

# URL pour recuperer les albums

ALBUM_ID="4aawyAB9vmqN3uQ7FjRGTy"
ALBUMS_URL = f"https://api.spotify.com/v1/albums?ids={ALBUM_ID}"


# Preciser les headers
# Remplacer les espaces par des "+" et les paires clés-valeurs séparées par des "&"
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    # Recuperer le token sans l'intervention du client
    "grant_type": "client_credentials",
    "client_id": CLIENT_ID,
    "client_secret": CLEINT_SECRET

}


# Envoie de la requete

response = requests.post(TOKEN_URL, headers=headers, data=data)

# recupération du token
if (response.status_code == 200):
    access_token = response.json().get("access_token")
    print("ACCESS_TOKEN-->", access_token)

    headers = {
        "Authorization": f"Bearer {access_token}"  # Inclure le token ici
    }
    # Envoie d'une requete pour recuperer les albums
    albums_response = requests.get(ALBUMS_URL,headers=headers)
    print(albums_response.json())


else:
    print("ERROR", response.status_code, response.text)
