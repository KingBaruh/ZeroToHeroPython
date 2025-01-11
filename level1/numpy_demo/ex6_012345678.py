import numpy as np
from imageio.v3 import imread
import matplotlib.pyplot as plt

#######################################################################
# Part 1 - numpy
def get_highest_weight_loss_participant(training_data, participant_names):
    """
    :param training_data: a numpy matrix of shape (n_participants, n_months) .
    :param participant_names: a list of strings, each string represents a participant.
    :return: the highest weight loss participant's name.
    """
    max_loss_index = np.argmax(training_data[:, 0] - training_data[:, -1])
    return participant_names[max_loss_index]

def get_diff_data(training_data):
    """
    :param training_data: a numpy matrix of shape (n_participants, n_months).
    :return: a numpy matrix of shape (n_participants, n_months-1) representing the difference between each pair of consecutive months.
    """
    pass


def get_highest_change_month(training_data, study_months):
    """
    :param training_data: a numpy matrix of shape (n_participants, n_months).
    :param study_months: a list of strings, each string represents a month in the study.
    :return: the month with the highest change across participants.
    """
    pass

def get_inconsistent_participants(training_data, participant_names):
    """
    :param training_data: a numpy matrix of shape (n_participants, n_months).
    :param participant_names: a list of strings, each string represents a participant.
    :return: a list of participant names that didn't lose weight consistently every month throughout the study.
    If there are no such participants, the function will return an empty list.
    """
    pass

#######################################################################
# Part 2 - numpy image processing

def read_image(img_path, mode='L'):
    """
    :param img_path: path of an image to read
    :param mode: (for bonus) the mode of the image to be read, 'L' for grayscale (default), 'RGB' for RGB.
    :return: a uint8 numpy array representing the image, with values between 0 and 255.
    will return an array shaped (h,w) (bonus: if mode == 'L', or (h,w,3) if mode == 'RGB'.)
    """
    pass

def naive_blending(img1, img2, mask):
    """
    :param img1: a uint8 numpy array representing an image
    :param img2: a uint8 numpy array representing an image
    :param mask: a uint8 numpy array representing a boolean image in equal size of im1 and im2, that defines how the two images should be blended.
    :return: a blended image where img_1 pixels are used for the white areas of the mask, and img_2 pixels are used for the black areas.
    """
    pass

def blur_and_downsample(img, nb_size=5):
    """
    A function that blurs the given image, and then reduces its resolution by 2 (both width and length) by choosing
    every second pixel in every second row.
    :param img: a uint8 numpy array representing an image
    :param nb_size: The neighborhood size to be used for blurring
    :return: the reduced and blurred image
    """
    pass


def build_gaussian_pyramid(img, max_levels, nb_size=5):
    """
    A function that builds a gaussian pyramid of the given image, by sequentially blurring and down-sampling the current
    image until reaching max_levels.
    :param img: a uint8 numpy array representing an image.
    :param max_levels: The maximal depth levels that should be constructed.
    :param nb_size: The neighborhood size to be used for blurring.
    :return: a list representing the image's gaussian pyramid, each entry is the previous image down-sampled to half the
    resolution of the previous one.
    """
    pass

def upsample_and_blur(img, nb_size=5):
    """
    A function that doubles the size of the given image, and blurs it.
    :param img: a uint8 numpy array representing an image.
    :param nb_size: The neighborhood size to be used for blurring.
    :return: a numpy array representing the expanded blurred image.
    """
    pass

def build_laplacian_pyramid(img, max_levels, nb_size=5):
    """
    A function that builds a laplacian pyramid of the given image, by sequentially up-sampling the next level gaussian
    image and subtracting it from the current level gaussian image, until reaching max_levels.
    :param img: a uint8 numpy array representing an image.
    :param max_levels: The maximal depth levels that should be constructed
    :param nb_size: The neighborhood size to be used for blurring.
    :return: a list representing a laplacian pyramid of the given image.
    """
    pass

