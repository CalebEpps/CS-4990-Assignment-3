import os

import a_acquire
import b_enhance
import c_describe
import d_match

if __name__ == "__main__":



    # # Match Steps:
    # # Step 1: Hough Transform
    # # Step 2: Return the Best Match
    # match = d_match.match(en_fingerprint_1, ridge_endings_1, bifurcations_1, en_fingerprint_2, ridge_endings_2, bifurcations_2, view=False)

    file_path = "Group4_dataset/"

    list_of_minutiae = [[0] * 10] * 10

    file_list = os.listdir(file_path)
    print(file_list)
    y = 0
    for x in range(len(file_list)):
        # Run comparisons in here and replace the above line
        # Acquire Test
        fingerprint_filepath_1 = "Group4_dataset/" + os.listdir("Group4_dataset")[x]
        print(fingerprint_filepath_1)
        fingerprint_filepath_2 = "Group4_dataset/" + os.listdir("Group4_dataset")[y]

        # Fingerprint 1 Test
        fingerprint_1 = a_acquire.acquire_from_file(file_path=fingerprint_filepath_1, view=False)
        pp_fingerprint_1, en_fingerprint_1, mask_1 = b_enhance.enhance(fingerprint_1, dark_ridges=False,
                                                                            view=False)
        ridge_endings_1, bifurcations_1 = c_describe.describe(en_fingerprint_1, mask_1, view=False)

        # Fingerprint 2 Test
        fingerprint_2 = a_acquire.acquire_from_file(file_path=fingerprint_filepath_2, view=False)
        pp_fingerprint_2, en_fingerprint_2, mask_2 = b_enhance.enhance(fingerprint_2, dark_ridges=False,
                                                                            view=False)
        ridge_endings_2, bifurcations_2 = c_describe.describe(en_fingerprint_2, mask_2, view=False)

        # Match Test
        match = d_match.match(en_fingerprint_1, ridge_endings_1, bifurcations_1, en_fingerprint_2, ridge_endings_2,
                                   bifurcations_2, view=False)

        list_of_minutiae[x][y] = max(match)
        list_of_minutiae[y][x] = max(match)
        y += 1


    for x in list_of_minutiae:
        print(' '.join(map(str, x)))
    #
    # for x in os.listdir(file_path):
    #     for y in os.listdir(file_path):
    #         fingerprint_filepath_1 = x
    #
    # for x in os.listdir("dataset"):
    #     # Acquisition Steps: (Trait Acquisition)
    #     # Step 1. Load data as a matrix of values
    #     fingerprint_filepath_1 = "dataset/" + x
    #     print(fingerprint_filepath_1)
    #     fingerprint_1 = a_acquire.acquire_from_file(file_path=fingerprint_filepath_1, view=False)
    #     # # Enhancement Steps: (Feature Enhancement)
    #     # # Step 1. Pre-processing
    #     # # Step 2. Segmentation
    #     # # Step 3. Compute Orientations
    #     # # Step 4. Compute Ridge Frequency
    #     # # Step 5. Apply Gabor Filters
    #     # # Step 6. Skeletonization
    #     #
    #     pp_fingerprint_1, en_fingerprint_1, mask_1 = b_enhance.enhance(fingerprint_1, dark_ridges=False, view=False)
    #     #
    #     # # Describe Steps: (Feature Extraction)
    #     # # Step 1: Detect Minutiae
    #     # # Step 2: Remove False Positive Minutiae
    #     ridge_endings_1, bifurcations_1 = c_describe.describe(enhanced_fingerprint=en_fingerprint_1, mask=mask_1,
    #                                                           view=False)
