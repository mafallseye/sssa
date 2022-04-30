import random


def getAdditiveShares(secret, N, fieldSize):
    '''Generate N additive shares from 'secret' in finite field of size 'fieldSize'.'''

    # Generate n-1 shares randomly
    shares = [random.randrange(fieldSize) for i in range(N-1)]

    # Append final share by subtracting all shares from secret
    # Modulo is done with fieldSize to ensure share is within finite field
    shares.append((secret - sum(shares)) % fieldSize)
    return shares


def reconstructSecret(shares, fieldSize):
    '''Regenerate secret from additive shares'''
    return sum(shares) % fieldSize


if __name__ == "__main__":
    # Generating the shares
    shares = getAdditiveShares(1234, 5, 10**5)
    print('Shares are:', shares)

    # Reconstructing the secret from shares
    print('Reconstructed secret:', reconstructSecret(shares, 10**5))
