def recoverSecret(triplets):
    lic = set()
    for triplet in triplets:
        lic.update(set(triplet))
    lic = list(lic)
    while True:
        cnt = 0
        for i in range(len(triplets)):
            for j in range(len(triplets[i]) - 1):
                a = triplets[i][j]
                b = triplets[i][j+1]
                index_a = lic.index(a)
                index_b = lic.index(b)
                if index_a > index_b:
                    lic[index_a], lic[index_b] = lic[index_b], lic[index_a]
                    cnt += 1
        if cnt == 0:
            return ''.join(lic)
