# src/external_api/router.py

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import HTMLResponse

from src.external_api.models import CountryDetailedModel, CountryRawModel
from src.external_api.service import service

router = APIRouter(prefix="/external", tags=["External API"])


@router.get("/data", response_model=CountryRawModel)
def get_raw(ip: str = Query("8.8.8.8", description="IP address")):
    try:
        return service.get_raw_country(ip)
    except Exception as e:
        raise HTTPException(500, str(e))


@router.get("/processed", response_model=CountryDetailedModel)
def get_processed(ip: str = Query("8.8.8.8")):
    try:
        return service.get_processed_country(ip)
    except Exception as e:
        raise HTTPException(500, str(e))


@router.get("/html", response_class=HTMLResponse)
def get_country_html(ip: str = "8.8.8.8"):
    """
    Повертає красиву HTML-сторінку з країною для заданого IP
    """
    try:
        result = service.get_processed_country(ip)

        html = f"""
        <!DOCTYPE html>
        <html lang="uk">
        <head>
            <meta charset="UTF-8">
            <title>Country Info for {result.ip}</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background: #f5f5f5;
                    display: flex;
                    justify-content: center;
                    padding-top: 50px;
                }}
                .card {{
                    background: #ffffff;
                    padding: 30px;
                    border-radius: 12px;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                    text-align: center;
                    width: 400px;
                }}
                .flag {{
                    font-size: 72px;
                    margin-bottom: 10px;
                }}
                .info {{
                    font-size: 20px;
                    margin: 8px 0;
                }}
                .ip {{
                    font-size: 14px;
                    color: #666;
                    margin-top: 10px;
                }}
            </style>
        </head>
        <body>
            <div class="card">
                <div class="flag">{result.emoji_flag}</div>
                <div class="info"><b>Країна:</b> {result.country_name}</div>
                <div class="info"><b>Континент:</b> {result.continent}</div>
                <div class="info"><b>Код країни:</b> {result.country_code}</div>
                <div class="ip">IP: {result.ip}</div>
            </div>
        </body>
        </html>
        """

        return html

    except Exception as e:
        return f"<h3>Error: {e}</h3>"
