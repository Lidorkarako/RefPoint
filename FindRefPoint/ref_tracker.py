"""
Created by Lidor Karako (LK)
May, 2020
"""


class GetRefPoint():
    def __init__(self, image_path, kernel=[]):
        self.image_path = image_path
        if kernel==[]:
            self.kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (35, 35))
        else:
            self.kernel = kernel
        return

    def refPoint(self):
        if not os.path.exists(self.image_path):
            return print('wrong path - try again!')
        else:
            current_image = cv2.imread(self.image_path)
            try:
                if current_image.shape[-1] == 3:
                    img_gray = cv2.cvtColor(current_image, cv2.COLOR_BGR2GRAY)
            except:
                img_gray = current_image
            _, img_gray_thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)
            dilated = cv2.dilate(img_gray_thresh, self.kernel, iterations=1)
            cnts = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            c = max(cnts, key=cv2.contourArea)
            left = tuple(c[c[:, :, 0].argmin()][0])
            right = tuple(c[c[:, :, 0].argmax()][0])
            up = tuple(c[c[:, :, 1].argmin()][0])
            bot = tuple(c[c[:, :, 1].argmax()][0])
            # line1:
            slope1 = (left[1] - right[1]) / (left[0] - right[0])
            yintrsct1 = left[1] - slope1 * left[0]
            # line2:
            slope2 = (up[1] - bot[1]) / (up[0] - bot[0])
            yintrsct2 = up[1] - slope2 * up[0]
            # intersection of two lines:
            x_center = (yintrsct2 - yintrsct1) / (slope1 - slope2)
            y_center = slope1 * x_center + yintrsct1
            return x_center, y_center

    def binaryMask(self):
        if not os.path.exists(self.image_path):
            return print('wrong path - try again!')
        else:
            current_image = cv2.imread(self.image_path)
            try:
                if current_image.shape[-1] == 3:
                    img_gray = cv2.cvtColor(current_image, cv2.COLOR_BGR2GRAY)
            except:
                img_gray = current_image
            _, img_gray_thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)
            dilated = cv2.dilate(img_gray_thresh, self.kernel, iterations=1)
            cnts = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            c = max(cnts, key=cv2.contourArea)

            mask = np.zeros(img_gray.shape, dtype='uint8')
            object_mask = cv2.drawContours(mask, [c], -1, 255, -1)
            # img_gray_cropped = img_gray * (object_mask / 255)
        return object_mask