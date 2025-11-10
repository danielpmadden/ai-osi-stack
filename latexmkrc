# SPDX-License-Identifier: Apache-2.0
# Authored and maintained solely by the Custodial Editorial Committee.
# This script is provided for non-operational, reproducibility support.
# No AEIP runtime logic is exposed or executed here.

$pdf_mode = 1;
$silent = 1;
$pdflatex = 'pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -synctex=1 -shell-escape';
$out_dir = 'versions';
$aux_dir = 'versions/.aux';
$ENV{TEXMFOUTPUT} = 'versions/.aux';
$ENV{SOURCE_DATE_EPOCH} = $ENV{SOURCE_DATE_EPOCH} // '1731196800';
$cleanup_includes_generated = 1;
$clean_ext .= ' synctex.gz';
