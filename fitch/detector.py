import json

from findit import FindIt

from fitch import config
from fitch.logger import logger


def detect(template, target) -> dict:
    fi = FindIt()
    # change config
    fi.config.cv_method = config.CV_METHOD
    # load template picture
    fi.load_template(template)
    # and find it
    result = fi.find(target)
    logger.info(json.dumps(result))
    return result


if __name__ == '__main__':
    res = detect('../point.png', '../screen2.png')
    print(res)
