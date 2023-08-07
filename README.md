# LIANA KG

A BioCypher workflow to create a knowledge graph for the contextualisation of
cell-cell interactions

## Installation

Clone the repo and install using Poetry:

```bash
git clone https://github.com/biocypher/liana.git
cd liana
poetry install
```

## Preparation

### Open Targets target-disease associations

Target-disease association evidence is available from the Open Targets website
at https://platform.opentargets.org/downloads. The data can be downloaded in
Parquet format, which is a columnar data format that is compatible with Spark
and other big data tools. Currently, the data have to be manually downloaded
(e.g. using the wget command supplied on the website) and placed in the
`data/ot_files` directory. The adapter currently supports version 23.02 of the
data. Available datasets: `Target`, `Disease/Phenotype`, `Drug`, `Target - gene
ontology`, `Target - mouse phenotypes` and `Target - Disease Evidence`. CAVE:
The latter, which is the main source of target-disease interactions in the open
targets platform, is provided in two links, one for the literature evidence
(`literature/evidence`) and one for the full aggregated set (simply `evidence`).
The adapter uses the full set, so make sure to download the correct one. The
scripts directory contains a `parquet_download.sh` script that can be used to
download the files (make sure to execute it in the correct folder,
`data/ot_files`).

### Custom LIANA data

Curated files from the LIANA project are available in the `data` directory.
These are `ligands_curated.csv`, `receptors_curated.csv` and
`omnipath_ligrec_curated.csv`.

## Usage

```bash
poetry run python create_knowledge_graph.py
```

## Note about pycurl

You may encounter an error in executing the script combining this adapter and
the UniProt adapter about the SSL backend in pycurl: `ImportError: pycurl:
libcurl link-time ssl backend (openssl) is different from compile-time ssl
backend (none/other)`

Should this happen, it can be fixed as described here:
https://stackoverflow.com/questions/68167426/how-to-install-a-package-with-poetry-that-requires-cli-args
by running `poetry shell` followed by `pip list`, noting the version of pycurl,
and then running `pip install --compile --install-option="--with-openssl"
--upgrade --force-reinstall pycurl==<version>` to provide the correct SSL
backend.

## Docker

You can also run the workflow in a Docker compose setup by using the provided
`docker-compose.yml` file. This will start a three-step process that builds the
KG, imports the data into Neo4j and starts a read-only Neo4j server. To run,
execute the following command in the root of the project:

```bash
docker compose up (-d)
```

You can add the `-d` flag to run the process in the background.