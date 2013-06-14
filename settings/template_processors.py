from settings.models import ColorScheme, BackgroundImage

def settings_processor(request):
    '''Add the default settings into the context of every template response'''

    context = {}
    try:
        default_color_scheme = ColorScheme.objects.get(is_default=True)
        context['colorscheme'] = default_color_scheme
    except ColorScheme.DoesNotExist:
        pass
    try:
        default_bg_img = BackgroundImage.objects.get(is_default=True)
        context['bgimage'] = default_bg_img
    except BackgroundImage.DoesNotExist:
        pass
    return context
