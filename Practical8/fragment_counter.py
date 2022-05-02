seq = 'ATGCAATCGACTACGATCAATCGAGGGCC'  # the variable sequence
num_fragment = seq.count('GAATTC') + 1  # counter
print(str(num_fragment) + " fragment(s) will generate if we use EcoRI to cut the sequence")
# print out the correct number of fragments generated.

# the sequence can't be cut if we apply the EcoRI enzyme.
# so the result is that 1 fragment(s) will generate if we use EcoRI to cut the sequence.
