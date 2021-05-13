'''
pathlib is blocked by Global Script/ControlScript
This module provides some of the features of pathlib, but is not complete (not even close, feel free to contribute at https://github.com/GrantGMiller/gs_pathlib)
'''


class Path:
    def __init__(self, path):
        self._fullpath = path.replace('\\', '/')

    @property
    def suffix(self):
        return '.' + self.name.split('.')[-1]

    @property
    def stem(self):
        return self.name.split('.')[0]

    @property
    def name(self):
        return self._fullpath.split('/')[-1]


if __name__ == '__main__':
    # test on a windows machine to make sure Path is behaving exactly like pathlib.Path
    from pathlib import Path as PathlibPath

    src = r'C:\Users\gmiller\PycharmProjects\gs_google_drive\trump.jpg'
    pp = PathlibPath(src)
    p = Path(src)

    for att in [
        'suffix',
        'stem',
        'name',
    ]:
        if getattr(p, att) != getattr(pp, att):
            print('error in "{att}", should have gotten "{correct}", instead got "{wrong}"'.format(
                att=att,
                correct=getattr(pp, att),
                wrong=getattr(p, att),
            ))
        else:
            print('correct', att, '=', getattr(pp, att))
