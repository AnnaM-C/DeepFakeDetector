from yacs.config import CfgNode as CN

_C = CN()

_C.TRAIN = CN()
_C.TRAIN.EPOCHS = 50
_C.TRAIN.DATA = CN()
_C.TRAIN.DATA.REAL_DATA = CN()
_C.TRAIN.DATA.REAL_DATA.DATASET = ''
_C.TRAIN.DATA.REAL_DATA.ROOT_PATH = ''
_C.TRAIN.DATA.REAL_DATA.SPLITS_FILE = ''
_C.TRAIN.DATA.FAKE_DATA = CN()
_C.TRAIN.DATA.FAKE_DATA.DATASET = ''
_C.TRAIN.DATA.FAKE_DATA.ROOT_PATH = ''
_C.TRAIN.DATA.FAKE_DATA.SPLITS_FILE = ''

_C.VALID = CN()
_C.VALID.DATA = CN()
_C.VALID.DATA.REAL_DATA = CN()
_C.VALID.DATA.REAL_DATA.DATASET = ''
_C.VALID.DATA.REAL_DATA.ROOT_PATH = ''
_C.VALID.DATA.REAL_DATA.SPLITS_FILE = ''
_C.VALID.DATA.FAKE_DATA = CN()
_C.VALID.DATA.FAKE_DATA.DATASET = ''
_C.VALID.DATA.FAKE_DATA.ROOT_PATH = ''
_C.VALID.DATA.FAKE_DATA.SPLITS_FILE = ''

_C.TEST = CN()
_C.TEST.DATA = CN()
_C.TEST.DATA.REAL_DATA = CN()
_C.TEST.DATA.REAL_DATA.DATASET = ''
_C.TEST.DATA.REAL_DATA.ROOT_PATH = ''
_C.TEST.DATA.REAL_DATA.SPLITS_FILE = ''
_C.TEST.DATA.FAKE_DATA = CN()
_C.TEST.DATA.FAKE_DATA.DATASET = ''
_C.TEST.DATA.FAKE_DATA.ROOT_PATH = ''
_C.TEST.DATA.FAKE_DATA.SPLITS_FILE = ''


def get_config(args):
    config = _C.clone()

    if args.config_file:
        config.merge_from_file(args.config_file)
    
    config.freeze()
    
    return config