import numpy as np
import matplotlib.pyplot as plt

def init_ca(size: int, center_value = 1, dtype = np.int32):
    """
    Returns an array initialized with 0 while the center value is being specified.

    Parameters
    ----------
    size : int
        The size of this array
    center_value : int, optional
        The value of center cell in the array
    dtyp : np.type
        The type of numbers in each cell
    """
    res = np.zeros(size, dtype = dtype)
    res[len(res)//2] = center_value
    return np.array([res]) 

def plot(ca):
    """
    Plot the given cellular automate

    Parameters
    ----------
    ca : numpy array
        The cellular automata
    """

    fig = plt.figure()
    plt.imshow(ca, interpolation='none', cmap="Greys")
    plt.draw()
    plt.waitforbuttonpress(0) # this will wait for indefinite time
    plt.close(fig)


def evolve(ca, timesteps, apply_rule):
    _, cols = ca.shape
    array = np.zeros((timesteps, cols), dtype=ca.dtype)
    array[0] = ca[-1]
    cell_indices = list((range(len(ca[-1]))))

    for t in range(1, timesteps):
        cells = array[t-1]
        strides = _index_strides(np.arange(len(cells)), 2 * 1 + 1)
        neighbourhoods = cells[strides]
        array[t] = np.array([apply_rule[_binary_trans(n)]   for n in neighbourhoods])
    return np.concatenate((ca, array[1:]), axis=0)

def _binary_trans(neighbourhood: list[int]):
    ans = 0
    for i, e in enumerate(reversed(neighbourhood)):
        ans += e*(pow(2,i))
    return ans

def _index_strides(arr, window_size):
    """
    Returns an array with dimensions len(cells) x window_size, representing the cell indices of the neighbourhood
    of each cell.

    :param arr: an array containing the cell indices; e.g. if there are 5 cells, then the argument
                will be [0, 1, 2, 3, 4]

    :param window_size: the size of the neighbourhood

    :return: an array with dimensions len(cells) x window_size, representing the cell indices of the neighbourhood
             of each cell
    """
    # this function is based on code in http://www.credid.io/cellular-automata-python-2.html
    arr = np.concatenate((arr[-window_size // 2 + 1:], arr, arr[:window_size // 2]))
    shape = arr.shape[:-1] + (arr.shape[-1] - window_size + 1, window_size)
    strides = arr.strides + (arr.strides[-1],)
    return np.lib.stride_tricks.as_strided(arr, shape=shape, strides=strides)