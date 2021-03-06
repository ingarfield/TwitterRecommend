# import code from Divisi2, a sparse matrix machine-learning library
# from the Media Lab
# (http://csc.media.mit.edu/docs/divisi2)
import divisi2
import numpy as np
import sys
from csc_utils.ordered_set import OrderedSet

thebands = OrderedSet([])

file = open('band-graph.txt')
for line in file:
    band, fan = line.strip().split()
    thebands.add(band)

NBANDS = len(thebands)
NBITS = 12
MODULO = 1<<NBITS
print NBANDS

matrix = divisi2.DenseMatrix(
    np.zeros((NBANDS, MODULO)),
    row_labels = thebands
)

file.seek(0)
counter = 0
for line in file:
    band, fan = line.strip().split()
    row = matrix.row_labels.index(band)
    col = hash(fan) % MODULO
    matrix[row,col] += 1
    counter += 1
    if counter % 1000 == 0:
        print >> sys.stderr, counter
file.close()

U, S, V = matrix.normalize_rows(offset=0.01).svd(k=20)
similar_bands = divisi2.reconstruct_similarity(U, S)
for band in thebands:
    similar = similar_bands.row_named(band).top_items(10)
    print "%s\t%s" % (band, similar)

