from django.db import models


class CountryChoices(models.TextChoices):
    BULGARIA = "BG", "Bulgaria"
    UNITED_KINGDOM = "UK", "United Kingdom"
    GERMANY = "DE", "Germany"
    FRANCE = "FR", "France"
    SPAIN = "ES", "Spain"
    ITALY = "IT", "Italy"
    OTHER = "OTHER", "Other"
