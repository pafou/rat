#-*- coding: utf-8 -*-

import re
import json
import os

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from subprocess import Popen, PIPE

RACINE = "/da/sc/np/home/data/scdsifa/src/python/tmps/" #PF:RACINE à modifier


def last_line(paragraph):
    """Provides last non empty line of a paragraph."""

    lst = paragraph.split("\n")
    the_last_line = ""
    for element in reversed(lst):
        if (re.match("\w",element)):
            the_last_line = element
            break
    return the_last_line

class RessourcesList(APIView):
    """
    List all ressources and create new ones. 
    """

    def get(self, request, env, ressources):
        """GET method: "-a get" launched: all ressources in json format""" 
        commande = os.path.join(RACINE,ressources) 
        commande_full = [commande, "-a", "get", "-e", env]
        try:
            p = Popen(commande_full, stdin=PIPE, stdout=PIPE, stderr=PIPE, bufsize=-1)
            output, error = p.communicate()
            if p.returncode == 0:
                # return code is ok
                output = json.loads(output) #PF:faire des verifs sur le format json
                return Response(output)
            else:
                # execution ok but return code is not 0
                assert p.returncode > 0
                rc = str(p.returncode)
                ll = last_line(output)
                output = "RC " + rc + " Script error: " + ll 
                return Response(output)
        except:
            output = "Exec error: " + " ".join(commande_full)
            return Response(output)

    def post(self, request, env, ressources):
        """POST method: "-a post" launched: creation from json.
        
        Returns a json with pk (primary key)
        """ 
        commande = os.path.join(RACINE,ressources) 
        json_from_body = json.loads(request.body)
        json_to_command = json.dumps(json_from_body)
        commande_full = [commande, "-a", "post", "-e", env, "-j", json_to_command]
        try:
            p = Popen(commande_full, stdin=PIPE, stdout=PIPE, stderr=PIPE, bufsize=-1)
            output, error = p.communicate()
            if p.returncode == 0:
                # return code is ok
                output = json.loads(output) #PF:faire des verifs sur le format json
                return Response(output)
            else:
                # execution ok but return code is not 0
                assert p.returncode > 0
                rc = str(p.returncode)
                ll = last_line(output)
                output = "RC " + rc + " Script error: " + ll
                return Response(output)
        except:
            output = "Exec error: " + " ".join(commande_full)
            return Response(output)


class RessourcesDetail(APIView):
    """
    Retrieve, update or delete a <ressource> instance.
    """
    def get_object(self, pk):
        print "PF"
        #try:
            #return Mqq.objects.get(pk=pk)
        #except Mqq.DoesNotExist:
            #raise Http404

    def get(self, request, pk, format=None):
        print "PF"
        #mqq = self.get_object(pk)
        #serializer = MqqSerializer(mqq)
        #return Response(serializer.data)

    def put(self, request, pk, format=None):
        print "PF"
        #mqq = self.get_object(pk)
        #serializer = MqqSerializer(mqq, data=request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        print "PF"
        #mqq = self.get_object(pk)
        #mqq.delete()
        #return Response(status=status.HTTP_204_NO_CONTENT)