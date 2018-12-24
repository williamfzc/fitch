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


def cal_location(result_dict: dict):
    """ analyse result and get its position """
    data = result_dict['data'][0]
    sim = data['max_val']
    target_point = data['max_loc']
    assert sim > config.CV_THRESHOLD, 'target point not found'
    logger.info('sim == {}, found it on ({}, {})'.format(sim, *target_point))
    return target_point


if __name__ == '__main__':
    res = detect('../point.png', '../screen.png')
    print(res)
