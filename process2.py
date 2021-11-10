def blur_norm(img):
    img = cv2.imread(img)
    blurred = cv2.blur(img, (3, 3))
    return blurred
    
def blur_gaus(img):
    img = cv2.imread(img)
    blurred = cv2.GaussianBlur(img, (3,3))
    return blurred

def blur_med(img):
    img = cv2.imread(img)
    blurred = cv2.medianBlur(img, 3)
    
    