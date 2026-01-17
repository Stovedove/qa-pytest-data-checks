# QA Data Checks (Pytest)

Validador de datos CSV con CLI y pruebas unitarias.

## Requisitos
- Python 3.10+

## Instalar
python -m venv .venv
.\.venv\Scripts\activate
pip install -e .

## Ejecutar
qa-data-checks run

## Configuracion
Variables de entorno:
- DATA_CHECKS_CSV_PATH
- DATA_CHECKS_REPORT_PATH

## Ejemplo rapido
qa-data-checks run --csv data/invalid_users.csv

## Reporte
Se guarda en `reports/latest.json` con resultados por fila y duplicados.

## Estructura
- data_checks/: loader, reglas, cli
- data/: csv de ejemplo
- tests/: unit tests
