from django.core.management import BaseCommand
from datasave.models import Data
from datasave.randomaizer import randomaizer



class Command(BaseCommand):
    def handle(self, *args, **options):

        for _ in range(5):
            try:
                self.stdout.write(u'Create str')
                text, axis_X, axis_Y, rotation, font_size, font_type, data_type = randomaizer()
                Data.objects.get_or_create(
                    text=text,
                    axis_X=axis_X,
                    axis_Y=axis_Y,
                    rotation=rotation,
                    font_size=font_size,
                    font_type=font_type,
                    data_type=data_type,
                )
                self.stdout.write(self.style.SUCCESS('Creation ended'))
            except Exception as ex:
                self.stdout.write(self.style.WARNING('Errors occured', ex))
