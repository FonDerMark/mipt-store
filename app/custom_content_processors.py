def debug_mode(request):
    from custom.settings import DEBUG
    return {'debug': DEBUG}