def laplacian_pyramid_to_image(laplacian_pyramid, nb_size=5):
    """
    A function that reconstructs an image from the given laplacian pyramid, by iteratively combining all laplacian
    images after up-sampling.
    :param laplacian_pyramid: a list representing a laplacian pyramid.
    :param nb_size: The neighborhood size to be used for blurring.
    :return: The reconstructed image.
    """
    pass

def pyramid_blending(img1, img2, mask, max_levels, nb_size=5):
    """
    A function that blends two images using pyramids.
    :param img1: a uint8 numpy array representing a grayscale image that will compose the white parts of the mask.
    :param img2: a uint8 numpy array representing a grayscale image that will compose the black parts of the mask.
    :param mask: a uint8 numpy array representing a boolean image in equal size of im1 and im2, that defines how the two images should be blended
    :param max_levels: The max depth of the pyramids used in this function
    :param nb_size: The neighborhood size to be used for blurring.
    :return: The blended image
    """
    pass

############ Bonus ############

def pyramid_blending_RGB_image(img1, img2, mask, max_levels, nb_size=5):
    """
    A function that blends two RGB images using pyramids.
    :param img1: a uint8 numpy array representing an RGB image that will compose the white parts of the mask.
    :param img2: a uint8 numpy array representing an RGB image that will compose the black parts of the mask.
    :param mask: a uint8 numpy array representing a boolean image in equal size of im1 and im2, that defines how the two images should be blended
    :param max_levels: The max depth of the pyramids used in this function
    :param nb_size: The neighborhood size to be used for blurring.
    :return: The blended image
    """
    pass


