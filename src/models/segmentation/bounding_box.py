import cv2
import numpy as np

from typing import List, Optional

def add_bounding_box(
    image_paths: List[str], save_fp: Optional[str] = None
) -> cv2.typing.MatLike | None:
    result = []

    for image_path in image_paths:
        image = cv2.imread(image_path)
        original_image = image.copy()
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        sharpening_filter = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        sharpened_image = cv2.filter2D(gray_image, -1, sharpening_filter)

        edges = cv2.Canny(sharpened_image, 50, 100)
        contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_L1)

        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(original_image, (x, y), (x + w, y + h), (0, 0, 255), 5)

        if save_fp:
            cv2.imwrite(save_fp, original_image)
        else:
            result.append(original_image)

    # cv2.imshow("Bounding Boxes", original_image)

    # while True:
    #     if cv2.waitKey(1) & 0xFF == ord("q"):
    #         break

    # cv2.destroyAllWindows()


    if save_fp:
        return

    return result

