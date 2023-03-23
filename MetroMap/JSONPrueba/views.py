from django.shortcuts import render
from django.template import Template, Context, loader
# Create your views here.
from django.http import HttpResponse

def cuestion(request):
    plantillaExterna = open("C:\\Users\\jmpor\\OneDrive\\Documentos\\GitHub\\ppi_06\\MetroMap\\JSONPrueba\\plantillas\\cuestion.html")
    template = Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto = Context()
    documeto = template.render(contexto)
    

    return HttpResponse(documeto)

def tt(request):
    api = {"ok": True, "data": {"semaforos": [{"lineaId": "A", "estado": "2", "link": "https://twitter.com/metrodemedellin/status/1637253088070316032?s=20"}, {"lineaId": "B", "estado": "2", "link": "https://twitter.com/metrodemedellin/status/1637253088070316032?s=20"}, {"lineaId": "H", "estado": "2", "link": "https://twitter.com/metrodemedellin/status/1637253088070316032?s=20"}, {"lineaId": "J", "estado": "2", "link": "https://twitter.com/metrodemedellin/status/1637253088070316032?s=20"}, {"lineaId": "K", "estado": "2", "link": "https://twitter.com/metrodemedellin/status/1637253088070316032?s=20"}, {"lineaId": "L", "estado": "53", "link": "https://twitter.com/metrodemedellin/status/1637245209615425539?s=20"}, {"lineaId": "M", "estado": "2", "link": "https://twitter.com/metrodemedellin/status/1637253088070316032?s=20"}, {"lineaId": "P", "estado": "2", "link": "https://twitter.com/metrodemedellin/status/1637253088070316032?s=20"}, {"lineaId": "T", "estado": "2", "link": "https://twitter.com/metrodemedellin/status/1637253088070316032?s=20"}, {"lineaId": "O", "estado": "2", "link": "https://twitter.com/metrodemedellin/status/1637253088070316032?s=20"}, {"lineaId": "1", "estado": "41", "link": "https://twitter.com/thexam_12/status/1428142811971469312?s=20"}, {"lineaId": "2", "estado": "41", "link": "https://twitter.com/metrodemedellin/status/1637624553068191744?s=20"}], "estados": [{"id": "1", "text": "En construcción", "color": "Gris"}, {"id": "2", "text": "Normal", "color": "Verde"}, {"id": "3", "text": "Fuera de servicio - Alta", "color": "Rojo"}, {"id": "41", "text": "Operación por partes - Alta", "color": "Amarillo"}, {"id": "53", "text": "Fuera de servicio - Media", "color": "Rojo"}, {"id": "54", "text": "Operación por partes - Media", "color": "Amarillo"}, {"id": "58", "text": "Fuera de servicio - Baja", "color": "Rojo"}, {"id": "59", "text": "Normal - Alta", "color": "Estación o parada por fuera"}]}}
    def obtener_lineas(api):
        lineas = []
        estados = api['data']['estados']
        semaforos = api['data']['semaforos']
        for semaforo in semaforos:
            linea_id = semaforo['lineaId']
            estado_id = semaforo['estado']
            link = semaforo['link']
            for estado in estados:
                if estado['id'] == estado_id:
                    estado_texto = estado['text']
                    color = estado['color']
                    break
            linea_info = [linea_id, estado_texto, color, link]
            lineas.append(linea_info)
        return lineas

    plantillaExterna = open("C:\\Users\\jmpor\\OneDrive\\Documentos\\GitHub\\ppi_06\\MetroMap\\JSONPrueba\\plantillas\\tt.html")
    template = Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto = Context({"lineas": obtener_lineas(api)})
    documeto = template.render(contexto)
    

    return HttpResponse(documeto)

