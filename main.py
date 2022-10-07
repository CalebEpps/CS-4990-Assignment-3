import os

import a_acquire
import b_enhance
import c_describe
import d_match


class Fingerprint_Comparison():

    def __init__(self):
        pass # Move methods here if you feel like it, assign some variables, or delete it, IDGAF

    def process_matrix(self, dataset_dir, list_of_minutiae):
        # Neat little method that gets all the file paths queuried into a list
        file_list = os.listdir(dataset_dir)
        print(file_list)

        # Outer loop
        for x in range(len(file_list)):
            # Inner loop (Can be replaced by assigning [x][y] to [y][x], just didn't do it yet
            for y in range(len(file_list)):
                # Below is basically the code we did in class
                # Acquire fingerprint x and fingerprint y filepaths
                fingerprint_filepath_1 = "Group4_dataset/" + os.listdir("Group4_dataset")[x]
                print(fingerprint_filepath_1)
                fingerprint_filepath_2 = "Group4_dataset/" + os.listdir("Group4_dataset")[y]

                # Fingerprint x acquirement, enhancement, and extraction
                fingerprint_1 = a_acquire.acquire_from_file(file_path=fingerprint_filepath_1, view=False)
                pp_fingerprint_1, en_fingerprint_1, mask_1 = b_enhance.enhance(fingerprint_1, dark_ridges=False,
                                                                               view=False)
                ridge_endings_1, bifurcations_1 = c_describe.describe(en_fingerprint_1, mask_1, view=False)

                # Fingerprint y acquirement, enhancement, and extraction
                fingerprint_2 = a_acquire.acquire_from_file(file_path=fingerprint_filepath_2, view=False)
                pp_fingerprint_2, en_fingerprint_2, mask_2 = b_enhance.enhance(fingerprint_2, dark_ridges=False,
                                                                               view=False)
                ridge_endings_2, bifurcations_2 = c_describe.describe(en_fingerprint_2, mask_2, view=False)

                # Match (Returns a list of matches with best at index 0, possible there are no matches and it needs to be accounted for)
                match = d_match.match(en_fingerprint_1, ridge_endings_1, bifurcations_1, en_fingerprint_2,
                                      ridge_endings_2,
                                      bifurcations_2, view=False)

                # Assigns the first match to the matrix, but it won't work if match is None
                list_of_minutiae[x][y] = match[0]

                # Printing loop only for testing purposes O(n^3) so very bad rip

                self.pretty_print_matrices(list_of_minutiae=list_of_minutiae)

    def pretty_print_matrices(self, list_of_minutiae):
        # Print the final resulting matrix
        for x in list_of_minutiae:
            print(' '.join(map(str, x)))


if __name__ == "__main__":
    dataset_dir = "Group4_dataset/"
    list_of_minutiae = [[0] * 10] * 10

    fingerprint_comp = Fingerprint_Comparison()
    fingerprint_comp.process_matrix(dataset_dir=dataset_dir, list_of_minutiae=list_of_minutiae)
