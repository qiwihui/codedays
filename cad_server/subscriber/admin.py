from django.contrib import admin
from django.db.models.functions import Trunc
from django.db.models import DateTimeField
from django.db.models import Count, Min, Max
from subscriber.models import Subscriber, SentProblems, SubscriberSummary


def get_next_in_date_hierarchy(request, date_hierarchy):

    if date_hierarchy + '__day' in request.GET:
        return 'hour'

    if date_hierarchy + '__month' in request.GET:
        return 'day'

    if date_hierarchy + '__year' in request.GET:
        return 'week'

    return 'month'


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    
    list_display = ('email', 'status', 'is_vip')


@admin.register(SubscriberSummary)
class SubscriberSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/subscriber_summary_change_list.html'
    date_hierarchy = 'created_time'

    def changelist_view(self, request, extra_context=None):

        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        # 统计每天订阅的人数
        summary_over_time = qs.annotate(
            period=Trunc(
                'created_time',
                'day',
                output_field=DateTimeField(),
            ),
        ).values('period').annotate(total=Count('id')).order_by('period')

        summary_range = summary_over_time.aggregate(
            low=Min('total'),
            high=Max('total'),
        )
        high = summary_range.get('high', 0)
        low = 0

        response.context_data['summary_over_time'] = [{
            'period': x['period'],
            'total': x['total'] or 0,
            'pct': \
               ((x['total'] or 0) - low) / (high - low) * 100
               if high > low else 0,
        } for x in summary_over_time]

        return response

admin.site.register(SentProblems)