if __name__ == '__main__':
    def array_compare(a, b, threshold=1e-10):
        if a.shape != b.shape:
            return False
        return np.abs(a - b).mean() < threshold

    #######################################################################
    # Q1 checks
    print("Starting Q1 checks")
    training_data = np.loadtxt('training_data.csv', delimiter=',')
    participant_names = ['Jane', 'Naomi', 'John', 'Moshe']
    study_months = ['November', 'December', 'January', 'February', 'March', 'April']

    diff_data_expected = np.array([[-2.7, 1.5, -2.7, -2.7, -2.2],
                                   [-4.4, -0.2, -0.7, -1.5, -1.4],
                                   [-1.0, -1.2, 0.6, -0.3, -1.6],
                                   [-2.5, -4.1, -3.1, -2.7, -2.8]])

    print(get_highest_weight_loss_participant(training_data, participant_names) == 'Moshe')
    print(array_compare(get_diff_data(training_data), diff_data_expected))
    print(get_highest_change_month(training_data, study_months) == 'November')
    print(set(get_inconsistent_participants(training_data, participant_names)) == set(['Jane', 'John']))

    training_data = np.array([[92.3, 91.5, 89.4, 89.2, 88.6, 85.9],
                              [104.6, 102.1, 100.8, 98.5, 96.3, 94.4],
                              [73.2, 72.6, 72.0, 71.4, 71.2, 70.9],
                              [78.3, 78.0, 77.2, 75.8, 74.7, 74.4]])

    diff_data_expected = np.array([[-0.8, -2.1, -0.2, -0.6, -2.7],
                                   [-2.5, -1.3, -2.3, -2.2, -1.9],
                                   [-0.6, -0.6, -0.6, -0.2, -0.3],
                                   [-0.3, -0.8, -1.4, -1.1, -0.3]])

    print(get_highest_weight_loss_participant(training_data, participant_names) == 'Naomi')
    print(array_compare(get_diff_data(training_data), diff_data_expected))
    print(get_highest_change_month(training_data, study_months) == 'March')
    print(get_inconsistent_participants(training_data, participant_names) == [])

    #######################################################################
    # Q2 checks
    print("Starting Q2 checks")
    plot_flag = True  # Convert to False to not show plots

    def compare_images(img, img_path, mode):
        if mode == 'RGB':
            plt.imsave(f"stud_{img_path}", img)
        else:
            plt.imsave(f"stud_{img_path}", img, cmap='gray')

        stud_naive_blended_im = imread(f"stud_{img_path}", mode=mode) / 255
        gt_naive_blended_im = imread(f"results_for_presubmit_tests/{img_path}", mode=mode) / 255
        print(array_compare(gt_naive_blended_im, stud_naive_blended_im, threshold=1/254))


    # Q1
    print("Q1.1")
    img1 = read_image('apple.png')
    img2 = read_image('orange.png')
    mask = read_image('mask.png')

    print(img1.shape == img2.shape == mask.shape == (448, 624))

    max_levels = 5
    nb_size = 5

    if plot_flag:
        import matplotlib.patches as patches

        fig, axes = plt.subplots(1, 3, figsize=(9, 3))
        axes[0].imshow(img1, cmap='gray')
        axes[0].axis('off')
        axes[0].title.set_text('Original Image 1')
        axes[1].imshow(img2, cmap='gray')
        axes[1].axis('off')
        axes[1].title.set_text('Original Image 2')
        axes[2].imshow(mask, cmap='gray')  # cmap is required for presenting a grayscale image
        axes[2].axis('off')
        axes[2].title.set_text('Mask')
        border = patches.Rectangle((0, 0), mask.shape[1], mask.shape[0],
                                   linewidth=3, edgecolor='black', facecolor='none')
        axes[2].add_patch(border)
        plt.show()

    # Q2
    print("Q1.2")
    naive_blended_img = naive_blending(img1, img2, mask)
    compare_images(naive_blended_img, "orapple_naive.png", mode='L')

    if plot_flag:
        plt.imshow(naive_blended_img, cmap='gray')
        plt.title("Q2 - naive blending")
        plt.axis('off')
        plt.show()

    # Q3.a
    print("Q1.3.a")
    blurred_img = blur_and_downsample(img1, 5)
    print(blurred_img.shape == (224, 312))
    compare_images(blurred_img, "blurred_apple.png", mode='L')
    if plot_flag:
        plt.imshow(blurred_img, cmap='gray')
        plt.title("Q3.a - image blur")
        plt.axis('off')
        plt.show()

    # Q3.b
    print("Q1.3.b")
    im1_gp = build_gaussian_pyramid(img1, 3, 5)
    print(len(im1_gp) == 3)

    for i in range(3):
        print(im1_gp[i].shape == tuple(s // (2 ** i) for s in img1.shape))
        compare_images(im1_gp[i], f"gp3_im{i}.png", mode='L')

    # Q3.c
    print("Q1.3.c")
    upsampled_im = upsample_and_blur(img1, 5)
    print(upsampled_im.shape == tuple(s * 2 for s in img1.shape))
    compare_images(upsampled_im, "upsampled_im.png", mode='L')

    # Q3.d
    print("Q1.3.d")
    im1_lp = build_laplacian_pyramid(img1, 3, 5)
    print(len(im1_lp) == 3)

    for i in range(3):
        print(im1_lp[i].shape == tuple(s // (2 ** i) for s in img1.shape))
        compare_images(im1_lp[i], f"lp3_im{i}.png", mode='L')

    # Q3.e
    print("Q1.3.e")
    reconstructed_img = laplacian_pyramid_to_image(im1_lp, 5)
    print(reconstructed_img.shape == img1.shape)
    compare_images(reconstructed_img, "reconstructed_apple.png", mode='L')

    # Q3.f
    print("Q1.3.f")
    blended_im_gray = pyramid_blending(img1, img2, mask, max_levels, nb_size)
    compare_images(blended_im_gray, "blended_im_gray.png", mode='L')
    if plot_flag:
        plt.imshow(blended_im_gray, cmap='gray')
        plt.title("Q3.f - image blending")
        plt.axis('off')
        plt.show()

    # Q3.g (Bonus)
    print("======= Bonus Part =======")
    print("Q1.3.g")
    img1 = read_image('apple.png', 'RGB')
    img2 = read_image('orange.png', 'RGB')
    mask = read_image('mask.png', 'L')
    print(img1.shape == img2.shape == (448, 624, 3))
    print(mask.shape == (448, 624))
    blended_im = pyramid_blending_RGB_image(img1, img2, mask, max_levels, nb_size)
    compare_images(blended_im, "orapple.png", mode='RGB')

    if plot_flag:
        plt.imshow(blended_im)
        plt.title("Q3.g - RGB image blending")
        plt.axis('off')
        plt.show()
