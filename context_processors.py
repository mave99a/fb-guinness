import facebook

def face(request):
    params = {}
    params['infbiframe'] = request.GET.__contains__('fb_sig_in_iframe')
    return params