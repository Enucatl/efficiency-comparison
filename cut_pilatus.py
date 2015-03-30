import h5py

with h5py.File("data/pilatus_time_series.hdf5") as input_file:
    group = input_file["raw_images"]
    for i, key in enumerate(group):
        index = int(key.split("_")[2])
        if index < 59146:
            del group[key]
