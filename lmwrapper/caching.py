from pathlib import Path
from joblib import Memory
import diskcache

cur_file = Path(__file__).parent.absolute()


def _cache_dir():
    return cur_file / '../lm_model_cache'


def _get_disk_cache_joblib() -> Memory:
    diskcache = Memory(_cache_dir(), verbose=0)
    return diskcache


def _get_disk_cache_diskcache() -> diskcache.FanoutCache:
    return diskcache.FanoutCache(
        str(_cache_dir()), timeout=int(9e9), size_limit=50e9, shards=4, eviction_policy='none')


def get_disk_cache():
    return _get_disk_cache_diskcache()


def clear_cache_dir():
    import shutil
    shutil.rmtree(_cache_dir())

