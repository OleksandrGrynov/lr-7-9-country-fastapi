# src/external_api/service.py

import requests

from src.external_api.models import CountryDetailedModel, CountryRawModel


class CountryService:
    base_url_raw = "https://api.country.is/"
    rest_countries_url = "https://restcountries.com/v3.1/alpha/"

    def get_raw_country(self, ip: str) -> CountryRawModel:
        resp = requests.get(self.base_url_raw + ip, timeout=5)
        resp.raise_for_status()
        data = resp.json()

        return CountryRawModel(**data)

    def get_processed_country(self, ip: str) -> CountryDetailedModel:
        raw = self.get_raw_country(ip)

        resp = requests.get(self.rest_countries_url + raw.country, timeout=5)
        resp.raise_for_status()
        info = resp.json()[0]

        return CountryDetailedModel(
            ip=raw.ip,
            country_code=raw.country,
            country_name=info["name"]["common"],
            continent=info["continents"][0],
            emoji_flag=info["flag"],
        )


service = CountryService()
