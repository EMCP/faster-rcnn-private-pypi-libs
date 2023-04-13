from datasets.coco_custom import coco_custom

__sets = {}
from datasets.coco_try_abletonlive10 import coco_try_alc
from datasets.coco import coco


# Set up alc_coco_<year>_<split>
for data_date in ['20191016']:
    for split in ['train']:
        name = 'coco_try_{}_abletonlive10_{}'.format(data_date, split)
        __sets[name] = (lambda split=split, datadate=data_date: coco_try_alc(split, data_date))

# Set up coco_2014_cap_<split>
for year in ['2014']:
    for split in ['train', 'val', 'capval', 'valminuscapval', 'trainval']:
        name = 'coco_{}_{}'.format(year, split)
        __sets[name] = (lambda split=split, year=year: coco(split, year))

# Set up coco_2015_<split>
for year in ['2015']:
    for split in ['test', 'test-dev']:
        name = 'coco_{}_{}'.format(year, split)
        __sets[name] = (lambda split=split, year=year: coco(split, year))


def get_imdb(name):
    """Get an imdb (image database) by name."""
    return coco_custom(name)


def list_imdbs():
    """List all registered imdbs."""
    return list(__sets.keys())
