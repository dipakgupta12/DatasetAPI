import csv
import re

from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Data

f = FileSystemStorage('tmp/')

class DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = '__all__'

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

    @action(detail=False, methods=['POST'])
    def upload_csv(self, request):
        file = request.FILES['file']

        content = file.read()

        file_content = ContentFile(content)
        file_name = f.save('temp.csv', file_content)
        file_temp = f.path(file_name)

        with open(file_temp, errors='ignore') as file:
            reader = csv.reader(file)
            next(reader)

            data = []

            for i, row in enumerate(reader):
                (title, description, image) = row
                try:
                    title = re.search('(Item\s\d+)', title).group()
                except:
                    pass


                data.append(
                    Data(
                        title=title,
                        description=description,
                        image=image
                    )
                )
            
            Data.objects.all().bulk_create(data)

        return Response("Success")

    @action(detail=False, methods=['POST'])
    def delete_all(self, request):
            Data.objects.all().delete()
            return Response('success')