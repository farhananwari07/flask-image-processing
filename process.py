import cv2
from numpy.core.fromnumeric import argsort
from skimage.filters import threshold_otsu, threshold_niblack, threshold_sauvola

def otsu_thresh(img):
    img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


def niblack_thresh(img):
    img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    res = img.copy()
    thresh_niblack = threshold_niblack(img, window_size=25, k=0.8)
    thresh_niblack = cv2.ximgproc.niBlackThreshold(img, maxValue=255, type=cv2.THRESH_BINARY_INV, blockSize=2*11+1, k=-0.2, binarizationMethod=cv2.ximgproc.BINARIZATION_NICK)

    binary_niblack = img > thresh_niblack

    for i in range(res.shape[0]):
        for j in range(res.shape[1]):
            if binary_niblack[i][j]==True:
                res[i][j]=255
            else:
                res[i][j]=0
    return res

def sauvola_thresh(img):
    img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    res = img.copy()
    thresh_sauvola = threshold_sauvola(img, window_size=25)
    thresh_sauvola = cv2.ximgproc.niBlackThreshold(img, maxValue=255, type=cv2.THRESH_BINARY_INV, blockSize=2*11+1, k=-0.2, binarizationMethod=cv2.ximgproc.BINARIZATION_SAUVOLA)

    binary_sauvola = img > thresh_sauvola

    for i in range(res.shape[0]):
        for j in range(res.shape[1]):
            if binary_sauvola[i][j]==True:
                res[i][j]=255
            else:
                res[i][j]=0
    return res

#ip_thres
def sim_thresh(img):
    img = cv2.imread(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    (T, threshInv) = cv2.threshold(blurred, 230, 255,cv2.THRESH_BINARY_INV)
    return threshInv

def mean_thresh(img):
    img = cv2.imread(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    thresh = cv2.adaptiveThreshold(blurred, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 10)
    return thresh

def gaus_thresh(img):
    img = cv2.imread(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 4)
    return thresh

#ip_canny

def wid_map(img):
    img = cv2.imread(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    wide = cv2.Canny(blurred, 10, 200)
    return wide

def mid_map(img):
    img = cv2.imread(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    mid = cv2.Canny(blurred, 30, 150)
    return mid

def tight_map(img):
    img = cv2.imread(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    tight = cv2.Canny(blurred, 240, 250)
    return tight
#color space

def blue(img):
    img = cv2.imread(img)
    B, G, R = cv2.split(img)
    return B

def red(img):
    img = cv2.imread(img)
    B, G, R = cv2.split(img)
    return R
    
def green(img):
    img = cv2.imread(img)
    B, G, R = cv2.split(img)
    return G

def hsv(img):
    img = cv2.imread(img)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    return hsv

def hue(img):
    img = cv2.imread(img)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    H, S, V = cv2.split(hsv)
    return H

def saturation(img):
    img = cv2.imread(img)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    H, S, V = cv2.split(hsv)
    return S

def value(img):
    img = cv2.imread(img)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    H, S, V = cv2.split(hsv)
    return V

def lab (img):
    img = cv2.imread(img)
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    return lab

def l (img):
    img = cv2.imread(img)
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    L, a, b = cv2.split(hsv)
    return L

    
    
    
    


    
    