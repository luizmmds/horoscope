# -*- encoding: utf-8 -*-
import requests
import string
from datetime import datetime
from flask import Flask, request, Response, json
from flask.ext.classy import FlaskView
from flask.ext.cors import CORS

app = Flask(__name__)

class HoroscopeView(FlaskView):
    route_base='horoscope/'
    signs = {
        "aries": ('03-21', '04-20'),
        "touro": ('04-21', '05-20'),
        "gemeos": ('05-21', '06-20'),
        "cancer": ('06-21', '07-21'),
        "leao": ('07-22', '08-22'),
        "virgem": ('08-23', '09-22'),
        "libra": ('09-23', '10-22'),
        "escorpiao": ('10-23', '11-21'),
        "sagitario": ('11-22', '12-21'),
        "aquario": ('01-21', '02-19'),
        "peixes": ('02-20', '03-20')
    }

    def get_sign(self, params):
        for sign in self.signs:
            try:
                if datetime.strptime(params.get('birthday'), '%m-%d') >= datetime.strptime(self.signs[sign][0], '%m-%d') and datetime.strptime(params.get('birthday'), '%m-%d') <= datetime.strptime(self.signs[sign][1], '%m-%d'):
                    return sign
            except ValueError:
                return False
        else:
            if datetime.strptime(params.get('birthday'), '%m-%d') >= datetime.strptime('12-22', '%m-%d') or datetime.strptime(params.get('birthday'), '%m-%d') <= datetime.strptime('01-20', '%m-%d'):
                return 'capricornio'
            else:
                return False

    def get_horoscope_text(self, text, begin, search):
        start_text = text.find(begin)
        start_search = text[start_text:].find("<%s"%search) + start_text
        finish_search = text[start_search:].find("</%s"%(search)) + start_search
        return text[start_search:finish_search]

    def get(self):
        sign = self.get_sign(request.args)
        if sign:
            r = requests.get("http://estilo.uol.com.br/horoscopo/%s/horoscopo-do-dia/"%(sign))
            title = self.get_horoscope_text(r.text, '<h1 class="h-external">', 'span>')
            text = self.get_horoscope_text(r.text, '<div class="text">', 'p>')
            return Response(json.dumps({"title": title, "text": text}))
        else:
            return Response("Signo não encontrado ):", 402)

HoroscopeView.register(app)
CORS(app)