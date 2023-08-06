"""В этом файле создаются команды, которые можно выполнять в консоли."""
from django.core.management import BaseCommand
from django.db.models import Max

from datasave.models import Data
from datasave.randomaizer import randomaizer

from functools import cmp_to_key


class Command(BaseCommand):
    """

    Консольная команда для создания 5 списков данных для моделей,
    их фильтрацией и созданием самих моделей.

    """

    @staticmethod
    def custom_filter(arg1: tuple, arg2: tuple) -> int:
        """Фильтр для сортировки приходящих данных."""
        if arg1[3] in (0, 180) and arg2[3] not in (0, 180):
            return 1
        elif arg1[3] in (90, 270) and arg2 not in (0, 180, 90, 270):
            return 1
        elif arg1[3] in (0, 180) and arg2 in (0, 180):
            return 0
        elif arg1[3] in (90, 270) and arg2 in (90, 270):
            return 0
        elif arg1[3] not in (0, 180, 90, 270) and arg2 not in (0, 180, 90, 270):
            return 0
        else:
            return -1

    def handle(self, *args, **options):

        list_of_new_data = []

        for i in range(10):
            try:
                new_data = randomaizer()
                list_of_new_data.append(new_data)

            except Exception as ex:
                self.stdout.write(self.style.ERROR('Errors occured', ex))

        cmp_func = cmp_to_key(self.custom_filter)
        list_of_new_data.sort(key=cmp_func)
        list_of_new_data.sort(key=lambda row: (row[4], row[2], row[1]))

        if Data.objects.count() == 0:
            batch = 1
        else:
            batch = Data.objects.all().aggregate(Max('batch'))['batch__max'] + 1


        for j in list_of_new_data:

            text, axis_X, axis_Y, rotation, font_size, font_type, data_type = j

            Data.objects.get_or_create(
                text=text,
                axis_X=axis_X,
                axis_Y=axis_Y,
                rotation=rotation,
                font_size=font_size,
                font_type=font_type,
                data_type=data_type,
                batch=batch,
            )
