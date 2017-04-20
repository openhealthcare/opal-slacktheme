from django import template

register = template.Library()

@register.inclusion_tag('slack_lists.html', takes_context=True)
def slack_lists(context):
    from opal.core.patient_lists import PatientList
    return dict(lists=PatientList.for_user(context['request'].user))
