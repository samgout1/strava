import gpxpy


if __name__ == "__main__":
    with open("strava_trail_run_12k.gpx", "r", encoding="utf-8") as f:
        gpx = gpxpy.parse(f)

    # Distance totale en 3D (mètres)
    distance_m = gpx.length_3d()

    # Dénivelé positif/négatif
    up_m, down_m = gpx.get_uphill_downhill()

    # Durée totale (secondes)
    duration_s = gpx.get_duration()

    # Temps/distance/vitesse en mouvement
    moving = gpx.get_moving_data()

    print("=== Résumé activité ===")
    print(f"Nom:   {gpx.tracks[0].name if gpx.tracks else '-'}")
    print(f"Type:  {gpx.tracks[0].type if gpx.tracks else '-'}")
    print(f"Distance totale: {distance_m/1000:.2f} km")
    print(f"D+: {up_m:.1f} m / D-: {down_m:.1f} m")
    print(f"Durée totale: {duration_s/60:.1f} min")
    print(f"Temps en mouvement: {moving.moving_time/60:.1f} min")
    print(f"Distance en mouvement: {moving.moving_distance/1000:.2f} km")
    print(f"Vitesse moyenne (moving): {moving.moving_distance/moving.moving_time*3.6:.2f} km/h")
    print(f"Vitesse max: {moving.max_speed*3.6:.2f} km/h")
