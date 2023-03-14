from biocypher import BioCypher
from adapters.uniprot_liana import (
    Uniprot,
    UniprotNodeType,
    UniprotNodeField,
)

# Instantiate the BioCypher driver
# You can use `config/biocypher_config.yaml` to configure the driver or supply
# settings via parameters below
bc = BioCypher()

# Take a look at the ontology structure of the KG according to the schema
bc.show_ontology_structure()

# Choose node types to include in the knowledge graph.
# These are defined in the adapter (`adapter.py`).
uniprot_node_types = [
    UniprotNodeType.PROTEIN,
]

uniprot_node_fields = [
    UniprotNodeField.PROTEIN_SECONDARY_IDS,
    UniprotNodeField.PROTEIN_LENGTH,
    UniprotNodeField.PROTEIN_MASS,
    UniprotNodeField.PROTEIN_NAMES,
    UniprotNodeField.PROTEIN_GENE_NAMES,
]

# Create a protein adapter instance
uniprot_adapter = Uniprot(
        organism="9606",
        node_types=uniprot_node_types,
        node_fields=uniprot_node_fields,
        test_mode=True,
        ligand_file="data/ligands_curated.csv",
        receptor_file="data/receptors_curated.csv",
    )

uniprot_adapter.download_uniprot_data(cache = True)

# Create a knowledge graph from the adapter
bc.write_nodes(uniprot_adapter.get_nodes())

# Write admin import statement
bc.write_import_call()

# Check output
bc.log_duplicates()
bc.log_missing_bl_types()
