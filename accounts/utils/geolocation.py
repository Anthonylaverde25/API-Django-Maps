

import requests
import time
import logging
from django.conf import settings
from django.contrib.gis.geos import Point
from geopy.exc import GeocoderServiceError, GeocoderTimedOut  # opcional para consistencia de errores


logger = logging.getLogger(__name__)

def geocode_address(country, state, city, street, postal_code):
    """
    Geocodifica usando Google Geocoding API.
    Mantiene el nombre de la función para que encaje con tu flujo actual.
    """
    address = ", ".join(p for p in [
        street.strip(),
        city.strip(),
        state.strip(),
        country.strip(),
        postal_code.strip()
    ] if p)

    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "key": settings.GOOGLE_GEOCODING_KEY,
        
    }

    try:
        logger.debug("Geocoding (Google): %s", address)
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()

        results = data.get("results")
        if not results:
            logger.warning("Google Geocoding no encontró: %s", address)
            return None

        loc = results[0]["geometry"]["location"]
        return Point(loc["lng"], loc["lat"])

    except (requests.exceptions.Timeout, GeocoderTimedOut):
        logger.warning("Timeout geocoding %s, retrying...", address)
    except (requests.exceptions.RequestException, GeocoderServiceError) as e:
        logger.error("Error en Google Geocoding para %s: %s", address, e)

    # Pequeña pausa para respetar políticas de rate limit si vuelves a llamar
    time.sleep(0.1)
    return None
