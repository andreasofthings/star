from django.db import models
from django.conf import settings
from django.core import urlresolvers
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _


class StarManager(models.Manager):
    def count_for_model(self, model):
        """
        QuerySet for all comments for a particular model (either an instance or
                                                          a class)
        """
        ct = ContentType.objects.get_for_model(model)
        qs = self.get_query_set().filter(content_type=ct)
        if isinstance(model, models.Model):
            qs = qs.filter(object_pk=force_text(model._get_pk_val()))
        return qs.count()


class Star(models.Model):

    # User
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('user'),
        related_name="stars"
    )

    # Content-object field
    content_type = models.ForeignKey(
        ContentType,
        verbose_name=_('content type'),
        related_name="content_type_set_for_%(class)s"
    )

    object_pk = models.TextField(_('object ID'))

    content_object = generic.GenericForeignKey(
        ct_field="content_type",
        fk_field="object_pk"
    )

    def __unicode__(self):
        return "Star of object %s by %s" % \
            (self.content_object, self.user.get_username())

    class Meta:
        db_table = 'stars'
        unique_together = [('user', 'content_type', 'object_pk', )]
        verbose_name = _('star')
        verbose_name_plural = _('stars')

    def get_content_object_url(self):
        """
        Get a URL suitable for redirecting to the content object.
        """
        return urlresolvers.reverse(
            "comments-url-redirect",
            args=(self.content_type_id, self.object_pk)
        )
