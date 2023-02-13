from .. models import Measurement

def get_measurements():
    return Measurement.objects.all()   

def get_measurement(meu_id):
    return Measurement.objects.get(id=meu_id)

def update_measurement(meu_id, new_meu):
    measurement = get_measurement(meu_id)
    measurement.variable = new_meu["variable"]
    measurement.value = new_meu["value"]
    measurement.unit = new_meu["unit"]
    measurement.place = new_meu["place"]
    measurement.dateTime = new_meu["dateTime"]
    measurement.save()
    return measurement


def create_measurement(meu):
    measurement = Measurement(variable=meu["variable"], value=meu["value"], unit=meu["unit"], place=meu["place"], dateTime=meu["dateTime"])
    measurement.save()
    return measurement

def delete_measurement(meu_id):
    measurement = get_measurement(meu_id)
    measurement.delete()

    