from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
from fastapi import FastAPI, UploadFile, File, HTTPException
import io
import gpxpy
from service import ActivityService
from dao import UtilisateurDAO, AcitivityDAO
from main import parse_strava_gpx

# ------------- Authentification Basique ------------------

app = FastAPI(title="Basic Auth demo")
security = HTTPBasic()

USERS = {
    "alice": {"password": "wonderland", "roles": ["admin"]},
    "bob":   {"password": "builder",    "roles": ["user"]},
}

def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    username = credentials.username
    password = credentials.password

    user = USERS.get(username)
    if not user or not secrets.compare_digest(password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )
    return {"username": username, "roles": user["roles"]}

@app.get("/f1")
def me(user = Depends(get_current_user)):
    return {"user": user}



# ----------------------------------------------------------


# Jamais de DAO dans les méthodes des objets métiers
# Les services orchestrent l'utilisation des objets métiers et de la DAO
# On peut aussi se passer des services et orchestrer directement dans le endpoint

@app.post("users/{user_id}/activities")
def create_activity(user_id):
    user = UtilisateurDAO().get(user_id)
    activity = user.create_activity()
    AcitivityDAO().save(activity)
    # OU
    # UtilisateurService().create_activity(user_id)

@app.get("users/{user_id}/feed")
def get_feed(user_id):
    activities = ActivityService().get_feed(user_id)
    return activities

@app.post("/upload-gpx")
async def upload_gpx(file: UploadFile = File(...)):
    # Lecture du contenu du fichier (texte)
    content = await file.read()
    # Parsing
    return parse_strava_gpx(content)
