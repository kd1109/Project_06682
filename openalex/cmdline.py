"""
This module creates a RIS and BibTex command line interface.
"""

#!/usr/bin/env python3

import click
from .works import Works


@click.command()
@click.argument("doi")
@click.option(
    "--citeformat",
    default="bibtex",
    type=click.Choice(["bibtex", "ris"]),
    help="Output format (default: bibtex)",
)
def cite(doi, citeformat):
    """
    
    """
    kat_0 = Works(doi)
    if citeformat == "bibtex":
        print(kat_0.bibtex())
    elif citeformat == "ris":
        print(kat_0.ris())
