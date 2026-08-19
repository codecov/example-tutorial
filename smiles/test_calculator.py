from .smiles import Smiles


def test_smiles():
    assert Smiles.smiles() == ':)'
