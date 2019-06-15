"""
MIT License

Copyright (c) 2018 williamfzc

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import json
import typing
import os

from findit_client import FindItStandardClient
from loguru import logger

from fitch import config

TEMP_TEMPLATE_NAME = 'cur_template'
TEMP_TARGET_NAME = 'cur_target'

fi_client = FindItStandardClient(
    host=config.FINDIT_SERVER_IP,
    port=config.FINDIT_SERVER_PORT,
    local_mode=not config.REMOTE_MODE,
    pic_root=config.DEFAULT_LOCAL_PIC_DIR,
    python_path=config.DEFAULT_PYTHON_EXECUTOR,

    # extra args
    engine=['template'],
    engine_template_cv_method_name=config.CV_METHOD_NAME,
    engine_template_scale=config.CV_PIC_SCALE,
    pro_mode=True,
)


def get_name_from_path(file_path: str) -> str:
    return file_path.split(os.sep)[-1]


def detect(template: typing.Sequence, target: str) -> dict:
    """ return a point list """
    result = fi_client.get_target_point_with_path(
        target, template, threshold=config.CV_THRESHOLD)
    logger.debug('Detect result: {}'.format(json.dumps(result)))
    return dict(zip(template, result))


if __name__ == '__main__':
    res = detect('../point.png', '../screen.png')
    print(res)
