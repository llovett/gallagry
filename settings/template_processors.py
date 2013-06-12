from settings.models import ColorScheme

def settings_processor(request):
    '''Add the default settings into the context of every template response'''

    try:
        default_color_scheme = ColorScheme.objects.get(is_default=True)
        return {'colorscheme':default_color_scheme}
    except ColorScheme.DoesNotExist:
        return {}
