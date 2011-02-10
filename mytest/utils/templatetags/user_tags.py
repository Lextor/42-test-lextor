from django import template
from django.core.urlresolvers import reverse


register = template.Library()


@register.simple_tag
def edit_link(inst):
    return reverse('admin:%s_%s_change' % (inst._meta.app_label, inst._meta.module_name), args=(inst.pk,))
