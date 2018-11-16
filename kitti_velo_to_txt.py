import numpy as np

def load_velo_scan(file):
    """Load and parse a velodyne binary file."""
    scan = np.fromfile(file, dtype=np.float32)       
    return scan.reshape((-1, 4))


def main():
    velo_file_txt = load_velo_scan("path/to/bin/file/00000.bin")           
    np.savetxt("path/for/text/file/00000.txt", velo_file_txt, fmt='%1.3f', delimiter = ',')

main()
