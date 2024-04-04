import os
import pandas as pd
from glob import glob
from mapping import MAPPER
from drop_cols import DUPLICATES, UNNEEDED


def preprocess(
    folder="preprocessing/data",
    concat=True,
    drop_dupes=True,
    drop_unneeded=True,
    processed_prefix="PROCESSED_",
    concat_prefix="CONCAT_",
    concat_file="",
    remove_old=True,
    DEBUG_drop_rows=False,
    DEBUG_print_status_full=False,
):
    # DOCUMENTATION
    """Preprocess files


    kwargs:

    folder -- folder containing input/output folders (default "preprocessing/data")

    concat -- if True, concatenate output files (default True)

    drop_dupes -- if True, drop dupe cols; defined in drop_cols.py (default True)

    drop_unneeded -- if True, drop unneeded cols; defined in drop_cols.py (default True)

    processed_prefix -- prefix for processed files (default "PROCESSED_)

    concat_prefix -- prefix for concat file (default "CONCAT_")

    concat_file -- if not an empty string, filename to use for concat file (default "")

    remove_old -- if True, remove old output files (default True)

    DEBUG_drop_rows -- if True, drop all but the first 100 rows of files (default False)

    DEBUG_print_status_full -- if True, print every col name during mapping (default False)
    """

    # makes dirs if not exist
    if not os.path.exists((folder + "/input") or (folder + "/output")):
        print("folder DNE; creating folders")
        os.makedirs(folder + "/input", exist_ok=True)
        os.makedirs(folder + "/output", exist_ok=True)

    # removes old output
    if remove_old:
        print("removing old output")
        for f in glob(folder + "/output/*.csv"):
            os.remove(f)

    # mapping
    print("~~~~~MAPPING~~~~~")
    for f in glob(folder + "/input/*.csv"):
        print("Processing file: " + os.path.basename(f))
        print("reading file")
        df = pd.read_csv(f, dtype="string")

        # drops rows/cols
        if DEBUG_drop_rows:
            print("dropping rows")
            df = df[:100]
        if drop_dupes:
            print("dropping dupe cols")
            try:
                df = df.drop(DUPLICATES, axis=1)
            except:
                pass
        if drop_unneeded:
            print("dropping unneeded cols")
            try:
                df = df.drop(UNNEEDED, axis=1)
            except:
                pass

        # remaps all col values according to mapping.py MAPPER
        print("remapping")
        for col in MAPPER.keys():
            if DEBUG_print_status_full:
                print("mapping: ", end="")

            try:
                df[col] = df[col].map(MAPPER.get(col), na_action="ignore")
                if DEBUG_print_status_full:
                    print(col)
            except KeyError:
                if DEBUG_print_status_full:
                    print("COL DROPPED")
                next

        # saves file
        print("saving file: " + processed_prefix + os.path.basename(f)[:-4] + ".csv")
        df.to_csv(
            folder + "/output/" + processed_prefix + os.path.basename(f)[:-4] + ".csv"
        )

    # concatenates
    if concat:
        print("\n~~~~~CONCATENATING~~~~~")
        print("reading files")
        files = glob(folder + "/output/*.csv")
        dfs = [pd.read_csv(f, dtype="string") for f in files]
        df = pd.concat(dfs, ignore_index=True)

        if concat_file == "":
            filename = (
                concat_prefix
                + "_".join([os.path.basename(f)[:-4] for f in files])
                + ".csv"
            )
        else:
            filename = concat_file + ".csv"

        print("saving concat file: " + filename)
        df.to_csv(folder + "/output/" + filename)
