# Additive Sharing with facility to Refresh shares via Proactivization
import random


def getAdditiveShares(secret, N, fieldSize):
    '''Generate N additive shares from 'secret' in finite field of size 'fieldSize'.'''

    # Generate n-1 shares randomly
    shares = [random.randrange(fieldSize) for i in range(N-1)]
    # Append final share by subtracting all shares from secret
    shares.append((secret - sum(shares)) % fieldSize)
    return shares


def reconstructSecret(shares, fieldSize):
    '''Regenerate secret from additive shares'''
    return sum(shares) % fieldSize


def proactivizeShares(shares):
    '''Refreshed shares by proactivization'''

    n = len(shares)
    refreshedShares = [0]*n

    for s in shares:

        # Divide each share into sub-fragments using additive sharing
        subShares = getAdditiveShares(s, n, 10**5)

        # Add subfragments of corresponding parties
        for p, sub in enumerate(subShares):
            refreshedShares[p] += sub

    return refreshedShares


if __name__ == "__main__":
    # Generating the shares
    shares = getAdditiveShares(1234, 5, 10**5)
    print('Shares are:', shares)

    # Running Proactivization
    newShares = proactivizeShares(shares)
    print('Refreshed Shares are:', newShares)

    # Reconstructing secret from refreshed shares
    print('Secret:', reconstructSecret(newShares, 10**5))
