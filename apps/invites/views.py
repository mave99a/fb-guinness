# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
import facebook
from models import *

def faceit(request):
    fb = facebook.Facebook('8210a054e8410c2e848c77faf8894fa8', '1f0f37d8b3aa920afcdb3ececbf9e4c0')
    fb.check_session(request)
    return fb
        
def invite(request):
    fb = faceit(request)
    
    ids = request.REQUEST.getlist('ids[]')
    
    #store in db
    for id in ids: 
        invite = Invite(sender = request.REQUEST['sender'], invitee = id)
        invite.put()
    
    return render_to_response("invite.html", {'ids':ids, 'fbuid':fb.uid}, context_instance=RequestContext(request) );

def index(request):
    fb = faceit(request)
    invites = Invite.all().filter('invitee =', fb.uid)
    invites.order('-when')
    invites.fetch(10)
 
    return render_to_response("home.html", {'invites':invites, 'fbuid':fb.uid}, context_instance=RequestContext(request) );
