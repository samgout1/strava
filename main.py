import gpxpy


def parse_strava_gpx(content):
    gpx = gpxpy.parse(content)
    # Distance totale en 3D (mètres)
    distance_m = gpx.length_3d()

    # Durée totale (secondes)
    duration_s = gpx.get_duration()

    # Temps/distance/vitesse en mouvement
    moving = gpx.get_moving_data()

    return {
        "nom": gpx.tracks[0].name,
        "type": gpx.tracks[0].type,
        "distance totale": distance_m/1000,
        "durée totale": duration_s/60,
        "temps en mouvement": moving.moving_time/60,
        "distance en mouvement": moving.moving_distance/1000,
        "vitesse moyenne": moving.moving_distance/moving.moving_time*3.6,
        "vitesse max": moving.max_speed*3.6
    }


if __name__ == "__main__":
    with open("strava_trail_run_12k.gpx", "r", encoding="utf-8") as content:
        print(parse_strava_gpx(content))
