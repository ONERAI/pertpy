from os.path import join

import anndata
import scanpy as sc
from anndata import AnnData


def test():
    print("test method")


# this function loads raw data, written before, probably deprecate
def mixscape_vignette_crohn(datasetdir: str = None) -> AnnData:
    """Bulk data with conditions ulcerative colitis (UC) and Crohn's disease (CD).

    The study assesses transcriptional profiles in peripheral blood mononuclear
    cells from 42 healthy individuals, 59 CD patients, and 26 UC patients by
    hybridization to microarrays interrogating more than 22,000 sequences.

    Reference:
        Burczynski et al., "Molecular classification of Crohn's disease and
        ulcerative colitis patients using transcriptional profiles in peripheral
        blood mononuclear cells"
        J Mol Diagn 8, 51 (2006). PMID:16436634.

    Args:
        datasetdir: Path to the directory of the dataset

    Returns:
        :class:`~anndata.AnnData` object of the Burczynski dataset
    """
    assert datasetdir is not None
    # filename = settings.datasetdir / 'burczynski06/GDS1615_full.soft.gz'
    filename = join(datasetdir, "burczynski06/GDS1615_full.soft.gz")
    # url = 'ftp://ftp.ncbi.nlm.nih.gov/geo/datasets/GDS1nnn/GDS1615/soft/GDS1615_full.soft.gz'
    adata = sc.read(filename)  # , backup_url=url)

    return adata


def mixscape_vignette_crispr(backup_dir: str = None) -> AnnData:
    """Applying the Mixscape Vignette to the Mixscape dataset.

    https://satijalab.org/seurat/articles/mixscape_vignette.html

    Args:
        backup_dir: Path to the directory of the dataset

    Returns:
        :class:`~anndata.AnnData` object of the Crispr dataset
    """
    assert backup_dir is not None
    adata = anndata.read(join(backup_dir, "eccite_mixscape_clean.h5ad"))

    return adata