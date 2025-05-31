from django.core.validators import RegexValidator

handle_validator = RegexValidator(
    regex='^[A-Za-z0-9_-]{3,30}$',
   message=(
    "El handle solo puede contener:\n"
    "- Letras (A–Z, a–z)\n"
    "- Números (0–9)\n"
    "- Guión bajo (_)\n"
    "- Guión medio (-)\n"
    "Longitud: 3–30 caracteres."
)

)