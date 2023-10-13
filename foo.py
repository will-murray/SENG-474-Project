import hdf5_getters as h5get
path = "MillionSongSubset\A\A\A\TRAAAAW128F429D538.h5"
songfile = h5get.open_h5_file_read(path)
print(h5get.get_tempo(songfile))

songfile.close()

