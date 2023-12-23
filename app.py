from utils.cv_booster import cvBooster

if __name__=='__main__':
    cv = cvBooster("./test/GabrieleCaletti.pdf")
    print(cv.infos)
    cv.re_write(cv.education, "expand")