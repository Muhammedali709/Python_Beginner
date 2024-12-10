matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]

def matris_carp(a, b):
    satir_a, sutun_a = len(a), len(a[0])
    satir_b, sutun_b = len(b), len(b[0])
    sonuc = [[0] * sutun_b for _ in range(satir_a)]
    for i in range(satir_a):
        for j in range(sutun_b):
            for k in range(sutun_a):
                sonuc[i][j] += a[i][k] * b[k][j]
    return sonuc

sonuc_matrisi = matris_carp(matrix_a, matrix_b)
for satir in sonuc_matrisi:
    print(satir)
