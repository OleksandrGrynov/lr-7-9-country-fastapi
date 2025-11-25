# src/external_api/models.py

from pydantic import BaseModel, Field, IPvAnyAddress


class CountryRawModel(BaseModel):
    ip: IPvAnyAddress = Field(..., description="Requested IP address")
    country: str = Field(
        ..., min_length=2, max_length=3, description="Country ISO code"
    )


class CountryDetailedModel(BaseModel):
    ip: IPvAnyAddress
    country_code: str
    country_name: str
    continent: str
    emoji_flag: str
