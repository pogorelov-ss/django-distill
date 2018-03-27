# -*- coding: utf-8 -*-


from django.conf.urls import url


from django_distill.errors import (DistillError, DistillWarning)


urls_to_distill = []


def distill_url(regex, view, kwargs=None, name=None, distill_func=None, distill_file=None):
    if distill_func:
        if not name:
            raise DistillError('Distill function provided with no name')
        if not callable(distill_func):
            err = 'Distill function not callable: {}'
            raise DistillError(err.format(distill_func))
        urls_to_distill.append((distill_func, distill_file, name, (regex, view), kwargs))
    else:
        e = 'URL registered with distill_url but no distill function supplied'
        raise DistillWarning(e)
    return url(regex, view, kwargs, name)


# eof
