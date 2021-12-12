import pytest
import src.app
from src.app import applySA

def test_pos():
    assert "Positive" == applySA("I am happy")

def test_sneu():
    assert "Neutral" == applySA("basic room no special employee attitude good downtown seattle location snobbish attitude desk friendly luggage handlers outdated interior need modernization, rooms fairly basic bit awkward small nonetheless clean, noisy ambiance proximity mono-rail blurts super sounding horn hours night, nice mall near hotel restaurants pike street market places walking distance, avoid seedy areas night located near pike market, bit pricey independent hotel definately think staying improve customer relations skill.")

def test_neg():
    assert "Negative" == applySA("The weather is bad so I won’t go out")


# cmd inside test folder => python -m pytest (file of must be named ast test_*.py)
